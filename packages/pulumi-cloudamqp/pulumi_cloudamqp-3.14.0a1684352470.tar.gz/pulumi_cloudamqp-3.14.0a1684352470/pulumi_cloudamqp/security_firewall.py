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

__all__ = ['SecurityFirewallArgs', 'SecurityFirewall']

@pulumi.input_type
class SecurityFirewallArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[int],
                 rules: pulumi.Input[Sequence[pulumi.Input['SecurityFirewallRuleArgs']]],
                 sleep: Optional[pulumi.Input[int]] = None,
                 timeout: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a SecurityFirewall resource.
        :param pulumi.Input[int] instance_id: The CloudAMQP instance ID.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityFirewallRuleArgs']]] rules: An array of rules, minimum of 1 needs to be configured. Each `rules` block consists of the field documented below.
        :param pulumi.Input[int] sleep: Configurable sleep time in seconds between retries for firewall configuration. Default set to 30 seconds.
        :param pulumi.Input[int] timeout: Configurable timeout time in seconds for firewall configuration. Default set to 1800 seconds.
               
               ___
               
               The `rules` block consists of:
        """
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "rules", rules)
        if sleep is not None:
            pulumi.set(__self__, "sleep", sleep)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[int]:
        """
        The CloudAMQP instance ID.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['SecurityFirewallRuleArgs']]]:
        """
        An array of rules, minimum of 1 needs to be configured. Each `rules` block consists of the field documented below.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['SecurityFirewallRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def sleep(self) -> Optional[pulumi.Input[int]]:
        """
        Configurable sleep time in seconds between retries for firewall configuration. Default set to 30 seconds.
        """
        return pulumi.get(self, "sleep")

    @sleep.setter
    def sleep(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sleep", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Configurable timeout time in seconds for firewall configuration. Default set to 1800 seconds.

        ___

        The `rules` block consists of:
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)


@pulumi.input_type
class _SecurityFirewallState:
    def __init__(__self__, *,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityFirewallRuleArgs']]]] = None,
                 sleep: Optional[pulumi.Input[int]] = None,
                 timeout: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering SecurityFirewall resources.
        :param pulumi.Input[int] instance_id: The CloudAMQP instance ID.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityFirewallRuleArgs']]] rules: An array of rules, minimum of 1 needs to be configured. Each `rules` block consists of the field documented below.
        :param pulumi.Input[int] sleep: Configurable sleep time in seconds between retries for firewall configuration. Default set to 30 seconds.
        :param pulumi.Input[int] timeout: Configurable timeout time in seconds for firewall configuration. Default set to 1800 seconds.
               
               ___
               
               The `rules` block consists of:
        """
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if sleep is not None:
            pulumi.set(__self__, "sleep", sleep)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[int]]:
        """
        The CloudAMQP instance ID.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityFirewallRuleArgs']]]]:
        """
        An array of rules, minimum of 1 needs to be configured. Each `rules` block consists of the field documented below.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityFirewallRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def sleep(self) -> Optional[pulumi.Input[int]]:
        """
        Configurable sleep time in seconds between retries for firewall configuration. Default set to 30 seconds.
        """
        return pulumi.get(self, "sleep")

    @sleep.setter
    def sleep(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sleep", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Configurable timeout time in seconds for firewall configuration. Default set to 1800 seconds.

        ___

        The `rules` block consists of:
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)


class SecurityFirewall(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityFirewallRuleArgs']]]]] = None,
                 sleep: Optional[pulumi.Input[int]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        ## Import

        `cloudamqp_security_firewall` can be imported using CloudAMQP instance identifier.

        ```sh
         $ pulumi import cloudamqp:index/securityFirewall:SecurityFirewall firewall <instance_id>`
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] instance_id: The CloudAMQP instance ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityFirewallRuleArgs']]]] rules: An array of rules, minimum of 1 needs to be configured. Each `rules` block consists of the field documented below.
        :param pulumi.Input[int] sleep: Configurable sleep time in seconds between retries for firewall configuration. Default set to 30 seconds.
        :param pulumi.Input[int] timeout: Configurable timeout time in seconds for firewall configuration. Default set to 1800 seconds.
               
               ___
               
               The `rules` block consists of:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityFirewallArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        `cloudamqp_security_firewall` can be imported using CloudAMQP instance identifier.

        ```sh
         $ pulumi import cloudamqp:index/securityFirewall:SecurityFirewall firewall <instance_id>`
        ```

        :param str resource_name: The name of the resource.
        :param SecurityFirewallArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityFirewallArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityFirewallRuleArgs']]]]] = None,
                 sleep: Optional[pulumi.Input[int]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityFirewallArgs.__new__(SecurityFirewallArgs)

            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            __props__.__dict__["sleep"] = sleep
            __props__.__dict__["timeout"] = timeout
        super(SecurityFirewall, __self__).__init__(
            'cloudamqp:index/securityFirewall:SecurityFirewall',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_id: Optional[pulumi.Input[int]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityFirewallRuleArgs']]]]] = None,
            sleep: Optional[pulumi.Input[int]] = None,
            timeout: Optional[pulumi.Input[int]] = None) -> 'SecurityFirewall':
        """
        Get an existing SecurityFirewall resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] instance_id: The CloudAMQP instance ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityFirewallRuleArgs']]]] rules: An array of rules, minimum of 1 needs to be configured. Each `rules` block consists of the field documented below.
        :param pulumi.Input[int] sleep: Configurable sleep time in seconds between retries for firewall configuration. Default set to 30 seconds.
        :param pulumi.Input[int] timeout: Configurable timeout time in seconds for firewall configuration. Default set to 1800 seconds.
               
               ___
               
               The `rules` block consists of:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecurityFirewallState.__new__(_SecurityFirewallState)

        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["rules"] = rules
        __props__.__dict__["sleep"] = sleep
        __props__.__dict__["timeout"] = timeout
        return SecurityFirewall(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[int]:
        """
        The CloudAMQP instance ID.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.SecurityFirewallRule']]:
        """
        An array of rules, minimum of 1 needs to be configured. Each `rules` block consists of the field documented below.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def sleep(self) -> pulumi.Output[Optional[int]]:
        """
        Configurable sleep time in seconds between retries for firewall configuration. Default set to 30 seconds.
        """
        return pulumi.get(self, "sleep")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[int]]:
        """
        Configurable timeout time in seconds for firewall configuration. Default set to 1800 seconds.

        ___

        The `rules` block consists of:
        """
        return pulumi.get(self, "timeout")

