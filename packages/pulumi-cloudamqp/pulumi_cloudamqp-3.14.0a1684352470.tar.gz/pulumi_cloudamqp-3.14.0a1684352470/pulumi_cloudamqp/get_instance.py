# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    """
    A collection of values returned by getInstance.
    """
    def __init__(__self__, apikey=None, backend=None, dedicated=None, host=None, host_internal=None, id=None, instance_id=None, name=None, no_default_alarms=None, nodes=None, plan=None, ready=None, region=None, rmq_version=None, tags=None, url=None, vhost=None, vpc_id=None, vpc_subnet=None):
        if apikey and not isinstance(apikey, str):
            raise TypeError("Expected argument 'apikey' to be a str")
        pulumi.set(__self__, "apikey", apikey)
        if backend and not isinstance(backend, str):
            raise TypeError("Expected argument 'backend' to be a str")
        pulumi.set(__self__, "backend", backend)
        if dedicated and not isinstance(dedicated, bool):
            raise TypeError("Expected argument 'dedicated' to be a bool")
        pulumi.set(__self__, "dedicated", dedicated)
        if host and not isinstance(host, str):
            raise TypeError("Expected argument 'host' to be a str")
        pulumi.set(__self__, "host", host)
        if host_internal and not isinstance(host_internal, str):
            raise TypeError("Expected argument 'host_internal' to be a str")
        pulumi.set(__self__, "host_internal", host_internal)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_id and not isinstance(instance_id, int):
            raise TypeError("Expected argument 'instance_id' to be a int")
        pulumi.set(__self__, "instance_id", instance_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if no_default_alarms and not isinstance(no_default_alarms, bool):
            raise TypeError("Expected argument 'no_default_alarms' to be a bool")
        pulumi.set(__self__, "no_default_alarms", no_default_alarms)
        if nodes and not isinstance(nodes, int):
            raise TypeError("Expected argument 'nodes' to be a int")
        pulumi.set(__self__, "nodes", nodes)
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        pulumi.set(__self__, "plan", plan)
        if ready and not isinstance(ready, bool):
            raise TypeError("Expected argument 'ready' to be a bool")
        pulumi.set(__self__, "ready", ready)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if rmq_version and not isinstance(rmq_version, str):
            raise TypeError("Expected argument 'rmq_version' to be a str")
        pulumi.set(__self__, "rmq_version", rmq_version)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)
        if vhost and not isinstance(vhost, str):
            raise TypeError("Expected argument 'vhost' to be a str")
        pulumi.set(__self__, "vhost", vhost)
        if vpc_id and not isinstance(vpc_id, int):
            raise TypeError("Expected argument 'vpc_id' to be a int")
        pulumi.set(__self__, "vpc_id", vpc_id)
        if vpc_subnet and not isinstance(vpc_subnet, str):
            raise TypeError("Expected argument 'vpc_subnet' to be a str")
        pulumi.set(__self__, "vpc_subnet", vpc_subnet)

    @property
    @pulumi.getter
    def apikey(self) -> str:
        return pulumi.get(self, "apikey")

    @property
    @pulumi.getter
    def backend(self) -> str:
        return pulumi.get(self, "backend")

    @property
    @pulumi.getter
    def dedicated(self) -> bool:
        return pulumi.get(self, "dedicated")

    @property
    @pulumi.getter
    def host(self) -> str:
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="hostInternal")
    def host_internal(self) -> str:
        return pulumi.get(self, "host_internal")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> int:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="noDefaultAlarms")
    def no_default_alarms(self) -> bool:
        return pulumi.get(self, "no_default_alarms")

    @property
    @pulumi.getter
    def nodes(self) -> int:
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter
    def plan(self) -> str:
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def ready(self) -> bool:
        return pulumi.get(self, "ready")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="rmqVersion")
    def rmq_version(self) -> str:
        return pulumi.get(self, "rmq_version")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def url(self) -> str:
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def vhost(self) -> str:
        return pulumi.get(self, "vhost")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> int:
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vpcSubnet")
    def vpc_subnet(self) -> str:
        return pulumi.get(self, "vpc_subnet")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            apikey=self.apikey,
            backend=self.backend,
            dedicated=self.dedicated,
            host=self.host,
            host_internal=self.host_internal,
            id=self.id,
            instance_id=self.instance_id,
            name=self.name,
            no_default_alarms=self.no_default_alarms,
            nodes=self.nodes,
            plan=self.plan,
            ready=self.ready,
            region=self.region,
            rmq_version=self.rmq_version,
            tags=self.tags,
            url=self.url,
            vhost=self.vhost,
            vpc_id=self.vpc_id,
            vpc_subnet=self.vpc_subnet)


def get_instance(instance_id: Optional[int] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Use this data source to retrieve information about an already created CloudAMQP instance. In order to retrieve the correct information, the CoudAMQP instance identifier is needed.

    ## Attributes reference

    All attributes reference are computed

    * `id`          - The identifier for this resource.
    * `name`        - The name of the CloudAMQP instance.
    * `plan`        - The subscription plan for the CloudAMQP instance.
    * `region`      - The cloud platform and region that host the CloudAMQP instance, `{platform}::{region}`.
    * `vpc_id`      - ID of the VPC configured for the CloudAMQP instance.
    * `vpc_subnet`  - Dedicated VPC subnet configured for the CloudAMQP instance.
    * `nodes`       - Number of nodes in the cluster of the CloudAMQP instance.
    * `rmq_version` - The version of installed Rabbit MQ.
    * `url`         - (Sensitive) The AMQP URL (uses the internal hostname if the instance was created with VPC), used by clients to connect for pub/sub.
    * `apikey`      - (Sensitive) The API key to secondary API handing alarms, integration etc.
    * `tags`        - Tags the CloudAMQP instance with categories.
    * `host`        - The external hostname for the CloudAMQP instance.
    * `host_internal` - The internal hostname for the CloudAMQP instance.
    * `vhost`       - The virtual host configured in Rabbit MQ.
    * `dedicated`   - Information if the CloudAMQP instance is shared or dedicated.
    * `backend`     - Information if the CloudAMQP instance runs either RabbitMQ or LavinMQ.


    :param int instance_id: The CloudAMQP instance identifier.
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudamqp:index/getInstance:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        apikey=__ret__.apikey,
        backend=__ret__.backend,
        dedicated=__ret__.dedicated,
        host=__ret__.host,
        host_internal=__ret__.host_internal,
        id=__ret__.id,
        instance_id=__ret__.instance_id,
        name=__ret__.name,
        no_default_alarms=__ret__.no_default_alarms,
        nodes=__ret__.nodes,
        plan=__ret__.plan,
        ready=__ret__.ready,
        region=__ret__.region,
        rmq_version=__ret__.rmq_version,
        tags=__ret__.tags,
        url=__ret__.url,
        vhost=__ret__.vhost,
        vpc_id=__ret__.vpc_id,
        vpc_subnet=__ret__.vpc_subnet)


@_utilities.lift_output_func(get_instance)
def get_instance_output(instance_id: Optional[pulumi.Input[int]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Use this data source to retrieve information about an already created CloudAMQP instance. In order to retrieve the correct information, the CoudAMQP instance identifier is needed.

    ## Attributes reference

    All attributes reference are computed

    * `id`          - The identifier for this resource.
    * `name`        - The name of the CloudAMQP instance.
    * `plan`        - The subscription plan for the CloudAMQP instance.
    * `region`      - The cloud platform and region that host the CloudAMQP instance, `{platform}::{region}`.
    * `vpc_id`      - ID of the VPC configured for the CloudAMQP instance.
    * `vpc_subnet`  - Dedicated VPC subnet configured for the CloudAMQP instance.
    * `nodes`       - Number of nodes in the cluster of the CloudAMQP instance.
    * `rmq_version` - The version of installed Rabbit MQ.
    * `url`         - (Sensitive) The AMQP URL (uses the internal hostname if the instance was created with VPC), used by clients to connect for pub/sub.
    * `apikey`      - (Sensitive) The API key to secondary API handing alarms, integration etc.
    * `tags`        - Tags the CloudAMQP instance with categories.
    * `host`        - The external hostname for the CloudAMQP instance.
    * `host_internal` - The internal hostname for the CloudAMQP instance.
    * `vhost`       - The virtual host configured in Rabbit MQ.
    * `dedicated`   - Information if the CloudAMQP instance is shared or dedicated.
    * `backend`     - Information if the CloudAMQP instance runs either RabbitMQ or LavinMQ.


    :param int instance_id: The CloudAMQP instance identifier.
    """
    ...
