# coding: utf-8

"""
    qg_api

    qualys guard rest api  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Vulner(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'qid': 'int',
        'patch_qid': 'int',
        'severity': 'str',
        'title': 'str',
        'category': 'int'
    }

    attribute_map = {
        'qid': 'qid',
        'patch_qid': 'patch_qid',
        'severity': 'severity',
        'title': 'title',
        'category': 'category'
    }

    def __init__(self, qid=None, patch_qid=None, severity=None, title=None, category=None):  # noqa: E501
        """Vulner - a model defined in Swagger"""  # noqa: E501
        self._qid = None
        self._patch_qid = None
        self._severity = None
        self._title = None
        self._category = None
        self.discriminator = None
        if qid is not None:
            self.qid = qid
        if patch_qid is not None:
            self.patch_qid = patch_qid
        if severity is not None:
            self.severity = severity
        if title is not None:
            self.title = title
        if category is not None:
            self.category = category

    @property
    def qid(self):
        """Gets the qid of this Vulner.  # noqa: E501


        :return: The qid of this Vulner.  # noqa: E501
        :rtype: int
        """
        return self._qid

    @qid.setter
    def qid(self, qid):
        """Sets the qid of this Vulner.


        :param qid: The qid of this Vulner.  # noqa: E501
        :type: int
        """

        self._qid = qid

    @property
    def patch_qid(self):
        """Gets the patch_qid of this Vulner.  # noqa: E501


        :return: The patch_qid of this Vulner.  # noqa: E501
        :rtype: int
        """
        return self._patch_qid

    @patch_qid.setter
    def patch_qid(self, patch_qid):
        """Sets the patch_qid of this Vulner.


        :param patch_qid: The patch_qid of this Vulner.  # noqa: E501
        :type: int
        """

        self._patch_qid = patch_qid

    @property
    def severity(self):
        """Gets the severity of this Vulner.  # noqa: E501


        :return: The severity of this Vulner.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Vulner.


        :param severity: The severity of this Vulner.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def title(self):
        """Gets the title of this Vulner.  # noqa: E501


        :return: The title of this Vulner.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Vulner.


        :param title: The title of this Vulner.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def category(self):
        """Gets the category of this Vulner.  # noqa: E501


        :return: The category of this Vulner.  # noqa: E501
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Vulner.


        :param category: The category of this Vulner.  # noqa: E501
        :type: int
        """

        self._category = category

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Vulner, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Vulner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
