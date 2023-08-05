# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest


class TestImport(unittest.TestCase):

    def test_import(self):
        from metalattice.abaqus.fortran import lib
        print(dir(lib.test))
        print(lib.test.pi)


if __name__ == '__main__':
    unittest.main()
