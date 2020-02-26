# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: master
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1WorkflowWatchEvent(object):
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
        'object': 'V1alpha1Workflow',
        'type': 'str'
    }

    attribute_map = {
        'object': 'object',
        'type': 'type'
    }

    def __init__(self, object=None, type=None):  # noqa: E501
        """V1alpha1WorkflowWatchEvent - a model defined in Swagger"""  # noqa: E501

        self._object = None
        self._type = None
        self.discriminator = None

        if object is not None:
            self.object = object
        if type is not None:
            self.type = type

    @property
    def object(self):
        """Gets the object of this V1alpha1WorkflowWatchEvent.  # noqa: E501


        :return: The object of this V1alpha1WorkflowWatchEvent.  # noqa: E501
        :rtype: V1alpha1Workflow
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this V1alpha1WorkflowWatchEvent.


        :param object: The object of this V1alpha1WorkflowWatchEvent.  # noqa: E501
        :type: V1alpha1Workflow
        """

        self._object = object

    @property
    def type(self):
        """Gets the type of this V1alpha1WorkflowWatchEvent.  # noqa: E501


        :return: The type of this V1alpha1WorkflowWatchEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1alpha1WorkflowWatchEvent.


        :param type: The type of this V1alpha1WorkflowWatchEvent.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(V1alpha1WorkflowWatchEvent, dict):
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
        if not isinstance(other, V1alpha1WorkflowWatchEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other