# -*- coding: UTF-8 -*-
#! python3

"""
    Usage from the repo root folder:

    ```python
    # for whole test
    python -m unittest tests.test_enums
    # for specific
    python -m unittest tests.test_enums.TestEnums
    ```
"""

# #############################################################################
# ########## Libraries #############
# ##################################

# standard library
import unittest

# module target
from isogeo_pysdk.enums import ContactRoles


# #############################################################################
# ########## Classes ###############
# ##################################


class TestEnums(unittest.TestCase):
    """Test Enum model of Isogeo API."""

    def setUp(self):
        """Executed before each test."""
        pass

    def tearDown(self):
        """Executed after each test."""
        pass

    # -- TESTS ---------------------------------------------------------

    def test_application_kinds(self):
        """Check metadata's types list"""
        self.assertEqual(len(ApplicationKinds), 2)
        self.assertTrue("group" in ApplicationKinds.__members__)
        self.assertFalse("User" in ApplicationKinds.__members__)
        for i in ApplicationKinds:
            self.assertIsInstance(i.value, int)

    def test_contact_roles(self):
        """Check contact's roles list"""
        self.assertEqual(len(ContactRoles), 11)
        self.assertTrue("author" in ContactRoles.__members__)
        self.assertFalse("Author" in ContactRoles.__members__)
        for role in ContactRoles:
            self.assertIsInstance(role.value, str)


# ##############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    unittest.main()
