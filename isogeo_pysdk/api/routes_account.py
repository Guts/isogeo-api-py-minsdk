# -*- coding: UTF-8 -*-
#! python3

"""
    Isogeo API v1 - API Routes for Account entities

    See: http://help.isogeo.com/api/complete/index.html
"""

# #############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import logging

# submodules
from isogeo_pysdk.checker import IsogeoChecker
from isogeo_pysdk.decorators import ApiDecorators
from isogeo_pysdk.models import User
from isogeo_pysdk.utils import IsogeoUtils

# #############################################################################
# ########## Global #############
# ##################################

logger = logging.getLogger(__name__)
checker = IsogeoChecker()
utils = IsogeoUtils()


# #############################################################################
# ########## Classes ###############
# ##################################
class ApiAccount:
    """Routes as methods of Isogeo API used to manipulate account (user).
    """

    def __init__(self, api_client=None):
        if api_client is not None:
            self.api_client = api_client

        # store API client (Request [Oauthlib] Session) and pass it to the decorators
        self.api_client = api_client
        ApiDecorators.api_client = api_client

        # ensure platform and others params to request
        self.platform, self.api_url, self.app_url, self.csw_url, self.mng_url, self.oc_url, self.ssl = utils.set_base_url(
            self.api_client.platform
        )
        # initialize
        super(ApiAccount, self).__init__()

    @ApiDecorators._check_bearer_validity
    def account(self, include: list = ["_abilities"], caching: bool = 1) -> User:
        """Get authenticated user account(= profile) informations.

        :param list include: additional parts of model to include in response
        :param bool caching: option to cache the response
        """
        # handling request parameters
        payload = {"_include": include}

        # request URL
        url_account = utils.get_request_base_url(route="account")

        # request
        req_account = self.api_client.get(
            url=url_account,
            headers=self.api_client.header,
            params=payload,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_account)
        if isinstance(req_check, tuple):
            return req_check

        # if caching use or store the response
        if caching and not self.api_client._user:
            self.api_client._user = User(**req_account.json())

        # end of method
        return User(**req_account.json())

    @ApiDecorators._check_bearer_validity
    def account_update(self, account: User, caching: bool = 1) -> User:
        """Update authenticated user account(= profile) informations.

        :param class account: user account model object to update
        :param bool caching: option to cache the response
        """
        # check account UUID
        if not checker.check_is_uuid(account._id):
            raise ValueError("User ID is not a correct UUID: {}".format(account._id))
        else:
            pass

        # URL
        url_account_update = utils.get_request_base_url(route="account")

        # request
        req_account_update = self.api_client.put(
            url=url_account_update,
            json=account.to_dict(),
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_account_update)
        if isinstance(req_check, tuple):
            return req_check

        # if caching use or store the response
        if caching and not self.api_client._user:
            self.api_client._user = User(**req_account_update.json())

        # end of method
        return User(**req_account_update.json())


# ##############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    """ standalone execution """
    api_account = ApiAccount()
