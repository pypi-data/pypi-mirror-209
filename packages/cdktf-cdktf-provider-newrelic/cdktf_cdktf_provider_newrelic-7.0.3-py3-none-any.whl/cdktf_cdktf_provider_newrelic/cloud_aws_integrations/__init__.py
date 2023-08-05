'''
# `newrelic_cloud_aws_integrations`

Refer to the Terraform Registory for docs: [`newrelic_cloud_aws_integrations`](https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class CloudAwsIntegrations(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrations",
):
    '''Represents a {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations newrelic_cloud_aws_integrations}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        linked_account_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        alb: typing.Optional[typing.Union["CloudAwsIntegrationsAlb", typing.Dict[builtins.str, typing.Any]]] = None,
        api_gateway: typing.Optional[typing.Union["CloudAwsIntegrationsApiGateway", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_scaling: typing.Optional[typing.Union["CloudAwsIntegrationsAutoScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_app_sync: typing.Optional[typing.Union["CloudAwsIntegrationsAwsAppSync", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_athena: typing.Optional[typing.Union["CloudAwsIntegrationsAwsAthena", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_cognito: typing.Optional[typing.Union["CloudAwsIntegrationsAwsCognito", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_connect: typing.Optional[typing.Union["CloudAwsIntegrationsAwsConnect", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_direct_connect: typing.Optional[typing.Union["CloudAwsIntegrationsAwsDirectConnect", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_fsx: typing.Optional[typing.Union["CloudAwsIntegrationsAwsFsx", typing.Dict[builtins.str, typing.Any]]] = None,
        billing: typing.Optional[typing.Union["CloudAwsIntegrationsBilling", typing.Dict[builtins.str, typing.Any]]] = None,
        cloudtrail: typing.Optional[typing.Union["CloudAwsIntegrationsCloudtrail", typing.Dict[builtins.str, typing.Any]]] = None,
        doc_db: typing.Optional[typing.Union["CloudAwsIntegrationsDocDb", typing.Dict[builtins.str, typing.Any]]] = None,
        ebs: typing.Optional[typing.Union["CloudAwsIntegrationsEbs", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticache: typing.Optional[typing.Union["CloudAwsIntegrationsElasticache", typing.Dict[builtins.str, typing.Any]]] = None,
        health: typing.Optional[typing.Union["CloudAwsIntegrationsHealth", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        s3: typing.Optional[typing.Union["CloudAwsIntegrationsS3", typing.Dict[builtins.str, typing.Any]]] = None,
        sqs: typing.Optional[typing.Union["CloudAwsIntegrationsSqs", typing.Dict[builtins.str, typing.Any]]] = None,
        trusted_advisor: typing.Optional[typing.Union["CloudAwsIntegrationsTrustedAdvisor", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[typing.Union["CloudAwsIntegrationsVpc", typing.Dict[builtins.str, typing.Any]]] = None,
        x_ray: typing.Optional[typing.Union["CloudAwsIntegrationsXRay", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations newrelic_cloud_aws_integrations} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param linked_account_id: The ID of the linked AWS account in New Relic. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#linked_account_id CloudAwsIntegrations#linked_account_id}
        :param account_id: The ID of the account in New Relic. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#account_id CloudAwsIntegrations#account_id}
        :param alb: alb block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#alb CloudAwsIntegrations#alb}
        :param api_gateway: api_gateway block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#api_gateway CloudAwsIntegrations#api_gateway}
        :param auto_scaling: auto_scaling block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#auto_scaling CloudAwsIntegrations#auto_scaling}
        :param aws_app_sync: aws_app_sync block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_app_sync CloudAwsIntegrations#aws_app_sync}
        :param aws_athena: aws_athena block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_athena CloudAwsIntegrations#aws_athena}
        :param aws_cognito: aws_cognito block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_cognito CloudAwsIntegrations#aws_cognito}
        :param aws_connect: aws_connect block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_connect CloudAwsIntegrations#aws_connect}
        :param aws_direct_connect: aws_direct_connect block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_direct_connect CloudAwsIntegrations#aws_direct_connect}
        :param aws_fsx: aws_fsx block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_fsx CloudAwsIntegrations#aws_fsx}
        :param billing: billing block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#billing CloudAwsIntegrations#billing}
        :param cloudtrail: cloudtrail block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#cloudtrail CloudAwsIntegrations#cloudtrail}
        :param doc_db: doc_db block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#doc_db CloudAwsIntegrations#doc_db}
        :param ebs: ebs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#ebs CloudAwsIntegrations#ebs}
        :param elasticache: elasticache block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#elasticache CloudAwsIntegrations#elasticache}
        :param health: health block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#health CloudAwsIntegrations#health}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#id CloudAwsIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param s3: s3 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#s3 CloudAwsIntegrations#s3}
        :param sqs: sqs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#sqs CloudAwsIntegrations#sqs}
        :param trusted_advisor: trusted_advisor block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#trusted_advisor CloudAwsIntegrations#trusted_advisor}
        :param vpc: vpc block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#vpc CloudAwsIntegrations#vpc}
        :param x_ray: x_ray block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#x_ray CloudAwsIntegrations#x_ray}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__218636da2f5c84b07b8f11f887c728956d546cee837b90d553762da5832a9fd8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudAwsIntegrationsConfig(
            linked_account_id=linked_account_id,
            account_id=account_id,
            alb=alb,
            api_gateway=api_gateway,
            auto_scaling=auto_scaling,
            aws_app_sync=aws_app_sync,
            aws_athena=aws_athena,
            aws_cognito=aws_cognito,
            aws_connect=aws_connect,
            aws_direct_connect=aws_direct_connect,
            aws_fsx=aws_fsx,
            billing=billing,
            cloudtrail=cloudtrail,
            doc_db=doc_db,
            ebs=ebs,
            elasticache=elasticache,
            health=health,
            id=id,
            s3=s3,
            sqs=sqs,
            trusted_advisor=trusted_advisor,
            vpc=vpc,
            x_ray=x_ray,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlb")
    def put_alb(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        load_balancer_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        :param load_balancer_prefixes: Specify each name or prefix for the LBs that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#load_balancer_prefixes CloudAwsIntegrations#load_balancer_prefixes}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        value = CloudAwsIntegrationsAlb(
            aws_regions=aws_regions,
            fetch_extended_inventory=fetch_extended_inventory,
            fetch_tags=fetch_tags,
            load_balancer_prefixes=load_balancer_prefixes,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putAlb", [value]))

    @jsii.member(jsii_name="putApiGateway")
    def put_api_gateway(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        stage_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param stage_prefixes: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#stage_prefixes CloudAwsIntegrations#stage_prefixes}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        value = CloudAwsIntegrationsApiGateway(
            aws_regions=aws_regions,
            metrics_polling_interval=metrics_polling_interval,
            stage_prefixes=stage_prefixes,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putApiGateway", [value]))

    @jsii.member(jsii_name="putAutoScaling")
    def put_auto_scaling(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsAutoScaling(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAutoScaling", [value]))

    @jsii.member(jsii_name="putAwsAppSync")
    def put_aws_app_sync(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsAwsAppSync(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAwsAppSync", [value]))

    @jsii.member(jsii_name="putAwsAthena")
    def put_aws_athena(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsAwsAthena(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAwsAthena", [value]))

    @jsii.member(jsii_name="putAwsCognito")
    def put_aws_cognito(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsAwsCognito(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAwsCognito", [value]))

    @jsii.member(jsii_name="putAwsConnect")
    def put_aws_connect(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsAwsConnect(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAwsConnect", [value]))

    @jsii.member(jsii_name="putAwsDirectConnect")
    def put_aws_direct_connect(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsAwsDirectConnect(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAwsDirectConnect", [value]))

    @jsii.member(jsii_name="putAwsFsx")
    def put_aws_fsx(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsAwsFsx(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAwsFsx", [value]))

    @jsii.member(jsii_name="putBilling")
    def put_billing(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsBilling(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putBilling", [value]))

    @jsii.member(jsii_name="putCloudtrail")
    def put_cloudtrail(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsCloudtrail(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putCloudtrail", [value]))

    @jsii.member(jsii_name="putDocDb")
    def put_doc_db(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsDocDb(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putDocDb", [value]))

    @jsii.member(jsii_name="putEbs")
    def put_ebs(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        value = CloudAwsIntegrationsEbs(
            aws_regions=aws_regions,
            fetch_extended_inventory=fetch_extended_inventory,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putEbs", [value]))

    @jsii.member(jsii_name="putElasticache")
    def put_elasticache(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        value = CloudAwsIntegrationsElasticache(
            aws_regions=aws_regions,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putElasticache", [value]))

    @jsii.member(jsii_name="putHealth")
    def put_health(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsHealth(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putHealth", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        value = CloudAwsIntegrationsS3(
            fetch_extended_inventory=fetch_extended_inventory,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSqs")
    def put_sqs(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        queue_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param queue_prefixes: Specify each name or prefix for the Queues that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#queue_prefixes CloudAwsIntegrations#queue_prefixes}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        value = CloudAwsIntegrationsSqs(
            aws_regions=aws_regions,
            fetch_extended_inventory=fetch_extended_inventory,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
            queue_prefixes=queue_prefixes,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putSqs", [value]))

    @jsii.member(jsii_name="putTrustedAdvisor")
    def put_trusted_advisor(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsTrustedAdvisor(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putTrustedAdvisor", [value]))

    @jsii.member(jsii_name="putVpc")
    def put_vpc(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_nat_gateway: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fetch_vpn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_nat_gateway: Specify if NAT gateway should be monitored. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_nat_gateway CloudAwsIntegrations#fetch_nat_gateway}
        :param fetch_vpn: Specify if VPN should be monitored. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_vpn CloudAwsIntegrations#fetch_vpn}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        value = CloudAwsIntegrationsVpc(
            aws_regions=aws_regions,
            fetch_nat_gateway=fetch_nat_gateway,
            fetch_vpn=fetch_vpn,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putVpc", [value]))

    @jsii.member(jsii_name="putXRay")
    def put_x_ray(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsXRay(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putXRay", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAlb")
    def reset_alb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlb", []))

    @jsii.member(jsii_name="resetApiGateway")
    def reset_api_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiGateway", []))

    @jsii.member(jsii_name="resetAutoScaling")
    def reset_auto_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoScaling", []))

    @jsii.member(jsii_name="resetAwsAppSync")
    def reset_aws_app_sync(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAppSync", []))

    @jsii.member(jsii_name="resetAwsAthena")
    def reset_aws_athena(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAthena", []))

    @jsii.member(jsii_name="resetAwsCognito")
    def reset_aws_cognito(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsCognito", []))

    @jsii.member(jsii_name="resetAwsConnect")
    def reset_aws_connect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsConnect", []))

    @jsii.member(jsii_name="resetAwsDirectConnect")
    def reset_aws_direct_connect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsDirectConnect", []))

    @jsii.member(jsii_name="resetAwsFsx")
    def reset_aws_fsx(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsFsx", []))

    @jsii.member(jsii_name="resetBilling")
    def reset_billing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBilling", []))

    @jsii.member(jsii_name="resetCloudtrail")
    def reset_cloudtrail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudtrail", []))

    @jsii.member(jsii_name="resetDocDb")
    def reset_doc_db(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocDb", []))

    @jsii.member(jsii_name="resetEbs")
    def reset_ebs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbs", []))

    @jsii.member(jsii_name="resetElasticache")
    def reset_elasticache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticache", []))

    @jsii.member(jsii_name="resetHealth")
    def reset_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealth", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetSqs")
    def reset_sqs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqs", []))

    @jsii.member(jsii_name="resetTrustedAdvisor")
    def reset_trusted_advisor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedAdvisor", []))

    @jsii.member(jsii_name="resetVpc")
    def reset_vpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpc", []))

    @jsii.member(jsii_name="resetXRay")
    def reset_x_ray(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXRay", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alb")
    def alb(self) -> "CloudAwsIntegrationsAlbOutputReference":
        return typing.cast("CloudAwsIntegrationsAlbOutputReference", jsii.get(self, "alb"))

    @builtins.property
    @jsii.member(jsii_name="apiGateway")
    def api_gateway(self) -> "CloudAwsIntegrationsApiGatewayOutputReference":
        return typing.cast("CloudAwsIntegrationsApiGatewayOutputReference", jsii.get(self, "apiGateway"))

    @builtins.property
    @jsii.member(jsii_name="autoScaling")
    def auto_scaling(self) -> "CloudAwsIntegrationsAutoScalingOutputReference":
        return typing.cast("CloudAwsIntegrationsAutoScalingOutputReference", jsii.get(self, "autoScaling"))

    @builtins.property
    @jsii.member(jsii_name="awsAppSync")
    def aws_app_sync(self) -> "CloudAwsIntegrationsAwsAppSyncOutputReference":
        return typing.cast("CloudAwsIntegrationsAwsAppSyncOutputReference", jsii.get(self, "awsAppSync"))

    @builtins.property
    @jsii.member(jsii_name="awsAthena")
    def aws_athena(self) -> "CloudAwsIntegrationsAwsAthenaOutputReference":
        return typing.cast("CloudAwsIntegrationsAwsAthenaOutputReference", jsii.get(self, "awsAthena"))

    @builtins.property
    @jsii.member(jsii_name="awsCognito")
    def aws_cognito(self) -> "CloudAwsIntegrationsAwsCognitoOutputReference":
        return typing.cast("CloudAwsIntegrationsAwsCognitoOutputReference", jsii.get(self, "awsCognito"))

    @builtins.property
    @jsii.member(jsii_name="awsConnect")
    def aws_connect(self) -> "CloudAwsIntegrationsAwsConnectOutputReference":
        return typing.cast("CloudAwsIntegrationsAwsConnectOutputReference", jsii.get(self, "awsConnect"))

    @builtins.property
    @jsii.member(jsii_name="awsDirectConnect")
    def aws_direct_connect(
        self,
    ) -> "CloudAwsIntegrationsAwsDirectConnectOutputReference":
        return typing.cast("CloudAwsIntegrationsAwsDirectConnectOutputReference", jsii.get(self, "awsDirectConnect"))

    @builtins.property
    @jsii.member(jsii_name="awsFsx")
    def aws_fsx(self) -> "CloudAwsIntegrationsAwsFsxOutputReference":
        return typing.cast("CloudAwsIntegrationsAwsFsxOutputReference", jsii.get(self, "awsFsx"))

    @builtins.property
    @jsii.member(jsii_name="billing")
    def billing(self) -> "CloudAwsIntegrationsBillingOutputReference":
        return typing.cast("CloudAwsIntegrationsBillingOutputReference", jsii.get(self, "billing"))

    @builtins.property
    @jsii.member(jsii_name="cloudtrail")
    def cloudtrail(self) -> "CloudAwsIntegrationsCloudtrailOutputReference":
        return typing.cast("CloudAwsIntegrationsCloudtrailOutputReference", jsii.get(self, "cloudtrail"))

    @builtins.property
    @jsii.member(jsii_name="docDb")
    def doc_db(self) -> "CloudAwsIntegrationsDocDbOutputReference":
        return typing.cast("CloudAwsIntegrationsDocDbOutputReference", jsii.get(self, "docDb"))

    @builtins.property
    @jsii.member(jsii_name="ebs")
    def ebs(self) -> "CloudAwsIntegrationsEbsOutputReference":
        return typing.cast("CloudAwsIntegrationsEbsOutputReference", jsii.get(self, "ebs"))

    @builtins.property
    @jsii.member(jsii_name="elasticache")
    def elasticache(self) -> "CloudAwsIntegrationsElasticacheOutputReference":
        return typing.cast("CloudAwsIntegrationsElasticacheOutputReference", jsii.get(self, "elasticache"))

    @builtins.property
    @jsii.member(jsii_name="health")
    def health(self) -> "CloudAwsIntegrationsHealthOutputReference":
        return typing.cast("CloudAwsIntegrationsHealthOutputReference", jsii.get(self, "health"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "CloudAwsIntegrationsS3OutputReference":
        return typing.cast("CloudAwsIntegrationsS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="sqs")
    def sqs(self) -> "CloudAwsIntegrationsSqsOutputReference":
        return typing.cast("CloudAwsIntegrationsSqsOutputReference", jsii.get(self, "sqs"))

    @builtins.property
    @jsii.member(jsii_name="trustedAdvisor")
    def trusted_advisor(self) -> "CloudAwsIntegrationsTrustedAdvisorOutputReference":
        return typing.cast("CloudAwsIntegrationsTrustedAdvisorOutputReference", jsii.get(self, "trustedAdvisor"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> "CloudAwsIntegrationsVpcOutputReference":
        return typing.cast("CloudAwsIntegrationsVpcOutputReference", jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="xRay")
    def x_ray(self) -> "CloudAwsIntegrationsXRayOutputReference":
        return typing.cast("CloudAwsIntegrationsXRayOutputReference", jsii.get(self, "xRay"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="albInput")
    def alb_input(self) -> typing.Optional["CloudAwsIntegrationsAlb"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsAlb"], jsii.get(self, "albInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGatewayInput")
    def api_gateway_input(self) -> typing.Optional["CloudAwsIntegrationsApiGateway"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsApiGateway"], jsii.get(self, "apiGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingInput")
    def auto_scaling_input(self) -> typing.Optional["CloudAwsIntegrationsAutoScaling"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsAutoScaling"], jsii.get(self, "autoScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAppSyncInput")
    def aws_app_sync_input(self) -> typing.Optional["CloudAwsIntegrationsAwsAppSync"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsAwsAppSync"], jsii.get(self, "awsAppSyncInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAthenaInput")
    def aws_athena_input(self) -> typing.Optional["CloudAwsIntegrationsAwsAthena"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsAwsAthena"], jsii.get(self, "awsAthenaInput"))

    @builtins.property
    @jsii.member(jsii_name="awsCognitoInput")
    def aws_cognito_input(self) -> typing.Optional["CloudAwsIntegrationsAwsCognito"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsAwsCognito"], jsii.get(self, "awsCognitoInput"))

    @builtins.property
    @jsii.member(jsii_name="awsConnectInput")
    def aws_connect_input(self) -> typing.Optional["CloudAwsIntegrationsAwsConnect"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsAwsConnect"], jsii.get(self, "awsConnectInput"))

    @builtins.property
    @jsii.member(jsii_name="awsDirectConnectInput")
    def aws_direct_connect_input(
        self,
    ) -> typing.Optional["CloudAwsIntegrationsAwsDirectConnect"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsAwsDirectConnect"], jsii.get(self, "awsDirectConnectInput"))

    @builtins.property
    @jsii.member(jsii_name="awsFsxInput")
    def aws_fsx_input(self) -> typing.Optional["CloudAwsIntegrationsAwsFsx"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsAwsFsx"], jsii.get(self, "awsFsxInput"))

    @builtins.property
    @jsii.member(jsii_name="billingInput")
    def billing_input(self) -> typing.Optional["CloudAwsIntegrationsBilling"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsBilling"], jsii.get(self, "billingInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudtrailInput")
    def cloudtrail_input(self) -> typing.Optional["CloudAwsIntegrationsCloudtrail"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsCloudtrail"], jsii.get(self, "cloudtrailInput"))

    @builtins.property
    @jsii.member(jsii_name="docDbInput")
    def doc_db_input(self) -> typing.Optional["CloudAwsIntegrationsDocDb"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsDocDb"], jsii.get(self, "docDbInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsInput")
    def ebs_input(self) -> typing.Optional["CloudAwsIntegrationsEbs"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsEbs"], jsii.get(self, "ebsInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheInput")
    def elasticache_input(self) -> typing.Optional["CloudAwsIntegrationsElasticache"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsElasticache"], jsii.get(self, "elasticacheInput"))

    @builtins.property
    @jsii.member(jsii_name="healthInput")
    def health_input(self) -> typing.Optional["CloudAwsIntegrationsHealth"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsHealth"], jsii.get(self, "healthInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedAccountIdInput")
    def linked_account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "linkedAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["CloudAwsIntegrationsS3"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="sqsInput")
    def sqs_input(self) -> typing.Optional["CloudAwsIntegrationsSqs"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsSqs"], jsii.get(self, "sqsInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedAdvisorInput")
    def trusted_advisor_input(
        self,
    ) -> typing.Optional["CloudAwsIntegrationsTrustedAdvisor"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsTrustedAdvisor"], jsii.get(self, "trustedAdvisorInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcInput")
    def vpc_input(self) -> typing.Optional["CloudAwsIntegrationsVpc"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsVpc"], jsii.get(self, "vpcInput"))

    @builtins.property
    @jsii.member(jsii_name="xRayInput")
    def x_ray_input(self) -> typing.Optional["CloudAwsIntegrationsXRay"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsXRay"], jsii.get(self, "xRayInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5219cec395e62e4e80020a1434f822e106636205b1c60eb208915ae3fb2ebcc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53bc997685d6f8091c1aeb3bc838d3517467f180193964c59a5ff4dec857a6d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="linkedAccountId")
    def linked_account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "linkedAccountId"))

    @linked_account_id.setter
    def linked_account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__947ffbc6d56f727b440fd8f8118b85c3b51c796e2061df9d54dc4f7e8a8ac873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedAccountId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAlb",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_extended_inventory": "fetchExtendedInventory",
        "fetch_tags": "fetchTags",
        "load_balancer_prefixes": "loadBalancerPrefixes",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsIntegrationsAlb:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        load_balancer_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        :param load_balancer_prefixes: Specify each name or prefix for the LBs that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#load_balancer_prefixes CloudAwsIntegrations#load_balancer_prefixes}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e40c59dd4d07db8036db912b3d55367876e9d77f5205cf22f9f483431901d19)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument load_balancer_prefixes", value=load_balancer_prefixes, expected_type=type_hints["load_balancer_prefixes"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if load_balancer_prefixes is not None:
            self._values["load_balancer_prefixes"] = load_balancer_prefixes
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def load_balancer_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each name or prefix for the LBs that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#load_balancer_prefixes CloudAwsIntegrations#load_balancer_prefixes}
        '''
        result = self._values.get("load_balancer_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsAlb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsAlbOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAlbOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572217df744846f2766d2affe294d69726b61e9680270a7bd923e0111b104af3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetLoadBalancerPrefixes")
    def reset_load_balancer_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerPrefixes", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="resetTagValue")
    def reset_tag_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValue", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerPrefixesInput")
    def load_balancer_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancerPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValueInput")
    def tag_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagValueInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9706cd7ff89e53664ab1cfd3c3035cda1a0cc1be501a30f0e5746e2d3e7e2e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b3ce8feaeaf2af84265f7259427c238e3cfbc42f4c9461ffded1079005d95c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abe6f052ff4d591211660ad507830c4891a9367c1347f6cc8366c041461ed5ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerPrefixes")
    def load_balancer_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancerPrefixes"))

    @load_balancer_prefixes.setter
    def load_balancer_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff379d8c86d86ed60ea79ebb3c74b0994dd7ad6522c150d4ef706818a5ab0df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e3734ab02a24e893e41f78ff92468a606167dbc8be3283b85012bd7b191f99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ed7ae7c08e77ed7e50f49e4c5c6888c8927d4b0a8ccb50aaca10edebdc4867)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__767b2668e3f3efc893160d37ed3ccd4a4903950da2102758a3ecd77ffc8bde44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsAlb]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsAlb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAwsIntegrationsAlb]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ecba4987951050f636453107e5a4b0740c989f21f1391c41ed3a15bc4b2e080)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsApiGateway",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
        "stage_prefixes": "stagePrefixes",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsIntegrationsApiGateway:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        stage_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param stage_prefixes: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#stage_prefixes CloudAwsIntegrations#stage_prefixes}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89c455c691d322c0e9b961d79d5bde588c516e04970357f51f4751bf5c9ca651)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument stage_prefixes", value=stage_prefixes, expected_type=type_hints["stage_prefixes"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if stage_prefixes is not None:
            self._values["stage_prefixes"] = stage_prefixes
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stage_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#stage_prefixes CloudAwsIntegrations#stage_prefixes}
        '''
        result = self._values.get("stage_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsApiGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsApiGatewayOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsApiGatewayOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c0794f271d38a04aa555de1b5ec64fb2d72c06537815188b1ffc3b74b2017ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetStagePrefixes")
    def reset_stage_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStagePrefixes", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="resetTagValue")
    def reset_tag_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValue", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="stagePrefixesInput")
    def stage_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stagePrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValueInput")
    def tag_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagValueInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6b07b9ac4b3c1c86fe1fe990ff471e943866bf78f624acacaf9956ea9190927)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e79ee75f76044b8ae48438ec73f10c6e0ad857ed30e8ed7347e647d247a2885)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="stagePrefixes")
    def stage_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stagePrefixes"))

    @stage_prefixes.setter
    def stage_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df396b0c5b30777f8bb53d69cdfc9dd1db0ea822aaad2bb7f6579b47c47c97da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stagePrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e2f50b2e93d3ce05e2b3e16b68de6ce8a31bb57531f62cbec8b253c53036527)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__520d3a4fe43e7a445173c8f404fe784d1f92ba90fb3425a01e48013b1061ad26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsApiGateway]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsApiGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsApiGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d53085079a55deb7ff8923b44e6ad6676461678ad21ab2c684a7df120f716881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAutoScaling",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsAutoScaling:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab1a637079b6721ef1936e2e172260f07f1596ffa6ce5b0859040f8ee31604d3)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsAutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsAutoScalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAutoScalingOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__492d1f319956f75f675cf675053fd025d349bbe0b2f861cdb21a76b8b9e78b91)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03f8bc1aa7ae647c694a1b75d3d84458de85506dff10366afee1adae3bccd62c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b792f26dc3907e199974d6a32f887bb94d57eb57ac2c2d1f827e677efb439cbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsAutoScaling]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsAutoScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsAutoScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a7c50d259f2a569292112597fd78316ca372be95904b02ac682fd5cceb0cc5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsAppSync",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsAwsAppSync:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeb27c211c2553d9a3ac20e3e8ec713612f8887916f61164f4ba610706ce5dbe)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsAwsAppSync(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsAwsAppSyncOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsAppSyncOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1732a8916426229bff1f258e1e0fbfb9551d43457e7900815ad67cbf8c935cf1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39d8eca29f363bbc313a464a8bf96b7e90acc97acac5f970ea1ae98c47a11982)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0990aaa0fc31abe1c9722fc8f90787dbab338f39159db03369c844db077ca4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsAwsAppSync]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsAppSync], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsAwsAppSync],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65da110080261e9965faa937acfeea8959eb5723430ddd78f97fbe5f9fedd3ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsAthena",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsAwsAthena:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc6d4a1c59279a1b5b4d108de10deb8322e29b7c26b6647a0b9f8abd0e9ab2da)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsAwsAthena(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsAwsAthenaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsAthenaOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a18b1f9bde7a5f8e4e5c85d35cdb72852d1ba915a27d65f1cdefce2e653d21c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1123ec36abb5a0ec0eeb13c02226108192b20c1c8835e822d9b1e2d37bd0c67f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a29993735352695316ee5dc5d3d302b286552c3017ab6912fd42790badc43b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsAwsAthena]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsAthena], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsAwsAthena],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aa9c8cd8ab12498062d6f65aca27198e443a2d07624451850b73388e451c720)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsCognito",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsAwsCognito:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__979a8717df7247972c094e198570b76c0254c4c58f9a386dc643ed39180b3f55)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsAwsCognito(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsAwsCognitoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsCognitoOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5af7b76d436e5475bd65f3d69efe50a2c796953a6b6fea6c1fb6a217d7fa882)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__876abea8542cd18043634adb5243217e00b06937cc0d36feb9860f0a5c094535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e057352b0abd3f42323ec536db2de4e697c734502a5a764a3ca91d3c72022aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsAwsCognito]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsCognito], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsAwsCognito],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__147e934fc44d3874acf250647d9d5452681a389af25271c4bb0d7fdbee12abe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsConnect",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsAwsConnect:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56418f9ce152dc44aaafd1c86907ac25ed16ce9e2b1af0e7aa4ff2b9ae0ad461)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsAwsConnect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsAwsConnectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsConnectOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74e95f82b6a8032ffd4ce668bf74d0f930ab97e94db5d61118551692b1821b11)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__811019247b441fa37f3114612ff411542ea28e5ca9eb8abcf855edfb24893241)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70607156bf068687595e89c93a129d0180b2621363451b7ef3d9398a43e0f8b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsAwsConnect]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsConnect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsAwsConnect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429cabf9d7bc9bbc306dba7a297f0da310c52e115ff57dbfb8dc1243f62d13c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsDirectConnect",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsAwsDirectConnect:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb9a828a1b41fc81696e6197a0e9f57784438b53b7fbbca98e825c9e881814c)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsAwsDirectConnect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsAwsDirectConnectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsDirectConnectOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39b26c7d199640199b08ac7444e459222e1018629846ed750b38efd053816aa1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dd6d86bf944bdfdf1c78bb03ac45a047292ac29ff698a125bcb02d2c9bbe7cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2efed19c1353098726510c48d3e02da2bf407f124af77475dbcec60c7a22c2f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsAwsDirectConnect]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsDirectConnect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsAwsDirectConnect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04033f504cd978f051b4328e6a4f723239bb791237f9682cce0416aebdc4e1a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsFsx",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsAwsFsx:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bd4834378e05043d61d8c41067b08f3a3f361dc6810f60afd63d529c07d5df0)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsAwsFsx(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsAwsFsxOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsAwsFsxOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__222209fdfbdad356c50e8013e190aef00e6ef4c39b648b826d384e636cffebb1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2657143f79e2d78e94c658d14e0bc3216a9954a3d51f9826bc1317a85e4263d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6f896545fa35a91199254e2690d4bc3be4b83626340921d0d25fb5ee699d6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsAwsFsx]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsFsx], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsAwsFsx],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__079d3b1543ee28287c873d94e6d45dc9aaf619f2a6fac2a424494379dc645ab9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsBilling",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudAwsIntegrationsBilling:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e9ccb32fc89d2507f407cef214d9b76981c4a2617faf94bdbaa95a6ca60f3d7)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsBilling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsBillingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsBillingOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a62b82999bd05c07ebf66e82fc1cd50209c887f3e8d6dc616b8642f2880f4679)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5dcbb93b5a3ec7ecb2b967fb94b1d9617184e309d8b240bc3497a0639781d84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsBilling]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsBilling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsBilling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d9b69b3eb4d71e529ac6b4536b8ceaaf0ec2e61eb0d3064868b86777f85484d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsCloudtrail",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsCloudtrail:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9133ba564bcdd8e4779348d80ab1c85ac796b37f55e670dd76c7e2d6c8aa73fb)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsCloudtrail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsCloudtrailOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsCloudtrailOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b6ddf9f2bfcf0c0e767bae6f5221261f7773891ee8bb2cb0935bb827b27f74a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8e5ffa65cec1a9d99267d29a7d0df8763911839b2c7fc3ec6b822357589d34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac2025d900c573c9470c10047d81f45e617e5ba44b85dab88d0e5f8141da6b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsCloudtrail]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsCloudtrail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsCloudtrail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2520ae8e39751ad9964fa5eb5ebc623daec32d6e9e54c03ba08593b5e99b0f82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "linked_account_id": "linkedAccountId",
        "account_id": "accountId",
        "alb": "alb",
        "api_gateway": "apiGateway",
        "auto_scaling": "autoScaling",
        "aws_app_sync": "awsAppSync",
        "aws_athena": "awsAthena",
        "aws_cognito": "awsCognito",
        "aws_connect": "awsConnect",
        "aws_direct_connect": "awsDirectConnect",
        "aws_fsx": "awsFsx",
        "billing": "billing",
        "cloudtrail": "cloudtrail",
        "doc_db": "docDb",
        "ebs": "ebs",
        "elasticache": "elasticache",
        "health": "health",
        "id": "id",
        "s3": "s3",
        "sqs": "sqs",
        "trusted_advisor": "trustedAdvisor",
        "vpc": "vpc",
        "x_ray": "xRay",
    },
)
class CloudAwsIntegrationsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        linked_account_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        alb: typing.Optional[typing.Union[CloudAwsIntegrationsAlb, typing.Dict[builtins.str, typing.Any]]] = None,
        api_gateway: typing.Optional[typing.Union[CloudAwsIntegrationsApiGateway, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_scaling: typing.Optional[typing.Union[CloudAwsIntegrationsAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
        aws_app_sync: typing.Optional[typing.Union[CloudAwsIntegrationsAwsAppSync, typing.Dict[builtins.str, typing.Any]]] = None,
        aws_athena: typing.Optional[typing.Union[CloudAwsIntegrationsAwsAthena, typing.Dict[builtins.str, typing.Any]]] = None,
        aws_cognito: typing.Optional[typing.Union[CloudAwsIntegrationsAwsCognito, typing.Dict[builtins.str, typing.Any]]] = None,
        aws_connect: typing.Optional[typing.Union[CloudAwsIntegrationsAwsConnect, typing.Dict[builtins.str, typing.Any]]] = None,
        aws_direct_connect: typing.Optional[typing.Union[CloudAwsIntegrationsAwsDirectConnect, typing.Dict[builtins.str, typing.Any]]] = None,
        aws_fsx: typing.Optional[typing.Union[CloudAwsIntegrationsAwsFsx, typing.Dict[builtins.str, typing.Any]]] = None,
        billing: typing.Optional[typing.Union[CloudAwsIntegrationsBilling, typing.Dict[builtins.str, typing.Any]]] = None,
        cloudtrail: typing.Optional[typing.Union[CloudAwsIntegrationsCloudtrail, typing.Dict[builtins.str, typing.Any]]] = None,
        doc_db: typing.Optional[typing.Union["CloudAwsIntegrationsDocDb", typing.Dict[builtins.str, typing.Any]]] = None,
        ebs: typing.Optional[typing.Union["CloudAwsIntegrationsEbs", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticache: typing.Optional[typing.Union["CloudAwsIntegrationsElasticache", typing.Dict[builtins.str, typing.Any]]] = None,
        health: typing.Optional[typing.Union["CloudAwsIntegrationsHealth", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        s3: typing.Optional[typing.Union["CloudAwsIntegrationsS3", typing.Dict[builtins.str, typing.Any]]] = None,
        sqs: typing.Optional[typing.Union["CloudAwsIntegrationsSqs", typing.Dict[builtins.str, typing.Any]]] = None,
        trusted_advisor: typing.Optional[typing.Union["CloudAwsIntegrationsTrustedAdvisor", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[typing.Union["CloudAwsIntegrationsVpc", typing.Dict[builtins.str, typing.Any]]] = None,
        x_ray: typing.Optional[typing.Union["CloudAwsIntegrationsXRay", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param linked_account_id: The ID of the linked AWS account in New Relic. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#linked_account_id CloudAwsIntegrations#linked_account_id}
        :param account_id: The ID of the account in New Relic. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#account_id CloudAwsIntegrations#account_id}
        :param alb: alb block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#alb CloudAwsIntegrations#alb}
        :param api_gateway: api_gateway block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#api_gateway CloudAwsIntegrations#api_gateway}
        :param auto_scaling: auto_scaling block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#auto_scaling CloudAwsIntegrations#auto_scaling}
        :param aws_app_sync: aws_app_sync block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_app_sync CloudAwsIntegrations#aws_app_sync}
        :param aws_athena: aws_athena block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_athena CloudAwsIntegrations#aws_athena}
        :param aws_cognito: aws_cognito block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_cognito CloudAwsIntegrations#aws_cognito}
        :param aws_connect: aws_connect block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_connect CloudAwsIntegrations#aws_connect}
        :param aws_direct_connect: aws_direct_connect block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_direct_connect CloudAwsIntegrations#aws_direct_connect}
        :param aws_fsx: aws_fsx block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_fsx CloudAwsIntegrations#aws_fsx}
        :param billing: billing block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#billing CloudAwsIntegrations#billing}
        :param cloudtrail: cloudtrail block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#cloudtrail CloudAwsIntegrations#cloudtrail}
        :param doc_db: doc_db block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#doc_db CloudAwsIntegrations#doc_db}
        :param ebs: ebs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#ebs CloudAwsIntegrations#ebs}
        :param elasticache: elasticache block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#elasticache CloudAwsIntegrations#elasticache}
        :param health: health block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#health CloudAwsIntegrations#health}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#id CloudAwsIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param s3: s3 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#s3 CloudAwsIntegrations#s3}
        :param sqs: sqs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#sqs CloudAwsIntegrations#sqs}
        :param trusted_advisor: trusted_advisor block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#trusted_advisor CloudAwsIntegrations#trusted_advisor}
        :param vpc: vpc block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#vpc CloudAwsIntegrations#vpc}
        :param x_ray: x_ray block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#x_ray CloudAwsIntegrations#x_ray}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alb, dict):
            alb = CloudAwsIntegrationsAlb(**alb)
        if isinstance(api_gateway, dict):
            api_gateway = CloudAwsIntegrationsApiGateway(**api_gateway)
        if isinstance(auto_scaling, dict):
            auto_scaling = CloudAwsIntegrationsAutoScaling(**auto_scaling)
        if isinstance(aws_app_sync, dict):
            aws_app_sync = CloudAwsIntegrationsAwsAppSync(**aws_app_sync)
        if isinstance(aws_athena, dict):
            aws_athena = CloudAwsIntegrationsAwsAthena(**aws_athena)
        if isinstance(aws_cognito, dict):
            aws_cognito = CloudAwsIntegrationsAwsCognito(**aws_cognito)
        if isinstance(aws_connect, dict):
            aws_connect = CloudAwsIntegrationsAwsConnect(**aws_connect)
        if isinstance(aws_direct_connect, dict):
            aws_direct_connect = CloudAwsIntegrationsAwsDirectConnect(**aws_direct_connect)
        if isinstance(aws_fsx, dict):
            aws_fsx = CloudAwsIntegrationsAwsFsx(**aws_fsx)
        if isinstance(billing, dict):
            billing = CloudAwsIntegrationsBilling(**billing)
        if isinstance(cloudtrail, dict):
            cloudtrail = CloudAwsIntegrationsCloudtrail(**cloudtrail)
        if isinstance(doc_db, dict):
            doc_db = CloudAwsIntegrationsDocDb(**doc_db)
        if isinstance(ebs, dict):
            ebs = CloudAwsIntegrationsEbs(**ebs)
        if isinstance(elasticache, dict):
            elasticache = CloudAwsIntegrationsElasticache(**elasticache)
        if isinstance(health, dict):
            health = CloudAwsIntegrationsHealth(**health)
        if isinstance(s3, dict):
            s3 = CloudAwsIntegrationsS3(**s3)
        if isinstance(sqs, dict):
            sqs = CloudAwsIntegrationsSqs(**sqs)
        if isinstance(trusted_advisor, dict):
            trusted_advisor = CloudAwsIntegrationsTrustedAdvisor(**trusted_advisor)
        if isinstance(vpc, dict):
            vpc = CloudAwsIntegrationsVpc(**vpc)
        if isinstance(x_ray, dict):
            x_ray = CloudAwsIntegrationsXRay(**x_ray)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc3ac5886f8796b4cd2e377d13a118f9277a15b3d6884b09bb067e13e9f18b87)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument linked_account_id", value=linked_account_id, expected_type=type_hints["linked_account_id"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument alb", value=alb, expected_type=type_hints["alb"])
            check_type(argname="argument api_gateway", value=api_gateway, expected_type=type_hints["api_gateway"])
            check_type(argname="argument auto_scaling", value=auto_scaling, expected_type=type_hints["auto_scaling"])
            check_type(argname="argument aws_app_sync", value=aws_app_sync, expected_type=type_hints["aws_app_sync"])
            check_type(argname="argument aws_athena", value=aws_athena, expected_type=type_hints["aws_athena"])
            check_type(argname="argument aws_cognito", value=aws_cognito, expected_type=type_hints["aws_cognito"])
            check_type(argname="argument aws_connect", value=aws_connect, expected_type=type_hints["aws_connect"])
            check_type(argname="argument aws_direct_connect", value=aws_direct_connect, expected_type=type_hints["aws_direct_connect"])
            check_type(argname="argument aws_fsx", value=aws_fsx, expected_type=type_hints["aws_fsx"])
            check_type(argname="argument billing", value=billing, expected_type=type_hints["billing"])
            check_type(argname="argument cloudtrail", value=cloudtrail, expected_type=type_hints["cloudtrail"])
            check_type(argname="argument doc_db", value=doc_db, expected_type=type_hints["doc_db"])
            check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
            check_type(argname="argument elasticache", value=elasticache, expected_type=type_hints["elasticache"])
            check_type(argname="argument health", value=health, expected_type=type_hints["health"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument sqs", value=sqs, expected_type=type_hints["sqs"])
            check_type(argname="argument trusted_advisor", value=trusted_advisor, expected_type=type_hints["trusted_advisor"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument x_ray", value=x_ray, expected_type=type_hints["x_ray"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "linked_account_id": linked_account_id,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if account_id is not None:
            self._values["account_id"] = account_id
        if alb is not None:
            self._values["alb"] = alb
        if api_gateway is not None:
            self._values["api_gateway"] = api_gateway
        if auto_scaling is not None:
            self._values["auto_scaling"] = auto_scaling
        if aws_app_sync is not None:
            self._values["aws_app_sync"] = aws_app_sync
        if aws_athena is not None:
            self._values["aws_athena"] = aws_athena
        if aws_cognito is not None:
            self._values["aws_cognito"] = aws_cognito
        if aws_connect is not None:
            self._values["aws_connect"] = aws_connect
        if aws_direct_connect is not None:
            self._values["aws_direct_connect"] = aws_direct_connect
        if aws_fsx is not None:
            self._values["aws_fsx"] = aws_fsx
        if billing is not None:
            self._values["billing"] = billing
        if cloudtrail is not None:
            self._values["cloudtrail"] = cloudtrail
        if doc_db is not None:
            self._values["doc_db"] = doc_db
        if ebs is not None:
            self._values["ebs"] = ebs
        if elasticache is not None:
            self._values["elasticache"] = elasticache
        if health is not None:
            self._values["health"] = health
        if id is not None:
            self._values["id"] = id
        if s3 is not None:
            self._values["s3"] = s3
        if sqs is not None:
            self._values["sqs"] = sqs
        if trusted_advisor is not None:
            self._values["trusted_advisor"] = trusted_advisor
        if vpc is not None:
            self._values["vpc"] = vpc
        if x_ray is not None:
            self._values["x_ray"] = x_ray

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def linked_account_id(self) -> jsii.Number:
        '''The ID of the linked AWS account in New Relic.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#linked_account_id CloudAwsIntegrations#linked_account_id}
        '''
        result = self._values.get("linked_account_id")
        assert result is not None, "Required property 'linked_account_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the account in New Relic.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#account_id CloudAwsIntegrations#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def alb(self) -> typing.Optional[CloudAwsIntegrationsAlb]:
        '''alb block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#alb CloudAwsIntegrations#alb}
        '''
        result = self._values.get("alb")
        return typing.cast(typing.Optional[CloudAwsIntegrationsAlb], result)

    @builtins.property
    def api_gateway(self) -> typing.Optional[CloudAwsIntegrationsApiGateway]:
        '''api_gateway block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#api_gateway CloudAwsIntegrations#api_gateway}
        '''
        result = self._values.get("api_gateway")
        return typing.cast(typing.Optional[CloudAwsIntegrationsApiGateway], result)

    @builtins.property
    def auto_scaling(self) -> typing.Optional[CloudAwsIntegrationsAutoScaling]:
        '''auto_scaling block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#auto_scaling CloudAwsIntegrations#auto_scaling}
        '''
        result = self._values.get("auto_scaling")
        return typing.cast(typing.Optional[CloudAwsIntegrationsAutoScaling], result)

    @builtins.property
    def aws_app_sync(self) -> typing.Optional[CloudAwsIntegrationsAwsAppSync]:
        '''aws_app_sync block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_app_sync CloudAwsIntegrations#aws_app_sync}
        '''
        result = self._values.get("aws_app_sync")
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsAppSync], result)

    @builtins.property
    def aws_athena(self) -> typing.Optional[CloudAwsIntegrationsAwsAthena]:
        '''aws_athena block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_athena CloudAwsIntegrations#aws_athena}
        '''
        result = self._values.get("aws_athena")
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsAthena], result)

    @builtins.property
    def aws_cognito(self) -> typing.Optional[CloudAwsIntegrationsAwsCognito]:
        '''aws_cognito block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_cognito CloudAwsIntegrations#aws_cognito}
        '''
        result = self._values.get("aws_cognito")
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsCognito], result)

    @builtins.property
    def aws_connect(self) -> typing.Optional[CloudAwsIntegrationsAwsConnect]:
        '''aws_connect block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_connect CloudAwsIntegrations#aws_connect}
        '''
        result = self._values.get("aws_connect")
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsConnect], result)

    @builtins.property
    def aws_direct_connect(
        self,
    ) -> typing.Optional[CloudAwsIntegrationsAwsDirectConnect]:
        '''aws_direct_connect block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_direct_connect CloudAwsIntegrations#aws_direct_connect}
        '''
        result = self._values.get("aws_direct_connect")
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsDirectConnect], result)

    @builtins.property
    def aws_fsx(self) -> typing.Optional[CloudAwsIntegrationsAwsFsx]:
        '''aws_fsx block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_fsx CloudAwsIntegrations#aws_fsx}
        '''
        result = self._values.get("aws_fsx")
        return typing.cast(typing.Optional[CloudAwsIntegrationsAwsFsx], result)

    @builtins.property
    def billing(self) -> typing.Optional[CloudAwsIntegrationsBilling]:
        '''billing block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#billing CloudAwsIntegrations#billing}
        '''
        result = self._values.get("billing")
        return typing.cast(typing.Optional[CloudAwsIntegrationsBilling], result)

    @builtins.property
    def cloudtrail(self) -> typing.Optional[CloudAwsIntegrationsCloudtrail]:
        '''cloudtrail block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#cloudtrail CloudAwsIntegrations#cloudtrail}
        '''
        result = self._values.get("cloudtrail")
        return typing.cast(typing.Optional[CloudAwsIntegrationsCloudtrail], result)

    @builtins.property
    def doc_db(self) -> typing.Optional["CloudAwsIntegrationsDocDb"]:
        '''doc_db block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#doc_db CloudAwsIntegrations#doc_db}
        '''
        result = self._values.get("doc_db")
        return typing.cast(typing.Optional["CloudAwsIntegrationsDocDb"], result)

    @builtins.property
    def ebs(self) -> typing.Optional["CloudAwsIntegrationsEbs"]:
        '''ebs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#ebs CloudAwsIntegrations#ebs}
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["CloudAwsIntegrationsEbs"], result)

    @builtins.property
    def elasticache(self) -> typing.Optional["CloudAwsIntegrationsElasticache"]:
        '''elasticache block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#elasticache CloudAwsIntegrations#elasticache}
        '''
        result = self._values.get("elasticache")
        return typing.cast(typing.Optional["CloudAwsIntegrationsElasticache"], result)

    @builtins.property
    def health(self) -> typing.Optional["CloudAwsIntegrationsHealth"]:
        '''health block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#health CloudAwsIntegrations#health}
        '''
        result = self._values.get("health")
        return typing.cast(typing.Optional["CloudAwsIntegrationsHealth"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#id CloudAwsIntegrations#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3(self) -> typing.Optional["CloudAwsIntegrationsS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#s3 CloudAwsIntegrations#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["CloudAwsIntegrationsS3"], result)

    @builtins.property
    def sqs(self) -> typing.Optional["CloudAwsIntegrationsSqs"]:
        '''sqs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#sqs CloudAwsIntegrations#sqs}
        '''
        result = self._values.get("sqs")
        return typing.cast(typing.Optional["CloudAwsIntegrationsSqs"], result)

    @builtins.property
    def trusted_advisor(self) -> typing.Optional["CloudAwsIntegrationsTrustedAdvisor"]:
        '''trusted_advisor block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#trusted_advisor CloudAwsIntegrations#trusted_advisor}
        '''
        result = self._values.get("trusted_advisor")
        return typing.cast(typing.Optional["CloudAwsIntegrationsTrustedAdvisor"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["CloudAwsIntegrationsVpc"]:
        '''vpc block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#vpc CloudAwsIntegrations#vpc}
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["CloudAwsIntegrationsVpc"], result)

    @builtins.property
    def x_ray(self) -> typing.Optional["CloudAwsIntegrationsXRay"]:
        '''x_ray block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#x_ray CloudAwsIntegrations#x_ray}
        '''
        result = self._values.get("x_ray")
        return typing.cast(typing.Optional["CloudAwsIntegrationsXRay"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsDocDb",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsDocDb:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b58ef8635db36e48a559b28b40b82ec4dd41bcbf964598d8e8c2610059fab98)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsDocDb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsDocDbOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsDocDbOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ceccfccb2c01b0f9212f0432a797550e67fbdd0276877c6b924299041c1031)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ebc6521dc6dbb79edfa912af0c774c5085a0c22a1fddfcb7136dfa7d1b116b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0251404e38849d33ade8e61fb4a4f375b9f0abdad07106312e45c3d4b21750a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsDocDb]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsDocDb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAwsIntegrationsDocDb]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc4f66bc4ff0d503483eee5301c5ff5f022809adb60e47f7984abedc805bb6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsEbs",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_extended_inventory": "fetchExtendedInventory",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsIntegrationsEbs:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__909f355c4271f6dcaecbb07f9ada237cc94ab8c821a91e5bafe9fa11b0eaa605)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsEbs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsEbsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsEbsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad2f8518ae0401dc8f55b50b3c4f7351d29e2e022e1474c44c76b6f83aa9f58e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="resetTagValue")
    def reset_tag_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValue", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValueInput")
    def tag_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagValueInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f4efed1910cb6ed6c2b896da5a388a514dc242df2299bec08795f96bdd0486)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36730bf112da13b303a8cd641ce619002c519eb7ac18cb5dd167683f9cdb69c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a615ef6c4966b9a26cc111d73aea7d15f816d304d60e6737c402a3722f5d7e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95154e577bf4ae3b0391027960e94449016f015171fd62ae84f5db2dbe8f54de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24bc95bebc9d91ac422ba41d510ba209286dd5faa95a22078d42ec2d106b948d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsEbs]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsEbs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAwsIntegrationsEbs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef261a2f59459427265681ecb47f61448eeba8cef04471586c8e9342b09dab59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsElasticache",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsIntegrationsElasticache:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94a265d833358b069d2e6598bcd48148ee03e786160cd47ea8e1515310681517)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsElasticache(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsElasticacheOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsElasticacheOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__982457a0f6895e0cc9e1f80aac5819a710b35fe5e69e1ad37a8566845b24346f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="resetTagValue")
    def reset_tag_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValue", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValueInput")
    def tag_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagValueInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f099daa9bd9e534c0a0e2779af92e057c7aee6d6f0750ca8e3273d49f44509c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c301267e8f5404c845359347350c0719602845136378747ad9233a1c1ec9bf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a74d1d6c880c68a800086be7ded5465334eb72d5d1427ee5568066ad8673059)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24d0a572643e1fb4e4492e03f8e8fe7f19bd6dcd5a0cfdf59ba556fc0b47d6e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__905e8b6e7e65d5ad8d98505c01e090be4e9b9a38eea9bbf29a9c8ff00b48ba92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsElasticache]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsElasticache], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsElasticache],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8994f3840bdf7c9bc56e11e083f5a7cc92c467fc900aa90d6e93c38ad2578349)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsHealth",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudAwsIntegrationsHealth:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46c219d859d9fa6c3f00149ad1692a19b0b2ab9eec6f51eacdd9731529b70b36)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsHealth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsHealthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsHealthOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86711bd01ca429e5db58f084e73315a1b7be773c21e46bb74a94ed2a1845097)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2e7878d24eba1730c9b8637f82d3912d9cab70e21be12e9c6003a465cd62f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsHealth]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsHealth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsHealth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24de463ea31715daafca9d6f499d395e152ac71f03aea5f4055fc70ff230ee33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsS3",
    jsii_struct_bases=[],
    name_mapping={
        "fetch_extended_inventory": "fetchExtendedInventory",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsIntegrationsS3:
    def __init__(
        self,
        *,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91ab9b96b00818e6013fe2103e98626b3ebfb0e15dda0b7f25488ae4ca0a47e8)
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsS3OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9e785c94925ae01e650b7ed9f3f0da5e0411ad1fc02448a3cc694243e0db6dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="resetTagValue")
    def reset_tag_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValue", []))

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValueInput")
    def tag_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagValueInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d5070716ec7a9d7a7071ca97c377020954879feea0af0375d8219a691771cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112668b464fb2439d9a502835f3f499c65e2e47667bdb66bbe1ed47e850aac1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6039bca92dc66d6f16736123bcf25b9ff1cdd5a6c24ea16785e120d7afc838d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae4920669dd0f46f8cea694a877d684f673679b85d71afb15f111b4adbeadffa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d80585b215775cad0e9a2ab99cc85bfb96a397ae1c1c2f67522c88666f5de5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsS3]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAwsIntegrationsS3]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__683ccb60ceff40081ecf5543bc48e2f1fe43c3201e15763be3993daa3aa831cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsSqs",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_extended_inventory": "fetchExtendedInventory",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
        "queue_prefixes": "queuePrefixes",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsIntegrationsSqs:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        queue_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param queue_prefixes: Specify each name or prefix for the Queues that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#queue_prefixes CloudAwsIntegrations#queue_prefixes}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff0fdb38a11ddff4ce2122194281474d0b4eb857f20967f959c0b6ff482274d2)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument queue_prefixes", value=queue_prefixes, expected_type=type_hints["queue_prefixes"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if queue_prefixes is not None:
            self._values["queue_prefixes"] = queue_prefixes
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_extended_inventory CloudAwsIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_tags CloudAwsIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def queue_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each name or prefix for the Queues that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#queue_prefixes CloudAwsIntegrations#queue_prefixes}
        '''
        result = self._values.get("queue_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsSqs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsSqsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsSqsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50c82c17993cd532f044fa9bbb76080639102a1097dd3bbd258b6a057e578a21)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetQueuePrefixes")
    def reset_queue_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueuePrefixes", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="resetTagValue")
    def reset_tag_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValue", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="queuePrefixesInput")
    def queue_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queuePrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValueInput")
    def tag_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagValueInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0219280ccbb7365033672650f0457d19210eec5eb655bc3d0e7d22327b3ff7c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd9eb6b104fa1f8dfc59ea1bc3b7db356606c2c4cba4ff623b18a868fd653197)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a8db6cb6573eae10a24accf4282134c50441a61865fed1f40eb25a7548ee70f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f811bea2416e9ddc5496c341d349847fef56cf5073d15b0acb04b3bd5f512d63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="queuePrefixes")
    def queue_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queuePrefixes"))

    @queue_prefixes.setter
    def queue_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__012ec307c9820febb8e3c2880f114b2fe239b4f9ad935334baf578c9dc5dc3ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queuePrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1303753e6b8fc4ca48d1c07abb7cbc0e77ff84cacf809634f6d69c038a004983)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5513d7d34b1d0443eabe5a593433bec77bf17b074d5dafc6871bfedb766913c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsSqs]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsSqs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAwsIntegrationsSqs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1dba19905ae3a482b0cf802cca6aaa7cdd3ef5f4ed826c6e6fc4fcb3d9bc2e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsTrustedAdvisor",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudAwsIntegrationsTrustedAdvisor:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__668858f73919a08f504c8a90bb65ffb65bc1d01d05572ddba939811087652a14)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsTrustedAdvisor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsTrustedAdvisorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsTrustedAdvisorOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8a147261cc3bf496a0e170a5e441607f620af5f12ed60056d946be7f8b8c0f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec4f346a457cb1508ddb025b8d144de7b4840241fc61fa8191b69cf6be3c6e85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsTrustedAdvisor]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsTrustedAdvisor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsTrustedAdvisor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4bc63cefa256d5b5346d16c3750a584927d393bdf9459dbab1f2801aa2c8f36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsVpc",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_nat_gateway": "fetchNatGateway",
        "fetch_vpn": "fetchVpn",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsIntegrationsVpc:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_nat_gateway: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fetch_vpn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_nat_gateway: Specify if NAT gateway should be monitored. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_nat_gateway CloudAwsIntegrations#fetch_nat_gateway}
        :param fetch_vpn: Specify if VPN should be monitored. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_vpn CloudAwsIntegrations#fetch_vpn}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5a05e1712a6079eebfb1cebb9021117640ecdb1735fc94235af901ee1bb64db)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_nat_gateway", value=fetch_nat_gateway, expected_type=type_hints["fetch_nat_gateway"])
            check_type(argname="argument fetch_vpn", value=fetch_vpn, expected_type=type_hints["fetch_vpn"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_nat_gateway is not None:
            self._values["fetch_nat_gateway"] = fetch_nat_gateway
        if fetch_vpn is not None:
            self._values["fetch_vpn"] = fetch_vpn
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_nat_gateway(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specify if NAT gateway should be monitored.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_nat_gateway CloudAwsIntegrations#fetch_nat_gateway}
        '''
        result = self._values.get("fetch_nat_gateway")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def fetch_vpn(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specify if VPN should be monitored.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#fetch_vpn CloudAwsIntegrations#fetch_vpn}
        '''
        result = self._values.get("fetch_vpn")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsVpcOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc03184763dca962a4a8ab314c5c148983b1f331637301224bdc278d238f3491)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchNatGateway")
    def reset_fetch_nat_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchNatGateway", []))

    @jsii.member(jsii_name="resetFetchVpn")
    def reset_fetch_vpn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchVpn", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="resetTagValue")
    def reset_tag_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValue", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchNatGatewayInput")
    def fetch_nat_gateway_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchNatGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchVpnInput")
    def fetch_vpn_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchVpnInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValueInput")
    def tag_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagValueInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__555e7d85f2e58ac7b541bacd19f13077a47af6954e80f4b40ac339755b9b7896)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchNatGateway")
    def fetch_nat_gateway(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchNatGateway"))

    @fetch_nat_gateway.setter
    def fetch_nat_gateway(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2657609fdf500a4e737b95dd4cc4b3d5550f0c3ef0c867e038437ea0e58637)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchNatGateway", value)

    @builtins.property
    @jsii.member(jsii_name="fetchVpn")
    def fetch_vpn(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchVpn"))

    @fetch_vpn.setter
    def fetch_vpn(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3da72c88928d008dd41e6355c8234df0e259a01b0abb531818bb0b36c7caf2c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchVpn", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9579bf68121b247cafa084f153862e870a9191414d93835d82fabaa96a992f14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ac7fa1649a4d226ab4fb2c00a338e4d9911e66ca678b5bcc71bd5245e0bb120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38ea2f558eb8f44587d62e70414f9e1cafca3e2ec1df4590a34f1a3d47499183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsVpc]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAwsIntegrationsVpc]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ac68e78d33565f199421a44fdec8c9985ca38d90c14b0a0d05bbf25fe5b8d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsXRay",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsXRay:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8df10b2612d85d90190d8350575e635e7b3cef8ab626c415ebe5664e6ba53fa3)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/newrelic/newrelic/3.23.0/docs/resources/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsXRay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsXRayOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsXRayOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a6346257c8ea2f1ec9b3140050ddcbf2de3e49b2b5a0d947981b6092478178a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79083a4b7f98cacdf2df9c5b1d5b897d17ff97f9019b6f6c3ae30bb3bebc0d61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4546e51c704af084ceb7556b0b73a76c7e2723052e3525aec1976082b7e3d1a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsXRay]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsXRay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAwsIntegrationsXRay]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a89f8a3bae21c57127494ed28f6b8aaadeb03b9affab91c6a763edc84787e128)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudAwsIntegrations",
    "CloudAwsIntegrationsAlb",
    "CloudAwsIntegrationsAlbOutputReference",
    "CloudAwsIntegrationsApiGateway",
    "CloudAwsIntegrationsApiGatewayOutputReference",
    "CloudAwsIntegrationsAutoScaling",
    "CloudAwsIntegrationsAutoScalingOutputReference",
    "CloudAwsIntegrationsAwsAppSync",
    "CloudAwsIntegrationsAwsAppSyncOutputReference",
    "CloudAwsIntegrationsAwsAthena",
    "CloudAwsIntegrationsAwsAthenaOutputReference",
    "CloudAwsIntegrationsAwsCognito",
    "CloudAwsIntegrationsAwsCognitoOutputReference",
    "CloudAwsIntegrationsAwsConnect",
    "CloudAwsIntegrationsAwsConnectOutputReference",
    "CloudAwsIntegrationsAwsDirectConnect",
    "CloudAwsIntegrationsAwsDirectConnectOutputReference",
    "CloudAwsIntegrationsAwsFsx",
    "CloudAwsIntegrationsAwsFsxOutputReference",
    "CloudAwsIntegrationsBilling",
    "CloudAwsIntegrationsBillingOutputReference",
    "CloudAwsIntegrationsCloudtrail",
    "CloudAwsIntegrationsCloudtrailOutputReference",
    "CloudAwsIntegrationsConfig",
    "CloudAwsIntegrationsDocDb",
    "CloudAwsIntegrationsDocDbOutputReference",
    "CloudAwsIntegrationsEbs",
    "CloudAwsIntegrationsEbsOutputReference",
    "CloudAwsIntegrationsElasticache",
    "CloudAwsIntegrationsElasticacheOutputReference",
    "CloudAwsIntegrationsHealth",
    "CloudAwsIntegrationsHealthOutputReference",
    "CloudAwsIntegrationsS3",
    "CloudAwsIntegrationsS3OutputReference",
    "CloudAwsIntegrationsSqs",
    "CloudAwsIntegrationsSqsOutputReference",
    "CloudAwsIntegrationsTrustedAdvisor",
    "CloudAwsIntegrationsTrustedAdvisorOutputReference",
    "CloudAwsIntegrationsVpc",
    "CloudAwsIntegrationsVpcOutputReference",
    "CloudAwsIntegrationsXRay",
    "CloudAwsIntegrationsXRayOutputReference",
]

publication.publish()

def _typecheckingstub__218636da2f5c84b07b8f11f887c728956d546cee837b90d553762da5832a9fd8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    linked_account_id: jsii.Number,
    account_id: typing.Optional[jsii.Number] = None,
    alb: typing.Optional[typing.Union[CloudAwsIntegrationsAlb, typing.Dict[builtins.str, typing.Any]]] = None,
    api_gateway: typing.Optional[typing.Union[CloudAwsIntegrationsApiGateway, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_scaling: typing.Optional[typing.Union[CloudAwsIntegrationsAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_app_sync: typing.Optional[typing.Union[CloudAwsIntegrationsAwsAppSync, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_athena: typing.Optional[typing.Union[CloudAwsIntegrationsAwsAthena, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_cognito: typing.Optional[typing.Union[CloudAwsIntegrationsAwsCognito, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_connect: typing.Optional[typing.Union[CloudAwsIntegrationsAwsConnect, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_direct_connect: typing.Optional[typing.Union[CloudAwsIntegrationsAwsDirectConnect, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_fsx: typing.Optional[typing.Union[CloudAwsIntegrationsAwsFsx, typing.Dict[builtins.str, typing.Any]]] = None,
    billing: typing.Optional[typing.Union[CloudAwsIntegrationsBilling, typing.Dict[builtins.str, typing.Any]]] = None,
    cloudtrail: typing.Optional[typing.Union[CloudAwsIntegrationsCloudtrail, typing.Dict[builtins.str, typing.Any]]] = None,
    doc_db: typing.Optional[typing.Union[CloudAwsIntegrationsDocDb, typing.Dict[builtins.str, typing.Any]]] = None,
    ebs: typing.Optional[typing.Union[CloudAwsIntegrationsEbs, typing.Dict[builtins.str, typing.Any]]] = None,
    elasticache: typing.Optional[typing.Union[CloudAwsIntegrationsElasticache, typing.Dict[builtins.str, typing.Any]]] = None,
    health: typing.Optional[typing.Union[CloudAwsIntegrationsHealth, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    s3: typing.Optional[typing.Union[CloudAwsIntegrationsS3, typing.Dict[builtins.str, typing.Any]]] = None,
    sqs: typing.Optional[typing.Union[CloudAwsIntegrationsSqs, typing.Dict[builtins.str, typing.Any]]] = None,
    trusted_advisor: typing.Optional[typing.Union[CloudAwsIntegrationsTrustedAdvisor, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[typing.Union[CloudAwsIntegrationsVpc, typing.Dict[builtins.str, typing.Any]]] = None,
    x_ray: typing.Optional[typing.Union[CloudAwsIntegrationsXRay, typing.Dict[builtins.str, typing.Any]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5219cec395e62e4e80020a1434f822e106636205b1c60eb208915ae3fb2ebcc2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53bc997685d6f8091c1aeb3bc838d3517467f180193964c59a5ff4dec857a6d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__947ffbc6d56f727b440fd8f8118b85c3b51c796e2061df9d54dc4f7e8a8ac873(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e40c59dd4d07db8036db912b3d55367876e9d77f5205cf22f9f483431901d19(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    load_balancer_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572217df744846f2766d2affe294d69726b61e9680270a7bd923e0111b104af3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9706cd7ff89e53664ab1cfd3c3035cda1a0cc1be501a30f0e5746e2d3e7e2e0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b3ce8feaeaf2af84265f7259427c238e3cfbc42f4c9461ffded1079005d95c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe6f052ff4d591211660ad507830c4891a9367c1347f6cc8366c041461ed5ee(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff379d8c86d86ed60ea79ebb3c74b0994dd7ad6522c150d4ef706818a5ab0df(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e3734ab02a24e893e41f78ff92468a606167dbc8be3283b85012bd7b191f99(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ed7ae7c08e77ed7e50f49e4c5c6888c8927d4b0a8ccb50aaca10edebdc4867(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__767b2668e3f3efc893160d37ed3ccd4a4903950da2102758a3ecd77ffc8bde44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ecba4987951050f636453107e5a4b0740c989f21f1391c41ed3a15bc4b2e080(
    value: typing.Optional[CloudAwsIntegrationsAlb],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89c455c691d322c0e9b961d79d5bde588c516e04970357f51f4751bf5c9ca651(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
    stage_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c0794f271d38a04aa555de1b5ec64fb2d72c06537815188b1ffc3b74b2017ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6b07b9ac4b3c1c86fe1fe990ff471e943866bf78f624acacaf9956ea9190927(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e79ee75f76044b8ae48438ec73f10c6e0ad857ed30e8ed7347e647d247a2885(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df396b0c5b30777f8bb53d69cdfc9dd1db0ea822aaad2bb7f6579b47c47c97da(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2f50b2e93d3ce05e2b3e16b68de6ce8a31bb57531f62cbec8b253c53036527(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520d3a4fe43e7a445173c8f404fe784d1f92ba90fb3425a01e48013b1061ad26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d53085079a55deb7ff8923b44e6ad6676461678ad21ab2c684a7df120f716881(
    value: typing.Optional[CloudAwsIntegrationsApiGateway],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab1a637079b6721ef1936e2e172260f07f1596ffa6ce5b0859040f8ee31604d3(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__492d1f319956f75f675cf675053fd025d349bbe0b2f861cdb21a76b8b9e78b91(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03f8bc1aa7ae647c694a1b75d3d84458de85506dff10366afee1adae3bccd62c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b792f26dc3907e199974d6a32f887bb94d57eb57ac2c2d1f827e677efb439cbd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a7c50d259f2a569292112597fd78316ca372be95904b02ac682fd5cceb0cc5a(
    value: typing.Optional[CloudAwsIntegrationsAutoScaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb27c211c2553d9a3ac20e3e8ec713612f8887916f61164f4ba610706ce5dbe(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1732a8916426229bff1f258e1e0fbfb9551d43457e7900815ad67cbf8c935cf1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39d8eca29f363bbc313a464a8bf96b7e90acc97acac5f970ea1ae98c47a11982(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0990aaa0fc31abe1c9722fc8f90787dbab338f39159db03369c844db077ca4c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65da110080261e9965faa937acfeea8959eb5723430ddd78f97fbe5f9fedd3ce(
    value: typing.Optional[CloudAwsIntegrationsAwsAppSync],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc6d4a1c59279a1b5b4d108de10deb8322e29b7c26b6647a0b9f8abd0e9ab2da(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a18b1f9bde7a5f8e4e5c85d35cdb72852d1ba915a27d65f1cdefce2e653d21c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1123ec36abb5a0ec0eeb13c02226108192b20c1c8835e822d9b1e2d37bd0c67f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a29993735352695316ee5dc5d3d302b286552c3017ab6912fd42790badc43b9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aa9c8cd8ab12498062d6f65aca27198e443a2d07624451850b73388e451c720(
    value: typing.Optional[CloudAwsIntegrationsAwsAthena],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979a8717df7247972c094e198570b76c0254c4c58f9a386dc643ed39180b3f55(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5af7b76d436e5475bd65f3d69efe50a2c796953a6b6fea6c1fb6a217d7fa882(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__876abea8542cd18043634adb5243217e00b06937cc0d36feb9860f0a5c094535(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e057352b0abd3f42323ec536db2de4e697c734502a5a764a3ca91d3c72022aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__147e934fc44d3874acf250647d9d5452681a389af25271c4bb0d7fdbee12abe2(
    value: typing.Optional[CloudAwsIntegrationsAwsCognito],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56418f9ce152dc44aaafd1c86907ac25ed16ce9e2b1af0e7aa4ff2b9ae0ad461(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74e95f82b6a8032ffd4ce668bf74d0f930ab97e94db5d61118551692b1821b11(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__811019247b441fa37f3114612ff411542ea28e5ca9eb8abcf855edfb24893241(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70607156bf068687595e89c93a129d0180b2621363451b7ef3d9398a43e0f8b1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429cabf9d7bc9bbc306dba7a297f0da310c52e115ff57dbfb8dc1243f62d13c4(
    value: typing.Optional[CloudAwsIntegrationsAwsConnect],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb9a828a1b41fc81696e6197a0e9f57784438b53b7fbbca98e825c9e881814c(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39b26c7d199640199b08ac7444e459222e1018629846ed750b38efd053816aa1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dd6d86bf944bdfdf1c78bb03ac45a047292ac29ff698a125bcb02d2c9bbe7cf(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2efed19c1353098726510c48d3e02da2bf407f124af77475dbcec60c7a22c2f9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04033f504cd978f051b4328e6a4f723239bb791237f9682cce0416aebdc4e1a5(
    value: typing.Optional[CloudAwsIntegrationsAwsDirectConnect],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bd4834378e05043d61d8c41067b08f3a3f361dc6810f60afd63d529c07d5df0(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__222209fdfbdad356c50e8013e190aef00e6ef4c39b648b826d384e636cffebb1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2657143f79e2d78e94c658d14e0bc3216a9954a3d51f9826bc1317a85e4263d0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6f896545fa35a91199254e2690d4bc3be4b83626340921d0d25fb5ee699d6e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__079d3b1543ee28287c873d94e6d45dc9aaf619f2a6fac2a424494379dc645ab9(
    value: typing.Optional[CloudAwsIntegrationsAwsFsx],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e9ccb32fc89d2507f407cef214d9b76981c4a2617faf94bdbaa95a6ca60f3d7(
    *,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a62b82999bd05c07ebf66e82fc1cd50209c887f3e8d6dc616b8642f2880f4679(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5dcbb93b5a3ec7ecb2b967fb94b1d9617184e309d8b240bc3497a0639781d84(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d9b69b3eb4d71e529ac6b4536b8ceaaf0ec2e61eb0d3064868b86777f85484d(
    value: typing.Optional[CloudAwsIntegrationsBilling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9133ba564bcdd8e4779348d80ab1c85ac796b37f55e670dd76c7e2d6c8aa73fb(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b6ddf9f2bfcf0c0e767bae6f5221261f7773891ee8bb2cb0935bb827b27f74a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8e5ffa65cec1a9d99267d29a7d0df8763911839b2c7fc3ec6b822357589d34(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac2025d900c573c9470c10047d81f45e617e5ba44b85dab88d0e5f8141da6b1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2520ae8e39751ad9964fa5eb5ebc623daec32d6e9e54c03ba08593b5e99b0f82(
    value: typing.Optional[CloudAwsIntegrationsCloudtrail],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3ac5886f8796b4cd2e377d13a118f9277a15b3d6884b09bb067e13e9f18b87(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    linked_account_id: jsii.Number,
    account_id: typing.Optional[jsii.Number] = None,
    alb: typing.Optional[typing.Union[CloudAwsIntegrationsAlb, typing.Dict[builtins.str, typing.Any]]] = None,
    api_gateway: typing.Optional[typing.Union[CloudAwsIntegrationsApiGateway, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_scaling: typing.Optional[typing.Union[CloudAwsIntegrationsAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_app_sync: typing.Optional[typing.Union[CloudAwsIntegrationsAwsAppSync, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_athena: typing.Optional[typing.Union[CloudAwsIntegrationsAwsAthena, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_cognito: typing.Optional[typing.Union[CloudAwsIntegrationsAwsCognito, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_connect: typing.Optional[typing.Union[CloudAwsIntegrationsAwsConnect, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_direct_connect: typing.Optional[typing.Union[CloudAwsIntegrationsAwsDirectConnect, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_fsx: typing.Optional[typing.Union[CloudAwsIntegrationsAwsFsx, typing.Dict[builtins.str, typing.Any]]] = None,
    billing: typing.Optional[typing.Union[CloudAwsIntegrationsBilling, typing.Dict[builtins.str, typing.Any]]] = None,
    cloudtrail: typing.Optional[typing.Union[CloudAwsIntegrationsCloudtrail, typing.Dict[builtins.str, typing.Any]]] = None,
    doc_db: typing.Optional[typing.Union[CloudAwsIntegrationsDocDb, typing.Dict[builtins.str, typing.Any]]] = None,
    ebs: typing.Optional[typing.Union[CloudAwsIntegrationsEbs, typing.Dict[builtins.str, typing.Any]]] = None,
    elasticache: typing.Optional[typing.Union[CloudAwsIntegrationsElasticache, typing.Dict[builtins.str, typing.Any]]] = None,
    health: typing.Optional[typing.Union[CloudAwsIntegrationsHealth, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    s3: typing.Optional[typing.Union[CloudAwsIntegrationsS3, typing.Dict[builtins.str, typing.Any]]] = None,
    sqs: typing.Optional[typing.Union[CloudAwsIntegrationsSqs, typing.Dict[builtins.str, typing.Any]]] = None,
    trusted_advisor: typing.Optional[typing.Union[CloudAwsIntegrationsTrustedAdvisor, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[typing.Union[CloudAwsIntegrationsVpc, typing.Dict[builtins.str, typing.Any]]] = None,
    x_ray: typing.Optional[typing.Union[CloudAwsIntegrationsXRay, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b58ef8635db36e48a559b28b40b82ec4dd41bcbf964598d8e8c2610059fab98(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ceccfccb2c01b0f9212f0432a797550e67fbdd0276877c6b924299041c1031(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ebc6521dc6dbb79edfa912af0c774c5085a0c22a1fddfcb7136dfa7d1b116b4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0251404e38849d33ade8e61fb4a4f375b9f0abdad07106312e45c3d4b21750a1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc4f66bc4ff0d503483eee5301c5ff5f022809adb60e47f7984abedc805bb6e(
    value: typing.Optional[CloudAwsIntegrationsDocDb],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__909f355c4271f6dcaecbb07f9ada237cc94ab8c821a91e5bafe9fa11b0eaa605(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2f8518ae0401dc8f55b50b3c4f7351d29e2e022e1474c44c76b6f83aa9f58e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f4efed1910cb6ed6c2b896da5a388a514dc242df2299bec08795f96bdd0486(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36730bf112da13b303a8cd641ce619002c519eb7ac18cb5dd167683f9cdb69c6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a615ef6c4966b9a26cc111d73aea7d15f816d304d60e6737c402a3722f5d7e5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95154e577bf4ae3b0391027960e94449016f015171fd62ae84f5db2dbe8f54de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24bc95bebc9d91ac422ba41d510ba209286dd5faa95a22078d42ec2d106b948d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef261a2f59459427265681ecb47f61448eeba8cef04471586c8e9342b09dab59(
    value: typing.Optional[CloudAwsIntegrationsEbs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94a265d833358b069d2e6598bcd48148ee03e786160cd47ea8e1515310681517(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__982457a0f6895e0cc9e1f80aac5819a710b35fe5e69e1ad37a8566845b24346f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f099daa9bd9e534c0a0e2779af92e057c7aee6d6f0750ca8e3273d49f44509c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c301267e8f5404c845359347350c0719602845136378747ad9233a1c1ec9bf4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a74d1d6c880c68a800086be7ded5465334eb72d5d1427ee5568066ad8673059(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24d0a572643e1fb4e4492e03f8e8fe7f19bd6dcd5a0cfdf59ba556fc0b47d6e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__905e8b6e7e65d5ad8d98505c01e090be4e9b9a38eea9bbf29a9c8ff00b48ba92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8994f3840bdf7c9bc56e11e083f5a7cc92c467fc900aa90d6e93c38ad2578349(
    value: typing.Optional[CloudAwsIntegrationsElasticache],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c219d859d9fa6c3f00149ad1692a19b0b2ab9eec6f51eacdd9731529b70b36(
    *,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86711bd01ca429e5db58f084e73315a1b7be773c21e46bb74a94ed2a1845097(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2e7878d24eba1730c9b8637f82d3912d9cab70e21be12e9c6003a465cd62f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24de463ea31715daafca9d6f499d395e152ac71f03aea5f4055fc70ff230ee33(
    value: typing.Optional[CloudAwsIntegrationsHealth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ab9b96b00818e6013fe2103e98626b3ebfb0e15dda0b7f25488ae4ca0a47e8(
    *,
    fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e785c94925ae01e650b7ed9f3f0da5e0411ad1fc02448a3cc694243e0db6dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d5070716ec7a9d7a7071ca97c377020954879feea0af0375d8219a691771cc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112668b464fb2439d9a502835f3f499c65e2e47667bdb66bbe1ed47e850aac1a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6039bca92dc66d6f16736123bcf25b9ff1cdd5a6c24ea16785e120d7afc838d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae4920669dd0f46f8cea694a877d684f673679b85d71afb15f111b4adbeadffa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d80585b215775cad0e9a2ab99cc85bfb96a397ae1c1c2f67522c88666f5de5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683ccb60ceff40081ecf5543bc48e2f1fe43c3201e15763be3993daa3aa831cc(
    value: typing.Optional[CloudAwsIntegrationsS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff0fdb38a11ddff4ce2122194281474d0b4eb857f20967f959c0b6ff482274d2(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fetch_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
    queue_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c82c17993cd532f044fa9bbb76080639102a1097dd3bbd258b6a057e578a21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0219280ccbb7365033672650f0457d19210eec5eb655bc3d0e7d22327b3ff7c8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd9eb6b104fa1f8dfc59ea1bc3b7db356606c2c4cba4ff623b18a868fd653197(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a8db6cb6573eae10a24accf4282134c50441a61865fed1f40eb25a7548ee70f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f811bea2416e9ddc5496c341d349847fef56cf5073d15b0acb04b3bd5f512d63(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__012ec307c9820febb8e3c2880f114b2fe239b4f9ad935334baf578c9dc5dc3ed(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1303753e6b8fc4ca48d1c07abb7cbc0e77ff84cacf809634f6d69c038a004983(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5513d7d34b1d0443eabe5a593433bec77bf17b074d5dafc6871bfedb766913c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1dba19905ae3a482b0cf802cca6aaa7cdd3ef5f4ed826c6e6fc4fcb3d9bc2e4(
    value: typing.Optional[CloudAwsIntegrationsSqs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__668858f73919a08f504c8a90bb65ffb65bc1d01d05572ddba939811087652a14(
    *,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8a147261cc3bf496a0e170a5e441607f620af5f12ed60056d946be7f8b8c0f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4f346a457cb1508ddb025b8d144de7b4840241fc61fa8191b69cf6be3c6e85(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4bc63cefa256d5b5346d16c3750a584927d393bdf9459dbab1f2801aa2c8f36(
    value: typing.Optional[CloudAwsIntegrationsTrustedAdvisor],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5a05e1712a6079eebfb1cebb9021117640ecdb1735fc94235af901ee1bb64db(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    fetch_nat_gateway: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fetch_vpn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc03184763dca962a4a8ab314c5c148983b1f331637301224bdc278d238f3491(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__555e7d85f2e58ac7b541bacd19f13077a47af6954e80f4b40ac339755b9b7896(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2657609fdf500a4e737b95dd4cc4b3d5550f0c3ef0c867e038437ea0e58637(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da72c88928d008dd41e6355c8234df0e259a01b0abb531818bb0b36c7caf2c8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9579bf68121b247cafa084f153862e870a9191414d93835d82fabaa96a992f14(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ac7fa1649a4d226ab4fb2c00a338e4d9911e66ca678b5bcc71bd5245e0bb120(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38ea2f558eb8f44587d62e70414f9e1cafca3e2ec1df4590a34f1a3d47499183(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ac68e78d33565f199421a44fdec8c9985ca38d90c14b0a0d05bbf25fe5b8d7(
    value: typing.Optional[CloudAwsIntegrationsVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8df10b2612d85d90190d8350575e635e7b3cef8ab626c415ebe5664e6ba53fa3(
    *,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_polling_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a6346257c8ea2f1ec9b3140050ddcbf2de3e49b2b5a0d947981b6092478178a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79083a4b7f98cacdf2df9c5b1d5b897d17ff97f9019b6f6c3ae30bb3bebc0d61(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4546e51c704af084ceb7556b0b73a76c7e2723052e3525aec1976082b7e3d1a3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a89f8a3bae21c57127494ed28f6b8aaadeb03b9affab91c6a763edc84787e128(
    value: typing.Optional[CloudAwsIntegrationsXRay],
) -> None:
    """Type checking stubs"""
    pass
