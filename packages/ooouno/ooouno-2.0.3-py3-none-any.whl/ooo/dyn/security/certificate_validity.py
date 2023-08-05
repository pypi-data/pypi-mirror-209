# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.security
import uno
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class CertificateValidity(metaclass=UnoConstMeta, type_name="com.sun.star.security.CertificateValidity", name_space="com.sun.star.security"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.security.CertificateValidity``"""
        pass

    class CertificateValidityEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.security.CertificateValidity", name_space="com.sun.star.security"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.security.CertificateValidity`` as Enum values"""
        pass

else:
    from com.sun.star.security import CertificateValidity as CertificateValidity

    class CertificateValidityEnum(IntFlag):
        """
        Enum of Const Class CertificateValidity

        Constant definition of a certificate characters.
        
        The certificate characters will be defined as bit-wise constants.
        """
        VALID = CertificateValidity.VALID
        INVALID = CertificateValidity.INVALID
        """
        The certificate is invalid.
        """
        UNTRUSTED = CertificateValidity.UNTRUSTED
        """
        The certificate itself is untrusted.
        """
        TIME_INVALID = CertificateValidity.TIME_INVALID
        """
        The current time is not in the range of time for which the certificate is valid.
        """
        NOT_TIME_NESTED = CertificateValidity.NOT_TIME_NESTED
        """
        The time range of a certificate does not fall within the time range of the issuing certificate.
        """
        REVOKED = CertificateValidity.REVOKED
        """
        It is a revoked certificate.
        """
        UNKNOWN_REVOKATION = CertificateValidity.UNKNOWN_REVOKATION
        """
        The certificate revocation status is unknown.
        """
        SIGNATURE_INVALID = CertificateValidity.SIGNATURE_INVALID
        """
        The certificate signature is invalid.
        """
        EXTENSION_INVALID = CertificateValidity.EXTENSION_INVALID
        """
        The certificate has invalid extensions.
        """
        EXTENSION_UNKNOWN = CertificateValidity.EXTENSION_UNKNOWN
        """
        The certificate has critical unknown extensions.
        """
        ISSUER_UNKNOWN = CertificateValidity.ISSUER_UNKNOWN
        """
        The certificate issuer is unknown.
        """
        ISSUER_UNTRUSTED = CertificateValidity.ISSUER_UNTRUSTED
        """
        The certificate issuer is untrusted.
        """
        ISSUER_INVALID = CertificateValidity.ISSUER_INVALID
        """
        The certificate issuer is invalid.
        """
        ROOT_UNKNOWN = CertificateValidity.ROOT_UNKNOWN
        """
        The root certificate is unknown.
        """
        ROOT_UNTRUSTED = CertificateValidity.ROOT_UNTRUSTED
        """
        The root certificate is untrusted.
        """
        ROOT_INVALID = CertificateValidity.ROOT_INVALID
        """
        The root certificate is invalid.
        """
        CHAIN_INCOMPLETE = CertificateValidity.CHAIN_INCOMPLETE
        """
        The certificate chain is incomplete.
        """

__all__ = ['CertificateValidity', 'CertificateValidityEnum']
