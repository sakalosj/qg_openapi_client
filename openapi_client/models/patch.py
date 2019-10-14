# coding: utf-8

"""
    qg_api

    qualys guard rest api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Patch(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'qid': 'int',
        'severity': 'int',
        'title': 'str',
        'vulners': 'list[Vulner]'
    }

    attribute_map = {
        'qid': 'qid',
        'severity': 'severity',
        'title': 'title',
        'vulners': 'vulners'
    }

    def __init__(self, qid=None, severity=None, title=None, vulners=None):  # noqa: E501
        """Patch - a model defined in OpenAPI"""  # noqa: E501

        self._qid = None
        self._severity = None
        self._title = None
        self._vulners = None
        self.discriminator = None

        if qid is not None:
            self.qid = qid
        if severity is not None:
            self.severity = severity
        if title is not None:
            self.title = title
        if vulners is not None:
            self.vulners = vulners

    @property
    def qid(self):
        """Gets the qid of this Patch.  # noqa: E501


        :return: The qid of this Patch.  # noqa: E501
        :rtype: int
        """
        return self._qid

    @qid.setter
    def qid(self, qid):
        """Sets the qid of this Patch.


        :param qid: The qid of this Patch.  # noqa: E501
        :type: int
        """

        self._qid = qid

    @property
    def severity(self):
        """Gets the severity of this Patch.  # noqa: E501


        :return: The severity of this Patch.  # noqa: E501
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Patch.


        :param severity: The severity of this Patch.  # noqa: E501
        :type: int
        """

        self._severity = severity

    @property
    def title(self):
        """Gets the title of this Patch.  # noqa: E501


        :return: The title of this Patch.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Patch.


        :param title: The title of this Patch.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def vulners(self):
        """Gets the vulners of this Patch.  # noqa: E501


        :return: The vulners of this Patch.  # noqa: E501
        :rtype: list[Vulner]
        """
        return self._vulners

    @vulners.setter
    def vulners(self, vulners):
        """Sets the vulners of this Patch.


        :param vulners: The vulners of this Patch.  # noqa: E501
        :type: list[Vulner]
        """

        self._vulners = vulners

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Patch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
