# -*- coding: UTF-8 -*-
#! python3

"""
    Isogeo API v1 - API Routes for Shares entities

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
from isogeo_pysdk.models import Share
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
class ApiShare:
    """Routes as methods of Isogeo API used to manipulate shares.
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
        super(ApiShare, self).__init__()

    @ApiDecorators._check_bearer_validity
    def shares(self, workgroup_id: str = None, caching: bool = 1) -> list:
        """Get all shares which are accessible by the authenticated user OR shares for a workgroup.

        :param str workgroup_id: identifier of the owner workgroup. If `None`, then list shares for the autenticated user
        :param bool caching: option to cache the response
        """
        # URL
        if workgroup_id is not None:
            logger.debug("Listing shares for a workgroup: {}".format(workgroup_id))
            if not checker.check_is_uuid(workgroup_id):
                raise ValueError("Workgroup ID is not a correct UUID.")
            else:
                url_shares = utils.get_request_base_url(
                    route="groups/{}/shares".format(workgroup_id)
                )
        else:
            logger.debug(
                "Listing shares for the authenticated user: {}".format(
                    self.api_client._user.contact.get("name")
                )
            )
            url_shares = utils.get_request_base_url(route="shares")

        # request
        req_shares = self.api_client.get(
            url=url_shares,
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=(5, 200),
        )

        # checking response
        req_check = checker.check_api_response(req_shares)
        if isinstance(req_check, tuple):
            return req_check

        shares = req_shares.json()

        # if caching use or store the workgroup shares
        if caching and workgroup_id is None:
            self.api_client._shares_names = {
                i.get("name"): i.get("_id") for i in shares
            }
        elif caching:
            self.api_client._wg_shares_names = {
                i.get("name"): i.get("_id") for i in shares
            }
        else:
            pass

        # end of method
        return shares

    @ApiDecorators._check_bearer_validity
    def share(self, share_id: str, include: list = ["_abilities", "groups"]) -> Share:
        """Get details about a specific share.

        :param str share_id: share UUID
        :param list include: additionnal subresource to include in the response
        """
        # check share UUID
        if not checker.check_is_uuid(share_id):
            raise ValueError("Share ID is not a correct UUID.")
        else:
            pass

        # handling request parameters
        payload = {"_include": include}

        # URL
        url_share = utils.get_request_base_url(route="shares/{}".format(share_id))

        # request
        req_share = self.api_client.get(
            url=url_share,
            headers=self.api_client.header,
            params=payload,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_share)
        if isinstance(req_check, tuple):
            return req_check

        # end of method
        return Share(**req_share.json())

    @ApiDecorators._check_bearer_validity
    def create(self, share: object = Share(), check_exists: int = 1) -> Share:
        """Add a new share to Isogeo.

        :param int check_exists: check if a share already exists inot the workgroup:

        - 0 = no check
        - 1 = compare name [DEFAULT]

        :param class share: Share model object to create
        """
        # check if share already exists in workgroup
        if check_exists == 1:
            # retrieve workgroup shares
            if not self.api_client._shares_names:
                self.shares(include=[])
            # check
            if share.name in self.api_client._shares_names:
                logger.debug(
                    "Share with the same name already exists: {}. Use 'share_update' instead.".format(
                        share.name
                    )
                )
                return False
        else:
            pass

        # URL
        url_share_create = utils.get_request_base_url(route="shares")

        # request
        req_new_share = self.api_client.post(
            url=url_share_create,
            json=share.to_dict_creation(),
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_new_share)
        if isinstance(req_check, tuple):
            return req_check

        # load new share and save it to the cache
        new_share = Share(**req_new_share.json())
        self.api_client._shares_names[new_share.name] = new_share._id

        # end of method
        return new_share

    @ApiDecorators._check_bearer_validity
    def delete(self, share_id: str):
        """Delete a share from Isogeo database.

        :param str share_id: identifier of the resource to delete
        """
        # check share UUID
        if not checker.check_is_uuid(share_id):
            raise ValueError("Share ID is not a correct UUID: {}".format(share_id))
        else:
            pass

        # request URL
        url_share_delete = utils.get_request_base_url(
            route="shares/{}".format(share_id)
        )

        # request
        req_share_deletion = self.api_client.delete(
            url=url_share_delete,
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_share_deletion)
        if isinstance(req_check, tuple):
            return req_check

        return req_share_deletion

    @ApiDecorators._check_bearer_validity
    def exists(self, share_id: str) -> bool:
        """Check if the specified share exists and is available for the authenticated user.

        :param str share_id: identifier of the share to verify
        """
        # check share UUID
        if not checker.check_is_uuid(share_id):
            raise ValueError("Share ID is not a correct UUID: {}".format(share_id))
        else:
            pass

        # URL builder
        url_share_exists = "{}{}".format(utils.get_request_base_url("shares"), share_id)

        # request
        req_share_exists = self.api_client.get(
            url_share_exists,
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_share_exists)
        if isinstance(req_check, tuple):
            return req_check

        return req_share_exists

    @ApiDecorators._check_bearer_validity
    def update(self, share: Share, caching: bool = 1) -> Share:
        """Update a share owned by a workgroup.

        :param class share: Share model object to update
        :param bool caching: option to cache the response
        """
        # check share UUID
        if not checker.check_is_uuid(share._id):
            raise ValueError("Share ID is not a correct UUID: {}".format(share._id))
        else:
            pass

        # URL
        url_share_update = utils.get_request_base_url(
            route="shares/{}".format(share._id)
        )

        # request
        req_share_update = self.api_client.put(
            url=url_share_update,
            json=share.to_dict_creation(),
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_share_update)
        if isinstance(req_check, tuple):
            return req_check

        # update share in cache
        new_share = Share(**req_share_update.json())
        if caching:
            self.api_client._shares_names[new_share.name] = new_share._id

        # end of method
        return new_share


# ##############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    """ standalone execution """
    api_share = ApiShare()
