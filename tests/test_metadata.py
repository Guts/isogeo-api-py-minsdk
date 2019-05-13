# -*- coding: UTF-8 -*-
#! python3

"""
    Usage from the repo root folder:

    ```python
    # for whole test
    python -m unittest tests.test_metadata
    # for specific
    python -m unittest tests.test_metadata.TestMetadata.test_metadata_create_basic
    ```
"""

# #############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import json
import logging
import unittest
from os import environ
from pathlib import Path
from random import sample
from socket import gethostname
from sys import exit
from time import gmtime, strftime

# 3rd party
from dotenv import load_dotenv
from oauthlib.oauth2 import LegacyApplicationClient
from requests import HTTPError

# module target
from isogeo_pysdk import IsogeoSession, Metadata
from isogeo_pysdk import __version__ as pysdk_version

# #############################################################################
# ######## Globals #################
# ##################################

load_dotenv("dev.env", override=True)

# host machine name - used as discriminator
hostname = gethostname()

# API access
app_script_id = environ.get("ISOGEO_API_USER_CLIENT_ID")
app_script_secret = environ.get("ISOGEO_API_USER_CLIENT_SECRET")
platform = environ.get("ISOGEO_PLATFORM", "qa")
user_email = environ.get("ISOGEO_USER_NAME")
user_password = environ.get("ISOGEO_USER_PASSWORD")
workgroup_test = environ.get("ISOGEO_WORKGROUP_TEST_UUID")

MD_COMPLETE = environ.get("ISOGEO_FIXTURES_METADATA_COMPLETE")

# #############################################################################
# ########## Classes ###############
# ##################################


class TestMetadata(unittest.TestCase):
    """Test Workgroup model of Isogeo API."""

    if not app_script_id or not app_script_secret:
        logging.critical("No API credentials set as env variables.")
        exit()
    else:
        pass
    logging.debug("Isogeo PySDK version: {0}".format(pysdk_version))

    # standard methods
    def setUp(self):
        """Executed before each test."""
        # tests stuff
        self.discriminator = "{}_{}".format(
            hostname, strftime("%Y-%m-%d_%H%M%S", gmtime())
        )
        self.li_metadata_to_delete = []
        # API connection
        self.isogeo = IsogeoSession(
            client=LegacyApplicationClient(client_id=app_script_id),
            auto_refresh_url="{}/oauth/token".format(environ.get("ISOGEO_ID_URL")),
            client_secret=app_script_secret,
            platform=platform,
        )

        # getting a token
        self.isogeo.connect(username=user_email, password=user_password)

        # fixtures
        self.local_metadata = [Path(r"tests/fixtures", "resource_complete_1.json")]

    def tearDown(self):
        """Executed after each test."""
        # clean created metadata
        if len(self.li_metadata_to_delete):
            for i in self.li_metadata_to_delete:
                self.isogeo.md_delete(resource_id=i)
        # close sessions
        self.isogeo.close()

    # -- ALL APPS ------------------------------------------------------------
    def test_metadata_create_basic(self):
        """POST :groups/{workgroup_UUID}/resource}"""
        # create it
        new_metadata = self.isogeo.md_create(
            workgroup_id=workgroup_test,
            resource_type="vectorDataset",
            title="TEST_UNIT_AUTO - MD CREATION - {}".format(self.discriminator),
            abstract="This metadata has been automatically created during unit tests of Python Package: {}. \n\nShould have been automatically cleaned (deleted). An error could have occurred...".format(
                self.discriminator
            ),
        )

        # load it
        my_new_metadata = Metadata(**new_metadata)

        # add created workgroup to deletion
        self.li_metadata_to_delete.append(my_new_metadata._id)

    def test_metadata_complete(self):
        """GET :/resources/{resource_uuid}}"""
        # -- ONLINE -----------------------------
        # get a complete metadata
        try:
            metadata_complete = self.isogeo.resource(
                resource_id=MD_COMPLETE, include="all"
            )
        except HTTPError:
            # retrieve workgroup metadata
            wg_metadata = self.isogeo.workgroup_metadata(
                workgroup_id=workgroup_test, page_size=30
            )
            # randomly pick one
            rand_metadata_uuid = sample(wg_metadata.get("results"), 1)[0].get("_id")
            metadata_complete = self.isogeo.resource(
                resource_id=rand_metadata_uuid, include="all"
            )

        # load it
        md_test = Metadata(**metadata_complete)
        # test object methods
        self.assertIsInstance(md_test.to_dict(), dict)
        self.assertIsInstance(md_test.to_dict_creation(), dict)

        # -- OFFLINE -----------------------------
        for local_md in self.local_metadata:
            with local_md.open() as in_json:
                md_loaded_from_json = json.loads(in_json.read())
                # manually handle bad attributes
                md_loaded_from_json["coordinateSystem"] = md_loaded_from_json.pop(
                    "coordinate-system", list
                )
                md_loaded_from_json["featureAttributes"] = md_loaded_from_json.pop(
                    "feature-attributes", list
                )
                # load it
                Metadata(**md_loaded_from_json)

    def test_metadata_get_workgroup(self):
        """GET :groups/{workgroup_uuid}/resources/search}"""
        # retrieve workgroup metadata
        wg_metadata = self.isogeo.workgroup_metadata(
            workgroup_id=workgroup_test, page_size=30
        )
        # parse and test object loader
        for i in wg_metadata.get("results"):
            metadata = Metadata(**i)
            # test object methods
            self.assertIsInstance(metadata.to_dict(), dict)
            self.assertIsInstance(metadata.to_dict_creation(), dict)
            # tests attributes structure
            # self.assertTrue(hasattr(ct, "_abilities"))
            # self.assertTrue(hasattr(ct, "_created"))
            # self.assertTrue(hasattr(ct, "_id"))
            # self.assertTrue(hasattr(ct, "_modified"))
            # self.assertTrue(hasattr(ct, "_tag"))
            # self.assertTrue(hasattr(ct, "code"))
            # self.assertTrue(hasattr(ct, "count"))
            # self.assertTrue(hasattr(ct, "name"))
            # self.assertTrue(hasattr(ct, "owner"))
            # self.assertTrue(hasattr(ct, "scan"))
            # # tests attributes value
            # self.assertEqual(ct.code, i.get("code"))
            # self.assertEqual(ct.name, i.get("name"))


# ##############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    unittest.main()
