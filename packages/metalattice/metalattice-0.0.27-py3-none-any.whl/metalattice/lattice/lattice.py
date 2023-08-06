from f90nml.namelist import Namelist
import meshio
from meshio.abaqus._abaqus import meshio_to_abaqus_type, abaqus_to_meshio_type
import numpy as np
from shutil import copyfile

from metalattice.material import Material
from metalattice.abaqus import fortran
from metalattice.abaqus.fortran import compile_fortran
from metalattice.abaqus.fortran import lib
from metalattice.abaqus.scripts import run_abaqus_script


class Lattice:
    def __init__(
        self,
        ns: list[int],
        strides: list[int] = [1, 1, 1],
        periodic: list[bool] = 3*[False],
        material: Material = Material(),
        custom_lattice_f: str = "custom_lattice.f",
    ) -> None:
        self.cell_ns = ns
        self.node_ns = [ns[i] + (not periodic[i]) for i in range(3)]
        self.strides = strides
        self.periodic = periodic
        self.material = material
        assert material.type == "Cauchy"

        self.custom_lattice_f = custom_lattice_f
        target = "custom_lattice.f"
        src = fortran.code_dir.joinpath(custom_lattice_f)
        dst = fortran.code_dir.joinpath(target)
        assert src.is_file()
        copyfile(src=src, dst=dst)
        fortran.idx += 1
        fortran.bin_dir_tmp = fortran.bin_dir.joinpath(f"{fortran.idx}")
        compile_fortran()

        self.nodes: dict[tuple(int), np.ndarray] = None
        self.beams: dict[tuple(int), lib.lattice.Beam] = None
        self.continuum_mesh: dict = None
        self.base_indices: list[list[int]] = None
        self.iel2ijk: np.ndarray = None
        self.iel2didjdk: np.ndarray = None

    def coord_of_idx(
        self,
        i: float,
        j: float,
        k: float,
    ) -> np.ndarray:
        return lib.lattice.py_coord_of_idx(i, j, k).result["c"]

    def beam_of_idx(
        self,
        ijk1: list[float],
        ijk2: list[float],
    ):
        beam = lib.lattice.beam_of_idx(
            ijk1, ijk2, np.array(self.node_ns)
        ).result
        return beam

    def beams_inside_cube(
        self,
        i: int, j: int, k: int,
        di: int = 1, dj: int = 1, dk: int = 1,
    ) -> list:
        res = lib.lattice.py_beams_inside_cube(
            i, j, k, di, dj, dk,
            np.array(self.cell_ns), np.array(self.periodic)
        ).result

        return [res["beams"][no] for no in range(res["num"])]

    def generate_nodes(self, regenerate: bool = False):
        node_ns = self.node_ns
        if not regenerate and self.nodes is not None:
            return
        self.nodes = {}
        for i in range(node_ns[0]):
            for j in range(node_ns[1]):
                for k in range(node_ns[2]):
                    self.nodes[(i, j, k)] = self.coord_of_idx(i, j, k)

    def generate_beams(self, regenerate: bool = False):
        cell_ns = self.cell_ns
        if not regenerate and self.beams is not None:
            return
        self.beams = {}
        for i in range(cell_ns[0]):
            for j in range(cell_ns[1]):
                for k in range(cell_ns[2]):
                    beams = self.beams_inside_cube(i, j, k)
                    for beam in beams:
                        key = tuple([
                            tuple(beam["indices"][:, 0].tolist()),
                            tuple(beam["indices"][:, 1].tolist()),
                        ])
                        if key not in self.beams:
                            self.beams[key] = beam

    def genertate_continuum_mesh(
        self,
        element_type: str = "MPC3D8",
        regenerate: bool = False,
    ):
        node_ns = self.node_ns
        cell_ns = self.cell_ns
        periodic = self.periodic
        strides = self.strides
        if not regenerate and self.continuum_mesh is not None:
            return
        self.continuum_mesh = {}
        self.continuum_mesh["nodes"]: dict[tuple[int], list[int]] = {}
        self.continuum_mesh["elements"]: list[list[int]] = []

        self.base_indices = [[] for d in range(3)]
        base_indices = self.base_indices
        for d in range(3):
            if periodic[d]:
                assert cell_ns[d] % strides[d] == 0
                base_indices[d] = [
                    i
                    for i in range(0, node_ns[d] + 1, strides[d])
                ]
            else:
                base_indices[d] = [0, ]
                n = cell_ns[d] - 2
                if n % strides[d] == 0:
                    base_indices[d].extend(
                        [
                            i
                            for i in range(1, node_ns[d]-1, strides[d])
                        ]
                    )
                else:
                    half = n // (2 * strides[d])
                    remain = n % (2 * strides[d])
                    base_indices[d].extend(
                        [
                            i
                            for i in range(
                                1, 1 + half * strides[d] + 1, strides[d]
                            )
                        ]
                    )
                    base_indices[d].extend(
                        [
                            i
                            for i in range(
                                1 + half * strides[d] + remain,
                                node_ns[d]-1,
                                strides[d]
                            )
                        ]
                    )
                base_indices[d].extend([node_ns[d] - 1])
        iel2ijk: list[list[int]] = []
        iel2didjdk: list[list[int]] = []

        for i in range(len(base_indices[0]) - 1):
            for j in range(len(base_indices[1]) - 1):
                for k in range(len(base_indices[2]) - 1):
                    self.construct_mesh_node(
                        [i, j, k],
                        element_type,
                    )

        for i in range(len(base_indices[0]) - 1):
            for j in range(len(base_indices[1]) - 1):
                for k in range(len(base_indices[2]) - 1):
                    self.construct_mesh_element(
                        [i, j, k],
                        element_type,
                    )
                    iel2ijk.append([
                        base_indices[0][i],
                        base_indices[1][j],
                        base_indices[2][k],
                    ])
                    iel2didjdk.append([
                        (
                            base_indices[0][i + 1] - base_indices[0][i]
                        ) % strides[0],
                        (
                            base_indices[1][j + 1] - base_indices[1][j]
                        ) % strides[1],
                        (
                            base_indices[2][k + 1] - base_indices[2][k]
                        ) % strides[2],
                    ])

        self.iel2ijk = np.array(iel2ijk).T
        self.iel2didjdk = np.array(iel2didjdk).T

    def construct_mesh_element_node_indices(
        self,
        ijk: list[int],
        element_type: str,
    ):
        base_indices = self.base_indices
        i, j, k = ijk
        i00 = base_indices[0][i]
        j00 = base_indices[1][j]
        k00 = base_indices[2][k]
        i10 = base_indices[0][i + 1]
        j10 = base_indices[1][j + 1]
        k10 = base_indices[2][k + 1]
        i05 = (i00 + i10) / 2.0
        j05 = (j00 + j10) / 2.0
        k05 = (k00 + k10) / 2.0
        i10 = i10 % self.node_ns[0]
        j10 = j10 % self.node_ns[1]
        k10 = k10 % self.node_ns[2]
        if "C3D8" in element_type:
            return [
                [i00, j00, k00],
                [i10, j00, k00],
                [i10, j10, k00],
                [i00, j10, k00],

                [i00, j00, k10],
                [i10, j00, k10],
                [i10, j10, k10],
                [i00, j10, k10],
            ]
        elif "C3D20" in element_type:
            return [
                [i00, j00, k00],
                [i10, j00, k00],
                [i10, j10, k00],
                [i00, j10, k00],

                [i00, j00, k10],
                [i10, j00, k10],
                [i10, j10, k10],
                [i00, j10, k10],

                [i05, j00, k00],
                [i10, j05, k00],
                [i05, j10, k00],
                [i00, j05, k00],

                [i05, j00, k10],
                [i10, j05, k10],
                [i05, j10, k10],
                [i00, j05, k10],

                [i00, j00, k05],
                [i10, j00, k05],
                [i10, j10, k05],
                [i00, j10, k05],
            ]
        else:
            raise Exception(f"Element type {element_type} is not supported!")

    def construct_mesh_node(
        self,
        ijk: list[int],
        element_type: str,
    ):
        node_indices = self.construct_mesh_element_node_indices(
            ijk, element_type
        )
        for indices in node_indices:
            key = (
                round(10 * indices[0]),
                round(10 * indices[1]),
                round(10 * indices[2]),
            )
            if key not in self.continuum_mesh["nodes"]:
                self.continuum_mesh["nodes"][key] = self.coord_of_idx(
                    indices[0], indices[1], indices[2]
                ).tolist()

    def construct_mesh_element(
        self,
        ijk: list[int],
        element_type: str,
    ):
        node_indices = self.construct_mesh_element_node_indices(
            ijk, element_type
        )
        node_key_list = list(self.continuum_mesh["nodes"].keys())
        conn = []
        for indices in node_indices:
            key = (
                round(10 * indices[0]),
                round(10 * indices[1]),
                round(10 * indices[2]),
            )
            conn.append(node_key_list.index(key))
        self.continuum_mesh["elements"].append(conn)

    def write_beam_job(
        self,
        job_name: str,
    ) -> None:
        self.generate_nodes()
        self.generate_beams()

        inp_file_name = job_name + ".inp"
        points = list(self.nodes.values())

        conn = []
        ijk_list = list(self.nodes.keys())
        for beam in self.beams.values():
            conn.append(
                [
                    ijk_list.index(tuple([
                        (ijk[d] - 1) % self.node_ns[d]
                        for d in range(3)
                    ]))
                    for ijk in beam["indices"].T
                ]
            )

        element_type = beam["element"]
        if element_type == lib.lattice.b31:
            meshio_type = "line"
            meshio_to_abaqus_type[meshio_type] = "B31"
        elif element_type == lib.lattice.b33:
            meshio_type = "line"
            meshio_to_abaqus_type[meshio_type] = "B33"
        else:
            raise Exception(
                f"Beam element type {element_type} is not supported!")
        cells = [
            (meshio_type, conn),
        ]
        meshio.write_points_cells(inp_file_name, points, cells)

        run_abaqus_script("generate_inp")

    def write_micropolar_job(
        self,
        job_name: str,
        element_type: str = "MPC3D8",
        regenerate: bool = False,
    ):
        self.generate_nodes()
        self.genertate_continuum_mesh(
            element_type=element_type,
            regenerate=regenerate,
        )

        inp_file_name = job_name + ".inp"
        points = list(self.continuum_mesh["nodes"].values())

        if "C3D8" in element_type:
            meshio_type = abaqus_to_meshio_type["C3D8"]
            meshio_to_abaqus_type[meshio_type] = "C3D8"
        elif "C3D20" in element_type:
            meshio_type = abaqus_to_meshio_type["C3D20"]
            meshio_to_abaqus_type[meshio_type] = "C3D20"
        else:
            raise Exception(
                f"Continuum element type {element_type} is not supported!")
        cells = [
            (meshio_type, self.continuum_mesh["elements"]),
        ]
        meshio.write_points_cells(inp_file_name, points, cells)

        info_file_name = job_name + ".metalattice.info"
        namelist_element = Namelist({
            "nml_info": {
                "nelems": len(self.continuum_mesh["elements"]),
                "mat": Namelist({
                    "E": self.material.E,
                    "nu": self.material.nu,
                    "G": self.material.G,
                    "rho": self.material.rho,
                }),
            }
        })
        namelist_element.write(info_file_name, force=True)

        ele_file_name = job_name + ".metalattice.ele"
        namelist_element = Namelist({
            "nml_ele": {
                "iel2ijk": self.iel2ijk.flatten(order="F").tolist(),
                "iel2didjdk": self.iel2didjdk.flatten(order="F").tolist(),
                "ns": self.cell_ns,
                "periodic": self.periodic,
            }
        })
        namelist_element.write(ele_file_name, force=True)
