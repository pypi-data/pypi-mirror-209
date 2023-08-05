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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.animations
import typing
from abc import abstractproperty
from .x_animation_node import XAnimationNode as XAnimationNode_1cf10eb9
if typing.TYPE_CHECKING:
    from .time_filter_pair import TimeFilterPair as TimeFilterPair_1d250ebc

class XAnimate(XAnimationNode_1cf10eb9):
    """
    Interface for generic animation.

    See Also:
        `API XAnimate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XAnimate.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.animations'
    __ooo_full_ns__: str = 'com.sun.star.animations.XAnimate'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.animations.XAnimate'

    @abstractproperty
    def KeyTimes(self) -> 'typing.Tuple[float, ...]':
        """
        """
        ...

    @abstractproperty
    def TimeFilter(self) -> 'typing.Tuple[TimeFilterPair_1d250ebc, ...]':
        """
        todo: timeFilter=\"0,0; 0.14,0.36; 0.43,0.73; 0.71,0.91; 1.0,1.0\" ?
        """
        ...

    @abstractproperty
    def Values(self) -> 'typing.Tuple[object, ...]':
        """
        A sequence of one or more values, each of which must be a legal value for the specified attribute.
        """
        ...

    @abstractproperty
    def Accumulate(self) -> bool:
        """
        Controls whether or not the animation is cumulative.
        """
        ...

    @abstractproperty
    def Additive(self) -> int:
        """
        Controls whether or not the animation is additive.
        """
        ...

    @abstractproperty
    def AttributeName(self) -> str:
        """
        Specifies the target attribute.
        """
        ...

    @abstractproperty
    def By(self) -> object:
        """
        Specifies a relative offset value for the animation.
        
        Must be a legal value of a domain for which addition to the attributeType domain is defined and which yields a value in the attributeType domain. Ignored if the values attribute is specified. Ignored if the Values attribute is specified.
        """
        ...

    @abstractproperty
    def CalcMode(self) -> int:
        """
        Specifies the interpolation mode for the animation.
        
        If the target attribute does not support linear interpolation (e.g. for strings), or if the values attribute has only one value, the CalcMode attribute is ignored and discrete interpolation is used.
        """
        ...

    @abstractproperty
    def Formula(self) -> str:
        """
        if this string is set, its contents will be parsed as a formula.
        
        All values are used as a parameter for this formula and the computed result will be used.
        """
        ...

    @abstractproperty
    def From(self) -> object:
        """
        Specifies the starting value of the animation.
        
        Must be a legal value for the specified attribute. Ignored if the Values attribute is specified.
        """
        ...

    @abstractproperty
    def SubItem(self) -> int:
        """
        This attribute specifies an optional subitem from the target element that should be animated.
        
        A value of zero should always be the default and animate the complete target. See documentation of used animation engine for supported subitems.
        """
        ...

    @abstractproperty
    def Target(self) -> object:
        """
        This attribute specifies the target element to be animated.
        
        See documentation of used animation engine for supported targets.
        """
        ...

    @abstractproperty
    def To(self) -> object:
        """
        Specifies the ending value of the animation.
        
        Must be a legal value for the specified attribute. Ignored if the Values attribute is specified.
        """
        ...

    @abstractproperty
    def ValueType(self) -> int:
        """
        """
        ...


__all__ = ['XAnimate']

