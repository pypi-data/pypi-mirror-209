from typing import Literal, TextIO

from metalattice.material import Material


step_type_list = ["Static", "Frequency"]


class AbaqusInpWriter:
    def __init__(
        self,
        inp_file_name: str,
    ) -> None:
        self.inp_file_name = inp_file_name
        self.inp = open(inp_file_name, "a")

    def close(self):
        if not self.inp.closed:
            self.inp.close()
    
    def write_material(
        self,
        mat: Material,
    ):
        self.inp.writelines([
            "** \n",
            "** MATERIALS\n",
            "** \n",
            "*Material, name={}\n".format(mat.name),
            "*Density\n",
            "{},\n".format(mat.rho),
            "*Elastic\n",
            "{}, {}\n".format(mat.E, mat.nu),
        ])

    def write_step(
        self,
        step: dict = {
            "name": "Step-1",
            "type": "Static",
            "BCs": {},
            "loads": {},
        },
    ):
        if "name" not in step:
            step["name"] = "Step-1"
        if "type" not in step:
            step["type"] = "Static"
        assert step["type"] in step_type_list

        self.inp.writelines([
            "** ----------------------------------------------------------------\n",
            "** \n",
            "** STEP: Step-1\n",
            "** \n",
        ])

        if step["type"] == "Static":
            self.inp.writelines([
                "*Step, name=Step-1, nlgeom=NO\n",
                "*Static\n",
                "1., 1., 1e-05, 1.\n",
            ])
        elif step["type"] == "Frequency":
            self.inp.writelines([
                "*Step, name=Step-1, nlgeom=NO\n",
                "*Frequency\n",
            ])
            if "num of eigenvalues" in step:
                self.inp.writelines([
                    "{}\n".format(step["num of eigenvalues"]),
                ])
            else:
                raise Exception()
        
        self.write_BCs(BCs=step["BCs"])
        self.write_loads(loads=step["loads"])
        self.inp.writelines([
            "** \n",
            "** OUTPUT REQUESTS\n",
            "** \n",
            "*Restart, write, frequency=0\n",
            "** \n",
            "** FIELD OUTPUT: F-Output-1\n",
            "** \n",
            "*Output, field, variable=PRESELECT\n",
            "** \n",
            "** HISTORY OUTPUT: H-Output-1\n",
            "** \n",
            "*Output, history, variable=PRESELECT\n",
            "*End Step\n",
        ])
    
    def write_BCs(
        self,
        BCs: dict[str, dict],
    ):
        if len(BCs) == 0:
            return
        self.inp.writelines([
            "** \n",
            "** BOUNDARY CONDITIONS\n",
            "** \n",
        ])
        for name, boundary in BCs.items():
            if "type" not in boundary:
                boundary["type"] = "Boundary"
            self.inp.writelines([
                "** Name: {}\n".format(name),
                "*{}\n".format(boundary["type"]),
            ])
            for data in boundary["data"]:
                self.inp.write(data)
                if "\n" not in data:
                    self.inp.write("\n")
    
    def write_loads(
        self,
        loads: dict[str, dict],
    ):
        if len(loads) == 0:
            return
        self.inp.writelines([
            "** \n",
            "** LOADS\n",
            "** \n",
        ])
        for name, load in loads.items():
            if "type" not in load:
                load["type"] = "Cload"
            self.inp.writelines([
                "** Name: {}\n".format(name),
                "*{}\n".format(load["type"]),
            ])
            for data in load["data"]:
                self.inp.write(data)
                if "\n" not in data:
                    self.inp.write("\n")

    def write_sections(
        self,
        sections: dict,
    ):
        for name, section in sections.items():
            self.inp.writelines([
                "** Section: {}\n".format(name),
                "*Beam Section, elset={}, material={}, section={}, lumped={}\n".format(
                    section["elset"],
                    section["material"],
                    section["section"],
                    section["lumped"],
                ),
                "{}\n".format(",".join(section["geom"])),
            ])
            if "n1" in section:
                self.inp.writelines([
                    "{}\n".format(",".join(section["n1"])),
                ])
