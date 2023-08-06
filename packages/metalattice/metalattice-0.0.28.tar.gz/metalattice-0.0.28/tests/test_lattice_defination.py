# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import numpy as np
import unittest


class TestLatticeDefination(unittest.TestCase):

    def test_py_coord_of_idx(self):
        from metalattice.abaqus.fortran.lib import lattice
        lattice.py_coord_of_idx(1.0, 1.0, 1.0)

    def test_beam_of_idx(self):
        from metalattice.abaqus.fortran.lib import lattice

        lattice.beam_of_idx(
            np.array([0, 0, 0]),
            np.array([0, 0, 1]),
            np.array([1, 1, 1]),
        )

    def test_py_beams_inside_cube(self):
        from metalattice.abaqus.fortran.lib import lattice

        lattice.py_beams_inside_cube(
            1, 1, 1, 2, 2, 2,
            np.array([10, 10, 10]), np.array([False, True, False])
        )


if __name__ == '__main__':
    unittest.main()
