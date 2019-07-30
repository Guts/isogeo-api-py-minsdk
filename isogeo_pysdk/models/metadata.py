# -*- coding: UTF-8 -*-
#! python3

"""
    Isogeo API v1 - Model of Metadata (= Resource) entity

    See: http://help.isogeo.com/api/complete/index.html#definition-resource
"""

# #############################################################################
# ########## Libraries #############
# ##################################

# standard library
import pprint


# #############################################################################
# ########## Classes ###############
# ##################################
class Metadata(object):
    """Metadata are the main entities in Isogeo, they represent metadata.

    Sample:

    ```json
    {
        "_abilities": [
            "string"
        ],
        "_created": "string (date-time)",
        "_creator": {
            "_abilities": [
            "string"
            ],
            "_created": "string (date-time)",
            "_id": "string (uuid)",
            "_modified": "string (date-time)",
            "areKeywordsRestricted": "boolean",
            "canCreateMetadata": "boolean",
            "code": "string",
            "contact": {
            "_created": "string (date-time)",
            "_id": "string (uuid)",
            "_modified": "string (date-time)",
            "addressLine1": "string",
            "addressLine2": "string",
            "addressLine3": "string",
            "available": "string",
            "city": "string",
            "count": "integer (int32)",
            "countryCode": "string",
            "email": "string",
            "fax": "string",
            "hash": "string",
            "name": "string",
            "organization": "string",
            "phone": "string",
            "type": "string",
            "zipCode": "string"
            },
            "keywordsCasing": "string",
            "metadataLanguage": "string",
            "themeColor": "string"
        },
        "_id": "string (uuid)",
        "_modified": "string (date-time)",
        "abstract": "string",
        "bbox": [
            "number (double)"
        ],
        "collectionContext": "string",
        "collectionMethod": "string",
        "conditions": [
            {
            "_id": "string (uuid)",
            "description": "string",
            "license": {
                "_id": "string (uuid)",
                "content": "string",
                "count": "integer (int32)",
                "link": "string",
                "name": "string"
            }
            }
        ],
        "contacts": [
            {
            "_id": "string (uuid)",
            "contact": {
                "_created": "string (date-time)",
                "_id": "string (uuid)",
                "_modified": "string (date-time)",
                "addressLine1": "string",
                "addressLine2": "string",
                "addressLine3": "string",
                "available": "string",
                "city": "string",
                "count": "integer (int32)",
                "countryCode": "string",
                "email": "string",
                "fax": "string",
                "hash": "string",
                "name": "string",
                "organization": "string",
                "phone": "string",
                "type": "string",
                "zipCode": "string"
            },
            "role": "string"
            }
        ],
        "context": "object",
        "coordinate-system": "object",
        "created": "string (date-time)",
        "distance": "number (double)",
        "editionProfile": "string",
        "encoding": "string",
        "envelope": "object",
        "features": "integer (int32)",
        "format": "string",
        "formatVersion": "string",
        "geometry": "string",
        "height": "integer (int32)",
        "keywords": [
            {}
        ]
        }
    ```

    """

    """
    Attributes:
      attr_types (dict): basic structure of metadata attributes. {"attribute name": "attribute type"}.
      attr_crea (dict): only attributes used to POST requests. {"attribute name": "attribute type"}
      attr_map (dict): mapping between read and write attributes. {"attribute name - GET": "attribute type - POST"}
    """
    attr_types = {
        "_abilities": list,
        "_created": str,
        "_creator": dict,
        "_id": str,
        "_modified": str,
        "abstract": str,
        "collectionContext": str,
        "collectionMethod": str,
        "conditions": list,
        "contacts": list,
        "coordinateSystem": dict,
        "created": str,
        "distance": float,
        "editionProfile": str,
        "encoding": str,
        "envelope": dict,
        "events": dict,
        "featureAttributes": dict,
        "features": int,
        "format": str,
        "formatVersion": str,
        "geometry": str,
        "keywords": list,
        "language": str,
        "layers": list,
        "limitations": list,
        "links": list,
        "modified": str,
        "name": str,
        "path": str,
        "published": str,
        "scale": int,
        "series": bool,
        "serviceLayers": list,
        "specifications": list,
        "tags": list,
        "title": str,
        "topologicalConsistency": str,
        "type": str,
        "updateFrequency": str,
        "validFrom": str,
        "validTo": str,
        "validityComment": str,
    }

    attr_crea = {
        # "_abilities": list,
        # "_creator": dict,
        # "_id": str,
        "abstract": str,
        "collectionContext": str,
        "collectionMethod": str,
        # "created": str,
        # "distance": float,
        # "editionProfile": str,
        "encoding": str,
        # "features": int,
        "format": str,
        "formatVersion": str,
        # "geometry": str,
        # "keywords": list,
        "language": str,
        "layers": list,
        # "modified": str,
        "name": str,
        "path": str,
        "precision": str,
        # "published": str,
        "scale": int,
        "series": bool,
        "serviceLayers": list,
        "title": str,
        "topologicalConsistency": str,
        "type": str,
        "updateFrequency": str,
        # "validFrom": str,
        # "validTo": str,
        # "validityComment": str,
    }

    attr_map = {
        "coordinateSystem": "coordinate-system",
        "featureAttributes": "feature-attributes",
    }

    def __init__(
        self,
        _abilities: list = None,
        _created: str = None,
        _creator: dict = None,
        _id: str = None,
        _modified: str = None,
        abstract: str = None,
        collectionContext: str = None,
        collectionMethod: str = None,
        conditions: list = None,
        contacts: list = None,
        coordinateSystem: dict = None,
        created: str = None,
        distance: float = None,
        editionProfile: str = None,
        encoding: str = None,
        envelope: dict = None,
        events: dict = None,
        featureAttributes: dict = None,
        features: int = None,
        format: str = None,
        formatVersion: str = None,
        geometry: str = None,
        keywords: list = None,
        language: str = None,
        layers: list = None,
        limitations: list = None,
        links: list = None,
        modified: str = None,
        name: str = None,
        operations: list = None,
        path: str = None,
        precision: str = None,
        published: str = None,
        scale: int = None,
        series: bool = None,
        serviceLayers: list = None,
        specifications: list = None,
        tags: list = None,
        title: str = None,
        topologicalConsistency: str = None,
        type: str = None,
        updateFrequency: str = None,
        validFrom: str = None,
        validTo: str = None,
        validityComment: str = None,
    ):
        """Metadata model"""

        # default values for the object attributes/properties
        self.__abilities = None
        self.__created = None
        self.__creator = None
        self.__id = None
        self.__modified = None
        self._abstract = None
        self._collectionContext = None
        self._collectionMethod = None
        self._conditions = None
        self._contacts = None
        self._coordinateSystem = None
        self._created = None
        self._distance = None
        self._editionProfile = None
        self._encoding = None
        self._envelope = None
        self._events = None
        self._featureAttributes = None
        self._features = None
        self._format = None
        self._formatVersion = None
        self._geometry = None
        self._keywords = None
        self._language = None
        self._layers = None
        self._limitations = None
        self._links = None
        self._modified = None
        self._name = None
        self._operations = None
        self._path = None
        self._precision = None
        self._published = None
        self._scale = None
        self._series = None
        self._serviceLayers = None
        self._specifications = None
        self._tags = None
        self._title = None
        self._topologicalConsistency = None
        self._type = None
        self._updateFrequency = None
        self._validFrom = None
        self._validTo = None
        self._validityComment = None

        # if values have been passed, so use them as objects attributes.
        # attributes are prefixed by an underscore '_'
        if _abilities is not None:
            self.__abilities = _abilities
        if _created is not None:
            self.__created = _created
        if _creator is not None:
            self.__creator = _creator
        if _id is not None:
            self.__id = _id
        if _modified is not None:
            self.__modified = _modified
        if abstract is not None:
            self._abstract = abstract
        if collectionContext is not None:
            self._collectionContext = collectionContext
        if collectionMethod is not None:
            self._collectionMethod = collectionMethod
        if conditions is not None:
            self._conditions = conditions
        if contacts is not None:
            self._contacts = contacts
        if coordinateSystem is not None:
            self._coordinateSystem = coordinateSystem
        if created is not None:
            self._created = created
        if distance is not None:
            self._distance = distance
        if editionProfile is not None:
            self._editionProfile = editionProfile
        if encoding is not None:
            self._encoding = encoding
        if envelope is not None:
            self._envelope = envelope
        if events is not None:
            self._events = events
        if featureAttributes is not None:
            self._featureAttributes = featureAttributes
        if features is not None:
            self._features = features
        if format is not None:
            self._format = format
        if geometry is not None:
            self._geometry = geometry
        if keywords is not None:
            self._keywords = keywords
        if language is not None:
            self._language = language
        if layers is not None:
            self._layers = layers
        if limitations is not None:
            self._limitations = limitations
        if links is not None:
            self._links = links
        if modified is not None:
            self._modified = modified
        if name is not None:
            self._name = name
        if operations is not None:
            self._operations = operations
        if path is not None:
            self._path = path
        if precision is not None:
            self._precision = precision
        if published is not None:
            self._published = published
        if scale is not None:
            self._scale = scale
        if serviceLayers is not None:
            self._serviceLayers = serviceLayers
        if specifications is not None:
            self._specifications = specifications
        if tags is not None:
            self._tags = tags
        if title is not None:
            self._title = title
        if topologicalConsistency is not None:
            self._topologicalConsistency = topologicalConsistency
        if type is not None:
            self._type = type
        if updateFrequency is not None:
            self._updateFrequency = updateFrequency
        if validFrom is not None:
            self._validFrom = validFrom
        if validTo is not None:
            self._validTo = validTo
        if validityComment is not None:
            self._validityComment = validityComment

    # -- PROPERTIES --------------------------------------------------------------------
    # abilities of the user related to the metadata
    @property
    def _abilities(self) -> str:
        """Gets the abilities of this Catalog.

        :return: The abilities of this Catalog.
        :rtype: str
        """
        return self.__abilities

    # metadata owner
    @property
    def _creator(self) -> str:
        """Gets the creator of this Catalog.

        :return: The creator of this Metadata.
        :rtype: str
        """
        return self.__creator

    # metadata UUID
    @property
    def _id(self) -> str:
        """Gets the id of this Metadata.

        :return: The id of this Metadata.
        :rtype: str
        """
        return self.__id

    @_id.setter
    def _id(self, _id: str):
        """Sets the id of this Metadata.

        :param str id: The id of this Metadata.
        """

        self.__id = _id

    # metadata description
    @property
    def abstract(self) -> str:
        """Gets the abstract.

        :return: The abstract of this Metadata.
        :rtype: str
        """
        return self._abstract

    @abstract.setter
    def abstract(self, abstract: str):
        """Sets the abstract used into Isogeo filters of this Metadata.

        :param str abstract: the abstract of this Metadata.
        """

        self._abstract = abstract

    # collection context
    @property
    def collectionContext(self) -> str:
        """Gets the collectionContext of this Metadata.

        :return: The collectionContext of this Metadata.
        :rtype: str
        """
        return self._collectionContext

    @collectionContext.setter
    def collectionContext(self, collectionContext: str):
        """Sets the first line of the address of this Metadata.

        :param str collectionContext: The first address line of this Metadata.
        """

        self._collectionContext = collectionContext

    # collection method
    @property
    def collectionMethod(self) -> str:
        """Gets the collectionMethod of this Metadata.

        :return: The collectionMethod of this Metadata.
        :rtype: str
        """
        return self._collectionMethod

    @collectionMethod.setter
    def collectionMethod(self, collectionMethod: str):
        """Sets the first line of the address of this Metadata.

        :param str collectionMethod: The first address line of this Metadata.
        """

        self._collectionMethod = collectionMethod

    # CGUs
    @property
    def conditions(self) -> str:
        """Gets the conditions of this Metadata.

        :return: The conditions of this Metadata.
        :rtype: str
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: str):
        """Sets the first line of the address of this Metadata.

        :param str conditions: The first address line of this Metadata.
        """

        self._conditions = conditions

    # contacts
    @property
    def contacts(self) -> str:
        """Gets the contacts of this Metadata.

        :return: The contacts of this Metadata.
        :rtype: str
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts: str):
        """Sets the first line of the address of this Metadata.

        :param str contacts: The first address line of this Metadata.
        """

        self._contacts = contacts

    # coordinateSystem
    @property
    def coordinateSystem(self) -> str:
        """Gets the coordinateSystem of this Metadata.

        :return: The coordinateSystem of this Metadata.
        :rtype: str
        """
        return self._coordinateSystem

    @coordinateSystem.setter
    def coordinateSystem(self, coordinateSystem: str):
        """Sets the first line of the address of this Metadata.

        :param str coordinateSystem: The first address line of this Metadata.
        """

        self._coordinateSystem = coordinateSystem

    # created
    @property
    def created(self) -> str:
        """Gets the created of this Metadata.

        :return: The created of this Metadata.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created: str):
        """Sets the first line of the address of this Metadata.

        :param str created: The first address line of this Metadata.
        """

        self._created = created

    # distance
    @property
    def distance(self) -> str:
        """Gets the distance of this Metadata.

        :return: The distance of this Metadata.
        :rtype: str
        """
        return self._distance

    @distance.setter
    def distance(self, distance: str):
        """Sets the first line of the address of this Metadata.

        :param str distance: The first address line of this Metadata.
        """

        self._distance = distance

    # editionProfile
    @property
    def editionProfile(self) -> str:
        """Gets the editionProfile of this Metadata.

        :return: The editionProfile of this Metadata.
        :rtype: str
        """
        return self._editionProfile

    @editionProfile.setter
    def editionProfile(self, editionProfile: str):
        """Sets the first line of the address of this Metadata.

        :param str editionProfile: The first address line of this Metadata.
        """

        self._editionProfile = editionProfile

    # encoding
    @property
    def encoding(self) -> str:
        """Gets the encoding of this Metadata.

        :return: The encoding of this Metadata.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding: str):
        """Sets the first line of the address of this Metadata.

        :param str encoding: The first address line of this Metadata.
        """

        self._encoding = encoding

    # envelope
    @property
    def envelope(self) -> str:
        """Gets the envelope of this Metadata.

        :return: The envelope of this Metadata.
        :rtype: str
        """
        return self._envelope

    @envelope.setter
    def envelope(self, envelope: str):
        """Sets the first line of the address of this Metadata.

        :param str envelope: The first address line of this Metadata.
        """

        self._envelope = envelope

    # events
    @property
    def events(self) -> str:
        """Gets the events of this Metadata.

        :return: The events of this Metadata.
        :rtype: str
        """
        return self._events

    @events.setter
    def events(self, events: str):
        """Sets the first line of the address of this Metadata.

        :param str events: The first address line of this Metadata.
        """

        self._events = events

    # featureAttributes
    @property
    def featureAttributes(self) -> str:
        """Gets the featureAttributes of this Metadata.

        :return: The featureAttributes of this Metadata.
        :rtype: str
        """
        return self._featureAttributes

    @featureAttributes.setter
    def featureAttributes(self, featureAttributes: str):
        """Sets the first line of the address of this Metadata.

        :param str featureAttributes: The first address line of this Metadata.
        """

        self._featureAttributes = featureAttributes

    # features
    @property
    def features(self) -> str:
        """Gets the features of this Metadata.

        :return: The features of this Metadata.
        :rtype: str
        """
        return self._features

    @features.setter
    def features(self, features: str):
        """Sets the first line of the address of this Metadata.

        :param str features: The first address line of this Metadata.
        """

        self._features = features

    # format
    @property
    def format(self) -> str:
        """Gets the format of this Metadata.

        :return: The format of this Metadata.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format: str):
        """Sets the first line of the address of this Metadata.

        :param str format: The first address line of this Metadata.
        """

        self._format = format

    # formatVersion
    @property
    def formatVersion(self) -> str:
        """Gets the formatVersion of this Metadata.

        :return: The formatVersion of this Metadata.
        :rtype: str
        """
        return self._formatVersion

    @formatVersion.setter
    def formatVersion(self, formatVersion: str):
        """Sets the first line of the address of this Metadata.

        :param str formatVersion: The first address line of this Metadata.
        """

        self._formatVersion = formatVersion

    # geometry
    @property
    def geometry(self) -> str:
        """Gets the geometry of this Metadata.

        :return: The geometry of this Metadata.
        :rtype: str
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry: str):
        """Sets the first line of the address of this Metadata.

        :param str geometry: The first address line of this Metadata.
        """

        self._geometry = geometry

    # keywords
    @property
    def keywords(self) -> str:
        """Gets the keywords of this Metadata.

        :return: The keywords of this Metadata.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords: str):
        """Sets the first line of the address of this Metadata.

        :param str keywords: The first address line of this Metadata.
        """

        self._keywords = keywords

    # language
    @property
    def language(self) -> str:
        """Gets the language of this Metadata.

        :return: The language of this Metadata.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str):
        """Sets the first line of the address of this Metadata.

        :param str language: The first address line of this Metadata.
        """

        self._language = language

    # layers
    @property
    def layers(self) -> list:
        """Gets the layers of this Metadata.

        :return: The layers of this Metadata.
        :rtype: list
        """
        return self._layers

    @layers.setter
    def layers(self, layers: list):
        """Sets the first line of the address of this Metadata.

        :param list layers: The first address line of this Metadata.
        """

        self._layers = layers

    # limitations
    @property
    def limitations(self) -> str:
        """Gets the limitations of this Metadata.

        :return: The limitations of this Metadata.
        :rtype: str
        """
        return self._limitations

    @limitations.setter
    def limitations(self, limitations: str):
        """Sets the first line of the address of this Metadata.

        :param str limitations: The first address line of this Metadata.
        """

        self._limitations = limitations

    # links
    @property
    def links(self) -> str:
        """Gets the links of this Metadata.

        :return: The links of this Metadata.
        :rtype: str
        """
        return self._links

    @links.setter
    def links(self, links: str):
        """Sets the first line of the address of this Metadata.

        :param str links: The first address line of this Metadata.
        """

        self._links = links

    # modified
    @property
    def modified(self) -> str:
        """Gets the modified of this Metadata.

        :return: The modified of this Metadata.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified: str):
        """Sets the first line of the address of this Metadata.

        :param str modified: The first address line of this Metadata.
        """

        self._modified = modified

    # name
    @property
    def name(self) -> str:
        """Gets the name of this Metadata.

        :return: The name of this Metadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets technical name of the Metadata.

        :param str name: technical name this Metadata.
        """

        self._name = name

    # operations
    @property
    def operations(self) -> list:
        """Gets the operations of this Metadata.

        :return: The operations of this Metadata.
        :rtype: list
        """
        return self._operations

    @operations.setter
    def operations(self, operations: list):
        """Sets the first line of the address of this Metadata.

        :param list operations: The first address line of this Metadata.
        """

        self._operations = operations

    # path
    @property
    def path(self) -> str:
        """Gets the path of this Metadata.

        :return: The path of this Metadata.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the first line of the address of this Metadata.

        :param str path: The first address line of this Metadata.
        """

        self._path = path

    # precision
    @property
    def precision(self) -> str:
        """Gets the precision of this Metadata.

        :return: The precision of this Metadata.
        :rtype: str
        """
        return self._precision

    @precision.setter
    def precision(self, precision: str):
        """Sets the first line of the address of this Metadata.

        :param str precision: The first address line of this Metadata.
        """

        self._precision = precision

    # published
    @property
    def published(self) -> str:
        """Gets the published of this Metadata.

        :return: The published of this Metadata.
        :rtype: str
        """
        return self._published

    @published.setter
    def published(self, published: str):
        """Sets the first line of the address of this Metadata.

        :param str published: The first address line of this Metadata.
        """

        self._published = published

    # scale
    @property
    def scale(self) -> str:
        """Gets the scale of this Metadata.

        :return: The scale of this Metadata.
        :rtype: str
        """
        return self._scale

    @scale.setter
    def scale(self, scale: str):
        """Sets the first line of the address of this Metadata.

        :param str scale: The first address line of this Metadata.
        """

        self._scale = scale

    # series
    @property
    def series(self) -> str:
        """Gets the series of this Metadata.

        :return: The series of this Metadata.
        :rtype: str
        """
        return self._series

    @series.setter
    def series(self, series: str):
        """Sets the first line of the address of this Metadata.

        :param str series: The first address line of this Metadata.
        """

        self._series = series

    # serviceLayers
    @property
    def serviceLayers(self) -> list:
        """Gets the serviceLayers of this Metadata.

        :return: The serviceLayers of this Metadata.
        :rtype: list
        """
        return self._serviceLayers

    @serviceLayers.setter
    def serviceLayers(self, serviceLayers: list):
        """Sets the first line of the address of this Metadata.

        :param list serviceLayers: The first address line of this Metadata.
        """

        self._serviceLayers = serviceLayers

    # specifications
    @property
    def specifications(self) -> str:
        """Gets the specifications of this Metadata.

        :return: The specifications of this Metadata.
        :rtype: str
        """
        return self._specifications

    @specifications.setter
    def specifications(self, specifications: str):
        """Sets the first line of the address of this Metadata.

        :param str specifications: The first address line of this Metadata.
        """

        self._specifications = specifications

    # tags
    @property
    def tags(self) -> str:
        """Gets the tags of this Metadata.

        :return: The tags of this Metadata.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags: str):
        """Sets the first line of the address of this Metadata.

        :param str tags: The first address line of this Metadata.
        """

        self._tags = tags

    # title
    @property
    def title(self) -> str:
        """Gets the title of this Metadata.

        :return: The title of this Metadata.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the first line of the address of this Metadata.

        :param str title: The first address line of this Metadata.
        """

        self._title = title

    # topologicalConsistency
    @property
    def topologicalConsistency(self) -> str:
        """Gets the topologicalConsistency of this Metadata.

        :return: The topologicalConsistency of this Metadata.
        :rtype: str
        """
        return self._topologicalConsistency

    @topologicalConsistency.setter
    def topologicalConsistency(self, topologicalConsistency: str):
        """Sets the first line of the address of this Metadata.

        :param str topologicalConsistency: The first address line of this Metadata.
        """

        self._topologicalConsistency = topologicalConsistency

    # type
    @property
    def type(self) -> str:
        """Gets the type of this Metadata.

        :return: The type of this Metadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Metadata.

        :param str type: The type of this Metadata.
        """

        self._type = type

    # updateFrequency
    @property
    def updateFrequency(self) -> str:
        """Gets the updateFrequency of this Metadata.

        :return: The updateFrequency of this Metadata.
        :rtype: str
        """
        return self._updateFrequency

    @updateFrequency.setter
    def updateFrequency(self, updateFrequency: str):
        """Sets the first line of the address of this Metadata.

        :param str updateFrequency: The first address line of this Metadata.
        """

        self._updateFrequency = updateFrequency

    # validFrom
    @property
    def validFrom(self) -> str:
        """Gets the validFrom of this Metadata.

        :return: The validFrom of this Metadata.
        :rtype: str
        """
        return self._validFrom

    @validFrom.setter
    def validFrom(self, validFrom: str):
        """Sets the first line of the address of this Metadata.

        :param str validFrom: The first address line of this Metadata.
        """

        self._validFrom = validFrom

    # validTo
    @property
    def validTo(self) -> str:
        """Gets the validTo of this Metadata.

        :return: The validTo of this Metadata.
        :rtype: str
        """
        return self._validTo

    @validTo.setter
    def validTo(self, validTo: str):
        """Sets the first line of the address of this Metadata.

        :param str validTo: The first address line of this Metadata.
        """

        self._validTo = validTo

    # validityComment
    @property
    def validityComment(self) -> str:
        """Gets the validityComment of this Metadata.

        :return: The validityComment of this Metadata.
        :rtype: str
        """
        return self._validityComment

    @validityComment.setter
    def validityComment(self, validityComment: str):
        """Sets the first line of the address of this Metadata.

        :param str validityComment: The first address line of this Metadata.
        """

        self._validityComment = validityComment

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
        if issubclass(Metadata, dict):
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
        if issubclass(Metadata, dict):
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
        if not isinstance(other, Metadata):
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
    md = Metadata()
    print(md)