# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paiplugin20220112 import models as pai_plugin_20220112_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('paiplugin', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_campaign_with_options(
        self,
        request: pai_plugin_20220112_models.CreateCampaignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateCampaignResponse:
        """
        注册运营活动。
        
        @param request: CreateCampaignRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCampaignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCampaign',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_campaign_with_options_async(
        self,
        request: pai_plugin_20220112_models.CreateCampaignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateCampaignResponse:
        """
        注册运营活动。
        
        @param request: CreateCampaignRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCampaignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCampaign',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_campaign(
        self,
        request: pai_plugin_20220112_models.CreateCampaignRequest,
    ) -> pai_plugin_20220112_models.CreateCampaignResponse:
        """
        注册运营活动。
        
        @param request: CreateCampaignRequest
        @return: CreateCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_campaign_with_options(request, headers, runtime)

    async def create_campaign_async(
        self,
        request: pai_plugin_20220112_models.CreateCampaignRequest,
    ) -> pai_plugin_20220112_models.CreateCampaignResponse:
        """
        注册运营活动。
        
        @param request: CreateCampaignRequest
        @return: CreateCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_campaign_with_options_async(request, headers, runtime)

    def create_group_with_options(
        self,
        request: pai_plugin_20220112_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateGroupResponse:
        """
        注册人群。
        
        @param request: CreateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.inference_job_id):
            body['InferenceJobId'] = request.inference_job_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.project):
            body['Project'] = request.project
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: pai_plugin_20220112_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateGroupResponse:
        """
        注册人群。
        
        @param request: CreateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.inference_job_id):
            body['InferenceJobId'] = request.inference_job_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.project):
            body['Project'] = request.project
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: pai_plugin_20220112_models.CreateGroupRequest,
    ) -> pai_plugin_20220112_models.CreateGroupResponse:
        """
        注册人群。
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: pai_plugin_20220112_models.CreateGroupRequest,
    ) -> pai_plugin_20220112_models.CreateGroupResponse:
        """
        注册人群。
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_group_with_options_async(request, headers, runtime)

    def create_inference_job_with_options(
        self,
        request: pai_plugin_20220112_models.CreateInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateInferenceJobResponse:
        """
        注册预测任务。
        
        @param request: CreateInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.campaign_id):
            body['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.data_path):
            body['DataPath'] = request.data_path
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.target_path):
            body['TargetPath'] = request.target_path
        if not UtilClient.is_unset(request.training_job_id):
            body['TrainingJobId'] = request.training_job_id
        if not UtilClient.is_unset(request.user_config):
            body['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInferenceJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/inference/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_inference_job_with_options_async(
        self,
        request: pai_plugin_20220112_models.CreateInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateInferenceJobResponse:
        """
        注册预测任务。
        
        @param request: CreateInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.campaign_id):
            body['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.data_path):
            body['DataPath'] = request.data_path
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.target_path):
            body['TargetPath'] = request.target_path
        if not UtilClient.is_unset(request.training_job_id):
            body['TrainingJobId'] = request.training_job_id
        if not UtilClient.is_unset(request.user_config):
            body['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInferenceJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/inference/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_inference_job(
        self,
        request: pai_plugin_20220112_models.CreateInferenceJobRequest,
    ) -> pai_plugin_20220112_models.CreateInferenceJobResponse:
        """
        注册预测任务。
        
        @param request: CreateInferenceJobRequest
        @return: CreateInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_inference_job_with_options(request, headers, runtime)

    async def create_inference_job_async(
        self,
        request: pai_plugin_20220112_models.CreateInferenceJobRequest,
    ) -> pai_plugin_20220112_models.CreateInferenceJobResponse:
        """
        注册预测任务。
        
        @param request: CreateInferenceJobRequest
        @return: CreateInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_inference_job_with_options_async(request, headers, runtime)

    def create_schedule_with_options(
        self,
        request: pai_plugin_20220112_models.CreateScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateScheduleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aisend_end_date):
            body['AISendEndDate'] = request.aisend_end_date
        if not UtilClient.is_unset(request.aisend_start_date):
            body['AISendStartDate'] = request.aisend_start_date
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_time):
            body['ExecuteTime'] = request.execute_time
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.repeat_cycle):
            body['RepeatCycle'] = request.repeat_cycle
        if not UtilClient.is_unset(request.repeat_cycle_unit):
            body['RepeatCycleUnit'] = request.repeat_cycle_unit
        if not UtilClient.is_unset(request.repeat_times):
            body['RepeatTimes'] = request.repeat_times
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSchedule',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/schedules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedule_with_options_async(
        self,
        request: pai_plugin_20220112_models.CreateScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateScheduleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aisend_end_date):
            body['AISendEndDate'] = request.aisend_end_date
        if not UtilClient.is_unset(request.aisend_start_date):
            body['AISendStartDate'] = request.aisend_start_date
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_time):
            body['ExecuteTime'] = request.execute_time
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.repeat_cycle):
            body['RepeatCycle'] = request.repeat_cycle
        if not UtilClient.is_unset(request.repeat_cycle_unit):
            body['RepeatCycleUnit'] = request.repeat_cycle_unit
        if not UtilClient.is_unset(request.repeat_times):
            body['RepeatTimes'] = request.repeat_times
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSchedule',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/schedules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedule(
        self,
        request: pai_plugin_20220112_models.CreateScheduleRequest,
    ) -> pai_plugin_20220112_models.CreateScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_schedule_with_options(request, headers, runtime)

    async def create_schedule_async(
        self,
        request: pai_plugin_20220112_models.CreateScheduleRequest,
    ) -> pai_plugin_20220112_models.CreateScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_schedule_with_options_async(request, headers, runtime)

    def create_signature_with_options(
        self,
        request: pai_plugin_20220112_models.CreateSignatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_signature_with_options_async(
        self,
        request: pai_plugin_20220112_models.CreateSignatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_signature(
        self,
        request: pai_plugin_20220112_models.CreateSignatureRequest,
    ) -> pai_plugin_20220112_models.CreateSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_signature_with_options(request, headers, runtime)

    async def create_signature_async(
        self,
        request: pai_plugin_20220112_models.CreateSignatureRequest,
    ) -> pai_plugin_20220112_models.CreateSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_signature_with_options_async(request, headers, runtime)

    def create_template_with_options(
        self,
        request: pai_plugin_20220112_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.signature):
            body['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: pai_plugin_20220112_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.signature):
            body['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: pai_plugin_20220112_models.CreateTemplateRequest,
    ) -> pai_plugin_20220112_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    async def create_template_async(
        self,
        request: pai_plugin_20220112_models.CreateTemplateRequest,
    ) -> pai_plugin_20220112_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(request, headers, runtime)

    def create_training_job_with_options(
        self,
        request: pai_plugin_20220112_models.CreateTrainingJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateTrainingJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.campaign_id):
            body['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.data_path):
            body['DataPath'] = request.data_path
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_config):
            body['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/training/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_training_job_with_options_async(
        self,
        request: pai_plugin_20220112_models.CreateTrainingJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.CreateTrainingJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.campaign_id):
            body['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.data_path):
            body['DataPath'] = request.data_path
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_config):
            body['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/training/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_training_job(
        self,
        request: pai_plugin_20220112_models.CreateTrainingJobRequest,
    ) -> pai_plugin_20220112_models.CreateTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_training_job_with_options(request, headers, runtime)

    async def create_training_job_async(
        self,
        request: pai_plugin_20220112_models.CreateTrainingJobRequest,
    ) -> pai_plugin_20220112_models.CreateTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_training_job_with_options_async(request, headers, runtime)

    def delete_campaign_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteCampaignResponse:
        """
        删除运营活动
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCampaignResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCampaign',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_campaign_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteCampaignResponse:
        """
        删除运营活动
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCampaignResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCampaign',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_campaign(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteCampaignResponse:
        """
        删除运营活动
        
        @return: DeleteCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_campaign_with_options(id, headers, runtime)

    async def delete_campaign_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteCampaignResponse:
        """
        删除运营活动
        
        @return: DeleteCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_campaign_with_options_async(id, headers, runtime)

    def delete_group_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteGroupResponse:
        """
        删除人群
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/groups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteGroupResponse:
        """
        删除人群
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/groups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteGroupResponse:
        """
        删除人群
        
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(id, headers, runtime)

    async def delete_group_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteGroupResponse:
        """
        删除人群
        
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_group_with_options_async(id, headers, runtime)

    def delete_inference_job_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteInferenceJobResponse:
        """
        删除预测任务。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInferenceJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInferenceJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/inference/jobs/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_inference_job_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteInferenceJobResponse:
        """
        删除预测任务。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInferenceJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInferenceJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/inference/jobs/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_inference_job(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteInferenceJobResponse:
        """
        删除预测任务。
        
        @return: DeleteInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_inference_job_with_options(id, headers, runtime)

    async def delete_inference_job_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteInferenceJobResponse:
        """
        删除预测任务。
        
        @return: DeleteInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_inference_job_with_options_async(id, headers, runtime)

    def delete_schedule_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteScheduleResponse:
        """
        删除触达计划。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSchedule',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/schedules/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schedule_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteScheduleResponse:
        """
        删除触达计划。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSchedule',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/schedules/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schedule(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteScheduleResponse:
        """
        删除触达计划。
        
        @return: DeleteScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_schedule_with_options(id, headers, runtime)

    async def delete_schedule_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteScheduleResponse:
        """
        删除触达计划。
        
        @return: DeleteScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_schedule_with_options_async(id, headers, runtime)

    def delete_signature_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteSignatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_signature_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteSignatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_signature(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_signature_with_options(id, headers, runtime)

    async def delete_signature_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_signature_with_options_async(id, headers, runtime)

    def delete_template_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteTemplateResponse:
        """
        删除模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteTemplateResponse:
        """
        删除模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteTemplateResponse:
        """
        删除模板
        
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(id, headers, runtime)

    async def delete_template_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteTemplateResponse:
        """
        删除模板
        
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(id, headers, runtime)

    def delete_training_job_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteTrainingJobResponse:
        """
        删除训练任务。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrainingJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/training/jobs/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_training_job_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.DeleteTrainingJobResponse:
        """
        删除训练任务。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrainingJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/training/jobs/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_training_job(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteTrainingJobResponse:
        """
        删除训练任务。
        
        @return: DeleteTrainingJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_training_job_with_options(id, headers, runtime)

    async def delete_training_job_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.DeleteTrainingJobResponse:
        """
        删除训练任务。
        
        @return: DeleteTrainingJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_training_job_with_options_async(id, headers, runtime)

    def get_algorithm_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetAlgorithmResponse:
        """
        获取算法详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAlgorithmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlgorithm',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/algorithms/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetAlgorithmResponse:
        """
        获取算法详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAlgorithmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlgorithm',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/algorithms/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetAlgorithmResponse:
        """
        获取算法详情。
        
        @return: GetAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_with_options(id, headers, runtime)

    async def get_algorithm_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetAlgorithmResponse:
        """
        获取算法详情。
        
        @return: GetAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_algorithm_with_options_async(id, headers, runtime)

    def get_campaign_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetCampaignResponse:
        """
        获取运营活动详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCampaignResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCampaign',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_campaign_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetCampaignResponse:
        """
        获取运营活动详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCampaignResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCampaign',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_campaign(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetCampaignResponse:
        """
        获取运营活动详情。
        
        @return: GetCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_campaign_with_options(id, headers, runtime)

    async def get_campaign_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetCampaignResponse:
        """
        获取运营活动详情。
        
        @return: GetCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_campaign_with_options_async(id, headers, runtime)

    def get_group_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetGroupResponse:
        """
        获取人群详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/groups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetGroupResponse:
        """
        获取人群详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/groups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetGroupResponse:
        """
        获取人群详情。
        
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_with_options(id, headers, runtime)

    async def get_group_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetGroupResponse:
        """
        获取人群详情。
        
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_group_with_options_async(id, headers, runtime)

    def get_inference_job_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetInferenceJobResponse:
        """
        获取预测任务详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInferenceJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInferenceJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/inference/jobs/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inference_job_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetInferenceJobResponse:
        """
        获取预测任务详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInferenceJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInferenceJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/inference/jobs/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inference_job(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetInferenceJobResponse:
        """
        获取预测任务详情。
        
        @return: GetInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_inference_job_with_options(id, headers, runtime)

    async def get_inference_job_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetInferenceJobResponse:
        """
        获取预测任务详情。
        
        @return: GetInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_inference_job_with_options_async(id, headers, runtime)

    def get_message_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetMessageConfigResponse:
        """
        获取短信配置。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMessageConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMessageConfig',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/messageConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetMessageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetMessageConfigResponse:
        """
        获取短信配置。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMessageConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMessageConfig',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/messageConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetMessageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_config(self) -> pai_plugin_20220112_models.GetMessageConfigResponse:
        """
        获取短信配置。
        
        @return: GetMessageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_message_config_with_options(headers, runtime)

    async def get_message_config_async(self) -> pai_plugin_20220112_models.GetMessageConfigResponse:
        """
        获取短信配置。
        
        @return: GetMessageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_message_config_with_options_async(headers, runtime)

    def get_schedule_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetScheduleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSchedule',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/schedules/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schedule_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetScheduleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSchedule',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/schedules/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schedule(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_schedule_with_options(id, headers, runtime)

    async def get_schedule_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_schedule_with_options_async(id, headers, runtime)

    def get_signature_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetSignatureResponse:
        """
        获取签名详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_signature_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetSignatureResponse:
        """
        获取签名详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_signature(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetSignatureResponse:
        """
        获取签名详情。
        
        @return: GetSignatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_signature_with_options(id, headers, runtime)

    async def get_signature_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetSignatureResponse:
        """
        获取签名详情。
        
        @return: GetSignatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_signature_with_options_async(id, headers, runtime)

    def get_template_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetTemplateResponse:
        """
        获取模板详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetTemplateResponse:
        """
        获取模板详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetTemplateResponse:
        """
        获取模板详情。
        
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(id, headers, runtime)

    async def get_template_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetTemplateResponse:
        """
        获取模板详情。
        
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(id, headers, runtime)

    def get_training_job_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetTrainingJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/training/jobs/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_training_job_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetTrainingJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/training/jobs/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_training_job(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_training_job_with_options(id, headers, runtime)

    async def get_training_job_async(
        self,
        id: str,
    ) -> pai_plugin_20220112_models.GetTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_training_job_with_options_async(id, headers, runtime)

    def get_user_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetUserResponse:
        """
        获取账号状态。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.GetUserResponse:
        """
        获取账号状态。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(self) -> pai_plugin_20220112_models.GetUserResponse:
        """
        获取账号状态。
        
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(headers, runtime)

    async def get_user_async(self) -> pai_plugin_20220112_models.GetUserResponse:
        """
        获取账号状态。
        
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(headers, runtime)

    def list_algorithms_with_options(
        self,
        request: pai_plugin_20220112_models.ListAlgorithmsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListAlgorithmsResponse:
        """
        获取算法列表。
        
        @param request: ListAlgorithmsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlgorithmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlgorithms',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/algorithms',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListAlgorithmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_algorithms_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListAlgorithmsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListAlgorithmsResponse:
        """
        获取算法列表。
        
        @param request: ListAlgorithmsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlgorithmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlgorithms',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/algorithms',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListAlgorithmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_algorithms(
        self,
        request: pai_plugin_20220112_models.ListAlgorithmsRequest,
    ) -> pai_plugin_20220112_models.ListAlgorithmsResponse:
        """
        获取算法列表。
        
        @param request: ListAlgorithmsRequest
        @return: ListAlgorithmsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_algorithms_with_options(request, headers, runtime)

    async def list_algorithms_async(
        self,
        request: pai_plugin_20220112_models.ListAlgorithmsRequest,
    ) -> pai_plugin_20220112_models.ListAlgorithmsResponse:
        """
        获取算法列表。
        
        @param request: ListAlgorithmsRequest
        @return: ListAlgorithmsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_algorithms_with_options_async(request, headers, runtime)

    def list_campaigns_with_options(
        self,
        request: pai_plugin_20220112_models.ListCampaignsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListCampaignsResponse:
        """
        获取运营活动列表。
        
        @param request: ListCampaignsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCampaignsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaigns',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListCampaignsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_campaigns_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListCampaignsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListCampaignsResponse:
        """
        获取运营活动列表。
        
        @param request: ListCampaignsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCampaignsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaigns',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListCampaignsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_campaigns(
        self,
        request: pai_plugin_20220112_models.ListCampaignsRequest,
    ) -> pai_plugin_20220112_models.ListCampaignsResponse:
        """
        获取运营活动列表。
        
        @param request: ListCampaignsRequest
        @return: ListCampaignsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_campaigns_with_options(request, headers, runtime)

    async def list_campaigns_async(
        self,
        request: pai_plugin_20220112_models.ListCampaignsRequest,
    ) -> pai_plugin_20220112_models.ListCampaignsResponse:
        """
        获取运营活动列表。
        
        @param request: ListCampaignsRequest
        @return: ListCampaignsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_campaigns_with_options_async(request, headers, runtime)

    def list_groups_with_options(
        self,
        request: pai_plugin_20220112_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListGroupsResponse:
        """
        获取人群列表。
        
        @param request: ListGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListGroupsResponse:
        """
        获取人群列表。
        
        @param request: ListGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: pai_plugin_20220112_models.ListGroupsRequest,
    ) -> pai_plugin_20220112_models.ListGroupsResponse:
        """
        获取人群列表。
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_groups_with_options(request, headers, runtime)

    async def list_groups_async(
        self,
        request: pai_plugin_20220112_models.ListGroupsRequest,
    ) -> pai_plugin_20220112_models.ListGroupsResponse:
        """
        获取人群列表。
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_groups_with_options_async(request, headers, runtime)

    def list_inference_jobs_with_options(
        self,
        request: pai_plugin_20220112_models.ListInferenceJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListInferenceJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.campaign_name):
            query['CampaignName'] = request.campaign_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.training_job_name):
            query['TrainingJobName'] = request.training_job_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInferenceJobs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/inference/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListInferenceJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_inference_jobs_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListInferenceJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListInferenceJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.campaign_name):
            query['CampaignName'] = request.campaign_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.training_job_name):
            query['TrainingJobName'] = request.training_job_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInferenceJobs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/inference/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListInferenceJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_inference_jobs(
        self,
        request: pai_plugin_20220112_models.ListInferenceJobsRequest,
    ) -> pai_plugin_20220112_models.ListInferenceJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_inference_jobs_with_options(request, headers, runtime)

    async def list_inference_jobs_async(
        self,
        request: pai_plugin_20220112_models.ListInferenceJobsRequest,
    ) -> pai_plugin_20220112_models.ListInferenceJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_inference_jobs_with_options_async(request, headers, runtime)

    def list_message_metrics_with_options(
        self,
        request: pai_plugin_20220112_models.ListMessageMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListMessageMetricsResponse:
        """
        获取短信发送统计列表。
        获取短信发送统计数据，可按指定条件获取分类别详细数据，返回数据按日期顺序排列，发送统计为空的日期默认不返回。
        发送数据在48小时内会随实际短信发送状态不断更新，最终数据以48小时后数据为准。
        
        @param request: ListMessageMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMessageMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessageMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessageMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_message_metrics_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListMessageMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListMessageMetricsResponse:
        """
        获取短信发送统计列表。
        获取短信发送统计数据，可按指定条件获取分类别详细数据，返回数据按日期顺序排列，发送统计为空的日期默认不返回。
        发送数据在48小时内会随实际短信发送状态不断更新，最终数据以48小时后数据为准。
        
        @param request: ListMessageMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMessageMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessageMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessageMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_message_metrics(
        self,
        request: pai_plugin_20220112_models.ListMessageMetricsRequest,
    ) -> pai_plugin_20220112_models.ListMessageMetricsResponse:
        """
        获取短信发送统计列表。
        获取短信发送统计数据，可按指定条件获取分类别详细数据，返回数据按日期顺序排列，发送统计为空的日期默认不返回。
        发送数据在48小时内会随实际短信发送状态不断更新，最终数据以48小时后数据为准。
        
        @param request: ListMessageMetricsRequest
        @return: ListMessageMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_message_metrics_with_options(request, headers, runtime)

    async def list_message_metrics_async(
        self,
        request: pai_plugin_20220112_models.ListMessageMetricsRequest,
    ) -> pai_plugin_20220112_models.ListMessageMetricsResponse:
        """
        获取短信发送统计列表。
        获取短信发送统计数据，可按指定条件获取分类别详细数据，返回数据按日期顺序排列，发送统计为空的日期默认不返回。
        发送数据在48小时内会随实际短信发送状态不断更新，最终数据以48小时后数据为准。
        
        @param request: ListMessageMetricsRequest
        @return: ListMessageMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_message_metrics_with_options_async(request, headers, runtime)

    def list_messages_with_options(
        self,
        request: pai_plugin_20220112_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListMessagesResponse:
        """
        查询短信发送详情列表。
        
        @param request: ListMessagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMessagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datetime):
            query['Datetime'] = request.datetime
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessages',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_messages_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListMessagesResponse:
        """
        查询短信发送详情列表。
        
        @param request: ListMessagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMessagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datetime):
            query['Datetime'] = request.datetime
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessages',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_messages(
        self,
        request: pai_plugin_20220112_models.ListMessagesRequest,
    ) -> pai_plugin_20220112_models.ListMessagesResponse:
        """
        查询短信发送详情列表。
        
        @param request: ListMessagesRequest
        @return: ListMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_messages_with_options(request, headers, runtime)

    async def list_messages_async(
        self,
        request: pai_plugin_20220112_models.ListMessagesRequest,
    ) -> pai_plugin_20220112_models.ListMessagesResponse:
        """
        查询短信发送详情列表。
        
        @param request: ListMessagesRequest
        @return: ListMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_messages_with_options_async(request, headers, runtime)

    def list_schedules_with_options(
        self,
        request: pai_plugin_20220112_models.ListSchedulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListSchedulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchedules',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/schedules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schedules_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListSchedulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListSchedulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchedules',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/schedules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListSchedulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schedules(
        self,
        request: pai_plugin_20220112_models.ListSchedulesRequest,
    ) -> pai_plugin_20220112_models.ListSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_schedules_with_options(request, headers, runtime)

    async def list_schedules_async(
        self,
        request: pai_plugin_20220112_models.ListSchedulesRequest,
    ) -> pai_plugin_20220112_models.ListSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_schedules_with_options_async(request, headers, runtime)

    def list_signatures_with_options(
        self,
        request: pai_plugin_20220112_models.ListSignaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListSignaturesResponse:
        """
        获取签名列表。
        
        @param request: ListSignaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSignaturesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSignatures',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_signatures_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListSignaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListSignaturesResponse:
        """
        获取签名列表。
        
        @param request: ListSignaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSignaturesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSignatures',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/signatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListSignaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_signatures(
        self,
        request: pai_plugin_20220112_models.ListSignaturesRequest,
    ) -> pai_plugin_20220112_models.ListSignaturesResponse:
        """
        获取签名列表。
        
        @param request: ListSignaturesRequest
        @return: ListSignaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_signatures_with_options(request, headers, runtime)

    async def list_signatures_async(
        self,
        request: pai_plugin_20220112_models.ListSignaturesRequest,
    ) -> pai_plugin_20220112_models.ListSignaturesResponse:
        """
        获取签名列表。
        
        @param request: ListSignaturesRequest
        @return: ListSignaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_signatures_with_options_async(request, headers, runtime)

    def list_templates_with_options(
        self,
        request: pai_plugin_20220112_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListTemplatesResponse:
        """
        获取模板列表。
        
        @param request: ListTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListTemplatesResponse:
        """
        获取模板列表。
        
        @param request: ListTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: pai_plugin_20220112_models.ListTemplatesRequest,
    ) -> pai_plugin_20220112_models.ListTemplatesResponse:
        """
        获取模板列表。
        
        @param request: ListTemplatesRequest
        @return: ListTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    async def list_templates_async(
        self,
        request: pai_plugin_20220112_models.ListTemplatesRequest,
    ) -> pai_plugin_20220112_models.ListTemplatesResponse:
        """
        获取模板列表。
        
        @param request: ListTemplatesRequest
        @return: ListTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(request, headers, runtime)

    def list_training_jobs_with_options(
        self,
        request: pai_plugin_20220112_models.ListTrainingJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListTrainingJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.campaign_name):
            query['CampaignName'] = request.campaign_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.training_schedule_id):
            query['TrainingScheduleId'] = request.training_schedule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrainingJobs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/training/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListTrainingJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_jobs_with_options_async(
        self,
        request: pai_plugin_20220112_models.ListTrainingJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.ListTrainingJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.campaign_name):
            query['CampaignName'] = request.campaign_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.training_schedule_id):
            query['TrainingScheduleId'] = request.training_schedule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrainingJobs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/training/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListTrainingJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_jobs(
        self,
        request: pai_plugin_20220112_models.ListTrainingJobsRequest,
    ) -> pai_plugin_20220112_models.ListTrainingJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_training_jobs_with_options(request, headers, runtime)

    async def list_training_jobs_async(
        self,
        request: pai_plugin_20220112_models.ListTrainingJobsRequest,
    ) -> pai_plugin_20220112_models.ListTrainingJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_training_jobs_with_options_async(request, headers, runtime)

    def send_message_with_options(
        self,
        request: pai_plugin_20220112_models.SendMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.out_ids):
            body['OutIds'] = request.out_ids
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.phone_numbers):
            body['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.schedule_id):
            body['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.sms_up_extend_codes):
            body['SmsUpExtendCodes'] = request.sms_up_extend_codes
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_params):
            body['TemplateParams'] = request.template_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: pai_plugin_20220112_models.SendMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.out_ids):
            body['OutIds'] = request.out_ids
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.phone_numbers):
            body['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.schedule_id):
            body['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.sms_up_extend_codes):
            body['SmsUpExtendCodes'] = request.sms_up_extend_codes
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_params):
            body['TemplateParams'] = request.template_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/messages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: pai_plugin_20220112_models.SendMessageRequest,
    ) -> pai_plugin_20220112_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_message_with_options(request, headers, runtime)

    async def send_message_async(
        self,
        request: pai_plugin_20220112_models.SendMessageRequest,
    ) -> pai_plugin_20220112_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_message_with_options_async(request, headers, runtime)

    def sms_report_with_options(
        self,
        request: pai_plugin_20220112_models.SmsReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SmsReportResponse:
        """
        短信回执。
        
        @param request: SmsReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SmsReportResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='SmsReport',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/recall/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SmsReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_report_with_options_async(
        self,
        request: pai_plugin_20220112_models.SmsReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SmsReportResponse:
        """
        短信回执。
        
        @param request: SmsReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SmsReportResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='SmsReport',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/recall/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SmsReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_report(
        self,
        request: pai_plugin_20220112_models.SmsReportRequest,
    ) -> pai_plugin_20220112_models.SmsReportResponse:
        """
        短信回执。
        
        @param request: SmsReportRequest
        @return: SmsReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sms_report_with_options(request, headers, runtime)

    async def sms_report_async(
        self,
        request: pai_plugin_20220112_models.SmsReportRequest,
    ) -> pai_plugin_20220112_models.SmsReportResponse:
        """
        短信回执。
        
        @param request: SmsReportRequest
        @return: SmsReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sms_report_with_options_async(request, headers, runtime)

    def sms_up_with_options(
        self,
        request: pai_plugin_20220112_models.SmsUpRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SmsUpResponse:
        """
        短信上行。
        
        @param request: SmsUpRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SmsUpResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='SmsUp',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/recall/up',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SmsUpResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_up_with_options_async(
        self,
        request: pai_plugin_20220112_models.SmsUpRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.SmsUpResponse:
        """
        短信上行。
        
        @param request: SmsUpRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SmsUpResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='SmsUp',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/recall/up',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SmsUpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_up(
        self,
        request: pai_plugin_20220112_models.SmsUpRequest,
    ) -> pai_plugin_20220112_models.SmsUpResponse:
        """
        短信上行。
        
        @param request: SmsUpRequest
        @return: SmsUpResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sms_up_with_options(request, headers, runtime)

    async def sms_up_async(
        self,
        request: pai_plugin_20220112_models.SmsUpRequest,
    ) -> pai_plugin_20220112_models.SmsUpResponse:
        """
        短信上行。
        
        @param request: SmsUpRequest
        @return: SmsUpResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sms_up_with_options_async(request, headers, runtime)

    def update_campaign_with_options(
        self,
        id: str,
        request: pai_plugin_20220112_models.UpdateCampaignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateCampaignResponse:
        """
        更新运营活动
        
        @param request: UpdateCampaignRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCampaignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCampaign',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_campaign_with_options_async(
        self,
        id: str,
        request: pai_plugin_20220112_models.UpdateCampaignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateCampaignResponse:
        """
        更新运营活动
        
        @param request: UpdateCampaignRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCampaignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCampaign',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/campaigns/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_campaign(
        self,
        id: str,
        request: pai_plugin_20220112_models.UpdateCampaignRequest,
    ) -> pai_plugin_20220112_models.UpdateCampaignResponse:
        """
        更新运营活动
        
        @param request: UpdateCampaignRequest
        @return: UpdateCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_campaign_with_options(id, request, headers, runtime)

    async def update_campaign_async(
        self,
        id: str,
        request: pai_plugin_20220112_models.UpdateCampaignRequest,
    ) -> pai_plugin_20220112_models.UpdateCampaignResponse:
        """
        更新运营活动
        
        @param request: UpdateCampaignRequest
        @return: UpdateCampaignResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_campaign_with_options_async(id, request, headers, runtime)

    def update_report_url_with_options(
        self,
        request: pai_plugin_20220112_models.UpdateReportUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateReportUrlResponse:
        """
        更新回执Url。
        
        @param request: UpdateReportUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateReportUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportUrl',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/reportUrl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateReportUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_report_url_with_options_async(
        self,
        request: pai_plugin_20220112_models.UpdateReportUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateReportUrlResponse:
        """
        更新回执Url。
        
        @param request: UpdateReportUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateReportUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportUrl',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/reportUrl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateReportUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_report_url(
        self,
        request: pai_plugin_20220112_models.UpdateReportUrlRequest,
    ) -> pai_plugin_20220112_models.UpdateReportUrlResponse:
        """
        更新回执Url。
        
        @param request: UpdateReportUrlRequest
        @return: UpdateReportUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_report_url_with_options(request, headers, runtime)

    async def update_report_url_async(
        self,
        request: pai_plugin_20220112_models.UpdateReportUrlRequest,
    ) -> pai_plugin_20220112_models.UpdateReportUrlResponse:
        """
        更新回执Url。
        
        @param request: UpdateReportUrlRequest
        @return: UpdateReportUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_report_url_with_options_async(request, headers, runtime)

    def update_upload_url_with_options(
        self,
        request: pai_plugin_20220112_models.UpdateUploadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateUploadUrlResponse:
        """
        更新上行Url。
        
        @param request: UpdateUploadUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUploadUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUploadUrl',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/uploadUrl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_upload_url_with_options_async(
        self,
        request: pai_plugin_20220112_models.UpdateUploadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20220112_models.UpdateUploadUrlResponse:
        """
        更新上行Url。
        
        @param request: UpdateUploadUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUploadUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUploadUrl',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v2/users/uploadUrl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.UpdateUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_upload_url(
        self,
        request: pai_plugin_20220112_models.UpdateUploadUrlRequest,
    ) -> pai_plugin_20220112_models.UpdateUploadUrlResponse:
        """
        更新上行Url。
        
        @param request: UpdateUploadUrlRequest
        @return: UpdateUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_upload_url_with_options(request, headers, runtime)

    async def update_upload_url_async(
        self,
        request: pai_plugin_20220112_models.UpdateUploadUrlRequest,
    ) -> pai_plugin_20220112_models.UpdateUploadUrlResponse:
        """
        更新上行Url。
        
        @param request: UpdateUploadUrlRequest
        @return: UpdateUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_upload_url_with_options_async(request, headers, runtime)
