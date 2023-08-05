# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._inputs import *

__all__ = ['DeploymentSettingsArgs', 'DeploymentSettings']

@pulumi.input_type
class DeploymentSettingsArgs:
    def __init__(__self__, *,
                 organization: pulumi.Input[str],
                 project: pulumi.Input[str],
                 source_context: pulumi.Input['DeploymentSettingsSourceContextArgs'],
                 stack: pulumi.Input[str],
                 executor_context: Optional[pulumi.Input['DeploymentSettingsExecutorContextArgs']] = None,
                 github: Optional[pulumi.Input['DeploymentSettingsGithubArgs']] = None,
                 operation_context: Optional[pulumi.Input['DeploymentSettingsOperationContextArgs']] = None):
        """
        The set of arguments for constructing a DeploymentSettings resource.
        :param pulumi.Input[str] organization: Organization name.
        :param pulumi.Input[str] project: Project name.
        :param pulumi.Input['DeploymentSettingsSourceContextArgs'] source_context: Settings related to the source of the deployment.
        :param pulumi.Input[str] stack: Stack name.
        :param pulumi.Input['DeploymentSettingsExecutorContextArgs'] executor_context: Settings related to the deployment executor.
        :param pulumi.Input['DeploymentSettingsGithubArgs'] github: GitHub settings for the deployment.
        :param pulumi.Input['DeploymentSettingsOperationContextArgs'] operation_context: Settings related to the Pulumi operation environment during the deployment.
        """
        pulumi.set(__self__, "organization", organization)
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "source_context", source_context)
        pulumi.set(__self__, "stack", stack)
        if executor_context is not None:
            pulumi.set(__self__, "executor_context", executor_context)
        if github is not None:
            pulumi.set(__self__, "github", github)
        if operation_context is not None:
            pulumi.set(__self__, "operation_context", operation_context)

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Input[str]:
        """
        Organization name.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        Project name.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="sourceContext")
    def source_context(self) -> pulumi.Input['DeploymentSettingsSourceContextArgs']:
        """
        Settings related to the source of the deployment.
        """
        return pulumi.get(self, "source_context")

    @source_context.setter
    def source_context(self, value: pulumi.Input['DeploymentSettingsSourceContextArgs']):
        pulumi.set(self, "source_context", value)

    @property
    @pulumi.getter
    def stack(self) -> pulumi.Input[str]:
        """
        Stack name.
        """
        return pulumi.get(self, "stack")

    @stack.setter
    def stack(self, value: pulumi.Input[str]):
        pulumi.set(self, "stack", value)

    @property
    @pulumi.getter(name="executorContext")
    def executor_context(self) -> Optional[pulumi.Input['DeploymentSettingsExecutorContextArgs']]:
        """
        Settings related to the deployment executor.
        """
        return pulumi.get(self, "executor_context")

    @executor_context.setter
    def executor_context(self, value: Optional[pulumi.Input['DeploymentSettingsExecutorContextArgs']]):
        pulumi.set(self, "executor_context", value)

    @property
    @pulumi.getter
    def github(self) -> Optional[pulumi.Input['DeploymentSettingsGithubArgs']]:
        """
        GitHub settings for the deployment.
        """
        return pulumi.get(self, "github")

    @github.setter
    def github(self, value: Optional[pulumi.Input['DeploymentSettingsGithubArgs']]):
        pulumi.set(self, "github", value)

    @property
    @pulumi.getter(name="operationContext")
    def operation_context(self) -> Optional[pulumi.Input['DeploymentSettingsOperationContextArgs']]:
        """
        Settings related to the Pulumi operation environment during the deployment.
        """
        return pulumi.get(self, "operation_context")

    @operation_context.setter
    def operation_context(self, value: Optional[pulumi.Input['DeploymentSettingsOperationContextArgs']]):
        pulumi.set(self, "operation_context", value)


class DeploymentSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 executor_context: Optional[pulumi.Input[pulumi.InputType['DeploymentSettingsExecutorContextArgs']]] = None,
                 github: Optional[pulumi.Input[pulumi.InputType['DeploymentSettingsGithubArgs']]] = None,
                 operation_context: Optional[pulumi.Input[pulumi.InputType['DeploymentSettingsOperationContextArgs']]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 source_context: Optional[pulumi.Input[pulumi.InputType['DeploymentSettingsSourceContextArgs']]] = None,
                 stack: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Deployment settings configure Pulumi Deployments for a stack

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DeploymentSettingsExecutorContextArgs']] executor_context: Settings related to the deployment executor.
        :param pulumi.Input[pulumi.InputType['DeploymentSettingsGithubArgs']] github: GitHub settings for the deployment.
        :param pulumi.Input[pulumi.InputType['DeploymentSettingsOperationContextArgs']] operation_context: Settings related to the Pulumi operation environment during the deployment.
        :param pulumi.Input[str] organization: Organization name.
        :param pulumi.Input[str] project: Project name.
        :param pulumi.Input[pulumi.InputType['DeploymentSettingsSourceContextArgs']] source_context: Settings related to the source of the deployment.
        :param pulumi.Input[str] stack: Stack name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Deployment settings configure Pulumi Deployments for a stack

        :param str resource_name: The name of the resource.
        :param DeploymentSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 executor_context: Optional[pulumi.Input[pulumi.InputType['DeploymentSettingsExecutorContextArgs']]] = None,
                 github: Optional[pulumi.Input[pulumi.InputType['DeploymentSettingsGithubArgs']]] = None,
                 operation_context: Optional[pulumi.Input[pulumi.InputType['DeploymentSettingsOperationContextArgs']]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 source_context: Optional[pulumi.Input[pulumi.InputType['DeploymentSettingsSourceContextArgs']]] = None,
                 stack: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentSettingsArgs.__new__(DeploymentSettingsArgs)

            __props__.__dict__["executor_context"] = executor_context
            __props__.__dict__["github"] = github
            __props__.__dict__["operation_context"] = operation_context
            if organization is None and not opts.urn:
                raise TypeError("Missing required property 'organization'")
            __props__.__dict__["organization"] = organization
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if source_context is None and not opts.urn:
                raise TypeError("Missing required property 'source_context'")
            __props__.__dict__["source_context"] = source_context
            if stack is None and not opts.urn:
                raise TypeError("Missing required property 'stack'")
            __props__.__dict__["stack"] = stack
        super(DeploymentSettings, __self__).__init__(
            'pulumiservice:index:DeploymentSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeploymentSettings':
        """
        Get an existing DeploymentSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentSettingsArgs.__new__(DeploymentSettingsArgs)

        __props__.__dict__["organization"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["stack"] = None
        return DeploymentSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Output[Optional[str]]:
        """
        Organization name.
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[Optional[str]]:
        """
        Project name.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def stack(self) -> pulumi.Output[Optional[str]]:
        """
        Stack name.
        """
        return pulumi.get(self, "stack")

