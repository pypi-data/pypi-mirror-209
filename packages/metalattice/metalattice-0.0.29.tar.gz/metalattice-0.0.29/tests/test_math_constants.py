# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest


class TestMathConstants(unittest.TestCase):

    def test_pi(self):
        import numpy as np
        from sympy import pi

        from metalattice.abaqus.fortran.lib import lattice

        assert np.isclose(lattice.pi, float(pi))

    def test_eps_tens(self):
        import numpy as np
        from sympy import LeviCivita

        from metalattice.abaqus.fortran.lib import lattice

        levicivita = np.zeros([3, 3, 3])
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    levicivita[i, j, k] = LeviCivita(i, j, k)
        assert np.allclose(lattice.eps_tens, levicivita)


if __name__ == '__main__':
    unittest.main()
