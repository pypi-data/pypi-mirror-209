# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_rpm.configuration import Configuration


class RpmRpmPublicationResponse(object):
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
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'repository_version': 'str',
        'repository': 'str',
        'metadata_checksum_type': 'MetadataChecksumTypeEnum',
        'package_checksum_type': 'PackageChecksumTypeEnum',
        'gpgcheck': 'int',
        'repo_gpgcheck': 'int',
        'sqlite_metadata': 'bool'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'repository_version': 'repository_version',
        'repository': 'repository',
        'metadata_checksum_type': 'metadata_checksum_type',
        'package_checksum_type': 'package_checksum_type',
        'gpgcheck': 'gpgcheck',
        'repo_gpgcheck': 'repo_gpgcheck',
        'sqlite_metadata': 'sqlite_metadata'
    }

    def __init__(self, pulp_href=None, pulp_created=None, repository_version=None, repository=None, metadata_checksum_type=None, package_checksum_type=None, gpgcheck=None, repo_gpgcheck=None, sqlite_metadata=False, local_vars_configuration=None):  # noqa: E501
        """RpmRpmPublicationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._repository_version = None
        self._repository = None
        self._metadata_checksum_type = None
        self._package_checksum_type = None
        self._gpgcheck = None
        self._repo_gpgcheck = None
        self._sqlite_metadata = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if repository_version is not None:
            self.repository_version = repository_version
        if repository is not None:
            self.repository = repository
        if metadata_checksum_type is not None:
            self.metadata_checksum_type = metadata_checksum_type
        if package_checksum_type is not None:
            self.package_checksum_type = package_checksum_type
        if gpgcheck is not None:
            self.gpgcheck = gpgcheck
        if repo_gpgcheck is not None:
            self.repo_gpgcheck = repo_gpgcheck
        if sqlite_metadata is not None:
            self.sqlite_metadata = sqlite_metadata

    @property
    def pulp_href(self):
        """Gets the pulp_href of this RpmRpmPublicationResponse.  # noqa: E501


        :return: The pulp_href of this RpmRpmPublicationResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this RpmRpmPublicationResponse.


        :param pulp_href: The pulp_href of this RpmRpmPublicationResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this RpmRpmPublicationResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this RpmRpmPublicationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this RpmRpmPublicationResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this RpmRpmPublicationResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def repository_version(self):
        """Gets the repository_version of this RpmRpmPublicationResponse.  # noqa: E501


        :return: The repository_version of this RpmRpmPublicationResponse.  # noqa: E501
        :rtype: str
        """
        return self._repository_version

    @repository_version.setter
    def repository_version(self, repository_version):
        """Sets the repository_version of this RpmRpmPublicationResponse.


        :param repository_version: The repository_version of this RpmRpmPublicationResponse.  # noqa: E501
        :type: str
        """

        self._repository_version = repository_version

    @property
    def repository(self):
        """Gets the repository of this RpmRpmPublicationResponse.  # noqa: E501

        A URI of the repository to be published.  # noqa: E501

        :return: The repository of this RpmRpmPublicationResponse.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this RpmRpmPublicationResponse.

        A URI of the repository to be published.  # noqa: E501

        :param repository: The repository of this RpmRpmPublicationResponse.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def metadata_checksum_type(self):
        """Gets the metadata_checksum_type of this RpmRpmPublicationResponse.  # noqa: E501

        The checksum type for metadata.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :return: The metadata_checksum_type of this RpmRpmPublicationResponse.  # noqa: E501
        :rtype: MetadataChecksumTypeEnum
        """
        return self._metadata_checksum_type

    @metadata_checksum_type.setter
    def metadata_checksum_type(self, metadata_checksum_type):
        """Sets the metadata_checksum_type of this RpmRpmPublicationResponse.

        The checksum type for metadata.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :param metadata_checksum_type: The metadata_checksum_type of this RpmRpmPublicationResponse.  # noqa: E501
        :type: MetadataChecksumTypeEnum
        """

        self._metadata_checksum_type = metadata_checksum_type

    @property
    def package_checksum_type(self):
        """Gets the package_checksum_type of this RpmRpmPublicationResponse.  # noqa: E501

        The checksum type for packages.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :return: The package_checksum_type of this RpmRpmPublicationResponse.  # noqa: E501
        :rtype: PackageChecksumTypeEnum
        """
        return self._package_checksum_type

    @package_checksum_type.setter
    def package_checksum_type(self, package_checksum_type):
        """Sets the package_checksum_type of this RpmRpmPublicationResponse.

        The checksum type for packages.  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512  # noqa: E501

        :param package_checksum_type: The package_checksum_type of this RpmRpmPublicationResponse.  # noqa: E501
        :type: PackageChecksumTypeEnum
        """

        self._package_checksum_type = package_checksum_type

    @property
    def gpgcheck(self):
        """Gets the gpgcheck of this RpmRpmPublicationResponse.  # noqa: E501

        An option specifying whether a client should perform a GPG signature check on packages.  # noqa: E501

        :return: The gpgcheck of this RpmRpmPublicationResponse.  # noqa: E501
        :rtype: int
        """
        return self._gpgcheck

    @gpgcheck.setter
    def gpgcheck(self, gpgcheck):
        """Sets the gpgcheck of this RpmRpmPublicationResponse.

        An option specifying whether a client should perform a GPG signature check on packages.  # noqa: E501

        :param gpgcheck: The gpgcheck of this RpmRpmPublicationResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                gpgcheck is not None and gpgcheck > 1):  # noqa: E501
            raise ValueError("Invalid value for `gpgcheck`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                gpgcheck is not None and gpgcheck < 0):  # noqa: E501
            raise ValueError("Invalid value for `gpgcheck`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gpgcheck = gpgcheck

    @property
    def repo_gpgcheck(self):
        """Gets the repo_gpgcheck of this RpmRpmPublicationResponse.  # noqa: E501

        An option specifying whether a client should perform a GPG signature check on the repodata.  # noqa: E501

        :return: The repo_gpgcheck of this RpmRpmPublicationResponse.  # noqa: E501
        :rtype: int
        """
        return self._repo_gpgcheck

    @repo_gpgcheck.setter
    def repo_gpgcheck(self, repo_gpgcheck):
        """Sets the repo_gpgcheck of this RpmRpmPublicationResponse.

        An option specifying whether a client should perform a GPG signature check on the repodata.  # noqa: E501

        :param repo_gpgcheck: The repo_gpgcheck of this RpmRpmPublicationResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                repo_gpgcheck is not None and repo_gpgcheck > 1):  # noqa: E501
            raise ValueError("Invalid value for `repo_gpgcheck`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                repo_gpgcheck is not None and repo_gpgcheck < 0):  # noqa: E501
            raise ValueError("Invalid value for `repo_gpgcheck`, must be a value greater than or equal to `0`")  # noqa: E501

        self._repo_gpgcheck = repo_gpgcheck

    @property
    def sqlite_metadata(self):
        """Gets the sqlite_metadata of this RpmRpmPublicationResponse.  # noqa: E501

        DEPRECATED: An option specifying whether Pulp should generate SQLite metadata.  # noqa: E501

        :return: The sqlite_metadata of this RpmRpmPublicationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._sqlite_metadata

    @sqlite_metadata.setter
    def sqlite_metadata(self, sqlite_metadata):
        """Sets the sqlite_metadata of this RpmRpmPublicationResponse.

        DEPRECATED: An option specifying whether Pulp should generate SQLite metadata.  # noqa: E501

        :param sqlite_metadata: The sqlite_metadata of this RpmRpmPublicationResponse.  # noqa: E501
        :type: bool
        """

        self._sqlite_metadata = sqlite_metadata

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
        if not isinstance(other, RpmRpmPublicationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmRpmPublicationResponse):
            return True

        return self.to_dict() != other.to_dict()
