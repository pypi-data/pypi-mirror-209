# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest


class TestLatticeOutput2Abaqus(unittest.TestCase):

    def test_rect_lattice(self):
        from metalattice.lattice.lattice import Lattice

        la = Lattice(
            ns=[7, 7, 7],
            strides=[2, 2, 2],
            custom_lattice_f="rect_lattice.f"
        )
        la.write_beam_job(
            job_name="test_beam"
        )
        la.write_micropolar_job(
            job_name="test_rect__micropolar_mpc3d8",
            element_type="MPC3D8",
            regenerate=True,
        )
        la.write_micropolar_job(
            job_name="testt_rect_micropolar_mpc3d20",
            element_type="MPC3D20",
            regenerate=True,
        )

    def test_cylin_lattice(self):
        from metalattice.lattice.lattice import Lattice

        la = Lattice(
            ns=[8, 48, 4],
            strides=[2, 2, 2],
            periodic=[False, True, False],
            custom_lattice_f="cylin_lattice.f"
        )
        la.write_beam_job(
            job_name="test_beam"
        )
        la.write_micropolar_job(
            job_name="test_cylin_micropolar_mpc3d8",
            element_type="MPC3D8",
            regenerate=True,
        )
        la.write_micropolar_job(
            job_name="test_cylin_micropolar_mpc3d20",
            element_type="MPC3D20",
            regenerate=True,
        )


if __name__ == '__main__':
    unittest.main()
