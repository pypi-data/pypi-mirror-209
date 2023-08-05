# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['PropertySetArgs', 'PropertySet']

@pulumi.input_type
class PropertySetArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input[Sequence[pulumi.Input['PropertySetPropertyArgs']]],
                 name: Optional[pulumi.Input[str]] = None,
                 visible: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a PropertySet resource.
        :param pulumi.Input[Sequence[pulumi.Input['PropertySetPropertyArgs']]] properties: A list of properties that will be part of the property set.
        :param pulumi.Input[str] name: Predefined property name.
        :param pulumi.Input[bool] visible: Defines if the list visible and assignable to the repository or artifact. Default value is `true`.
        """
        pulumi.set(__self__, "properties", properties)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if visible is not None:
            pulumi.set(__self__, "visible", visible)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Sequence[pulumi.Input['PropertySetPropertyArgs']]]:
        """
        A list of properties that will be part of the property set.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input[Sequence[pulumi.Input['PropertySetPropertyArgs']]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Predefined property name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def visible(self) -> Optional[pulumi.Input[bool]]:
        """
        Defines if the list visible and assignable to the repository or artifact. Default value is `true`.
        """
        return pulumi.get(self, "visible")

    @visible.setter
    def visible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "visible", value)


@pulumi.input_type
class _PropertySetState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Sequence[pulumi.Input['PropertySetPropertyArgs']]]] = None,
                 visible: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering PropertySet resources.
        :param pulumi.Input[str] name: Predefined property name.
        :param pulumi.Input[Sequence[pulumi.Input['PropertySetPropertyArgs']]] properties: A list of properties that will be part of the property set.
        :param pulumi.Input[bool] visible: Defines if the list visible and assignable to the repository or artifact. Default value is `true`.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if visible is not None:
            pulumi.set(__self__, "visible", visible)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Predefined property name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PropertySetPropertyArgs']]]]:
        """
        A list of properties that will be part of the property set.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PropertySetPropertyArgs']]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def visible(self) -> Optional[pulumi.Input[bool]]:
        """
        Defines if the list visible and assignable to the repository or artifact. Default value is `true`.
        """
        return pulumi.get(self, "visible")

    @visible.setter
    def visible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "visible", value)


class PropertySet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertySetPropertyArgs']]]]] = None,
                 visible: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Provides an Artifactory Property Set resource.
        This resource configuration corresponds to 'propertySets' config block in system configuration XML
        (REST endpoint: artifactory/api/system/configuration).

        ~>The `PropertySet` resource utilizes endpoints which are blocked/removed in SaaS environments (i.e. in Artifactory online), rendering this resource incompatible with Artifactory SaaS environments.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_artifactory as artifactory

        foo = artifactory.PropertySet("foo",
            properties=[
                artifactory.PropertySetPropertyArgs(
                    closed_predefined_values=True,
                    multiple_choice=True,
                    name="set1property1",
                    predefined_values=[
                        artifactory.PropertySetPropertyPredefinedValueArgs(
                            default_value=True,
                            name="passed-QA",
                        ),
                        artifactory.PropertySetPropertyPredefinedValueArgs(
                            default_value=False,
                            name="failed-QA",
                        ),
                    ],
                ),
                artifactory.PropertySetPropertyArgs(
                    closed_predefined_values=False,
                    multiple_choice=False,
                    name="set1property2",
                    predefined_values=[
                        artifactory.PropertySetPropertyPredefinedValueArgs(
                            default_value=True,
                            name="passed-QA",
                        ),
                        artifactory.PropertySetPropertyPredefinedValueArgs(
                            default_value=False,
                            name="failed-QA",
                        ),
                    ],
                ),
            ],
            visible=True)
        ```

        ## Import

        Current Property Set can be imported using `property-set1` as the `ID`, e.g.

        ```sh
         $ pulumi import artifactory:index/propertySet:PropertySet foo property-set1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Predefined property name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertySetPropertyArgs']]]] properties: A list of properties that will be part of the property set.
        :param pulumi.Input[bool] visible: Defines if the list visible and assignable to the repository or artifact. Default value is `true`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PropertySetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Artifactory Property Set resource.
        This resource configuration corresponds to 'propertySets' config block in system configuration XML
        (REST endpoint: artifactory/api/system/configuration).

        ~>The `PropertySet` resource utilizes endpoints which are blocked/removed in SaaS environments (i.e. in Artifactory online), rendering this resource incompatible with Artifactory SaaS environments.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_artifactory as artifactory

        foo = artifactory.PropertySet("foo",
            properties=[
                artifactory.PropertySetPropertyArgs(
                    closed_predefined_values=True,
                    multiple_choice=True,
                    name="set1property1",
                    predefined_values=[
                        artifactory.PropertySetPropertyPredefinedValueArgs(
                            default_value=True,
                            name="passed-QA",
                        ),
                        artifactory.PropertySetPropertyPredefinedValueArgs(
                            default_value=False,
                            name="failed-QA",
                        ),
                    ],
                ),
                artifactory.PropertySetPropertyArgs(
                    closed_predefined_values=False,
                    multiple_choice=False,
                    name="set1property2",
                    predefined_values=[
                        artifactory.PropertySetPropertyPredefinedValueArgs(
                            default_value=True,
                            name="passed-QA",
                        ),
                        artifactory.PropertySetPropertyPredefinedValueArgs(
                            default_value=False,
                            name="failed-QA",
                        ),
                    ],
                ),
            ],
            visible=True)
        ```

        ## Import

        Current Property Set can be imported using `property-set1` as the `ID`, e.g.

        ```sh
         $ pulumi import artifactory:index/propertySet:PropertySet foo property-set1
        ```

        :param str resource_name: The name of the resource.
        :param PropertySetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PropertySetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertySetPropertyArgs']]]]] = None,
                 visible: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PropertySetArgs.__new__(PropertySetArgs)

            __props__.__dict__["name"] = name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            __props__.__dict__["visible"] = visible
        super(PropertySet, __self__).__init__(
            'artifactory:index/propertySet:PropertySet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertySetPropertyArgs']]]]] = None,
            visible: Optional[pulumi.Input[bool]] = None) -> 'PropertySet':
        """
        Get an existing PropertySet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Predefined property name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertySetPropertyArgs']]]] properties: A list of properties that will be part of the property set.
        :param pulumi.Input[bool] visible: Defines if the list visible and assignable to the repository or artifact. Default value is `true`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PropertySetState.__new__(_PropertySetState)

        __props__.__dict__["name"] = name
        __props__.__dict__["properties"] = properties
        __props__.__dict__["visible"] = visible
        return PropertySet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Predefined property name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Sequence['outputs.PropertySetProperty']]:
        """
        A list of properties that will be part of the property set.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def visible(self) -> pulumi.Output[Optional[bool]]:
        """
        Defines if the list visible and assignable to the repository or artifact. Default value is `true`.
        """
        return pulumi.get(self, "visible")

