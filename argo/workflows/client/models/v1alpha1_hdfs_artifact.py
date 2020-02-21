# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: 2.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.models import V1ConfigMapKeySelector
from kubernetes.client.models import V1SecretKeySelector

class V1alpha1HDFSArtifact(object):
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
        'addresses': 'list[str]',
        'force': 'bool',
        'hdfs_user': 'str',
        'krb_c_cache_secret': 'V1SecretKeySelector',
        'krb_config_config_map': 'V1ConfigMapKeySelector',
        'krb_keytab_secret': 'V1SecretKeySelector',
        'krb_realm': 'str',
        'krb_service_principal_name': 'str',
        'krb_username': 'str',
        'path': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'force': 'force',
        'hdfs_user': 'hdfsUser',
        'krb_c_cache_secret': 'krbCCacheSecret',
        'krb_config_config_map': 'krbConfigConfigMap',
        'krb_keytab_secret': 'krbKeytabSecret',
        'krb_realm': 'krbRealm',
        'krb_service_principal_name': 'krbServicePrincipalName',
        'krb_username': 'krbUsername',
        'path': 'path'
    }

    def __init__(self, addresses=None, force=None, hdfs_user=None, krb_c_cache_secret=None, krb_config_config_map=None, krb_keytab_secret=None, krb_realm=None, krb_service_principal_name=None, krb_username=None, path=None):  # noqa: E501
        """V1alpha1HDFSArtifact - a model defined in Swagger"""  # noqa: E501

        self._addresses = None
        self._force = None
        self._hdfs_user = None
        self._krb_c_cache_secret = None
        self._krb_config_config_map = None
        self._krb_keytab_secret = None
        self._krb_realm = None
        self._krb_service_principal_name = None
        self._krb_username = None
        self._path = None
        self.discriminator = None

        self.addresses = addresses
        if force is not None:
            self.force = force
        if hdfs_user is not None:
            self.hdfs_user = hdfs_user
        if krb_c_cache_secret is not None:
            self.krb_c_cache_secret = krb_c_cache_secret
        if krb_config_config_map is not None:
            self.krb_config_config_map = krb_config_config_map
        if krb_keytab_secret is not None:
            self.krb_keytab_secret = krb_keytab_secret
        if krb_realm is not None:
            self.krb_realm = krb_realm
        if krb_service_principal_name is not None:
            self.krb_service_principal_name = krb_service_principal_name
        if krb_username is not None:
            self.krb_username = krb_username
        self.path = path

    @property
    def addresses(self):
        """Gets the addresses of this V1alpha1HDFSArtifact.  # noqa: E501

        Addresses is accessible addresses of HDFS name nodes  # noqa: E501

        :return: The addresses of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this V1alpha1HDFSArtifact.

        Addresses is accessible addresses of HDFS name nodes  # noqa: E501

        :param addresses: The addresses of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: list[str]
        """
        if addresses is None:
            raise ValueError("Invalid value for `addresses`, must not be `None`")  # noqa: E501

        self._addresses = addresses

    @property
    def force(self):
        """Gets the force of this V1alpha1HDFSArtifact.  # noqa: E501

        Force copies a file forcibly even if it exists (default: false)  # noqa: E501

        :return: The force of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this V1alpha1HDFSArtifact.

        Force copies a file forcibly even if it exists (default: false)  # noqa: E501

        :param force: The force of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def hdfs_user(self):
        """Gets the hdfs_user of this V1alpha1HDFSArtifact.  # noqa: E501

        HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used.  # noqa: E501

        :return: The hdfs_user of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: str
        """
        return self._hdfs_user

    @hdfs_user.setter
    def hdfs_user(self, hdfs_user):
        """Sets the hdfs_user of this V1alpha1HDFSArtifact.

        HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used.  # noqa: E501

        :param hdfs_user: The hdfs_user of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: str
        """

        self._hdfs_user = hdfs_user

    @property
    def krb_c_cache_secret(self):
        """Gets the krb_c_cache_secret of this V1alpha1HDFSArtifact.  # noqa: E501

        KrbCCacheSecret is the secret selector for Kerberos ccache Either ccache or keytab can be set to use Kerberos.  # noqa: E501

        :return: The krb_c_cache_secret of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._krb_c_cache_secret

    @krb_c_cache_secret.setter
    def krb_c_cache_secret(self, krb_c_cache_secret):
        """Sets the krb_c_cache_secret of this V1alpha1HDFSArtifact.

        KrbCCacheSecret is the secret selector for Kerberos ccache Either ccache or keytab can be set to use Kerberos.  # noqa: E501

        :param krb_c_cache_secret: The krb_c_cache_secret of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._krb_c_cache_secret = krb_c_cache_secret

    @property
    def krb_config_config_map(self):
        """Gets the krb_config_config_map of this V1alpha1HDFSArtifact.  # noqa: E501

        KrbConfig is the configmap selector for Kerberos config as string It must be set if either ccache or keytab is used.  # noqa: E501

        :return: The krb_config_config_map of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: V1ConfigMapKeySelector
        """
        return self._krb_config_config_map

    @krb_config_config_map.setter
    def krb_config_config_map(self, krb_config_config_map):
        """Sets the krb_config_config_map of this V1alpha1HDFSArtifact.

        KrbConfig is the configmap selector for Kerberos config as string It must be set if either ccache or keytab is used.  # noqa: E501

        :param krb_config_config_map: The krb_config_config_map of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: V1ConfigMapKeySelector
        """

        self._krb_config_config_map = krb_config_config_map

    @property
    def krb_keytab_secret(self):
        """Gets the krb_keytab_secret of this V1alpha1HDFSArtifact.  # noqa: E501

        KrbKeytabSecret is the secret selector for Kerberos keytab Either ccache or keytab can be set to use Kerberos.  # noqa: E501

        :return: The krb_keytab_secret of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._krb_keytab_secret

    @krb_keytab_secret.setter
    def krb_keytab_secret(self, krb_keytab_secret):
        """Sets the krb_keytab_secret of this V1alpha1HDFSArtifact.

        KrbKeytabSecret is the secret selector for Kerberos keytab Either ccache or keytab can be set to use Kerberos.  # noqa: E501

        :param krb_keytab_secret: The krb_keytab_secret of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._krb_keytab_secret = krb_keytab_secret

    @property
    def krb_realm(self):
        """Gets the krb_realm of this V1alpha1HDFSArtifact.  # noqa: E501

        KrbRealm is the Kerberos realm used with Kerberos keytab It must be set if keytab is used.  # noqa: E501

        :return: The krb_realm of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: str
        """
        return self._krb_realm

    @krb_realm.setter
    def krb_realm(self, krb_realm):
        """Sets the krb_realm of this V1alpha1HDFSArtifact.

        KrbRealm is the Kerberos realm used with Kerberos keytab It must be set if keytab is used.  # noqa: E501

        :param krb_realm: The krb_realm of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: str
        """

        self._krb_realm = krb_realm

    @property
    def krb_service_principal_name(self):
        """Gets the krb_service_principal_name of this V1alpha1HDFSArtifact.  # noqa: E501

        KrbServicePrincipalName is the principal name of Kerberos service It must be set if either ccache or keytab is used.  # noqa: E501

        :return: The krb_service_principal_name of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: str
        """
        return self._krb_service_principal_name

    @krb_service_principal_name.setter
    def krb_service_principal_name(self, krb_service_principal_name):
        """Sets the krb_service_principal_name of this V1alpha1HDFSArtifact.

        KrbServicePrincipalName is the principal name of Kerberos service It must be set if either ccache or keytab is used.  # noqa: E501

        :param krb_service_principal_name: The krb_service_principal_name of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: str
        """

        self._krb_service_principal_name = krb_service_principal_name

    @property
    def krb_username(self):
        """Gets the krb_username of this V1alpha1HDFSArtifact.  # noqa: E501

        KrbUsername is the Kerberos username used with Kerberos keytab It must be set if keytab is used.  # noqa: E501

        :return: The krb_username of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: str
        """
        return self._krb_username

    @krb_username.setter
    def krb_username(self, krb_username):
        """Sets the krb_username of this V1alpha1HDFSArtifact.

        KrbUsername is the Kerberos username used with Kerberos keytab It must be set if keytab is used.  # noqa: E501

        :param krb_username: The krb_username of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: str
        """

        self._krb_username = krb_username

    @property
    def path(self):
        """Gets the path of this V1alpha1HDFSArtifact.  # noqa: E501

        Path is a file path in HDFS  # noqa: E501

        :return: The path of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1alpha1HDFSArtifact.

        Path is a file path in HDFS  # noqa: E501

        :param path: The path of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

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
        if issubclass(V1alpha1HDFSArtifact, dict):
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
        if not isinstance(other, V1alpha1HDFSArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
