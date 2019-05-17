# -*- coding: UTF-8 -*-
#! python3

"""
    Isogeo API v1 - API Routes for Workgroups entities

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
from isogeo_pysdk.models import Contact, Workgroup
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
class ApiWorkgroup:
    """Routes as methods of Isogeo API used to manipulate workgroups (conditions).
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
        super(ApiWorkgroup, self).__init__()

    @ApiDecorators._check_bearer_validity
    def workgroups(
        self, include: list = ["_abilities", "limits"], caching: bool = 1
    ) -> list:
        """Get workgroups.

        :param list include: additionnal subresource to include in the response
        :param bool caching: option to cache the response
        """
        # handling request parameters
        payload = {"_include": include}

        # request URL
        url_workgroups = utils.get_request_base_url(route="groups")

        # request
        req_workgroups = self.api_client.get(
            url=url_workgroups,
            headers=self.api_client.header,
            params=payload,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_workgroups)
        if isinstance(req_check, tuple):
            return req_check

        wg_workgroups = req_workgroups.json()

        # if caching use or store the workgroup workgroups
        if caching:
            self.api_client._workgroups_names = {
                i.get("contact").get("name"): i.get("_id") for i in wg_workgroups
            }
            pass

        # end of method
        return wg_workgroups

    @ApiDecorators._check_bearer_validity
    def workgroup(
        self, workgroup_id: str, include: list = ["_abilities", "limits"]
    ) -> Workgroup:
        """Get details about a specific workgroup.

        :param str workgroup_id: workgroup UUID
        :param list include: additionnal subresource to include in the response
        """
        # check workgroup UUID
        if not checker.check_is_uuid(workgroup_id):
            raise ValueError("Workgroup ID is not a correct UUID.")
        else:
            pass

        # handling request parameters
        payload = {"_include": include}

        # URL
        url_workgroup = utils.get_request_base_url(
            route="groups/{}".format(workgroup_id)
        )

        # request
        req_workgroup = self.api_client.get(
            url=url_workgroup,
            headers=self.api_client.header,
            params=payload,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_workgroup)
        if isinstance(req_check, tuple):
            return req_check

        # end of method
        return Workgroup(**req_workgroup.json())

    @ApiDecorators._check_bearer_validity
    def workgroup_create(
        self, workgroup: object = Workgroup(), check_exists: int = 1
    ) -> Workgroup:
        """Add a new workgroup to Isogeo.

        :param class workgroup: Workgroup model object to create
        :param int check_exists: check if a workgroup already exists:

        - 0 = no check
        - 1 = compare name [DEFAULT]

        """
        # check if object has a correct contact
        if not hasattr(workgroup, "contact") or not isinstance(
            workgroup.contact, Contact
        ):
            raise ValueError(
                "`workgroup.contact.name`is required to create a workgroup."
            )

        # check if workgroup already exists in workgroup
        if check_exists == 1:
            # retrieve workgroup workgroups
            if not self.api_client._workgroups_names:
                self.workgroups(include=[])
            # check
            if workgroup.contact.name in self.api_client._workgroups_names:
                logger.debug(
                    "Workgroup with the same name already exists: {}. Use 'workgroup_update' instead.".format(
                        workgroup.contact.name
                    )
                )
                return False
        else:
            pass

        # URL
        url_workgroup_create = utils.get_request_base_url(route="groups")

        # request
        req_new_workgroup = self.api_client.post(
            url=url_workgroup_create,
            data=workgroup.to_dict_creation(),
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_new_workgroup)
        if isinstance(req_check, tuple):
            return req_check

        # load new workgroup and save it to the cache
        new_workgroup = Workgroup(**req_new_workgroup.json())
        self.api_client._workgroups_names[
            new_workgroup.contact.get("name")
        ] = new_workgroup._id

        # end of method
        return new_workgroup

    @ApiDecorators._check_bearer_validity
    def workgroup_delete(self, workgroup_id: str):
        """Delete a workgroup from Isogeo database.

        :param str workgroup_id: identifier of the workgroup
        """
        # check workgroup UUID
        if not checker.check_is_uuid(workgroup_id):
            raise ValueError(
                "Workgroup ID is not a correct UUID: {}".format(workgroup_id)
            )
        else:
            pass

        # URL
        url_workgroup_delete = utils.get_request_base_url(
            route="groups/{}".format(workgroup_id)
        )

        # request
        req_workgroup_deletion = self.api_client.delete(
            url=url_workgroup_delete,
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_workgroup_deletion)
        if isinstance(req_check, tuple):
            return req_check

        return req_workgroup_deletion

    @ApiDecorators._check_bearer_validity
    def workgroup_exists(self, workgroup_id: str) -> bool:
        """Check if the specified workgroup exists and is available for the authenticated user.

        :param str workgroup_id: identifier of the workgroup to verify
        """
        # check workgroup UUID
        if not checker.check_is_uuid(workgroup_id):
            raise ValueError(
                "Workgroup ID is not a correct UUID: {}".format(workgroup_id)
            )
        else:
            pass

        # URL builder
        url_workgroup_exists = utils.get_request_base_url(
            route="groups/{}".format(workgroup_id)
        )

        # request
        req_workgroup_exists = self.api_client.get(
            url=url_workgroup_exists,
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_workgroup_exists)
        if isinstance(req_check, tuple):
            return req_check

        return req_workgroup_exists

    @ApiDecorators._check_bearer_validity
    def workgroup_update(self, workgroup: Workgroup, caching: bool = 1) -> Workgroup:
        """Update a workgroup owned by a workgroup.

        :param class workgroup: Workgroup model object to update
        :param bool caching: option to cache the response
        """
        # check workgroup UUID
        if not checker.check_is_uuid(workgroup._id):
            raise ValueError(
                "Workgroup ID is not a correct UUID: {}".format(workgroup._id)
            )
        else:
            pass

        # URL
        url_workgroup_update = utils.get_request_base_url(
            route="groups/{}".format(workgroup._id)
        )

        # request
        req_workgroup_update = self.api_client.put(
            url=url_workgroup_update,
            json=workgroup.to_dict(),
            headers=self.api_client.header,
            proxies=self.api_client.proxies,
            verify=self.api_client.ssl,
            timeout=self.api_client.timeout,
        )

        # checking response
        req_check = checker.check_api_response(req_workgroup_update)
        if isinstance(req_check, tuple):
            return req_check

        # update workgroup in cache
        workgroup_updated = Workgroup(**req_workgroup_update.json())
        if caching:
            self.api_client._workgroups_names[
                workgroup_updated.contact.get("name")
            ] = workgroup_updated._id

        # end of method
        return workgroup_updated


# ##############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    """ standalone execution """
    api_workgroup = ApiWorkgroup()
