# -*- coding: UTF-8 -*-
#! python3

"""
    Isogeo API v1 - Model of Condition entity

    See: http://help.isogeo.com/api/complete/index.html#definition-resourceCondition
"""

# #############################################################################
# ########## Libraries #############
# ##################################

# standard library
import pprint

# others related models
from isogeo_pysdk.models import License


# #############################################################################
# ########## Classes ###############
# ##################################
class Condition(object):
    """Conditions are entities defining general conditions of use (CGUs) of a data.
    It's mainly composed by a license and a description.

    :param str _id: object UUID
    :param str description: description of the condition
    :param dict license: license object or dict linked to the condition
    :param str parent_resource: UUID of the metadata containing the condition

    :Example:

    .. code-block:: json

        {
            "_id": "string (uuid)",
            "description": "string",
            "license": "string",
        }
    """

    attr_types = {
        "_id": str,
        "description": str,
        "license": License,
        "parent_resource": str,
    }

    attr_crea = {"description": "str", "license": "str"}

    attr_map = {}

    def __init__(
        self,
        _id: str = None,
        description: str = None,
        license: dict or License = None,
        # specific implementation
        parent_resource: str = None,
    ):

        # default values for the object attributes/properties
        self.__id = None
        self._description = None
        self._license = None
        self._parent_resource = None

        # if values have been passed, so use them as objects attributes.
        # attributes are prefixed by an underscore '_'
        if _id is not None:
            self.__id = _id
        if description is not None:
            self._description = description
        if license is not None:
            self._license = License(**license)
        if parent_resource is not None:
            self._parent_resource = parent_resource

    # -- PROPERTIES --------------------------------------------------------------------
    # condition UUID
    @property
    def _id(self) -> str:
        """Gets the id of this Condition.

        :return: The id of this Condition.
        :rtype: str
        """
        return self.__id

    # description
    @property
    def description(self) -> str:
        """Gets the description of this Condition.

        :return: The description of this Condition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Condition.

        :param str description: The description of this Condition. Accept markdown syntax.
        """

        self._description = description

    @property
    def license(self) -> str:
        """Gets the license of this Condition.

        :return: The license of this Condition.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license: dict or License):
        """Sets the license of this Condition.

        :param dict license: The license of this Condition.
        """
        if isinstance(license, License):
            self._license = license
        elif isinstance(license, dict):
            self._license = License(**license)
        else:
            raise Warning(
                "Invalid license parameter ({}) to set as license for this condition.".format(
                    license
                )
            )
            self._license = license

    # parent metadata
    @property
    def parent_resource(self):
        """Gets the parent_resource of this Condition.

        :return: The parent_resource of this Condition.
        :rtype: UUID
        """
        return self._parent_resource

    @parent_resource.setter
    def parent_resource(self, parent_resource_UUID):
        """Sets the parent metadata UUID of this Condition.

        :return: The parent_resource of this Condition.
        :rtype: UUID
        """
        self._parent_resource = parent_resource_UUID

    # -- METHODS -----------------------------------------------------------------------
    def to_dict(self) -> dict:
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.attr_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(Condition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_dict_creation(self) -> dict:
        """Returns the model properties as a dict structured for creation purpose (POST)"""
        result = {}

        for attr, _ in self.attr_crea.items():
            # get attribute value
            value = getattr(self, attr)
            # switch attribute name for creation purpose
            if attr in self.attr_map:
                attr = self.attr_map.get(attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(Condition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other


# ##############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    """ standalone execution """
    lic = Condition(name="Condition Test", description="Test condition description")
    print(lic)
