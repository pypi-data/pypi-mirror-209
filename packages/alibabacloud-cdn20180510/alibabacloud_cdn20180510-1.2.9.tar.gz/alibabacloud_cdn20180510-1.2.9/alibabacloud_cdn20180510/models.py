# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AddCdnDomainRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddCdnDomainRequest(TeaModel):
    def __init__(
        self,
        cdn_type: str = None,
        check_url: str = None,
        domain_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        scope: str = None,
        security_token: str = None,
        sources: str = None,
        tag: List[AddCdnDomainRequestTag] = None,
        top_level_domain: str = None,
    ):
        self.cdn_type = cdn_type
        self.check_url = check_url
        self.domain_name = domain_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_group_id = resource_group_id
        self.scope = scope
        self.security_token = security_token
        self.sources = sources
        self.tag = tag
        self.top_level_domain = top_level_domain

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = AddCdnDomainRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class AddCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCdnDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFCTriggerRequest(TeaModel):
    def __init__(
        self,
        event_meta_name: str = None,
        event_meta_version: str = None,
        function_arn: str = None,
        notes: str = None,
        role_arn: str = None,
        source_arn: str = None,
        trigger_arn: str = None,
    ):
        # The name of the event.
        self.event_meta_name = event_meta_name
        # The version of the event.
        self.event_meta_version = event_meta_version
        # The feature trigger.
        self.function_arn = function_arn
        # The remarks.
        self.notes = notes
        # The assigned Resource Access Management (RAM) role.
        self.role_arn = role_arn
        # The resources and filters for event listening.
        self.source_arn = source_arn
        # The trigger that corresponds to the Function Compute service.
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        if self.function_arn is not None:
            result['FunctionARN'] = self.function_arn
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceARN'] = self.source_arn
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        if m.get('FunctionARN') is not None:
            self.function_arn = m.get('FunctionARN')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceARN') is not None:
            self.source_arn = m.get('SourceARN')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class AddFCTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFCTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddCdnDomainRequest(TeaModel):
    def __init__(
        self,
        cdn_type: str = None,
        check_url: str = None,
        domain_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        scope: str = None,
        security_token: str = None,
        sources: str = None,
        top_level_domain: str = None,
    ):
        self.cdn_type = cdn_type
        self.check_url = check_url
        self.domain_name = domain_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_group_id = resource_group_id
        self.scope = scope
        self.security_token = security_token
        self.sources = sources
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class BatchAddCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchAddCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddCdnDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchAddCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteCdnDomainConfigRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        function_names: str = None,
        owner_account: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The operation that you want to perform. Set the value to **BatchDeleteCdnDomainConfig**.
        self.domain_names = domain_names
        # The names of the features that you want to manage. Separate feature names with commas (,).
        self.function_names = function_names
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchDeleteCdnDomainConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Deletes configurations of multiple accelerated domain names at a time.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteCdnDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteCdnDomainConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteCdnDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetCdnDomainConfigRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        functions: str = None,
        owner_account: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the configuration.
        self.domain_names = domain_names
        # The domain name.
        self.functions = functions
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchSetCdnDomainConfigResponseBodyDomainConfigListDomainConfigModel(TeaModel):
    def __init__(
        self,
        config_id: int = None,
        domain_name: str = None,
        function_name: str = None,
    ):
        # The list of domain configurations.
        self.config_id = config_id
        # The accelerated domain name. Separate multiple accelerated domain names with commas (,).
        self.domain_name = domain_name
        # The domain name.
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class BatchSetCdnDomainConfigResponseBodyDomainConfigList(TeaModel):
    def __init__(
        self,
        domain_config_model: List[BatchSetCdnDomainConfigResponseBodyDomainConfigListDomainConfigModel] = None,
    ):
        self.domain_config_model = domain_config_model

    def validate(self):
        if self.domain_config_model:
            for k in self.domain_config_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfigModel'] = []
        if self.domain_config_model is not None:
            for k in self.domain_config_model:
                result['DomainConfigModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_config_model = []
        if m.get('DomainConfigModel') is not None:
            for k in m.get('DomainConfigModel'):
                temp_model = BatchSetCdnDomainConfigResponseBodyDomainConfigListDomainConfigModel()
                self.domain_config_model.append(temp_model.from_map(k))
        return self


class BatchSetCdnDomainConfigResponseBody(TeaModel):
    def __init__(
        self,
        domain_config_list: BatchSetCdnDomainConfigResponseBodyDomainConfigList = None,
        request_id: str = None,
    ):
        # > *   You can call this operation up to 30 times per second per account.
        # *   You can specify multiple domain names and must separate them with commas (,). You can specify up to 50 domain names in each call.
        # *   If the BatchSetCdnDomainConfig operation is successful, a unique configuration ID (ConfigId) is generated. You can use configuration IDs to update or delete configurations. For more information, see [Usage notes on ConfigId](~~388994~~).
        self.domain_config_list = domain_config_list
        # The name of the feature.
        self.request_id = request_id

    def validate(self):
        if self.domain_config_list:
            self.domain_config_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_config_list is not None:
            result['DomainConfigList'] = self.domain_config_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainConfigList') is not None:
            temp_model = BatchSetCdnDomainConfigResponseBodyDomainConfigList()
            self.domain_config_list = temp_model.from_map(m['DomainConfigList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchSetCdnDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchSetCdnDomainConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchSetCdnDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetCdnDomainServerCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_type: str = None,
        domain_name: str = None,
        force_set: str = None,
        owner_id: int = None,
        region: str = None,
        sslpri: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        security_token: str = None,
    ):
        # The region.
        self.cert_name = cert_name
        # Specifies whether to enable the SSL certificate. Valid values:
        # 
        # *   **on**: enables the SSL certificate.
        # *   **off**: disables the SSL certificate. This is the default value.
        self.cert_type = cert_type
        # The type of the SSL certificate. Valid values:
        # 
        # *   **upload**: a user-uploaded SSL certificate.
        # *   **cas**: a certificate that is issued by SSL Certificates Service.
        self.domain_name = domain_name
        self.force_set = force_set
        self.owner_id = owner_id
        self.region = region
        # The content of the SSL certificate. Specify the content of the certificate only if you want to enable the SSL certificate.
        self.sslpri = sslpri
        # The ID of the request.
        self.sslprotocol = sslprotocol
        # The operation that you want to perform. Set the value to **BatchSetCdnDomainServerCertificate**.
        self.sslpub = sslpub
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.force_set is not None:
            result['ForceSet'] = self.force_set
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchSetCdnDomainServerCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchSetCdnDomainServerCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchSetCdnDomainServerCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchSetCdnDomainServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartCdnDomainRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the request.
        self.domain_names = domain_names
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchStartCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 1.0.0
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchStartCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchStartCdnDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchStartCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopCdnDomainRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # *   After an accelerated domain name is disabled, Alibaba Cloud CDN retains its information and reroutes all the requests that are destined for the accelerated domain name to the origin.
        # *   If you need to temporarily disable CDN acceleration for a domain name, we recommend that you call the StopDomain operation.
        # *   You can call this operation up to 30 times per second per account.
        # *   You can specify up to 50 domain names in each request.
        self.domain_names = domain_names
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchStopCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The names of the accelerated domain names. You can specify one or more domain names in each request. Separate multiple domain names with commas (,).
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchStopCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchStopCdnDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchStopCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateCdnDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        security_token: str = None,
        sources: str = None,
        top_level_domain: str = None,
    ):
        # The top-level domain name.
        # 
        # >  You can set only one of **Sources** and **TopLevelDomain**. If you set both **Sources** and **TopLevelDomain**, **TopLevelDomain** does not take effect.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The ID of the request.
        self.resource_group_id = resource_group_id
        self.security_token = security_token
        # The accelerated domain names. You can specify one or more accelerated domain names. Separate domain names with commas (,).
        self.sources = sources
        # The operation that you want to perform. Set the value to **BatchUpdateCdnDomain**.
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class BatchUpdateCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The information about the addresses of origin servers.
        # 
        # >  You can set only one of **Sources** and **TopLevelDomain**. If you set both **Sources** and **TopLevelDomain**, **TopLevelDomain** does not take effect.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchUpdateCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateCdnDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchUpdateCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnCertificateSigningRequestRequest(TeaModel):
    def __init__(
        self,
        city: str = None,
        common_name: str = None,
        country: str = None,
        email: str = None,
        organization: str = None,
        organization_unit: str = None,
        sans: str = None,
        state: str = None,
    ):
        # The city to which the organization belongs. Default value: Hangzhou.
        self.city = city
        # The email address that can be used to contact the organization.
        self.common_name = common_name
        # The content of the CSR.
        self.country = country
        # The operation that you want to perform. Set the value to **CreateCdnCertificateSigningRequest**.
        self.email = email
        # The Subject Alternative Name (SAN) extension of the SSL certificate. This extension is used to add domain names to the certificate. Separate multiple domain names with commas (,).
        self.organization = organization
        # The MD5 value of the certificate public key.
        self.organization_unit = organization_unit
        # The Common Name of the certificate.
        self.sans = sans
        # The name of the organization. Default value: Alibaba Inc.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.email is not None:
            result['Email'] = self.email
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.sans is not None:
            result['SANs'] = self.sans
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('SANs') is not None:
            self.sans = m.get('SANs')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class CreateCdnCertificateSigningRequestResponseBody(TeaModel):
    def __init__(
        self,
        common_name: str = None,
        csr: str = None,
        pub_md_5: str = None,
        request_id: str = None,
    ):
        # The name of the organization unit. Default value: Aliyun CDN.
        self.common_name = common_name
        # The Common Name of the SSL certificate.
        self.csr = csr
        # The provincial district to which the organization belongs. Default value: Zhejiang.
        self.pub_md_5 = pub_md_5
        # The country to which the organization belongs. Default value: CN.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.pub_md_5 is not None:
            result['PubMd5'] = self.pub_md_5
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('PubMd5') is not None:
            self.pub_md_5 = m.get('PubMd5')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCdnCertificateSigningRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCdnCertificateSigningRequestResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCdnCertificateSigningRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnDeliverTaskRequest(TeaModel):
    def __init__(
        self,
        deliver: str = None,
        domain_name: str = None,
        name: str = None,
        reports: str = None,
        schedule: str = None,
    ):
        # The ID of the tracking task.
        self.deliver = deliver
        # The method that is used to send operations reports. Operations reports are sent to you only by email. The settings must be escaped in JSON.
        self.domain_name = domain_name
        # > You can call this operation up to three times per second per account.
        self.name = name
        # The operations reports that are tracked by the task. The data must be escaped in JSON.
        self.reports = reports
        # The parameters that specify the time interval at which the tracking task sends operations reports. The settings must be escaped in JSON.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deliver is not None:
            result['Deliver'] = self.deliver
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.name is not None:
            result['Name'] = self.name
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class CreateCdnDeliverTaskResponseBody(TeaModel):
    def __init__(
        self,
        deliver_id: str = None,
        request_id: str = None,
    ):
        # **Fields of the ReDatas parameter**\
        # 
        # | Parameter | Type | Required | Description |
        # | --------- | ---- | -------- | ----------- |
        # | reportId | String | Yes | The ID of the operations report. |
        # | conditions | ConDatas[] | No | The filter conditions for the operations report. |
        # 
        # **Fields of the ConDatas parameter**\
        # 
        # | Parameter | Type | Required | Description |
        # | --------- | ---- | -------- | ----------- |
        # | field | String | No | The filter field. |
        # | op | String | No | The filter operation. |
        # | value | String[] | No | The array of field values. |
        # 
        # **Fields of the email parameter**\
        # 
        # | Parameter | Type | Required | Description |
        # | --------- | ---- | -------- | ----------- |
        # | subject | String | Yes | The email subject. |
        # | to | String[] | Yes | The email addresses to which operations reports are sent. |
        # 
        # **Fields of the Deliver parameter**\
        # 
        # | Parameter | Type | Required | Description |
        # | --------- | ---- | -------- | ----------- |
        # | subject | String | No | The email subject. |
        # | to | String[] | Yes | The email addresses to which operations reports are sent. |
        # 
        # **Fields of the Schedule parameter**\
        # 
        # | Parameter | Type | Required | Description |
        # | --------- | ---- | -------- | ----------- |
        # | schedName | String | No | The name of the tracking task. |
        # | description | String | No | The description of the tracking task. |
        # | crontab | String | Yes | The period during which the operations reports are tracked. |
        # | frequency | String | Yes | The interval at which the reports are sent. Valid values:<br/>**h**: every hour <br/>**d**: every day <br/>**w**: every week |
        # | status | String | No | The status of the tracking task. Valid values:<br/>**enable**: enabled<br/>**disable**: disabled |
        # | effectiveFrom | String | No | The start time of the tracking task. |
        # | effectiveEnd | String | No | The end time of the tracking task. |
        self.deliver_id = deliver_id
        # Creates a tracking task that generates operations reports. The tracking task sends operations reports to a specified email address based on a specified schedule.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCdnDeliverTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCdnDeliverTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnSubTaskRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        report_ids: str = None,
    ):
        self.domain_name = domain_name
        self.report_ids = report_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')
        return self


class CreateCdnSubTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCdnSubTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCdnSubTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRealTimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        logstore: str = None,
        project: str = None,
        region: str = None,
    ):
        # The accelerated domain name for which you want to configure real-time log delivery.
        self.domain = domain
        # The name of the Logstore where log entries are stored.
        self.logstore = logstore
        # The name of the Log Service project that is used for real-time log delivery.
        self.project = project
        # The ID of the region where the Log Service project is deployed. For more information, see [Regions that support real-time log delivery](~~144883~~).
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateRealTimeLogDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRealTimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRealTimeLogDeliveryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRealTimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUsageDetailDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        end_time: str = None,
        group: str = None,
        language: str = None,
        start_time: str = None,
        task_name: str = None,
        type: str = None,
    ):
        self.domain_names = domain_names
        self.end_time = end_time
        self.group = group
        self.language = language
        self.start_time = start_time
        self.task_name = task_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group is not None:
            result['Group'] = self.group
        if self.language is not None:
            result['Language'] = self.language
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateUsageDetailDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        task_id: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateUsageDetailDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUsageDetailDataExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUsageDetailDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserUsageDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        language: str = None,
        start_time: str = None,
        task_name: str = None,
    ):
        self.end_time = end_time
        self.language = language
        self.start_time = start_time
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.language is not None:
            result['Language'] = self.language
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateUserUsageDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        task_id: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateUserUsageDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserUsageDataExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserUsageDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCdnDeliverTaskRequest(TeaModel):
    def __init__(
        self,
        deliver_id: int = None,
    ):
        # The IDs of the tracking tasks that you want to delete. You can call the [DescribeCdnDeliverList](~~270877~~) operation to query task IDs.
        self.deliver_id = deliver_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        return self


class DeleteCdnDeliverTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCdnDeliverTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCdnDeliverTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCdnDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
    ):
        # The ID of the request.
        self.domain_name = domain_name
        self.owner_account = owner_account
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 1.0.0
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCdnDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCdnSubTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCdnSubTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCdnSubTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFCTriggerRequest(TeaModel):
    def __init__(
        self,
        trigger_arn: str = None,
    ):
        # The trigger that corresponds to the Function Compute service.
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class DeleteFCTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFCTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRealTimeLogLogstoreRequest(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region: str = None,
    ):
        # The ID of the region where the Log Service project is deployed. For more information, see [Regions that support real-time log delivery](~~144883~~).
        self.logstore = logstore
        # Deletes the Logstore that is used by a specified configuration record of real-time
        #                   log delivery.
        self.project = project
        # The name of the Log Service project that is used for real-time log delivery.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteRealTimeLogLogstoreResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRealTimeLogLogstoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRealTimeLogLogstoreResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRealTimeLogLogstoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        logstore: str = None,
        project: str = None,
        region: str = None,
    ):
        # The acceleration domain name for which you want to disable real-time log delivery. You can specify multiple domain names and separate them with commas (,).
        self.domain = domain
        # The name of the Logstore where log entries are stored.
        self.logstore = logstore
        # The name of the Log Service project that is used for real-time log delivery.
        self.project = project
        # The ID of the region where the Log Service project is deployed. For more information, see [Regions that support real-time log delivery](~~144883~~).
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRealtimeLogDeliveryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpecificConfigRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The configuration IDs. Separate configuration IDs with commas (,). For more information about ConfigId, see [Usage notes on ConfigId](~~388994~~).
        self.config_id = config_id
        # The operation that you want to perform. Set the value to **DeleteSpecificConfig**.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteSpecificConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSpecificConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSpecificConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpecificStagingConfigRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The configuration IDs. Separate configuration IDs with commas (,). For more information about ConfigId, see [Usage notes on ConfigId](~~388994~~).
        self.config_id = config_id
        # The operation that you want to perform. Set the value to **DeleteSpecificStagingConfig**.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteSpecificStagingConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSpecificStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSpecificStagingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSpecificStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUsageDetailDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The ID of the task. You can call the [DescribeUserUsageDataExportTask](~~91062~~) operation to query the most recent task list.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteUsageDetailDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUsageDetailDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUsageDetailDataExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUsageDetailDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserUsageDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The ID of the export task that you want to delete.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteUserUsageDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserUsageDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserUsageDataExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserUsageDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlockedRegionsRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
    ):
        # The language. Valid values:
        # 
        # *   **zh**: simplified Chinese
        # *   **en**: English
        # *   **jp**: Japanese
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class DescribeBlockedRegionsResponseBodyInfoListInfoItem(TeaModel):
    def __init__(
        self,
        continent: str = None,
        countries_and_regions: str = None,
        countries_and_regions_name: str = None,
    ):
        # The district to which the country or region belongs.
        self.continent = continent
        # The abbreviation of the name of the country or region.
        self.countries_and_regions = countries_and_regions
        # The name of the country or region.
        self.countries_and_regions_name = countries_and_regions_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.continent is not None:
            result['Continent'] = self.continent
        if self.countries_and_regions is not None:
            result['CountriesAndRegions'] = self.countries_and_regions
        if self.countries_and_regions_name is not None:
            result['CountriesAndRegionsName'] = self.countries_and_regions_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Continent') is not None:
            self.continent = m.get('Continent')
        if m.get('CountriesAndRegions') is not None:
            self.countries_and_regions = m.get('CountriesAndRegions')
        if m.get('CountriesAndRegionsName') is not None:
            self.countries_and_regions_name = m.get('CountriesAndRegionsName')
        return self


class DescribeBlockedRegionsResponseBodyInfoList(TeaModel):
    def __init__(
        self,
        info_item: List[DescribeBlockedRegionsResponseBodyInfoListInfoItem] = None,
    ):
        self.info_item = info_item

    def validate(self):
        if self.info_item:
            for k in self.info_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InfoItem'] = []
        if self.info_item is not None:
            for k in self.info_item:
                result['InfoItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info_item = []
        if m.get('InfoItem') is not None:
            for k in m.get('InfoItem'):
                temp_model = DescribeBlockedRegionsResponseBodyInfoListInfoItem()
                self.info_item.append(temp_model.from_map(k))
        return self


class DescribeBlockedRegionsResponseBody(TeaModel):
    def __init__(
        self,
        info_list: DescribeBlockedRegionsResponseBodyInfoList = None,
        request_id: str = None,
    ):
        # The information returned.
        self.info_list = info_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.info_list:
            self.info_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info_list is not None:
            result['InfoList'] = self.info_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoList') is not None:
            temp_model = DescribeBlockedRegionsResponseBodyInfoList()
            self.info_list = temp_model.from_map(m['InfoList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBlockedRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBlockedRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBlockedRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnCertificateDetailRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the SSL certificate. You can query only one certificate at a time.
        self.cert_name = cert_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnCertificateDetailResponseBody(TeaModel):
    def __init__(
        self,
        cert: str = None,
        cert_id: int = None,
        cert_name: str = None,
        key: str = None,
        request_id: str = None,
    ):
        # The certificate.
        self.cert = cert
        # The ID of the certificate.
        self.cert_id = cert_id
        # The name of the certificate.
        self.cert_name = cert_name
        # The key of the SSL certificate.
        self.key = key
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.key is not None:
            result['Key'] = self.key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnCertificateDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnCertificateListRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The accelerated domain name. Separate multiple accelerated domain names with commas (,).
        # 
        # If you do not specify an accelerated domain name, SSL certificates of all your accelerated domain names are queried.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
    def __init__(
        self,
        cert_id: int = None,
        cert_name: str = None,
        common: str = None,
        fingerprint: str = None,
        issuer: str = None,
        last_time: int = None,
    ):
        # The ID of the certificate.
        self.cert_id = cert_id
        # The name of the certificate.
        self.cert_name = cert_name
        # The Common Name (CN) attribute of the certificate. In most cases, the CN is a domain name.
        self.common = common
        # The fingerprint of the certificate.
        self.fingerprint = fingerprint
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer
        # The timestamp.
        self.last_time = last_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common is not None:
            result['Common'] = self.common
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        return self


class DescribeCdnCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(
        self,
        cert: List[DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert] = None,
    ):
        self.cert = cert

    def validate(self):
        if self.cert:
            for k in self.cert:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cert'] = []
        if self.cert is not None:
            for k in self.cert:
                result['Cert'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert = []
        if m.get('Cert') is not None:
            for k in m.get('Cert'):
                temp_model = DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        return self


class DescribeCdnCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(
        self,
        cert_list: DescribeCdnCertificateListResponseBodyCertificateListModelCertList = None,
        count: int = None,
    ):
        # The list of certificates.
        self.cert_list = cert_list
        # The number of certificates that are returned.
        self.count = count

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_list is not None:
            result['CertList'] = self.cert_list.to_map()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertList') is not None:
            temp_model = DescribeCdnCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeCdnCertificateListResponseBody(TeaModel):
    def __init__(
        self,
        certificate_list_model: DescribeCdnCertificateListResponseBodyCertificateListModel = None,
        request_id: str = None,
    ):
        # Details about certificates.
        self.certificate_list_model = certificate_list_model
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeCdnCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnCertificateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnCertificateListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDeletedDomainsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The number of the page to return. Valid values: **1** to **100000**. Default value: **1**.
        self.page_number = page_number
        # The number of domain names to return per page. Valid values: an integer between **1** and **500**. Default value: **20**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCdnDeletedDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        gmt_modified: str = None,
    ):
        # The accelerated domain name.
        self.domain_name = domain_name
        # The time when the accelerated domain name was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DescribeCdnDeletedDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        page_data: List[DescribeCdnDeletedDomainsResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = DescribeCdnDeletedDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeCdnDeletedDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domains: DescribeCdnDeletedDomainsResponseBodyDomains = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of accelerated domain names and the time each domain name was last modified.
        self.domains = domains
        # The page number of the returned page, which is the same as the **PageNumber** parameter in request parameters.
        self.page_number = page_number
        # The number of domain names returned per page, which is the same as the **PageSize** parameter in request parameters.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of domain names returned.
        self.total_count = total_count

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = DescribeCdnDeletedDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCdnDeletedDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnDeletedDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnDeletedDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDeliverListRequest(TeaModel):
    def __init__(
        self,
        deliver_id: int = None,
    ):
        # The ID of the tracking task that you want to query. If you do not specify an ID, all tracking tasks are queried.
        self.deliver_id = deliver_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        return self


class DescribeCdnDeliverListResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        # The information about the tracking task.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDeliverListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnDeliverListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnDeliverListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainByCertificateRequest(TeaModel):
    def __init__(
        self,
        sslpub: str = None,
        sslstatus: bool = None,
    ):
        # The public key of the SSL certificate. You must encode the public key in Base64 before you invoke the encodeURIComponent function to encode a URI component.
        # 
        # A public key in the Privacy Enhanced Mail (PEM) format is supported.
        self.sslpub = sslpub
        # Specifies whether to return only domain names with HTTPS enabled or disabled.
        # 
        # *   true: returns only domain names with HTTPS enabled.
        # *   false: returns only domain names with HTTPS disabled.
        self.sslstatus = sslstatus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sslstatus is not None:
            result['SSLStatus'] = self.sslstatus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SSLStatus') is not None:
            self.sslstatus = m.get('SSLStatus')
        return self


class DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        cert_ca_is_legacy: str = None,
        cert_expire_time: str = None,
        cert_expired: str = None,
        cert_start_time: str = None,
        cert_subject_common_name: str = None,
        cert_type: str = None,
        domain_list: str = None,
        domain_names: str = None,
        issuer: str = None,
    ):
        # Indicates whether the SSL certificate is obsolete. Valid values:
        # 
        # *   **yes**\
        # *   **no**\
        self.cert_ca_is_legacy = cert_ca_is_legacy
        # The expiration time of the certificate.
        self.cert_expire_time = cert_expire_time
        # Indicates whether the SSL certificate is expired. Valid values:
        # 
        # *   **yes**\
        # *   **no**\
        self.cert_expired = cert_expired
        # The effective time of the certificate.
        self.cert_start_time = cert_start_time
        # The name of the SSL certificate owner.
        self.cert_subject_common_name = cert_subject_common_name
        # The type of the certificate. Valid values: **RSA**, **DSA**, and **ECDSA**.
        self.cert_type = cert_type
        # The list of domain names. If a value is returned, the value matches the SSL certificate. Multiple domain names are separated by commas (,).
        self.domain_list = domain_list
        # The domain names (DNS fields) that match the SSL certificate. Multiple domain names are separated by commas (,).
        self.domain_names = domain_names
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_ca_is_legacy is not None:
            result['CertCaIsLegacy'] = self.cert_ca_is_legacy
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_expired is not None:
            result['CertExpired'] = self.cert_expired
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_subject_common_name is not None:
            result['CertSubjectCommonName'] = self.cert_subject_common_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCaIsLegacy') is not None:
            self.cert_ca_is_legacy = m.get('CertCaIsLegacy')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertExpired') is not None:
            self.cert_expired = m.get('CertExpired')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertSubjectCommonName') is not None:
            self.cert_subject_common_name = m.get('CertSubjectCommonName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        return self


class DescribeCdnDomainByCertificateResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainByCertificateResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeCdnDomainByCertificateResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        # The certificate information.
        self.cert_infos = cert_infos
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeCdnDomainByCertificateResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainByCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnDomainByCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainByCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainConfigsRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        domain_name: str = None,
        function_names: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the configuration. For more information about ConfigId, see [Usage notes on ConfigId](~~388994~~).
        self.config_id = config_id
        # The accelerated domain name. You can specify only one domain name in each request.
        self.domain_name = domain_name
        # The names of the features. Separate multiple feature names with commas (,). For more information, see [Parameters for configuring features for domain names](~~388460~~).
        self.function_names = function_names
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        # The parameter name, which is the configuration item of **functionName**. You can configure multiple configuration items.
        self.arg_name = arg_name
        # The parameter value, which is the value of the configuration item of **functionName**.
        self.arg_value = arg_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(
        self,
        function_arg: List[DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg] = None,
    ):
        self.function_arg = function_arg

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k in self.function_arg:
                result['FunctionArg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function_arg = []
        if m.get('FunctionArg') is not None:
            for k in m.get('FunctionArg'):
                temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        function_args: DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs = None,
        function_name: str = None,
        parent_id: str = None,
        status: str = None,
    ):
        # The ID of the configuration.
        self.config_id = config_id
        # The configuration of each feature.
        self.function_args = function_args
        # The name of the feature.
        self.function_name = function_name
        # The ID of the rule condition. This parameter is optional.
        # 
        # To create a rule condition, you can configure the **condition** feature that is described in the [Parameters for configuring features for domain names](~~388460~~) topic. A rule condition can identify parameters that are included in requests and filter requests based on the identified parameters. Each rule condition has a [ConfigId](~~388994~~). You can use ConfigId as ParentId that is referenced by other features. This way, you can combine rule conditions and features for flexible configurations.
        # 
        # For more information, see [BatchSetCdnDomainConfig](~~90915~~) or ParentId configuration example in this topic.
        self.parent_id = parent_id
        # The status of the configuration. Valid values:
        # 
        # *   **success**\
        # *   **testing**\
        # *   **failed**\
        # *   **configuring**\
        self.status = status

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCdnDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        domain_config: List[DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig] = None,
    ):
        self.domain_config = domain_config

    def validate(self):
        if self.domain_config:
            for k in self.domain_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfig'] = []
        if self.domain_config is not None:
            for k in self.domain_config:
                result['DomainConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_config = []
        if m.get('DomainConfig') is not None:
            for k in m.get('DomainConfig'):
                temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainConfigsResponseBody(TeaModel):
    def __init__(
        self,
        domain_configs: DescribeCdnDomainConfigsResponseBodyDomainConfigs = None,
        request_id: str = None,
    ):
        # The configurations of the domain name.
        self.domain_configs = domain_configs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainConfigs') is not None:
            temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnDomainConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainDetailRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel(TeaModel):
    def __init__(
        self,
        content: str = None,
        enabled: str = None,
        port: int = None,
        priority: str = None,
        type: str = None,
        weight: str = None,
    ):
        # The address of the origin server.
        self.content = content
        # The status.
        self.enabled = enabled
        # The port over which requests are redirected to the origin server. Ports 443 and 80 are supported.
        self.port = port
        # The priority.
        self.priority = priority
        # The type of the origin server. Valid values:
        # 
        # *   **ipaddr**: an origin IP address
        # *   **domain**: an origin domain name
        # *   **oss**: the domain name of an Object Storage Service (OSS) bucket
        # *   **fc_domain:** a Function Compute domain name
        self.type = type
        # The weight of the origin server if multiple origin servers have been specified.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels(TeaModel):
    def __init__(
        self,
        source_model: List[DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel] = None,
    ):
        self.source_model = source_model

    def validate(self):
        if self.source_model:
            for k in self.source_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceModel'] = []
        if self.source_model is not None:
            for k in self.source_model:
                result['SourceModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_model = []
        if m.get('SourceModel') is not None:
            for k in m.get('SourceModel'):
                temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel()
                self.source_model.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModel(TeaModel):
    def __init__(
        self,
        cdn_type: str = None,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        https_cname: str = None,
        resource_group_id: str = None,
        scope: str = None,
        server_certificate_status: str = None,
        source_models: DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels = None,
    ):
        # The workload type of the accelerated domain name. Valid values:
        # 
        # *   **web**: images and small files
        # *   **download**: large files
        # *   **video**: on-demand video and audio streaming
        self.cdn_type = cdn_type
        # The CNAME that is assigned to the accelerated domain name. You must add the CNAME record in the system of your DNS service provider to map the accelerated domain name to the CNAME.
        self.cname = cname
        # The description of the domain name.
        self.description = description
        # The accelerated domain name.
        self.domain_name = domain_name
        # The status of the accelerated domain name. Valid values:
        # 
        # *   **online**\
        # *   **offline**\
        # *   **configuring**\
        # *   **configure_failed**\
        # *   **checking**\
        # *   **check_failed**\
        # *   **stopping**\
        # *   **deleting**\
        self.domain_status = domain_status
        # The time when the domain name was created.
        self.gmt_created = gmt_created
        # The time when the domain name was last modified.
        self.gmt_modified = gmt_modified
        # The CNAME for which HTTPS is enabled.
        self.https_cname = https_cname
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The acceleration region.
        self.scope = scope
        # Indicates whether the SSL certificate is enabled. Valid values:
        # 
        # *   **on**\
        # *   **off**\
        self.server_certificate_status = server_certificate_status
        # The information about the origin server.
        self.source_models = source_models

    def validate(self):
        if self.source_models:
            self.source_models.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.https_cname is not None:
            result['HttpsCname'] = self.https_cname
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.source_models is not None:
            result['SourceModels'] = self.source_models.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HttpsCname') is not None:
            self.https_cname = m.get('HttpsCname')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('SourceModels') is not None:
            temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels()
            self.source_models = temp_model.from_map(m['SourceModels'])
        return self


class DescribeCdnDomainDetailResponseBody(TeaModel):
    def __init__(
        self,
        get_domain_detail_model: DescribeCdnDomainDetailResponseBodyGetDomainDetailModel = None,
        request_id: str = None,
    ):
        # The details about the accelerated domain name.
        self.get_domain_detail_model = get_domain_detail_model
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.get_domain_detail_model:
            self.get_domain_detail_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_domain_detail_model is not None:
            result['GetDomainDetailModel'] = self.get_domain_detail_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetDomainDetailModel') is not None:
            temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModel()
            self.get_domain_detail_model = temp_model.from_map(m['GetDomainDetailModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnDomainDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainLogsRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        log_name: str = None,
        log_path: str = None,
        log_size: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.log_name = log_name
        self.log_path = log_path
        self.log_size = log_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos(TeaModel):
    def __init__(
        self,
        log_info_detail: List[DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail] = None,
    ):
        self.log_info_detail = log_info_detail

    def validate(self):
        if self.log_info_detail:
            for k in self.log_info_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogInfoDetail'] = []
        if self.log_info_detail is not None:
            for k in self.log_info_detail:
                result['LogInfoDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_info_detail = []
        if m.get('LogInfoDetail') is not None:
            for k in m.get('LogInfoDetail'):
                temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail()
                self.log_info_detail.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        log_count: int = None,
        log_infos: DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos = None,
        page_infos: DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos = None,
    ):
        self.domain_name = domain_name
        self.log_count = log_count
        self.log_infos = log_infos
        self.page_infos = page_infos

    def validate(self):
        if self.log_infos:
            self.log_infos.validate()
        if self.page_infos:
            self.page_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.log_count is not None:
            result['LogCount'] = self.log_count
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('LogInfos') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        if m.get('PageInfos') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m['PageInfos'])
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetails(TeaModel):
    def __init__(
        self,
        domain_log_detail: List[DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail] = None,
    ):
        self.domain_log_detail = domain_log_detail

    def validate(self):
        if self.domain_log_detail:
            for k in self.domain_log_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainLogDetail'] = []
        if self.domain_log_detail is not None:
            for k in self.domain_log_detail:
                result['DomainLogDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_log_detail = []
        if m.get('DomainLogDetail') is not None:
            for k in m.get('DomainLogDetail'):
                temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainLogsResponseBody(TeaModel):
    def __init__(
        self,
        domain_log_details: DescribeCdnDomainLogsResponseBodyDomainLogDetails = None,
        request_id: str = None,
    ):
        self.domain_log_details = domain_log_details
        self.request_id = request_id

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnDomainLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainStagingConfigRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        function_names: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name in each request.
        self.domain_name = domain_name
        # The list of feature names. Separate multiple values with commas (,). For more information, see [A list of features](~~388460~~).
        self.function_names = function_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        return self


class DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs(TeaModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        # The configuration name.
        self.arg_name = arg_name
        # The configuration value.
        self.arg_value = arg_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeCdnDomainStagingConfigResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        function_args: List[DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs] = None,
        function_name: str = None,
        parent_id: str = None,
        status: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The description of each feature.
        self.function_args = function_args
        # The feature name.
        self.function_name = function_name
        # The rule condition ID. This parameter is optional. To create a rule condition, you can configure the **condition** feature that is described in the [Parameters for configuring features for domain names](~~388460~~) topic. A rule condition can identify parameters that are included in requests and filter requests based on the identified parameters. Each rule condition has a [ConfigId](~~388994~~). You can reference ConfigId instead of ParentId in other features. This way, you can combine rule conditions and features for flexible configurations. For more information, see [BatchSetCdnDomainConfig](~~90915~~) or ParentId configuration example in this topic.
        self.parent_id = parent_id
        # The configuration status. Valid values:
        # 
        # *   **testing**\
        # *   **configuring**\
        # *   **success**\
        # *   **failed**\
        self.status = status

    def validate(self):
        if self.function_args:
            for k in self.function_args:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['FunctionArgs'] = []
        if self.function_args is not None:
            for k in self.function_args:
                result['FunctionArgs'].append(k.to_map() if k else None)
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.function_args = []
        if m.get('FunctionArgs') is not None:
            for k in m.get('FunctionArgs'):
                temp_model = DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k))
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCdnDomainStagingConfigResponseBody(TeaModel):
    def __init__(
        self,
        domain_configs: List[DescribeCdnDomainStagingConfigResponseBodyDomainConfigs] = None,
        domain_name: str = None,
        request_id: str = None,
    ):
        # The domain name configurations.
        self.domain_configs = domain_configs
        # The accelerated domain name.
        self.domain_name = domain_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeCdnDomainStagingConfigResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnDomainStagingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnHttpsDomainListRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The keyword that is used to search for certificates.
        self.keyword = keyword
        # The number of the page to return. Valid values: **1** to **100000**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        cert_common_name: str = None,
        cert_expire_time: str = None,
        cert_name: str = None,
        cert_start_time: str = None,
        cert_status: str = None,
        cert_type: str = None,
        cert_update_time: str = None,
        domain_name: str = None,
    ):
        # The returned primary domain name of the certificate.
        self.cert_common_name = cert_common_name
        # The time at which the certificate expires.
        self.cert_expire_time = cert_expire_time
        # The name of the certificate.
        self.cert_name = cert_name
        # The time at which the certificate became effective.
        self.cert_start_time = cert_start_time
        # The status of the certificate.
        # 
        # *   **ok**: The certificate is working as expected.
        # *   **mismatch**: The certificate does not match the specified domain name.
        # *   **expired**: The certificate has expired.
        # *   **expire_soon**: The certificate will expire soon.
        self.cert_status = cert_status
        # The type of the certificate.
        # 
        # *   **free**: a free certificate.
        # *   **cas**: a certificate that is purchased from Alibaba Cloud SSL Certificates Service.
        # *   **upload**: a certificate that is uploaded by the user.
        self.cert_type = cert_type
        # The time at which the certificate was updated.
        self.cert_update_time = cert_update_time
        # The accelerated domain name.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_status is not None:
            result['CertStatus'] = self.cert_status
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_update_time is not None:
            result['CertUpdateTime'] = self.cert_update_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertStatus') is not None:
            self.cert_status = m.get('CertStatus')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertUpdateTime') is not None:
            self.cert_update_time = m.get('CertUpdateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeCdnHttpsDomainListResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeCdnHttpsDomainListResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeCdnHttpsDomainListResponseBodyCertInfos = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the certificate.
        self.cert_infos = cert_infos
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeCdnHttpsDomainListResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCdnHttpsDomainListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnHttpsDomainListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnHttpsDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnOrderCommodityCodeRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The original commodity code.
        self.commodity_code = commodity_code
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnOrderCommodityCodeResponseBody(TeaModel):
    def __init__(
        self,
        order_commodity_code: str = None,
        request_id: str = None,
    ):
        # The commodity code that includes the organization unit.
        self.order_commodity_code = order_commodity_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_commodity_code is not None:
            result['OrderCommodityCode'] = self.order_commodity_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderCommodityCode') is not None:
            self.order_commodity_code = m.get('OrderCommodityCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnOrderCommodityCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnOrderCommodityCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnOrderCommodityCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnRegionAndIspRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnRegionAndIspResponseBodyIspsIsp(TeaModel):
    def __init__(
        self,
        name_en: str = None,
        name_zh: str = None,
    ):
        # The English name of the ISP.
        self.name_en = name_en
        # The Chinese name of the ISP.
        self.name_zh = name_zh

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.name_zh is not None:
            result['NameZh'] = self.name_zh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('NameZh') is not None:
            self.name_zh = m.get('NameZh')
        return self


class DescribeCdnRegionAndIspResponseBodyIsps(TeaModel):
    def __init__(
        self,
        isp: List[DescribeCdnRegionAndIspResponseBodyIspsIsp] = None,
    ):
        self.isp = isp

    def validate(self):
        if self.isp:
            for k in self.isp:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Isp'] = []
        if self.isp is not None:
            for k in self.isp:
                result['Isp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp = []
        if m.get('Isp') is not None:
            for k in m.get('Isp'):
                temp_model = DescribeCdnRegionAndIspResponseBodyIspsIsp()
                self.isp.append(temp_model.from_map(k))
        return self


class DescribeCdnRegionAndIspResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        name_en: str = None,
        name_zh: str = None,
    ):
        # The English name of the region.
        self.name_en = name_en
        # The Chinese name of the region.
        self.name_zh = name_zh

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.name_zh is not None:
            result['NameZh'] = self.name_zh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('NameZh') is not None:
            self.name_zh = m.get('NameZh')
        return self


class DescribeCdnRegionAndIspResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeCdnRegionAndIspResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeCdnRegionAndIspResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeCdnRegionAndIspResponseBody(TeaModel):
    def __init__(
        self,
        isps: DescribeCdnRegionAndIspResponseBodyIsps = None,
        regions: DescribeCdnRegionAndIspResponseBodyRegions = None,
        request_id: str = None,
    ):
        # The list of ISPs.
        self.isps = isps
        # The list of regions.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.isps:
            self.isps.validate()
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isps is not None:
            result['Isps'] = self.isps.to_map()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Isps') is not None:
            temp_model = DescribeCdnRegionAndIspResponseBodyIsps()
            self.isps = temp_model.from_map(m['Isps'])
        if m.get('Regions') is not None:
            temp_model = DescribeCdnRegionAndIspResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnRegionAndIspResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnRegionAndIspResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnRegionAndIspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnReportRequest(TeaModel):
    def __init__(
        self,
        area: str = None,
        domain_name: str = None,
        end_time: str = None,
        http_code: str = None,
        is_overseas: str = None,
        report_id: int = None,
        start_time: str = None,
    ):
        self.area = area
        self.domain_name = domain_name
        self.end_time = end_time
        self.http_code = http_code
        self.is_overseas = is_overseas
        self.report_id = report_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.is_overseas is not None:
            result['IsOverseas'] = self.is_overseas
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('IsOverseas') is not None:
            self.is_overseas = m.get('IsOverseas')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnReportResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnReportListRequest(TeaModel):
    def __init__(
        self,
        report_id: int = None,
    ):
        # The ID of the operations report that you want to query. If you do not specify an ID, all operations reports are queried.
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class DescribeCdnReportListResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        # The information about the report that is queried.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnReportListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnReportListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnReportListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnSMCertificateDetailRequest(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the certificate.
        self.cert_identifier = cert_identifier
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnSMCertificateDetailResponseBody(TeaModel):
    def __init__(
        self,
        cert_expire_time: str = None,
        cert_identifier: str = None,
        cert_name: str = None,
        cert_org: str = None,
        common_name: str = None,
        encrypt_certificate: str = None,
        request_id: str = None,
        sans: str = None,
        sign_certificate: str = None,
    ):
        # The name of the certificate.
        self.cert_expire_time = cert_expire_time
        # The ID of the certificate.
        self.cert_identifier = cert_identifier
        # The time when the certificate expires. The time is displayed in UTC.
        self.cert_name = cert_name
        # The certificate authority (CA) that issued the certificate.
        self.cert_org = cert_org
        # The top-level domain name.
        self.common_name = common_name
        # The ID of the request.
        self.encrypt_certificate = encrypt_certificate
        # The content of the encryption certificate.
        self.request_id = request_id
        # The subdomain name.
        self.sans = sans
        # The content of the signature certificate.
        self.sign_certificate = sign_certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.encrypt_certificate is not None:
            result['EncryptCertificate'] = self.encrypt_certificate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.sign_certificate is not None:
            result['SignCertificate'] = self.sign_certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('EncryptCertificate') is not None:
            self.encrypt_certificate = m.get('EncryptCertificate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SignCertificate') is not None:
            self.sign_certificate = m.get('SignCertificate')
        return self


class DescribeCdnSMCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnSMCertificateDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnSMCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnSMCertificateListRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name in each request.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnSMCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        cert_name: str = None,
        common: str = None,
        issuer: str = None,
    ):
        # The ID of the certificate.
        self.cert_identifier = cert_identifier
        # The name of the certificate.
        self.cert_name = cert_name
        # The common name of the certificate.
        self.common = common
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common is not None:
            result['Common'] = self.common
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        return self


class DescribeCdnSMCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(
        self,
        cert: List[DescribeCdnSMCertificateListResponseBodyCertificateListModelCertListCert] = None,
    ):
        self.cert = cert

    def validate(self):
        if self.cert:
            for k in self.cert:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cert'] = []
        if self.cert is not None:
            for k in self.cert:
                result['Cert'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert = []
        if m.get('Cert') is not None:
            for k in m.get('Cert'):
                temp_model = DescribeCdnSMCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        return self


class DescribeCdnSMCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(
        self,
        cert_list: DescribeCdnSMCertificateListResponseBodyCertificateListModelCertList = None,
        count: int = None,
    ):
        # The list of certificates.
        self.cert_list = cert_list
        # The number of certificates that are returned.
        self.count = count

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_list is not None:
            result['CertList'] = self.cert_list.to_map()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertList') is not None:
            temp_model = DescribeCdnSMCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeCdnSMCertificateListResponseBody(TeaModel):
    def __init__(
        self,
        certificate_list_model: DescribeCdnSMCertificateListResponseBodyCertificateListModel = None,
        request_id: str = None,
    ):
        # The type of the certificate information.
        self.certificate_list_model = certificate_list_model
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeCdnSMCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnSMCertificateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnSMCertificateListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnSMCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnServiceResponseBodyOperationLocksLockReason(TeaModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why the service is locked. A value of financial indicates that the service is locked due to overdue payments.
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        return self


class DescribeCdnServiceResponseBodyOperationLocks(TeaModel):
    def __init__(
        self,
        lock_reason: List[DescribeCdnServiceResponseBodyOperationLocksLockReason] = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        if self.lock_reason:
            for k in self.lock_reason:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k in self.lock_reason:
                result['LockReason'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock_reason = []
        if m.get('LockReason') is not None:
            for k in m.get('LockReason'):
                temp_model = DescribeCdnServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        return self


class DescribeCdnServiceResponseBody(TeaModel):
    def __init__(
        self,
        changing_affect_time: str = None,
        changing_charge_type: str = None,
        instance_id: str = None,
        internet_charge_type: str = None,
        opening_time: str = None,
        operation_locks: DescribeCdnServiceResponseBodyOperationLocks = None,
        request_id: str = None,
    ):
        # The time when the metering method for the next cycle takes effect. The time is displayed in GMT.
        self.changing_affect_time = changing_affect_time
        # The metering method for the next cycle. Valid values:
        # 
        # *   **PayByTraffic**: pay-by-data-transfer
        # *   **PayByBandwidth**: pay-by-bandwidth
        self.changing_charge_type = changing_charge_type
        # The ID of the instance.
        self.instance_id = instance_id
        # The current metering method. Valid values:
        # 
        # *   **PayByTraffic**: pay-by-data-transfer
        # *   **PayByBandwidth**: pay-by-bandwidth
        self.internet_charge_type = internet_charge_type
        # The time when the service was activated. The time follows the ISO 8601 standard.
        self.opening_time = opening_time
        # The lock status.
        self.operation_locks = operation_locks
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time
        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')
        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')
        if m.get('OperationLocks') is not None:
            temp_model = DescribeCdnServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnSubListResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnSubListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnSubListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnSubListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserBillHistoryRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # InvalidParameterAliUid
        self.end_time = end_time
        # InvalidParameter.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem(TeaModel):
    def __init__(
        self,
        bandwidth: float = None,
        cdn_region: str = None,
        charge_type: str = None,
        count: float = None,
        flow: float = None,
    ):
        self.bandwidth = bandwidth
        self.cdn_region = cdn_region
        self.charge_type = charge_type
        self.count = count
        self.flow = flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cdn_region is not None:
            result['CdnRegion'] = self.cdn_region
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.count is not None:
            result['Count'] = self.count
        if self.flow is not None:
            result['Flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CdnRegion') is not None:
            self.cdn_region = m.get('CdnRegion')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        return self


class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData(TeaModel):
    def __init__(
        self,
        billing_data_item: List[DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem] = None,
    ):
        self.billing_data_item = billing_data_item

    def validate(self):
        if self.billing_data_item:
            for k in self.billing_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillingDataItem'] = []
        if self.billing_data_item is not None:
            for k in self.billing_data_item:
                result['BillingDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.billing_data_item = []
        if m.get('BillingDataItem') is not None:
            for k in m.get('BillingDataItem'):
                temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem()
                self.billing_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem(TeaModel):
    def __init__(
        self,
        bill_time: str = None,
        bill_type: str = None,
        billing_data: DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData = None,
        dimension: str = None,
    ):
        self.bill_time = bill_time
        self.bill_type = bill_type
        self.billing_data = billing_data
        # Invalid Parameter EndTime.
        self.dimension = dimension

    def validate(self):
        if self.billing_data:
            self.billing_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_time is not None:
            result['BillTime'] = self.bill_time
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.billing_data is not None:
            result['BillingData'] = self.billing_data.to_map()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillTime') is not None:
            self.bill_time = m.get('BillTime')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BillingData') is not None:
            temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData()
            self.billing_data = temp_model.from_map(m['BillingData'])
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        return self


class DescribeCdnUserBillHistoryResponseBodyBillHistoryData(TeaModel):
    def __init__(
        self,
        bill_history_data_item: List[DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem] = None,
    ):
        self.bill_history_data_item = bill_history_data_item

    def validate(self):
        if self.bill_history_data_item:
            for k in self.bill_history_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillHistoryDataItem'] = []
        if self.bill_history_data_item is not None:
            for k in self.bill_history_data_item:
                result['BillHistoryDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_history_data_item = []
        if m.get('BillHistoryDataItem') is not None:
            for k in m.get('BillHistoryDataItem'):
                temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem()
                self.bill_history_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillHistoryResponseBody(TeaModel):
    def __init__(
        self,
        bill_history_data: DescribeCdnUserBillHistoryResponseBodyBillHistoryData = None,
        request_id: str = None,
    ):
        # Invalid Parameter StartTime.
        self.bill_history_data = bill_history_data
        # Invalid Parameter AliUid.
        self.request_id = request_id

    def validate(self):
        if self.bill_history_data:
            self.bill_history_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_history_data is not None:
            result['BillHistoryData'] = self.bill_history_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillHistoryData') is not None:
            temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryData()
            self.bill_history_data = temp_model.from_map(m['BillHistoryData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnUserBillHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnUserBillHistoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserBillHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserBillPredictionRequest(TeaModel):
    def __init__(
        self,
        area: str = None,
        dimension: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.area = area
        self.dimension = dimension
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem(TeaModel):
    def __init__(
        self,
        area: str = None,
        time_stp: str = None,
        value: float = None,
    ):
        self.area = area
        self.time_stp = time_stp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.time_stp is not None:
            result['TimeStp'] = self.time_stp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('TimeStp') is not None:
            self.time_stp = m.get('TimeStp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeCdnUserBillPredictionResponseBodyBillPredictionData(TeaModel):
    def __init__(
        self,
        bill_prediction_data_item: List[DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem] = None,
    ):
        self.bill_prediction_data_item = bill_prediction_data_item

    def validate(self):
        if self.bill_prediction_data_item:
            for k in self.bill_prediction_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillPredictionDataItem'] = []
        if self.bill_prediction_data_item is not None:
            for k in self.bill_prediction_data_item:
                result['BillPredictionDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_prediction_data_item = []
        if m.get('BillPredictionDataItem') is not None:
            for k in m.get('BillPredictionDataItem'):
                temp_model = DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem()
                self.bill_prediction_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillPredictionResponseBody(TeaModel):
    def __init__(
        self,
        bill_prediction_data: DescribeCdnUserBillPredictionResponseBodyBillPredictionData = None,
        bill_type: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.bill_prediction_data = bill_prediction_data
        self.bill_type = bill_type
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.bill_prediction_data:
            self.bill_prediction_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_prediction_data is not None:
            result['BillPredictionData'] = self.bill_prediction_data.to_map()
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillPredictionData') is not None:
            temp_model = DescribeCdnUserBillPredictionResponseBodyBillPredictionData()
            self.bill_prediction_data = temp_model.from_map(m['BillPredictionData'])
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnUserBillPredictionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnUserBillPredictionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserBillPredictionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserBillTypeRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem(TeaModel):
    def __init__(
        self,
        bill_type: str = None,
        billing_cycle: str = None,
        dimension: str = None,
        end_time: str = None,
        product: str = None,
        start_time: str = None,
    ):
        self.bill_type = bill_type
        self.billing_cycle = billing_cycle
        self.dimension = dimension
        self.end_time = end_time
        self.product = product
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.product is not None:
            result['Product'] = self.product
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnUserBillTypeResponseBodyBillTypeData(TeaModel):
    def __init__(
        self,
        bill_type_data_item: List[DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem] = None,
    ):
        self.bill_type_data_item = bill_type_data_item

    def validate(self):
        if self.bill_type_data_item:
            for k in self.bill_type_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillTypeDataItem'] = []
        if self.bill_type_data_item is not None:
            for k in self.bill_type_data_item:
                result['BillTypeDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_type_data_item = []
        if m.get('BillTypeDataItem') is not None:
            for k in m.get('BillTypeDataItem'):
                temp_model = DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem()
                self.bill_type_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillTypeResponseBody(TeaModel):
    def __init__(
        self,
        bill_type_data: DescribeCdnUserBillTypeResponseBodyBillTypeData = None,
        request_id: str = None,
    ):
        self.bill_type_data = bill_type_data
        self.request_id = request_id

    def validate(self):
        if self.bill_type_data:
            self.bill_type_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_type_data is not None:
            result['BillTypeData'] = self.bill_type_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillTypeData') is not None:
            temp_model = DescribeCdnUserBillTypeResponseBodyBillTypeData()
            self.bill_type_data = temp_model.from_map(m['BillTypeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnUserBillTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnUserBillTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserBillTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserConfigsRequest(TeaModel):
    def __init__(
        self,
        function_name: str = None,
    ):
        # The name of the parameter.
        # 
        # The configurations set by enterprise or government users.
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class DescribeCdnUserConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
        function_name: str = None,
    ):
        # The name of the feature.
        self.arg_name = arg_name
        # The value of the configuration. Valid values:
        # 
        # *   **cc_rule**: HTTP flood protection rules
        # *   **ddos_dispatch**: integration with Anti-DDoS
        # *   **edge_safe**: application security settings on edge nodes
        # *   **blocked_regions**: blocked regions
        # *   **http_acl_policy**: access control list (ACL) rules
        # *   **bot_manager**: bot traffic management
        # *   **ip_reputation**: IP reputation library
        self.arg_value = arg_value
        # The configuration item that you want to query. Valid values:
        # 
        # *   **domain_business_control**: Alibaba Cloud CDN configurations
        # *   **waf**: Web Application Firewall (WAF) configurations
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class DescribeCdnUserConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[DescribeCdnUserConfigsResponseBodyConfigs] = None,
        request_id: str = None,
    ):
        # >  The maximum number of times that each user can call this operation per second is 30.
        self.configs = configs
        # The name of the feature.
        self.request_id = request_id

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = DescribeCdnUserConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnUserConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnUserConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserDomainsByFuncRequest(TeaModel):
    def __init__(
        self,
        func_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        self.func_id = func_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.func_id is not None:
            result['FuncId'] = self.func_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(
        self,
        content: str = None,
        port: int = None,
        priority: str = None,
        type: str = None,
        weight: str = None,
    ):
        self.content = content
        self.port = port
        self.priority = priority
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData(TeaModel):
    def __init__(
        self,
        cdn_type: str = None,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        resource_group_id: str = None,
        sources: DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources = None,
        ssl_protocol: str = None,
    ):
        self.cdn_type = cdn_type
        self.cname = cname
        self.description = description
        self.domain_name = domain_name
        self.domain_status = domain_status
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.resource_group_id = resource_group_id
        self.sources = sources
        self.ssl_protocol = ssl_protocol

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sources') is not None:
            temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        return self


class DescribeCdnUserDomainsByFuncResponseBodyDomains(TeaModel):
    def __init__(
        self,
        page_data: List[DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeCdnUserDomainsByFuncResponseBody(TeaModel):
    def __init__(
        self,
        domains: DescribeCdnUserDomainsByFuncResponseBodyDomains = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.domains = domains
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCdnUserDomainsByFuncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnUserDomainsByFuncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserDomainsByFuncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserQuotaRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCdnUserQuotaResponseBody(TeaModel):
    def __init__(
        self,
        block_quota: int = None,
        block_remain: int = None,
        domain_quota: int = None,
        ignore_params_quota: int = None,
        ignore_params_remain: int = None,
        preload_quota: int = None,
        preload_remain: int = None,
        refresh_dir_quota: int = None,
        refresh_dir_remain: int = None,
        refresh_url_quota: int = None,
        refresh_url_remain: int = None,
        request_id: str = None,
    ):
        # The maximum number of URLs and directories that can be blocked.
        self.block_quota = block_quota
        # The remaining number of URLs and directories that can be blocked.
        self.block_remain = block_remain
        # The maximum number of accelerated domain names.
        self.domain_quota = domain_quota
        self.ignore_params_quota = ignore_params_quota
        self.ignore_params_remain = ignore_params_remain
        # The maximum number of URLs that can be prefetched.
        self.preload_quota = preload_quota
        # The remaining number of URLs that can be prefetched.
        self.preload_remain = preload_remain
        # The maximum number of directories that can be refreshed.
        self.refresh_dir_quota = refresh_dir_quota
        # The remaining number of directories that can be refreshed.
        self.refresh_dir_remain = refresh_dir_remain
        # The maximum number of URLs that can be refreshed.
        self.refresh_url_quota = refresh_url_quota
        # The remaining number of URLs that can be refreshed.
        self.refresh_url_remain = refresh_url_remain
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.block_remain is not None:
            result['BlockRemain'] = self.block_remain
        if self.domain_quota is not None:
            result['DomainQuota'] = self.domain_quota
        if self.ignore_params_quota is not None:
            result['IgnoreParamsQuota'] = self.ignore_params_quota
        if self.ignore_params_remain is not None:
            result['IgnoreParamsRemain'] = self.ignore_params_remain
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.refresh_dir_quota is not None:
            result['RefreshDirQuota'] = self.refresh_dir_quota
        if self.refresh_dir_remain is not None:
            result['RefreshDirRemain'] = self.refresh_dir_remain
        if self.refresh_url_quota is not None:
            result['RefreshUrlQuota'] = self.refresh_url_quota
        if self.refresh_url_remain is not None:
            result['RefreshUrlRemain'] = self.refresh_url_remain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')
        if m.get('DomainQuota') is not None:
            self.domain_quota = m.get('DomainQuota')
        if m.get('IgnoreParamsQuota') is not None:
            self.ignore_params_quota = m.get('IgnoreParamsQuota')
        if m.get('IgnoreParamsRemain') is not None:
            self.ignore_params_remain = m.get('IgnoreParamsRemain')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RefreshDirQuota') is not None:
            self.refresh_dir_quota = m.get('RefreshDirQuota')
        if m.get('RefreshDirRemain') is not None:
            self.refresh_dir_remain = m.get('RefreshDirRemain')
        if m.get('RefreshUrlQuota') is not None:
            self.refresh_url_quota = m.get('RefreshUrlQuota')
        if m.get('RefreshUrlRemain') is not None:
            self.refresh_url_remain = m.get('RefreshUrlRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnUserQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnUserQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserResourcePackageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        status: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        # The remaining quota of the resource plan.
        # 
        # *   The total amount of data transfer provided by the resource plan. Unit: bytes.
        # *   The remaining number of requests provided by the resource plan.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        curr_capacity: str = None,
        display_name: str = None,
        end_time: str = None,
        init_capacity: str = None,
        instance_id: str = None,
        start_time: str = None,
        status: str = None,
        template_name: str = None,
    ):
        # The total quota of the resource plan.
        # 
        # *   The total amount of data transfer provided by the resource plan. Unit: bytes.
        # *   The total number of requests provided by the resource plan.
        self.commodity_code = commodity_code
        # The ID of the instance.
        self.curr_capacity = curr_capacity
        # The time when the resource plan took effect.
        self.display_name = display_name
        # The operation that you want to perform. Set the value to **DescribeCdnUserResourcePackage**.
        self.end_time = end_time
        # The ID of the resource plan.
        self.init_capacity = init_capacity
        # The ID of the request.
        self.instance_id = instance_id
        # The name of the template.
        self.start_time = start_time
        # The status of the data transfer plan. Valid values:
        # 
        # *   **valid**: valid
        # *   **closed**: invalid
        self.status = status
        # The details about each resource plan. The details are organized in an array. The array consists of the subparameter values of the ResourcePackageInfo parameter.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos(TeaModel):
    def __init__(
        self,
        resource_package_info: List[DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo] = None,
    ):
        self.resource_package_info = resource_package_info

    def validate(self):
        if self.resource_package_info:
            for k in self.resource_package_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourcePackageInfo'] = []
        if self.resource_package_info is not None:
            for k in self.resource_package_info:
                result['ResourcePackageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_package_info = []
        if m.get('ResourcePackageInfo') is not None:
            for k in m.get('ResourcePackageInfo'):
                temp_model = DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo()
                self.resource_package_info.append(temp_model.from_map(k))
        return self


class DescribeCdnUserResourcePackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_package_infos: DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos = None,
    ):
        # The name of the resource plan.
        self.request_id = request_id
        # The time when the resource plan expires.
        self.resource_package_infos = resource_package_infos

    def validate(self):
        if self.resource_package_infos:
            self.resource_package_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_package_infos is not None:
            result['ResourcePackageInfos'] = self.resource_package_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourcePackageInfos') is not None:
            temp_model = DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos()
            self.resource_package_infos = temp_model.from_map(m['ResourcePackageInfos'])
        return self


class DescribeCdnUserResourcePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnUserResourcePackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnWafDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The domain name that you want to query.
        # 
        # You can specify only one domain name in each request. You have three options to configure this parameter:
        # 
        # *   Specify an exact domain name. For example, if you set this parameter to example.com, configuration information of example.com is queried.
        # *   Specify a keyword. For example, if you set this parameter to example, configuration information about all domain names that contain example is queried.
        # *   Leave this parameter empty. If this parameter is left empty, all accelerated domain names for which WAF is configured are queried.
        self.domain_name = domain_name
        # The region where WAF is enabled. Valid values:
        # 
        # *   **cn-hangzhou**: inside the Chinese mainland
        # *   **ap-southeast-1**: outside the Chinese mainland
        # 
        # > ap-southeast-1 includes Hong Kong (China), Macao (China), Taiwan (China), and other countries and regions.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeCdnWafDomainResponseBodyOutPutDomains(TeaModel):
    def __init__(
        self,
        acl_status: str = None,
        cc_status: str = None,
        domain: str = None,
        status: str = None,
        waf_status: str = None,
    ):
        # The status of the access control list (ACL) feature. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.acl_status = acl_status
        # The status of protection against HTTP flood attacks. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.cc_status = cc_status
        # The accelerated domain name.
        self.domain = domain
        # The WAF status of the domain name. Valid values:
        # 
        # *   **1**: The domain name is added to WAF or valid.
        # *   **10**: The domain name is being added to WAF.
        # *   **11**: The domain name failed to be added to WAF.
        self.status = status
        # The status of WAF. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.waf_status = waf_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.cc_status is not None:
            result['CcStatus'] = self.cc_status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_status is not None:
            result['WafStatus'] = self.waf_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('CcStatus') is not None:
            self.cc_status = m.get('CcStatus')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafStatus') is not None:
            self.waf_status = m.get('WafStatus')
        return self


class DescribeCdnWafDomainResponseBody(TeaModel):
    def __init__(
        self,
        out_put_domains: List[DescribeCdnWafDomainResponseBodyOutPutDomains] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the accelerated domain name.
        self.out_put_domains = out_put_domains
        # The ID of the request.
        self.request_id = request_id
        # The number of accelerated domain names.
        self.total_count = total_count

    def validate(self):
        if self.out_put_domains:
            for k in self.out_put_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OutPutDomains'] = []
        if self.out_put_domains is not None:
            for k in self.out_put_domains:
                result['OutPutDomains'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.out_put_domains = []
        if m.get('OutPutDomains') is not None:
            for k in m.get('OutPutDomains'):
                temp_model = DescribeCdnWafDomainResponseBodyOutPutDomains()
                self.out_put_domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCdnWafDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnWafDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnWafDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateInfoByIDRequest(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
    ):
        # The ID of the certificate. You can query only one certificate in each call.
        self.cert_id = cert_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        return self


class DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        cert_expire_time: str = None,
        cert_id: str = None,
        cert_name: str = None,
        cert_type: str = None,
        create_time: str = None,
        domain_list: str = None,
        https_crt: str = None,
    ):
        # The time at which the certificate expires.
        self.cert_expire_time = cert_expire_time
        # The ID of the certificate.
        self.cert_id = cert_id
        # The name of the certificate.
        self.cert_name = cert_name
        # The type of the certificate.
        # 
        # *   free: a free certificate
        # *   cas: a certificate purchased by using Certificate Management Service
        # *   upload: a user-uploaded certificate
        self.cert_type = cert_type
        # The time when the certificate became effective.
        self.create_time = create_time
        # The domain names that use the certificate.
        self.domain_list = domain_list
        # The content of the certificate.
        self.https_crt = https_crt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.https_crt is not None:
            result['HttpsCrt'] = self.https_crt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('HttpsCrt') is not None:
            self.https_crt = m.get('HttpsCrt')
        return self


class DescribeCertificateInfoByIDResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeCertificateInfoByIDResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeCertificateInfoByIDResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        # The information about the certificate.
        self.cert_infos = cert_infos
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeCertificateInfoByIDResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCertificateInfoByIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCertificateInfoByIDResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCertificateInfoByIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomLogConfigRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
    ):
        # A sample log configuration.
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class DescribeCustomLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        remark: str = None,
        request_id: str = None,
        sample: str = None,
        tag: str = None,
    ):
        # The format of the log configuration.
        self.remark = remark
        # The ID of the custom configuration.
        self.request_id = request_id
        # The ID of the request.
        self.sample = sample
        # >  The maximum number of times that each user can call this operation per second is 100.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeCustomLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomLogConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAverageResponseTimeRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_type: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
        time_merge: str = None,
    ):
        # The operation that you want to perform. Set the value to **DescribeDomainAverageResponseTime**.
        self.domain_name = domain_name
        # The name of the Internet service provider (ISP) for your Alibaba Cloud CDN service. You can call the [DescribeCdnRegionAndIsp](~~91077~~) operation to query ISPs. If you do not set this parameter, all ISPs are queried.
        self.domain_type = domain_type
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The time interval between the data entries. Unit: seconds. The value varies based on the values of the **StartTime** and **EndTime** parameters. Valid values:
        # 
        # *   If the time span between StartTime and EndTime is less than 3 days (3 days excluded), valid values are **300**, **3600**, and **86400**. Default value: **300**.
        # *   If the time span between StartTime and EndTime is from 3 to 31 days (31 days excluded), valid values are **3600** and **86400**. Default value: **3600**.
        # *   If the time range between StartTime and EndTime is 31 days or longer, the valid value is **86400**. Default value: **86400**.
        self.interval = interval
        # Specifies whether to automatically set the interval. If you set the value to 1, the value of the Interval parameter is automatically assigned based on the StartTime and EndTime parameters. You can set this parameter or the Interval parameter.
        self.isp_name_en = isp_name_en
        # The average response time.
        self.location_name_en = location_name_en
        # The end of the time range queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The end time must be later than the start time.
        self.start_time = start_time
        # The accelerated domain name. Separate multiple accelerated domain names with commas (,).
        # 
        # By default, this operation queries the bandwidth values during back-to-origin routing for all accelerated domain names that belong to your Alibaba Cloud account.
        self.time_merge = time_merge

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        return self


class DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        # Queries the average response time of one or more accelerated domain names. You can query data collected within the last 90 days.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainAverageResponseTimeResponseBody(TeaModel):
    def __init__(
        self,
        avg_rtper_interval: DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval = None,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The timestamp of the returned data.
        self.avg_rtper_interval = avg_rtper_interval
        # The ID of the request.
        self.data_interval = data_interval
        # The average response time collected at each time interval.
        self.domain_name = domain_name
        # The beginning of the time range during which data was queried.
        self.end_time = end_time
        # The time interval between the data entries returned.
        self.request_id = request_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        if self.avg_rtper_interval:
            self.avg_rtper_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_rtper_interval is not None:
            result['AvgRTPerInterval'] = self.avg_rtper_interval.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgRTPerInterval') is not None:
            temp_model = DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval()
            self.avg_rtper_interval = temp_model.from_map(m['AvgRTPerInterval'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainAverageResponseTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainAverageResponseTimeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainAverageResponseTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        domestic_value: str = None,
        https_domestic_value: str = None,
        https_overseas_value: str = None,
        https_value: str = None,
        overseas_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.domestic_value = domestic_value
        self.https_domestic_value = https_domestic_value
        self.https_overseas_value = https_overseas_value
        self.https_value = https_value
        self.overseas_value = overseas_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        bps_data_per_interval: DescribeDomainBpsDataResponseBodyBpsDataPerInterval = None,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.bps_data_per_interval = bps_data_per_interval
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainBpsDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataByLayerRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        layer: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.layer = layer
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        traffic_value: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        self.traffic_value = traffic_value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainBpsDataByLayerResponseBody(TeaModel):
    def __init__(
        self,
        bps_data_interval: DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval = None,
        data_interval: str = None,
        request_id: str = None,
    ):
        self.bps_data_interval = bps_data_interval
        self.data_interval = data_interval
        self.request_id = request_id

    def validate(self):
        if self.bps_data_interval:
            self.bps_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_interval is not None:
            result['BpsDataInterval'] = self.bps_data_interval.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsDataInterval') is not None:
            temp_model = DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval()
            self.bps_data_interval = temp_model.from_map(m['BpsDataInterval'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainBpsDataByLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainBpsDataByLayerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainBpsDataByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataByTimeStampRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        isp_names: str = None,
        location_names: str = None,
        time_point: str = None,
    ):
        self.domain_name = domain_name
        self.isp_names = isp_names
        self.location_names = location_names
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.isp_names is not None:
            result['IspNames'] = self.isp_names
        if self.location_names is not None:
            result['LocationNames'] = self.location_names
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IspNames') is not None:
            self.isp_names = m.get('IspNames')
        if m.get('LocationNames') is not None:
            self.location_names = m.get('LocationNames')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        return self


class DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel(TeaModel):
    def __init__(
        self,
        bps: int = None,
        isp_name: str = None,
        location_name: str = None,
        time_stamp: str = None,
    ):
        self.bps = bps
        self.isp_name = isp_name
        self.location_name = location_name
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList(TeaModel):
    def __init__(
        self,
        bps_data_model: List[DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel] = None,
    ):
        self.bps_data_model = bps_data_model

    def validate(self):
        if self.bps_data_model:
            for k in self.bps_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BpsDataModel'] = []
        if self.bps_data_model is not None:
            for k in self.bps_data_model:
                result['BpsDataModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bps_data_model = []
        if m.get('BpsDataModel') is not None:
            for k in m.get('BpsDataModel'):
                temp_model = DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel()
                self.bps_data_model.append(temp_model.from_map(k))
        return self


class DescribeDomainBpsDataByTimeStampResponseBody(TeaModel):
    def __init__(
        self,
        bps_data_list: DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList = None,
        domain_name: str = None,
        request_id: str = None,
        time_stamp: str = None,
    ):
        self.bps_data_list = bps_data_list
        self.domain_name = domain_name
        self.request_id = request_id
        self.time_stamp = time_stamp

    def validate(self):
        if self.bps_data_list:
            self.bps_data_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_list is not None:
            result['BpsDataList'] = self.bps_data_list.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsDataList') is not None:
            temp_model = DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList()
            self.bps_data_list = temp_model.from_map(m['BpsDataList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainBpsDataByTimeStampResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainBpsDataByTimeStampResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainBpsDataByTimeStampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCcActivityLogRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_name: str = None,
        start_time: str = None,
        trigger_object: str = None,
        value: str = None,
    ):
        # The object that triggered rate limiting.
        self.domain_name = domain_name
        # The number of the page to return. Default value: **1**.
        self.end_time = end_time
        # The number of entries to return on each page. Default value: **30**.
        self.page_number = page_number
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        # 
        # The end time must be later than the start time.
        self.page_size = page_size
        # The accelerated domain name.
        self.rule_name = rule_name
        # The value of the object that triggered rate limiting.
        self.start_time = start_time
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        # 
        # Data is collected every 5 minutes.
        # 
        # If you do not set this parameter, data within the last 24 hours is queried.
        self.trigger_object = trigger_object
        # The page number of the returned page.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.trigger_object is not None:
            result['TriggerObject'] = self.trigger_object
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TriggerObject') is not None:
            self.trigger_object = m.get('TriggerObject')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainCcActivityLogResponseBodyActivityLog(TeaModel):
    def __init__(
        self,
        action: str = None,
        domain_name: str = None,
        rule_name: str = None,
        time_stamp: str = None,
        trigger_object: str = None,
        ttl: int = None,
        value: str = None,
    ):
        # The object that triggered rate limiting.
        # 
        # If you do not set this parameter, all events that triggered rate limiting are queried.
        self.action = action
        # The ID of the request.
        self.domain_name = domain_name
        self.rule_name = rule_name
        # The log entry of the event that triggered rate limiting.
        self.time_stamp = time_stamp
        # The number of entries returned per page.
        self.trigger_object = trigger_object
        # The action that was triggered.
        self.ttl = ttl
        # The accelerated domain name. You can specify multiple domain names and separate them with commas (,).
        # 
        # If you do not specify a domain name, data of all domain names is queried.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.trigger_object is not None:
            result['TriggerObject'] = self.trigger_object
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TriggerObject') is not None:
            self.trigger_object = m.get('TriggerObject')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainCcActivityLogResponseBody(TeaModel):
    def __init__(
        self,
        activity_log: List[DescribeDomainCcActivityLogResponseBodyActivityLog] = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # A custom rule name. Valid values:
        # 
        # *   Default mode: default_normal.
        # *   Emergency mode: default_attack.
        # 
        # If you do not set this parameter, all events that triggered rate limiting are queried.
        self.activity_log = activity_log
        # The period of time that rate limiting remains effective.
        self.page_index = page_index
        # Set the value to **DescribeDomainCcActivityLog**.
        self.page_size = page_size
        # The name of the rule that was triggered
        self.request_id = request_id
        # The value of the object that triggered rate limiting.
        # 
        # If you do not set this parameter, the values of all events that triggered rate limiting are queried.
        self.total = total

    def validate(self):
        if self.activity_log:
            for k in self.activity_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActivityLog'] = []
        if self.activity_log is not None:
            for k in self.activity_log:
                result['ActivityLog'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activity_log = []
        if m.get('ActivityLog') is not None:
            for k in m.get('ActivityLog'):
                temp_model = DescribeDomainCcActivityLogResponseBodyActivityLog()
                self.activity_log.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDomainCcActivityLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainCcActivityLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainCcActivityLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCertificateInfoRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # The information about the SSL certificate.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        cert_domain_name: str = None,
        cert_expire_time: str = None,
        cert_id: str = None,
        cert_life: str = None,
        cert_name: str = None,
        cert_org: str = None,
        cert_region: str = None,
        cert_start_time: str = None,
        cert_type: str = None,
        cert_update_time: str = None,
        domain_cname_status: str = None,
        domain_name: str = None,
        server_certificate: str = None,
        server_certificate_status: str = None,
        status: str = None,
    ):
        # The name of the certificate authority (CA) that issued the SSL certificate.
        self.cert_domain_name = cert_domain_name
        # The status of the SSL certificate.
        # 
        # *   **success**: The SSL certificate is effective.
        # *   **checking**: The system is checking whether the domain name is accelerated by Alibaba Cloud CDN.
        # *   **cname_error**: The domain name is not accelerated by Alibaba Cloud CDN.
        # *   **top_domain_cname_error**: The top-level domain name is not an accelerated domain name.
        # *   **domain_invalid**: The domain name contains invalid characters.
        # *   **unsupport_wildcard**: Wildcard domain names are not supported.
        # *   **applying**: The application for a certificate is in progress.
        # *   **fget_token_timeout**: The application for a certificate timed out.
        # *   **check_token_timeout**: The verification timed out.
        # *   **get_cert_timeout**: The request to obtain the certificate timed out.
        # *   **failed**: The application for a certificate failed.
        self.cert_expire_time = cert_expire_time
        # The domain name that matches the SSL certificate.
        self.cert_id = cert_id
        # The time when the certificate was renewed.
        self.cert_life = cert_life
        # The public key of the SSL certificate.
        self.cert_name = cert_name
        # The time when the SSL certificate became effective.
        self.cert_org = cert_org
        # The status of HTTPS.
        # 
        # *   **on**: enabled.
        # *   **off**: disabled.
        self.cert_region = cert_region
        # The name of the SSL certificate.
        self.cert_start_time = cert_start_time
        # The status of the CNAME of the domain name.
        # 
        # *   **ok**: The domain name points to the CNAME assigned from Alibaba Cloud Content Delivery Network (CDN).
        # *   **cname_error**: An error occurred and the domain name cannot point to the CNAME.
        # *   **top_domain_cname_error**: An error occurred to the CNAME of the top-level domain name. The domain name cannot point to the CNAME.
        # *   **unsupport_wildcard**: Wildcard domain names are not supported.
        self.cert_type = cert_type
        # The status of HTTPS.
        # 
        # *   **on**: enabled.
        # *   **off**: disabled.
        self.cert_update_time = cert_update_time
        # >  The maximum number of times that each user can call this operation per second is 100.
        self.domain_cname_status = domain_cname_status
        # The type of the SSL certificate. Valid values:
        # 
        # *   **free**: a free SSL certificate.
        # *   **cas**: an SSL certificate purchased from Alibaba Cloud SSL Certificates Service.
        # *   **upload**: a user-uploaded SSL certificate.
        self.domain_name = domain_name
        # The public key of the SSL certificate.
        self.server_certificate = server_certificate
        # The accelerated domain name.
        self.server_certificate_status = server_certificate_status
        # The domain name that matches the SSL certificate.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_update_time is not None:
            result['CertUpdateTime'] = self.cert_update_time
        if self.domain_cname_status is not None:
            result['DomainCnameStatus'] = self.domain_cname_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertUpdateTime') is not None:
            self.cert_update_time = m.get('CertUpdateTime')
        if m.get('DomainCnameStatus') is not None:
            self.domain_cname_status = m.get('DomainCnameStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDomainCertificateInfoResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeDomainCertificateInfoResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeDomainCertificateInfoResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        # The unit of the validity period of the SSL certificate.
        # 
        # *   **months**: The validity period is measured in months.
        # *   **years**: The validity period is measured in years.
        self.cert_infos = cert_infos
        # The time when the SSL certificate expires.
        self.request_id = request_id

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainCertificateInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainCertificateInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCnameRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # The accelerated domain name that you want to query. Separate multiple domain names with commas (,). This parameter cannot be left empty.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainCnameResponseBodyCnameDatasData(TeaModel):
    def __init__(
        self,
        cname: str = None,
        domain: str = None,
        status: int = None,
    ):
        # The CNAME assigned to the domain name by Alibaba Cloud CDN.
        self.cname = cname
        # The accelerated domain name.
        self.domain = domain
        # The CNAME detection result. Valid values:
        # 
        # *   0: The DNS can detect the CNAME assigned to the domain name.
        # *   Value other than 0: The DNS cannot detect the CNAME assigned to the domain name.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDomainCnameResponseBodyCnameDatas(TeaModel):
    def __init__(
        self,
        data: List[DescribeDomainCnameResponseBodyCnameDatasData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDomainCnameResponseBodyCnameDatasData()
                self.data.append(temp_model.from_map(k))
        return self


class DescribeDomainCnameResponseBody(TeaModel):
    def __init__(
        self,
        cname_datas: DescribeDomainCnameResponseBodyCnameDatas = None,
        request_id: str = None,
    ):
        # Details about the CNAME detection results.
        self.cname_datas = cname_datas
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cname_datas:
            self.cname_datas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname_datas is not None:
            result['CnameDatas'] = self.cname_datas.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnameDatas') is not None:
            temp_model = DescribeDomainCnameResponseBodyCnameDatas()
            self.cname_datas = temp_model.from_map(m['CnameDatas'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainCnameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainCnameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainCnameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCustomLogConfigRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainCustomLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        remark: str = None,
        request_id: str = None,
        sample: str = None,
        tag: str = None,
    ):
        # The sample log configuration.
        self.config_id = config_id
        # The ID of the request.
        self.remark = remark
        # The format of the log configuration.
        self.request_id = request_id
        # The operation that you want to perform. Set the value to **DescribeDomainCustomLogConfig**.
        self.sample = sample
        # The ID of the log configuration.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeDomainCustomLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainCustomLogConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainDetailDataByLayerRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        isp_name_en: str = None,
        layer: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        # The bandwidth. Unit: bit/s.
        self.domain_name = domain_name
        # The protocol by which you want to query data. Valid values: **http**, **https**, **quic**, and **all**.
        # 
        # The default value is **all**.
        self.end_time = end_time
        # The number of queries per second.
        self.field = field
        # The amount of network traffic. Unit: bytes.
        self.isp_name_en = isp_name_en
        # The operation that you want to perform. Set the value to **DescribeDomainDetailDataByLayer**.
        self.layer = layer
        # The number of IPv6 requests per second.
        self.location_name_en = location_name_en
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.field is not None:
            result['Field'] = self.field
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainDetailDataByLayerResponseBodyDataDataModule(TeaModel):
    def __init__(
        self,
        acc: int = None,
        bps: float = None,
        domain_name: str = None,
        http_code: str = None,
        ipv_6acc: int = None,
        ipv_6bps: float = None,
        ipv_6qps: float = None,
        ipv_6traf: int = None,
        qps: float = None,
        time_stamp: str = None,
        traf: int = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time.
        self.acc = acc
        # Queries the detailed data of one or more accelerated domain names by protocol. Data is collected by domain name.
        self.bps = bps
        # DescribeDomainDetailDataByLayer
        self.domain_name = domain_name
        # The domain name.
        self.http_code = http_code
        # The detailed data of the accelerated domain names.
        self.ipv_6acc = ipv_6acc
        # The metric that you want to query. You can specify one or more metrics and separate them with commas (,). Valid values: **bps**, **qps**, **traf**, **acc**, **ipv6\_traf**, **ipv6\_bps**, **ipv6\_acc**, **ipv6\_qps**, and **http_code**.
        self.ipv_6bps = ipv_6bps
        # The proportions of HTTP status codes.
        self.ipv_6qps = ipv_6qps
        # The amount of network traffic generated by IPv6 requests. Unit: bytes.
        self.ipv_6traf = ipv_6traf
        # The name of the region. You can call the [DescribeCdnRegionAndIsp](~~91077~~) operation to query regions.
        # 
        # If you do not specify a region, data in all regions is queried.
        self.qps = qps
        # The ID of the request.
        self.time_stamp = time_stamp
        # The number of IPv6 requests.
        self.traf = traf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.ipv_6acc is not None:
            result['Ipv6Acc'] = self.ipv_6acc
        if self.ipv_6bps is not None:
            result['Ipv6Bps'] = self.ipv_6bps
        if self.ipv_6qps is not None:
            result['Ipv6Qps'] = self.ipv_6qps
        if self.ipv_6traf is not None:
            result['Ipv6Traf'] = self.ipv_6traf
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.traf is not None:
            result['Traf'] = self.traf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Ipv6Acc') is not None:
            self.ipv_6acc = m.get('Ipv6Acc')
        if m.get('Ipv6Bps') is not None:
            self.ipv_6bps = m.get('Ipv6Bps')
        if m.get('Ipv6Qps') is not None:
            self.ipv_6qps = m.get('Ipv6Qps')
        if m.get('Ipv6Traf') is not None:
            self.ipv_6traf = m.get('Ipv6Traf')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Traf') is not None:
            self.traf = m.get('Traf')
        return self


class DescribeDomainDetailDataByLayerResponseBodyData(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainDetailDataByLayerResponseBodyDataDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainDetailDataByLayerResponseBodyDataDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainDetailDataByLayerResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDomainDetailDataByLayerResponseBodyData = None,
        request_id: str = None,
    ):
        # The name of the Internet service provider (ISP) for your Alibaba Cloud CDN service. You can call the [DescribeCdnRegionAndIsp](~~91077~~) operation to query ISP names.
        # 
        # If you do not specify an ISP, data of all ISPs is queried.
        self.data = data
        # The timestamp of the data returned.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDomainDetailDataByLayerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainDetailDataByLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainDetailDataByLayerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainDetailDataByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHitRateDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule(TeaModel):
    def __init__(
        self,
        https_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.https_value = https_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainHitRateDataResponseBodyHitRateInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        hit_rate_interval: DescribeDomainHitRateDataResponseBodyHitRateInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.hit_rate_interval = hit_rate_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.hit_rate_interval:
            self.hit_rate_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hit_rate_interval is not None:
            result['HitRateInterval'] = self.hit_rate_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HitRateInterval') is not None:
            temp_model = DescribeDomainHitRateDataResponseBodyHitRateInterval()
            self.hit_rate_interval = temp_model.from_map(m['HitRateInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainHitRateDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHttpCodeDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        proportion: str = None,
    ):
        self.code = code
        self.count = count
        self.proportion = proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        code_proportion_data: List[DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData] = None,
    ):
        self.code_proportion_data = code_proportion_data

    def validate(self):
        if self.code_proportion_data:
            for k in self.code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CodeProportionData'] = []
        if self.code_proportion_data is not None:
            for k in self.code_proportion_data:
                result['CodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_proportion_data = []
        if m.get('CodeProportionData') is not None:
            for k in m.get('CodeProportionData'):
                temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData()
                self.code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        http_code_data: DescribeDomainHttpCodeDataResponseBodyHttpCodeData = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.http_code_data = http_code_data
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.http_code_data:
            self.http_code_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.http_code_data is not None:
            result['HttpCodeData'] = self.http_code_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HttpCodeData') is not None:
            temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeData()
            self.http_code_data = temp_model.from_map(m['HttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainHttpCodeDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHttpCodeDataByLayerRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        layer: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.layer = layer
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        total_value: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        self.total_value = total_value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_value is not None:
            result['TotalValue'] = self.total_value
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalValue') is not None:
            self.total_value = m.get('TotalValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainHttpCodeDataByLayerResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        http_code_data_interval: DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval = None,
        request_id: str = None,
    ):
        self.data_interval = data_interval
        self.http_code_data_interval = http_code_data_interval
        self.request_id = request_id

    def validate(self):
        if self.http_code_data_interval:
            self.http_code_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.http_code_data_interval is not None:
            result['HttpCodeDataInterval'] = self.http_code_data_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('HttpCodeDataInterval') is not None:
            temp_model = DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval()
            self.http_code_data_interval = temp_model.from_map(m['HttpCodeDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainHttpCodeDataByLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainHttpCodeDataByLayerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainHttpCodeDataByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainISPDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The request error rate.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The end time must be later than the start time.
        self.end_time = end_time
        # The accelerated domain name.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainISPDataResponseBodyValueISPProportionData(TeaModel):
    def __init__(
        self,
        avg_object_size: str = None,
        avg_response_rate: str = None,
        avg_response_time: str = None,
        bps: str = None,
        bytes_proportion: str = None,
        isp: str = None,
        isp_ename: str = None,
        proportion: str = None,
        qps: str = None,
        req_err_rate: str = None,
        total_bytes: str = None,
        total_query: str = None,
    ):
        # The average response time. Unit: milliseconds.
        self.avg_object_size = avg_object_size
        # The access statistics by ISP.
        self.avg_response_rate = avg_response_rate
        # The total number of requests.
        self.avg_response_time = avg_response_time
        # The time interval between the data entries. Unit: seconds.
        self.bps = bps
        self.bytes_proportion = bytes_proportion
        # Queries the proportions of data usage of different Internet service providers (ISPs). Data is collected every day. You can query data collected within the last 90 days.
        self.isp = isp
        # The ID of the request.
        self.isp_ename = isp_ename
        # The average response size. Unit: bytes.
        self.proportion = proportion
        # The bandwidth value.
        self.qps = qps
        # The beginning of the time range that was queried.
        self.req_err_rate = req_err_rate
        # The information about the ISP.
        self.total_bytes = total_bytes
        # The average response speed. Unit: byte/ms.
        self.total_query = total_query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        return self


class DescribeDomainISPDataResponseBodyValue(TeaModel):
    def __init__(
        self,
        ispproportion_data: List[DescribeDomainISPDataResponseBodyValueISPProportionData] = None,
    ):
        self.ispproportion_data = ispproportion_data

    def validate(self):
        if self.ispproportion_data:
            for k in self.ispproportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ISPProportionData'] = []
        if self.ispproportion_data is not None:
            for k in self.ispproportion_data:
                result['ISPProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ispproportion_data = []
        if m.get('ISPProportionData') is not None:
            for k in m.get('ISPProportionData'):
                temp_model = DescribeDomainISPDataResponseBodyValueISPProportionData()
                self.ispproportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainISPDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        value: DescribeDomainISPDataResponseBodyValue = None,
    ):
        # The accelerated domain name. You can specify only one domain name in each call.
        # 
        # By default, this operation queries the proportions of data usage for all accelerated domain names.
        self.data_interval = data_interval
        # The end of the time range that was queried.
        self.domain_name = domain_name
        # The operation that you want to perform. Set the value to **DescribeDomainISPData**.
        self.end_time = end_time
        # The number of queries per second.
        self.request_id = request_id
        # The proportion of network traffic.
        self.start_time = start_time
        # The proportion of the HTTP status code.
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Value') is not None:
            temp_model = DescribeDomainISPDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainISPDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainISPDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainISPDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainMax95BpsDataRequest(TeaModel):
    def __init__(
        self,
        cycle: str = None,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
        time_point: str = None,
    ):
        # 1001
        self.cycle = cycle
        # data.content.domesticMax95Bps
        self.domain_name = domain_name
        # The 95th percentile bandwidth.
        self.end_time = end_time
        # data.content.overseasMax95Bps
        self.start_time = start_time
        # data.content.max95Bps
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cycle is not None:
            result['Cycle'] = self.cycle
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        return self


class DescribeDomainMax95BpsDataResponseBodyDetailDataMax95Detail(TeaModel):
    def __init__(
        self,
        area: str = None,
        max_95bps: float = None,
        max_95bps_peak_time: str = None,
        time_stamp: str = None,
    ):
        self.area = area
        self.max_95bps = max_95bps
        self.max_95bps_peak_time = max_95bps_peak_time
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.max_95bps is not None:
            result['Max95Bps'] = self.max_95bps
        if self.max_95bps_peak_time is not None:
            result['Max95BpsPeakTime'] = self.max_95bps_peak_time
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Max95Bps') is not None:
            self.max_95bps = m.get('Max95Bps')
        if m.get('Max95BpsPeakTime') is not None:
            self.max_95bps_peak_time = m.get('Max95BpsPeakTime')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainMax95BpsDataResponseBodyDetailData(TeaModel):
    def __init__(
        self,
        max_95detail: List[DescribeDomainMax95BpsDataResponseBodyDetailDataMax95Detail] = None,
    ):
        self.max_95detail = max_95detail

    def validate(self):
        if self.max_95detail:
            for k in self.max_95detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Max95Detail'] = []
        if self.max_95detail is not None:
            for k in self.max_95detail:
                result['Max95Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.max_95detail = []
        if m.get('Max95Detail') is not None:
            for k in m.get('Max95Detail'):
                temp_model = DescribeDomainMax95BpsDataResponseBodyDetailDataMax95Detail()
                self.max_95detail.append(temp_model.from_map(k))
        return self


class DescribeDomainMax95BpsDataResponseBody(TeaModel):
    def __init__(
        self,
        detail_data: DescribeDomainMax95BpsDataResponseBodyDetailData = None,
        domain_name: str = None,
        domestic_max_95bps: str = None,
        end_time: str = None,
        max_95bps: str = None,
        overseas_max_95bps: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.detail_data = detail_data
        # http://inner.jing.alibaba-inc.com:1160/v2/api/rtlog/max95BpsData
        self.domain_name = domain_name
        self.domestic_max_95bps = domestic_max_95bps
        # domainName
        self.end_time = end_time
        self.max_95bps = max_95bps
        self.overseas_max_95bps = overseas_max_95bps
        # Specified EndTime does not math the specified StartTime.
        self.request_id = request_id
        # http://inner.jing.alibaba-inc.com:1160/v2/api/rtlog/max95BpsData
        self.start_time = start_time

    def validate(self):
        if self.detail_data:
            self.detail_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_data is not None:
            result['DetailData'] = self.detail_data.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domestic_max_95bps is not None:
            result['DomesticMax95Bps'] = self.domestic_max_95bps
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_95bps is not None:
            result['Max95Bps'] = self.max_95bps
        if self.overseas_max_95bps is not None:
            result['OverseasMax95Bps'] = self.overseas_max_95bps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailData') is not None:
            temp_model = DescribeDomainMax95BpsDataResponseBodyDetailData()
            self.detail_data = temp_model.from_map(m['DetailData'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomesticMax95Bps') is not None:
            self.domestic_max_95bps = m.get('DomesticMax95Bps')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Max95Bps') is not None:
            self.max_95bps = m.get('Max95Bps')
        if m.get('OverseasMax95Bps') is not None:
            self.overseas_max_95bps = m.get('OverseasMax95Bps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainMax95BpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainMax95BpsDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainMax95BpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainMultiUsageDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The operation that you want to perform. Set the value to **DescribeDomainMultiUsageData**.
        self.domain_name = domain_name
        # The number of requests.
        self.end_time = end_time
        # The information about requests collected every 5 minutes.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule(TeaModel):
    def __init__(
        self,
        domain: str = None,
        request: int = None,
        time_stamp: str = None,
        type: str = None,
    ):
        # DescribeDomainMultiUsageData
        self.domain = domain
        self.request = request
        # Queries the amount of data transfer and the number of requests for one or more accelerated domain names at a time. Data is collected every 5 minutes.
        self.time_stamp = time_stamp
        # The information about the accelerated domain name.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.request is not None:
            result['Request'] = self.request
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Request') is not None:
            self.request = m.get('Request')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDomainMultiUsageDataResponseBodyRequestPerInterval(TeaModel):
    def __init__(
        self,
        request_data_module: List[DescribeDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule] = None,
    ):
        self.request_data_module = request_data_module

    def validate(self):
        if self.request_data_module:
            for k in self.request_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestDataModule'] = []
        if self.request_data_module is not None:
            for k in self.request_data_module:
                result['RequestDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_data_module = []
        if m.get('RequestDataModule') is not None:
            for k in m.get('RequestDataModule'):
                temp_model = DescribeDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule()
                self.request_data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule(TeaModel):
    def __init__(
        self,
        area: str = None,
        bps: float = None,
        domain: str = None,
        time_stamp: str = None,
        type: str = None,
    ):
        self.area = area
        self.bps = bps
        self.domain = domain
        self.time_stamp = time_stamp
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDomainMultiUsageDataResponseBodyTrafficPerInterval(TeaModel):
    def __init__(
        self,
        traffic_data_module: List[DescribeDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule] = None,
    ):
        self.traffic_data_module = traffic_data_module

    def validate(self):
        if self.traffic_data_module:
            for k in self.traffic_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrafficDataModule'] = []
        if self.traffic_data_module is not None:
            for k in self.traffic_data_module:
                result['TrafficDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_data_module = []
        if m.get('TrafficDataModule') is not None:
            for k in m.get('TrafficDataModule'):
                temp_model = DescribeDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule()
                self.traffic_data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainMultiUsageDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        request_per_interval: DescribeDomainMultiUsageDataResponseBodyRequestPerInterval = None,
        start_time: str = None,
        traffic_per_interval: DescribeDomainMultiUsageDataResponseBodyTrafficPerInterval = None,
    ):
        # The end of the time range that was queried.
        self.end_time = end_time
        # The type of data returned.
        # 
        # >  For Alibaba Cloud CDN, the valid value is Simple.
        self.request_id = request_id
        # The ID of the request.
        self.request_per_interval = request_per_interval
        # The accelerated domain names. You can specify multiple accelerated domain names and separate domain names with commas (,).
        # 
        # > *   You can specify at most 30 accelerated domain names.
        # *   If you do not set this parameter, the data of all accelerated domain names that belong to your Alibaba Cloud account is queried.
        self.start_time = start_time
        self.traffic_per_interval = traffic_per_interval

    def validate(self):
        if self.request_per_interval:
            self.request_per_interval.validate()
        if self.traffic_per_interval:
            self.traffic_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_per_interval is not None:
            result['RequestPerInterval'] = self.request_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.traffic_per_interval is not None:
            result['TrafficPerInterval'] = self.traffic_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestPerInterval') is not None:
            temp_model = DescribeDomainMultiUsageDataResponseBodyRequestPerInterval()
            self.request_per_interval = temp_model.from_map(m['RequestPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TrafficPerInterval') is not None:
            temp_model = DescribeDomainMultiUsageDataResponseBodyTrafficPerInterval()
            self.traffic_per_interval = temp_model.from_map(m['TrafficPerInterval'])
        return self


class DescribeDomainMultiUsageDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainMultiUsageDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainMultiUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainPathDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.path = path
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path is not None:
            result['Path'] = self.path
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData(TeaModel):
    def __init__(
        self,
        acc: int = None,
        path: str = None,
        time: str = None,
        traffic: int = None,
    ):
        self.acc = acc
        self.path = path
        self.time = time
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.path is not None:
            result['Path'] = self.path
        if self.time is not None:
            result['Time'] = self.time
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeDomainPathDataResponseBodyPathDataPerInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainPathDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        path_data_per_interval: DescribeDomainPathDataResponseBodyPathDataPerInterval = None,
        start_time: str = None,
        total_count: int = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.path_data_per_interval = path_data_per_interval
        self.start_time = start_time
        self.total_count = total_count

    def validate(self):
        if self.path_data_per_interval:
            self.path_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path_data_per_interval is not None:
            result['PathDataPerInterval'] = self.path_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PathDataPerInterval') is not None:
            temp_model = DescribeDomainPathDataResponseBodyPathDataPerInterval()
            self.path_data_per_interval = temp_model.from_map(m['PathDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDomainPathDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainPathDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainPathDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainPvDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The timestamp of the returned data.
        self.domain_name = domain_name
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The number of PVs at each interval.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        # Queries the page view (PV) data of an accelerated domain name. The data is collected at an interval of 1 hour. You can query data within the last 90 days.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainPvDataResponseBodyPvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainPvDataResponseBodyPvDataIntervalUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainPvDataResponseBodyPvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainPvDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        pv_data_interval: DescribeDomainPvDataResponseBodyPvDataInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The ID of the request.
        self.data_interval = data_interval
        # The time interval between the data entries. Unit: seconds.
        self.domain_name = domain_name
        # The accelerated domain name.
        self.end_time = end_time
        # The operation that you want to perform. Set the value to **DescribeDomainPvData**.
        self.pv_data_interval = pv_data_interval
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The end time must be later than the start time.
        self.request_id = request_id
        # The beginning of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pv_data_interval is not None:
            result['PvDataInterval'] = self.pv_data_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PvDataInterval') is not None:
            temp_model = DescribeDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainPvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainPvDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainPvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule(TeaModel):
    def __init__(
        self,
        acc_domestic_value: str = None,
        acc_overseas_value: str = None,
        acc_value: str = None,
        domestic_value: str = None,
        https_acc_domestic_value: str = None,
        https_acc_overseas_value: str = None,
        https_acc_value: str = None,
        https_domestic_value: str = None,
        https_overseas_value: str = None,
        https_value: str = None,
        overseas_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.acc_domestic_value = acc_domestic_value
        self.acc_overseas_value = acc_overseas_value
        self.acc_value = acc_value
        self.domestic_value = domestic_value
        self.https_acc_domestic_value = https_acc_domestic_value
        self.https_acc_overseas_value = https_acc_overseas_value
        self.https_acc_value = https_acc_value
        self.https_domestic_value = https_domestic_value
        self.https_overseas_value = https_overseas_value
        self.https_value = https_value
        self.overseas_value = overseas_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc_domestic_value is not None:
            result['AccDomesticValue'] = self.acc_domestic_value
        if self.acc_overseas_value is not None:
            result['AccOverseasValue'] = self.acc_overseas_value
        if self.acc_value is not None:
            result['AccValue'] = self.acc_value
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.https_acc_domestic_value is not None:
            result['HttpsAccDomesticValue'] = self.https_acc_domestic_value
        if self.https_acc_overseas_value is not None:
            result['HttpsAccOverseasValue'] = self.https_acc_overseas_value
        if self.https_acc_value is not None:
            result['HttpsAccValue'] = self.https_acc_value
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccDomesticValue') is not None:
            self.acc_domestic_value = m.get('AccDomesticValue')
        if m.get('AccOverseasValue') is not None:
            self.acc_overseas_value = m.get('AccOverseasValue')
        if m.get('AccValue') is not None:
            self.acc_value = m.get('AccValue')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('HttpsAccDomesticValue') is not None:
            self.https_acc_domestic_value = m.get('HttpsAccDomesticValue')
        if m.get('HttpsAccOverseasValue') is not None:
            self.https_acc_overseas_value = m.get('HttpsAccOverseasValue')
        if m.get('HttpsAccValue') is not None:
            self.https_acc_value = m.get('HttpsAccValue')
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainQpsDataResponseBodyQpsDataInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        qps_data_interval: DescribeDomainQpsDataResponseBodyQpsDataInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.qps_data_interval = qps_data_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.qps_data_interval:
            self.qps_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.qps_data_interval is not None:
            result['QpsDataInterval'] = self.qps_data_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('QpsDataInterval') is not None:
            temp_model = DescribeDomainQpsDataResponseBodyQpsDataInterval()
            self.qps_data_interval = temp_model.from_map(m['QpsDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainQpsDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsDataByLayerRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        layer: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.layer = layer
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule(TeaModel):
    def __init__(
        self,
        acc_domestic_value: str = None,
        acc_overseas_value: str = None,
        acc_value: str = None,
        domestic_value: str = None,
        overseas_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.acc_domestic_value = acc_domestic_value
        self.acc_overseas_value = acc_overseas_value
        self.acc_value = acc_value
        self.domestic_value = domestic_value
        self.overseas_value = overseas_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc_domestic_value is not None:
            result['AccDomesticValue'] = self.acc_domestic_value
        if self.acc_overseas_value is not None:
            result['AccOverseasValue'] = self.acc_overseas_value
        if self.acc_value is not None:
            result['AccValue'] = self.acc_value
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccDomesticValue') is not None:
            self.acc_domestic_value = m.get('AccDomesticValue')
        if m.get('AccOverseasValue') is not None:
            self.acc_overseas_value = m.get('AccOverseasValue')
        if m.get('AccValue') is not None:
            self.acc_value = m.get('AccValue')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainQpsDataByLayerResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        layer: str = None,
        qps_data_interval: DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.layer = layer
        self.qps_data_interval = qps_data_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.qps_data_interval:
            self.qps_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.qps_data_interval is not None:
            result['QpsDataInterval'] = self.qps_data_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('QpsDataInterval') is not None:
            temp_model = DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval()
            self.qps_data_interval = temp_model.from_map(m['QpsDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsDataByLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainQpsDataByLayerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainQpsDataByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeBpsDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel(TeaModel):
    def __init__(
        self,
        bps: float = None,
        time_stamp: str = None,
    ):
        self.bps = bps
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainRealTimeBpsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        bps_model: List[DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel] = None,
    ):
        self.bps_model = bps_model

    def validate(self):
        if self.bps_model:
            for k in self.bps_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BpsModel'] = []
        if self.bps_model is not None:
            for k in self.bps_model:
                result['BpsModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bps_model = []
        if m.get('BpsModel') is not None:
            for k in m.get('BpsModel'):
                temp_model = DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel()
                self.bps_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDomainRealTimeBpsDataResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDomainRealTimeBpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRealTimeBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeBpsDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeByteHitRateDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel(TeaModel):
    def __init__(
        self,
        byte_hit_rate: float = None,
        time_stamp: str = None,
    ):
        self.byte_hit_rate = byte_hit_rate
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainRealTimeByteHitRateDataResponseBodyData(TeaModel):
    def __init__(
        self,
        byte_hit_rate_data_model: List[DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel] = None,
    ):
        self.byte_hit_rate_data_model = byte_hit_rate_data_model

    def validate(self):
        if self.byte_hit_rate_data_model:
            for k in self.byte_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ByteHitRateDataModel'] = []
        if self.byte_hit_rate_data_model is not None:
            for k in self.byte_hit_rate_data_model:
                result['ByteHitRateDataModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.byte_hit_rate_data_model = []
        if m.get('ByteHitRateDataModel') is not None:
            for k in m.get('ByteHitRateDataModel'):
                temp_model = DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel()
                self.byte_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeByteHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDomainRealTimeByteHitRateDataResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDomainRealTimeByteHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRealTimeByteHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeByteHitRateDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeByteHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeDetailDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        merge: str = None,
        merge_loc_isp: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2019-11-30T05:40:00Z.
        # 
        # >  The end time must be later than the start time. The time range between the end time and the start time cannot exceed 10 minutes.
        self.domain_name = domain_name
        # The metrics that you want to query. You can specify multiple metrics and separate them with commas (,). Valid values:
        # 
        # *   **qps**: the number of queries per second
        # *   **bps**: bandwidth values
        # *   **http_code**: HTTP status codes
        self.end_time = end_time
        # The data usage of each ISP and the number of visits in each region.
        self.field = field
        # The operation that you want to perform. Set the value to **DescribeDomainRealTimeDetailData**.
        self.isp_name_en = isp_name_en
        # The ID of the request.
        self.location_name_en = location_name_en
        # The name of the region. You can call the [DescribeCdnRegionAndIsp](~~91077~~) operation to query the most recent region list.
        self.merge = merge
        # Queries detailed monitoring data of one or more accelerated domain names at a time.
        self.merge_loc_isp = merge_loc_isp
        # Specifies whether to merge the results. Valid values:
        # 
        # *   **true**: merges the results.
        # *   **false**: does not merge the results. This is the default value.
        # 
        # Default value: **false**.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.field is not None:
            result['Field'] = self.field
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.merge is not None:
            result['Merge'] = self.merge
        if self.merge_loc_isp is not None:
            result['MergeLocIsp'] = self.merge_loc_isp
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('Merge') is not None:
            self.merge = m.get('Merge')
        if m.get('MergeLocIsp') is not None:
            self.merge_loc_isp = m.get('MergeLocIsp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeDetailDataResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # DescribeDomainRealTimeDetailData
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRealTimeDetailDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeDetailDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeDetailDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeHttpCodeDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        proportion: str = None,
    ):
        self.code = code
        self.count = count
        self.proportion = proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        real_time_code_proportion_data: List[DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData] = None,
    ):
        self.real_time_code_proportion_data = real_time_code_proportion_data

    def validate(self):
        if self.real_time_code_proportion_data:
            for k in self.real_time_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RealTimeCodeProportionData'] = []
        if self.real_time_code_proportion_data is not None:
            for k in self.real_time_code_proportion_data:
                result['RealTimeCodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.real_time_code_proportion_data = []
        if m.get('RealTimeCodeProportionData') is not None:
            for k in m.get('RealTimeCodeProportionData'):
                temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData()
                self.real_time_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        real_time_http_code_data: DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.real_time_http_code_data = real_time_http_code_data
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.real_time_http_code_data:
            self.real_time_http_code_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_http_code_data is not None:
            result['RealTimeHttpCodeData'] = self.real_time_http_code_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RealTimeHttpCodeData') is not None:
            temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData()
            self.real_time_http_code_data = temp_model.from_map(m['RealTimeHttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeHttpCodeDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeQpsDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel(TeaModel):
    def __init__(
        self,
        qps: float = None,
        time_stamp: str = None,
    ):
        self.qps = qps
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainRealTimeQpsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        qps_model: List[DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel] = None,
    ):
        self.qps_model = qps_model

    def validate(self):
        if self.qps_model:
            for k in self.qps_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QpsModel'] = []
        if self.qps_model is not None:
            for k in self.qps_model:
                result['QpsModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qps_model = []
        if m.get('QpsModel') is not None:
            for k in m.get('QpsModel'):
                temp_model = DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel()
                self.qps_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDomainRealTimeQpsDataResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDomainRealTimeQpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRealTimeQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeQpsDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeReqHitRateDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.domain_name = domain_name
        # The response parameters.
        self.end_time = end_time
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel(TeaModel):
    def __init__(
        self,
        req_hit_rate: float = None,
        time_stamp: str = None,
    ):
        # The timestamp. The time follows the ISO 8601 standard. The time is displayed in UTC.
        self.req_hit_rate = req_hit_rate
        # Queries the request hit ratios for one or more accelerated domain names.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainRealTimeReqHitRateDataResponseBodyData(TeaModel):
    def __init__(
        self,
        req_hit_rate_data_model: List[DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel] = None,
    ):
        self.req_hit_rate_data_model = req_hit_rate_data_model

    def validate(self):
        if self.req_hit_rate_data_model:
            for k in self.req_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReqHitRateDataModel'] = []
        if self.req_hit_rate_data_model is not None:
            for k in self.req_hit_rate_data_model:
                result['ReqHitRateDataModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.req_hit_rate_data_model = []
        if m.get('ReqHitRateDataModel') is not None:
            for k in m.get('ReqHitRateDataModel'):
                temp_model = DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel()
                self.req_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeReqHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDomainRealTimeReqHitRateDataResponseBodyData = None,
        request_id: str = None,
    ):
        # The operation that you want to perform. Set the value to **DescribeDomainRealTimeReqHitRateData**.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDomainRealTimeReqHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRealTimeReqHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeReqHitRateDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeSrcBpsDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        real_time_src_bps_data_per_interval: DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.real_time_src_bps_data_per_interval = real_time_src_bps_data_per_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.real_time_src_bps_data_per_interval:
            self.real_time_src_bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_src_bps_data_per_interval is not None:
            result['RealTimeSrcBpsDataPerInterval'] = self.real_time_src_bps_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RealTimeSrcBpsDataPerInterval') is not None:
            temp_model = DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval()
            self.real_time_src_bps_data_per_interval = temp_model.from_map(m['RealTimeSrcBpsDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeSrcBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeSrcBpsDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeSrcHttpCodeDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        proportion: str = None,
    ):
        self.code = code
        self.count = count
        self.proportion = proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        real_time_src_code_proportion_data: List[DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData] = None,
    ):
        self.real_time_src_code_proportion_data = real_time_src_code_proportion_data

    def validate(self):
        if self.real_time_src_code_proportion_data:
            for k in self.real_time_src_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RealTimeSrcCodeProportionData'] = []
        if self.real_time_src_code_proportion_data is not None:
            for k in self.real_time_src_code_proportion_data:
                result['RealTimeSrcCodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.real_time_src_code_proportion_data = []
        if m.get('RealTimeSrcCodeProportionData') is not None:
            for k in m.get('RealTimeSrcCodeProportionData'):
                temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData()
                self.real_time_src_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        real_time_src_http_code_data: DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.real_time_src_http_code_data = real_time_src_http_code_data
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.real_time_src_http_code_data:
            self.real_time_src_http_code_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_src_http_code_data is not None:
            result['RealTimeSrcHttpCodeData'] = self.real_time_src_http_code_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RealTimeSrcHttpCodeData') is not None:
            temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData()
            self.real_time_src_http_code_data = temp_model.from_map(m['RealTimeSrcHttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeSrcHttpCodeDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeSrcTrafficDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        real_time_src_traffic_data_per_interval: DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.real_time_src_traffic_data_per_interval = real_time_src_traffic_data_per_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.real_time_src_traffic_data_per_interval:
            self.real_time_src_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_src_traffic_data_per_interval is not None:
            result['RealTimeSrcTrafficDataPerInterval'] = self.real_time_src_traffic_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RealTimeSrcTrafficDataPerInterval') is not None:
            temp_model = DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval()
            self.real_time_src_traffic_data_per_interval = temp_model.from_map(m['RealTimeSrcTrafficDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeSrcTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeSrcTrafficDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeSrcTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeTrafficDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        real_time_traffic_data_per_interval: DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.real_time_traffic_data_per_interval = real_time_traffic_data_per_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.real_time_traffic_data_per_interval:
            self.real_time_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.real_time_traffic_data_per_interval is not None:
            result['RealTimeTrafficDataPerInterval'] = self.real_time_traffic_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RealTimeTrafficDataPerInterval') is not None:
            temp_model = DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval()
            self.real_time_traffic_data_per_interval = temp_model.from_map(m['RealTimeTrafficDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealTimeTrafficDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # The ID of the request.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.logstore = logstore
        self.project = project
        self.region = region
        self.request_id = request_id
        # The ID of the region where the Log Service project is deployed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDomainRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRealtimeLogDeliveryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRegionDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.  
        # 
        # The end time must be later than the start time.
        self.domain_name = domain_name
        # The proportion of bytes transferred from each region. For example, a value of 90 indicates that 90% of the bytes are transferred from the specified area.
        self.end_time = end_time
        # The information of the regions.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
    def __init__(
        self,
        avg_object_size: str = None,
        avg_response_rate: str = None,
        avg_response_time: str = None,
        bps: str = None,
        bytes_proportion: str = None,
        proportion: str = None,
        qps: str = None,
        region: str = None,
        region_ename: str = None,
        req_err_rate: str = None,
        total_bytes: str = None,
        total_query: str = None,
    ):
        # The bandwidth.
        self.avg_object_size = avg_object_size
        # The beginning of the time range that was queried.
        self.avg_response_rate = avg_response_rate
        # The average response time. Unit: milliseconds.
        self.avg_response_time = avg_response_time
        # The average response size. Unit: bytes.
        self.bps = bps
        self.bytes_proportion = bytes_proportion
        self.proportion = proportion
        # The ID of the request.
        self.qps = qps
        # DescribeDomainRegionData
        self.region = region
        # Queries the geographic distribution of users. The data is collected at an interval of 1 day. You can query data collected within the last 90 days.
        self.region_ename = region_ename
        # The time interval between the data entries returned. Unit: seconds.
        self.req_err_rate = req_err_rate
        # The total number of requests.
        self.total_bytes = total_bytes
        # The proportions of requests initiated from each area.
        self.total_query = total_query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        return self


class DescribeDomainRegionDataResponseBodyValue(TeaModel):
    def __init__(
        self,
        region_proportion_data: List[DescribeDomainRegionDataResponseBodyValueRegionProportionData] = None,
    ):
        self.region_proportion_data = region_proportion_data

    def validate(self):
        if self.region_proportion_data:
            for k in self.region_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionProportionData'] = []
        if self.region_proportion_data is not None:
            for k in self.region_proportion_data:
                result['RegionProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_proportion_data = []
        if m.get('RegionProportionData') is not None:
            for k in m.get('RegionProportionData'):
                temp_model = DescribeDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRegionDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        value: DescribeDomainRegionDataResponseBodyValue = None,
    ):
        # The proportion of visits from each region. For example, a value of 90 indicates that 90% of the visits are from the specified area.
        self.data_interval = data_interval
        # The accelerated domain name. Separate multiple accelerated domain names with commas (,).  
        # 
        # By default, this operation queries the geographic distribution of users for all accelerated domain names.
        self.domain_name = domain_name
        # The number of queries per second.
        self.end_time = end_time
        # The name of the region.
        self.request_id = request_id
        # The end of the time range that was queried.
        self.start_time = start_time
        # The average response speed. Unit: bit/s.
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Value') is not None:
            temp_model = DescribeDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainRegionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainRegionDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainRegionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainReqHitRateDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule(TeaModel):
    def __init__(
        self,
        https_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.https_value = https_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainReqHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        req_hit_rate_interval: DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.req_hit_rate_interval = req_hit_rate_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.req_hit_rate_interval:
            self.req_hit_rate_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.req_hit_rate_interval is not None:
            result['ReqHitRateInterval'] = self.req_hit_rate_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReqHitRateInterval') is not None:
            temp_model = DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval()
            self.req_hit_rate_interval = temp_model.from_map(m['ReqHitRateInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainReqHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainReqHitRateDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcBpsDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        https_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.https_value = https_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        src_bps_data_per_interval: DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.src_bps_data_per_interval = src_bps_data_per_interval
        self.start_time = start_time

    def validate(self):
        if self.src_bps_data_per_interval:
            self.src_bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.src_bps_data_per_interval is not None:
            result['SrcBpsDataPerInterval'] = self.src_bps_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SrcBpsDataPerInterval') is not None:
            temp_model = DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval()
            self.src_bps_data_per_interval = temp_model.from_map(m['SrcBpsDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainSrcBpsDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcHttpCodeDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        proportion: str = None,
    ):
        self.code = code
        self.count = count
        self.proportion = proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        return self


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        code_proportion_data: List[DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData] = None,
    ):
        self.code_proportion_data = code_proportion_data

    def validate(self):
        if self.code_proportion_data:
            for k in self.code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CodeProportionData'] = []
        if self.code_proportion_data is not None:
            for k in self.code_proportion_data:
                result['CodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_proportion_data = []
        if m.get('CodeProportionData') is not None:
            for k in m.get('CodeProportionData'):
                temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData()
                self.code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        http_code_data: DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.http_code_data = http_code_data
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.http_code_data:
            self.http_code_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.http_code_data is not None:
            result['HttpCodeData'] = self.http_code_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HttpCodeData') is not None:
            temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData()
            self.http_code_data = temp_model.from_map(m['HttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainSrcHttpCodeDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcQpsDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        src_qps_data_per_interval: DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.src_qps_data_per_interval = src_qps_data_per_interval
        self.start_time = start_time

    def validate(self):
        if self.src_qps_data_per_interval:
            self.src_qps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.src_qps_data_per_interval is not None:
            result['SrcQpsDataPerInterval'] = self.src_qps_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SrcQpsDataPerInterval') is not None:
            temp_model = DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval()
            self.src_qps_data_per_interval = temp_model.from_map(m['SrcQpsDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainSrcQpsDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcTopUrlVisitRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        sort_by: str = None,
        start_time: str = None,
    ):
        # The accelerated domain name. Separate multiple accelerated domain names with commas (,).
        self.domain_name = domain_name
        # The proportion of visits to the URL.
        self.end_time = end_time
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  If you do not set the StartTime parameter, the data within the previous day is queried.
        self.sort_by = sort_by
        # A list of frequently requested URLs.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        # The complete URL.
        self.flow = flow
        # The method that is used to sort the returned URLs.**** Valid values:
        # 
        # *   **traf**: by network traffic.
        # *   **pv**: by the number of page views. This is the default value.
        self.flow_proportion = flow_proportion
        # The beginning of the time range that was queried.
        self.url_detail = url_detail
        # The ID of the request.
        self.visit_data = visit_data
        # Queries frequently requested back-to-origin URLs of one or more accelerated domain names.
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl200List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl300List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl400List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl500List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBody(TeaModel):
    def __init__(
        self,
        all_url_list: DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList = None,
        domain_name: str = None,
        request_id: str = None,
        start_time: str = None,
        url_200list: DescribeDomainSrcTopUrlVisitResponseBodyUrl200List = None,
        url_300list: DescribeDomainSrcTopUrlVisitResponseBodyUrl300List = None,
        url_400list: DescribeDomainSrcTopUrlVisitResponseBodyUrl400List = None,
        url_500list: DescribeDomainSrcTopUrlVisitResponseBodyUrl500List = None,
    ):
        # The amount of network traffic. Unit: bytes.
        self.all_url_list = all_url_list
        # The proportion of network traffic consumed to access the URL.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time. The difference between the end time and the start time cannot exceed seven days.
        self.request_id = request_id
        # The accelerated domain name.
        self.start_time = start_time
        self.url_200list = url_200list
        self.url_300list = url_300list
        self.url_400list = url_400list
        self.url_500list = url_500list

    def validate(self):
        if self.all_url_list:
            self.all_url_list.validate()
        if self.url_200list:
            self.url_200list.validate()
        if self.url_300list:
            self.url_300list.validate()
        if self.url_400list:
            self.url_400list.validate()
        if self.url_500list:
            self.url_500list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_url_list is not None:
            result['AllUrlList'] = self.all_url_list.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.url_200list is not None:
            result['Url200List'] = self.url_200list.to_map()
        if self.url_300list is not None:
            result['Url300List'] = self.url_300list.to_map()
        if self.url_400list is not None:
            result['Url400List'] = self.url_400list.to_map()
        if self.url_500list is not None:
            result['Url500List'] = self.url_500list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllUrlList') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url200List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m['Url200List'])
        if m.get('Url300List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m['Url300List'])
        if m.get('Url400List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m['Url400List'])
        if m.get('Url500List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m['Url500List'])
        return self


class DescribeDomainSrcTopUrlVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainSrcTopUrlVisitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcTrafficDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        https_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.https_value = https_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        src_traffic_data_per_interval: DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.src_traffic_data_per_interval = src_traffic_data_per_interval
        self.start_time = start_time

    def validate(self):
        if self.src_traffic_data_per_interval:
            self.src_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.src_traffic_data_per_interval is not None:
            result['SrcTrafficDataPerInterval'] = self.src_traffic_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SrcTrafficDataPerInterval') is not None:
            temp_model = DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval()
            self.src_traffic_data_per_interval = temp_model.from_map(m['SrcTrafficDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainSrcTrafficDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopClientIpVisitRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        limit: str = None,
        location_name_en: str = None,
        sort_by: str = None,
        start_time: str = None,
    ):
        # The ranking of the client IP address returned.
        self.domain_name = domain_name
        # A list of client IP addresses.
        self.end_time = end_time
        # The maximum number of entries to return. Maximum value: 100.
        # 
        # Default value: 20. The default value 20 specifies that the top 20 data entries are returned.
        self.limit = limit
        # The client IP address returned. Only IPv4 addressed are supported.
        self.location_name_en = location_name_en
        # The method that is used to sort the client IP addresses. Valid values:
        # 
        # *   **traf**: by network traffic. This is the default value.
        # *   **acc**: by the number of requests.
        self.sort_by = sort_by
        # The operation that you want to perform. Set the value to **DescribeDomainTopClientIpVisit**.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainTopClientIpVisitResponseBodyClientIpList(TeaModel):
    def __init__(
        self,
        acc: int = None,
        client_ip: str = None,
        rank: int = None,
        traffic: int = None,
    ):
        # Queries client IP addresses that are ranked by the number of requests or the amount of network traffic within a specific time range for one or more accelerated domain names. You can query data collected within the last 90 days.
        self.acc = acc
        # The ID of the request.
        self.client_ip = client_ip
        # The total amount of network traffic consumed. Unit: bytes.
        self.rank = rank
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeDomainTopClientIpVisitResponseBody(TeaModel):
    def __init__(
        self,
        client_ip_list: List[DescribeDomainTopClientIpVisitResponseBodyClientIpList] = None,
        request_id: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The end time must be later than the start time.
        self.client_ip_list = client_ip_list
        # The accelerated domain name. Separate multiple accelerated domain names with commas (,).
        # 
        # By default, this operation queries client IP addresses for all accelerated domain names.
        self.request_id = request_id

    def validate(self):
        if self.client_ip_list:
            for k in self.client_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientIpList'] = []
        if self.client_ip_list is not None:
            for k in self.client_ip_list:
                result['ClientIpList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_ip_list = []
        if m.get('ClientIpList') is not None:
            for k in m.get('ClientIpList'):
                temp_model = DescribeDomainTopClientIpVisitResponseBodyClientIpList()
                self.client_ip_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainTopClientIpVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainTopClientIpVisitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainTopClientIpVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopReferVisitRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        sort_by: str = None,
        start_time: str = None,
    ):
        # The operation that you want to perform. Set the value to **DescribeDomainTopReferVisit**.
        self.domain_name = domain_name
        # The accelerated domain names. Separate multiple accelerated domain names with commas (,).
        self.end_time = end_time
        # The most frequently requested web pages.
        self.sort_by = sort_by
        # The number of visits to the web page.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainTopReferVisitResponseBodyTopReferListReferList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        refer_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        # The ID of the request.
        self.flow = flow
        # The proportion of the amount of network traffic consumed for visiting the web page.
        self.flow_proportion = flow_proportion
        # Queries frequently requested web pages of one or more accelerated domain names on a specified day and sorts the web pages. You can query data collected within the last 90 days.
        self.refer_detail = refer_detail
        # The proportion of visits to the web page.
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.refer_detail is not None:
            result['ReferDetail'] = self.refer_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('ReferDetail') is not None:
            self.refer_detail = m.get('ReferDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainTopReferVisitResponseBodyTopReferList(TeaModel):
    def __init__(
        self,
        refer_list: List[DescribeDomainTopReferVisitResponseBodyTopReferListReferList] = None,
    ):
        self.refer_list = refer_list

    def validate(self):
        if self.refer_list:
            for k in self.refer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReferList'] = []
        if self.refer_list is not None:
            for k in self.refer_list:
                result['ReferList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.refer_list = []
        if m.get('ReferList') is not None:
            for k in m.get('ReferList'):
                temp_model = DescribeDomainTopReferVisitResponseBodyTopReferListReferList()
                self.refer_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopReferVisitResponseBody(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        request_id: str = None,
        start_time: str = None,
        top_refer_list: DescribeDomainTopReferVisitResponseBodyTopReferList = None,
    ):
        # The sorting method. Valid values:
        # 
        # *   **traf**: by network traffic.
        # *   **pv**: by the number of page views. This is the default value.
        self.domain_name = domain_name
        # The URLs to the most frequently requested web pages.
        self.request_id = request_id
        # The beginning of the time range that was queried.
        self.start_time = start_time
        # The amount of network traffic. Unit: bytes.
        self.top_refer_list = top_refer_list

    def validate(self):
        if self.top_refer_list:
            self.top_refer_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top_refer_list is not None:
            result['TopReferList'] = self.top_refer_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TopReferList') is not None:
            temp_model = DescribeDomainTopReferVisitResponseBodyTopReferList()
            self.top_refer_list = temp_model.from_map(m['TopReferList'])
        return self


class DescribeDomainTopReferVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainTopReferVisitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainTopReferVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopUrlVisitRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        sort_by: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.sort_by = sort_by
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyAllUrlList(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl200List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl300List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl400List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl500List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBody(TeaModel):
    def __init__(
        self,
        all_url_list: DescribeDomainTopUrlVisitResponseBodyAllUrlList = None,
        domain_name: str = None,
        request_id: str = None,
        start_time: str = None,
        url_200list: DescribeDomainTopUrlVisitResponseBodyUrl200List = None,
        url_300list: DescribeDomainTopUrlVisitResponseBodyUrl300List = None,
        url_400list: DescribeDomainTopUrlVisitResponseBodyUrl400List = None,
        url_500list: DescribeDomainTopUrlVisitResponseBodyUrl500List = None,
    ):
        self.all_url_list = all_url_list
        self.domain_name = domain_name
        self.request_id = request_id
        self.start_time = start_time
        self.url_200list = url_200list
        self.url_300list = url_300list
        self.url_400list = url_400list
        self.url_500list = url_500list

    def validate(self):
        if self.all_url_list:
            self.all_url_list.validate()
        if self.url_200list:
            self.url_200list.validate()
        if self.url_300list:
            self.url_300list.validate()
        if self.url_400list:
            self.url_400list.validate()
        if self.url_500list:
            self.url_500list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_url_list is not None:
            result['AllUrlList'] = self.all_url_list.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.url_200list is not None:
            result['Url200List'] = self.url_200list.to_map()
        if self.url_300list is not None:
            result['Url300List'] = self.url_300list.to_map()
        if self.url_400list is not None:
            result['Url400List'] = self.url_400list.to_map()
        if self.url_500list is not None:
            result['Url500List'] = self.url_500list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllUrlList') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url200List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m['Url200List'])
        if m.get('Url300List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m['Url300List'])
        if m.get('Url400List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m['Url400List'])
        if m.get('Url500List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m['Url500List'])
        return self


class DescribeDomainTopUrlVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainTopUrlVisitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTrafficDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        domestic_value: str = None,
        https_domestic_value: str = None,
        https_overseas_value: str = None,
        https_value: str = None,
        overseas_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.domestic_value = domestic_value
        self.https_domestic_value = https_domestic_value
        self.https_overseas_value = https_overseas_value
        self.https_value = https_value
        self.overseas_value = overseas_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        traffic_data_per_interval: DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.traffic_data_per_interval = traffic_data_per_interval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeDomainTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainTrafficDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainUsageDataRequest(TeaModel):
    def __init__(
        self,
        area: str = None,
        data_protocol: str = None,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        interval: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The amount of resource usage.
        self.area = area
        # The information about resource usage that was collected at each interval.
        self.data_protocol = data_protocol
        # The type of content.
        self.domain_name = domain_name
        # The ID of the billable region where the data was collected.
        self.end_time = end_time
        # The time interval between the data entries returned. Unit: seconds.
        self.field = field
        # The timestamp of the data returned.
        # 
        # > **TimeStamp** indicates the timestamp of the data returned at each interval.
        self.interval = interval
        # static
        self.start_time = start_time
        # The resource usage that was collected at each interval.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.data_protocol is not None:
            result['DataProtocol'] = self.data_protocol
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.field is not None:
            result['Field'] = self.field
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('DataProtocol') is not None:
            self.data_protocol = m.get('DataProtocol')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        peak_time: str = None,
        special_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.peak_time = peak_time
        self.special_value = special_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.peak_time is not None:
            result['PeakTime'] = self.peak_time
        if self.special_value is not None:
            result['SpecialValue'] = self.special_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeakTime') is not None:
            self.peak_time = m.get('PeakTime')
        if m.get('SpecialValue') is not None:
            self.special_value = m.get('SpecialValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainUsageDataResponseBodyUsageDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainUsageDataResponseBody(TeaModel):
    def __init__(
        self,
        area: str = None,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        type: str = None,
        usage_data_per_interval: DescribeDomainUsageDataResponseBodyUsageDataPerInterval = None,
    ):
        self.area = area
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        # The resource usage in a specific scenario.
        # 
        # > SpecialValue indicates the data usage in a specific scenario. If no special billable item is specified, ignore this parameter.
        self.request_id = request_id
        self.start_time = start_time
        self.type = type
        self.usage_data_per_interval = usage_data_per_interval

    def validate(self):
        if self.usage_data_per_interval:
            self.usage_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.usage_data_per_interval is not None:
            result['UsageDataPerInterval'] = self.usage_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UsageDataPerInterval') is not None:
            temp_model = DescribeDomainUsageDataResponseBodyUsageDataPerInterval()
            self.usage_data_per_interval = temp_model.from_map(m['UsageDataPerInterval'])
        return self


class DescribeDomainUsageDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainUsageDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainUvDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The end time must be later than the start time.
        self.end_time = end_time
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        # The timestamp of the returned data.
        self.time_stamp = time_stamp
        # The number of UVs.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainUvDataResponseBodyUvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainUvDataResponseBodyUvDataIntervalUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeDomainUvDataResponseBodyUvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainUvDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        uv_data_interval: DescribeDomainUvDataResponseBodyUvDataInterval = None,
    ):
        # The time interval. Unit: seconds.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range that was queried.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range that was queried.
        self.start_time = start_time
        # The number of UVs at each interval.
        self.uv_data_interval = uv_data_interval

    def validate(self):
        if self.uv_data_interval:
            self.uv_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uv_data_interval is not None:
            result['UvDataInterval'] = self.uv_data_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UvDataInterval') is not None:
            temp_model = DescribeDomainUvDataResponseBodyUvDataInterval()
            self.uv_data_interval = temp_model.from_map(m['UvDataInterval'])
        return self


class DescribeDomainUvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainUvDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsBySourceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        sources: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        # The origin servers. Separate multiple origin servers with commas (,). Fuzzy match is not supported.
        self.sources = sources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo(TeaModel):
    def __init__(
        self,
        cdn_type: str = None,
        create_time: str = None,
        domain_cname: str = None,
        domain_name: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The workload type of the accelerated domain name. Valid values:
        # 
        # *   **web**: images and small files
        # *   **download**: large files
        # *   **video**: on-demand video and audio streaming
        self.cdn_type = cdn_type
        # The creation time.
        self.create_time = create_time
        # The CNAME record assigned to the domain name.
        self.domain_cname = domain_cname
        # The domain name.
        self.domain_name = domain_name
        # The status of the domain name. Valid values:
        # 
        # *   **applying**: The domain name is under review.
        # *   **configuring**: The domain name is being configured.
        # *   **online**: The domain name is working as expected.
        # *   **stopping**: The domain name is being stopped.
        # *   **offline**: The domain name is disabled.
        # *   **disabling**: The domain name is being removed.
        self.status = status
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_cname is not None:
            result['DomainCname'] = self.domain_cname
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainCname') is not None:
            self.domain_cname = m.get('DomainCname')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos(TeaModel):
    def __init__(
        self,
        domain_info: List[DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo] = None,
    ):
        self.domain_info = domain_info

    def validate(self):
        if self.domain_info:
            for k in self.domain_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['domainInfo'] = []
        if self.domain_info is not None:
            for k in self.domain_info:
                result['domainInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_info = []
        if m.get('domainInfo') is not None:
            for k in m.get('domainInfo'):
                temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo()
                self.domain_info.append(temp_model.from_map(k))
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains(TeaModel):
    def __init__(
        self,
        domain_names: List[str] = None,
    ):
        self.domain_names = domain_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['domainNames'] = self.domain_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainNames') is not None:
            self.domain_names = m.get('domainNames')
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsData(TeaModel):
    def __init__(
        self,
        domain_infos: DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos = None,
        domains: DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains = None,
        source: str = None,
    ):
        # Information about the domain name.
        self.domain_infos = domain_infos
        # The domain names that correspond to each origin server.
        self.domains = domains
        # The origin server.
        self.source = source

    def validate(self):
        if self.domain_infos:
            self.domain_infos.validate()
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_infos is not None:
            result['DomainInfos'] = self.domain_infos.to_map()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainInfos') is not None:
            temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos()
            self.domain_infos = temp_model.from_map(m['DomainInfos'])
        if m.get('Domains') is not None:
            temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeDomainsBySourceResponseBodyDomainsList(TeaModel):
    def __init__(
        self,
        domains_data: List[DescribeDomainsBySourceResponseBodyDomainsListDomainsData] = None,
    ):
        self.domains_data = domains_data

    def validate(self):
        if self.domains_data:
            for k in self.domains_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainsData'] = []
        if self.domains_data is not None:
            for k in self.domains_data:
                result['DomainsData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains_data = []
        if m.get('DomainsData') is not None:
            for k in m.get('DomainsData'):
                temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsData()
                self.domains_data.append(temp_model.from_map(k))
        return self


class DescribeDomainsBySourceResponseBody(TeaModel):
    def __init__(
        self,
        domains_list: DescribeDomainsBySourceResponseBodyDomainsList = None,
        request_id: str = None,
        sources: str = None,
    ):
        # The domain names corresponding to each origin server.
        self.domains_list = domains_list
        # The ID of the request.
        self.request_id = request_id
        # The origin servers.
        self.sources = sources

    def validate(self):
        if self.domains_list:
            self.domains_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains_list is not None:
            result['DomainsList'] = self.domains_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sources is not None:
            result['Sources'] = self.sources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainsList') is not None:
            temp_model = DescribeDomainsBySourceResponseBodyDomainsList()
            self.domains_list = temp_model.from_map(m['DomainsList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        return self


class DescribeDomainsBySourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainsBySourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainsBySourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsUsageByDayRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay(TeaModel):
    def __init__(
        self,
        bytes_hit_rate: str = None,
        max_bps: str = None,
        max_bps_time: str = None,
        max_src_bps: str = None,
        max_src_bps_time: str = None,
        qps: str = None,
        request_hit_rate: str = None,
        time_stamp: str = None,
        total_access: str = None,
        total_traffic: str = None,
    ):
        self.bytes_hit_rate = bytes_hit_rate
        self.max_bps = max_bps
        self.max_bps_time = max_bps_time
        self.max_src_bps = max_src_bps
        self.max_src_bps_time = max_src_bps_time
        self.qps = qps
        self.request_hit_rate = request_hit_rate
        self.time_stamp = time_stamp
        self.total_access = total_access
        self.total_traffic = total_traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes_hit_rate is not None:
            result['BytesHitRate'] = self.bytes_hit_rate
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        if self.max_src_bps is not None:
            result['MaxSrcBps'] = self.max_src_bps
        if self.max_src_bps_time is not None:
            result['MaxSrcBpsTime'] = self.max_src_bps_time
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.request_hit_rate is not None:
            result['RequestHitRate'] = self.request_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BytesHitRate') is not None:
            self.bytes_hit_rate = m.get('BytesHitRate')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        if m.get('MaxSrcBps') is not None:
            self.max_src_bps = m.get('MaxSrcBps')
        if m.get('MaxSrcBpsTime') is not None:
            self.max_src_bps_time = m.get('MaxSrcBpsTime')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('RequestHitRate') is not None:
            self.request_hit_rate = m.get('RequestHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        return self


class DescribeDomainsUsageByDayResponseBodyUsageByDays(TeaModel):
    def __init__(
        self,
        usage_by_day: List[DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay] = None,
    ):
        self.usage_by_day = usage_by_day

    def validate(self):
        if self.usage_by_day:
            for k in self.usage_by_day:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageByDay'] = []
        if self.usage_by_day is not None:
            for k in self.usage_by_day:
                result['UsageByDay'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_by_day = []
        if m.get('UsageByDay') is not None:
            for k in m.get('UsageByDay'):
                temp_model = DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay()
                self.usage_by_day.append(temp_model.from_map(k))
        return self


class DescribeDomainsUsageByDayResponseBodyUsageTotal(TeaModel):
    def __init__(
        self,
        bytes_hit_rate: str = None,
        max_bps: str = None,
        max_bps_time: str = None,
        max_src_bps: str = None,
        max_src_bps_time: str = None,
        request_hit_rate: str = None,
        total_access: str = None,
        total_traffic: str = None,
    ):
        self.bytes_hit_rate = bytes_hit_rate
        self.max_bps = max_bps
        self.max_bps_time = max_bps_time
        self.max_src_bps = max_src_bps
        self.max_src_bps_time = max_src_bps_time
        self.request_hit_rate = request_hit_rate
        self.total_access = total_access
        self.total_traffic = total_traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes_hit_rate is not None:
            result['BytesHitRate'] = self.bytes_hit_rate
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        if self.max_src_bps is not None:
            result['MaxSrcBps'] = self.max_src_bps
        if self.max_src_bps_time is not None:
            result['MaxSrcBpsTime'] = self.max_src_bps_time
        if self.request_hit_rate is not None:
            result['RequestHitRate'] = self.request_hit_rate
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BytesHitRate') is not None:
            self.bytes_hit_rate = m.get('BytesHitRate')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        if m.get('MaxSrcBps') is not None:
            self.max_src_bps = m.get('MaxSrcBps')
        if m.get('MaxSrcBpsTime') is not None:
            self.max_src_bps_time = m.get('MaxSrcBpsTime')
        if m.get('RequestHitRate') is not None:
            self.request_hit_rate = m.get('RequestHitRate')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        return self


class DescribeDomainsUsageByDayResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        usage_by_days: DescribeDomainsUsageByDayResponseBodyUsageByDays = None,
        usage_total: DescribeDomainsUsageByDayResponseBodyUsageTotal = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.usage_by_days = usage_by_days
        self.usage_total = usage_total

    def validate(self):
        if self.usage_by_days:
            self.usage_by_days.validate()
        if self.usage_total:
            self.usage_total.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.usage_by_days is not None:
            result['UsageByDays'] = self.usage_by_days.to_map()
        if self.usage_total is not None:
            result['UsageTotal'] = self.usage_total.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UsageByDays') is not None:
            temp_model = DescribeDomainsUsageByDayResponseBodyUsageByDays()
            self.usage_by_days = temp_model.from_map(m['UsageByDays'])
        if m.get('UsageTotal') is not None:
            temp_model = DescribeDomainsUsageByDayResponseBodyUsageTotal()
            self.usage_total = temp_model.from_map(m['UsageTotal'])
        return self


class DescribeDomainsUsageByDayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainsUsageByDayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainsUsageByDayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEsExceptionDataRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        rule_id: str = None,
        start_time: str = None,
    ):
        # The ID of the request.
        self.end_time = end_time
        # The operation that you want to perform. Set the value to **DescribeEsExceptionData**.
        self.rule_id = rule_id
        # The value of each time and the column of each data entry.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeEsExceptionDataResponseBodyContentsPoints(TeaModel):
    def __init__(
        self,
        points: List[str] = None,
    ):
        self.points = points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.points is not None:
            result['Points'] = self.points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Points') is not None:
            self.points = m.get('Points')
        return self


class DescribeEsExceptionDataResponseBodyContents(TeaModel):
    def __init__(
        self,
        columns: List[str] = None,
        name: str = None,
        points: List[DescribeEsExceptionDataResponseBodyContentsPoints] = None,
    ):
        self.columns = columns
        self.name = name
        self.points = points

    def validate(self):
        if self.points:
            for k in self.points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['Columns'] = self.columns
        if self.name is not None:
            result['Name'] = self.name
        result['Points'] = []
        if self.points is not None:
            for k in self.points:
                result['Points'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.points = []
        if m.get('Points') is not None:
            for k in m.get('Points'):
                temp_model = DescribeEsExceptionDataResponseBodyContentsPoints()
                self.points.append(temp_model.from_map(k))
        return self


class DescribeEsExceptionDataResponseBody(TeaModel):
    def __init__(
        self,
        contents: List[DescribeEsExceptionDataResponseBodyContents] = None,
        request_id: str = None,
    ):
        # Queries the executions errors of scripts in EdgeScript (ES).
        self.contents = contents
        # The content of the script.
        self.request_id = request_id

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = DescribeEsExceptionDataResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEsExceptionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEsExceptionDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEsExceptionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEsExecuteDataRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        rule_id: str = None,
        start_time: str = None,
    ):
        # The name of the chart that shows the status of the script.
        self.end_time = end_time
        # The value of each time and the column of each data entry.
        self.rule_id = rule_id
        # The column names of the chart that shows the status of the script and the time of each data entry.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeEsExecuteDataResponseBodyContents(TeaModel):
    def __init__(
        self,
        columns: List[str] = None,
        name: str = None,
        points: List[str] = None,
    ):
        self.columns = columns
        # The content of the script.
        self.name = name
        # Queries the execution status of scripts in EdgeScript (ES).
        self.points = points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['Columns'] = self.columns
        if self.name is not None:
            result['Name'] = self.name
        if self.points is not None:
            result['Points'] = self.points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        return self


class DescribeEsExecuteDataResponseBody(TeaModel):
    def __init__(
        self,
        contents: List[DescribeEsExecuteDataResponseBodyContents] = None,
        request_id: str = None,
    ):
        # The operation that you want to perform. Set the value to **DescribeEsExecuteData**.
        self.contents = contents
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = DescribeEsExecuteDataResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEsExecuteDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEsExecuteDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEsExecuteDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFCTriggerRequest(TeaModel):
    def __init__(
        self,
        trigger_arn: str = None,
    ):
        # The trigger that corresponds to the Function Compute service.
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class DescribeFCTriggerResponseBodyFCTrigger(TeaModel):
    def __init__(
        self,
        event_meta_name: str = None,
        event_meta_version: str = None,
        notes: str = None,
        role_arn: str = None,
        source_arn: str = None,
        trigger_arn: str = None,
    ):
        # The name of the event.
        self.event_meta_name = event_meta_name
        # The version of the event.
        self.event_meta_version = event_meta_version
        # The remarks of the Function Compute trigger.
        self.notes = notes
        # The assigned Resource Access Management (RAM) role.
        self.role_arn = role_arn
        # The resources and filters for event listening.
        self.source_arn = source_arn
        # The trigger that corresponds to the Function Compute service.
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class DescribeFCTriggerResponseBody(TeaModel):
    def __init__(
        self,
        fctrigger: DescribeFCTriggerResponseBodyFCTrigger = None,
        request_id: str = None,
    ):
        # The Function Compute trigger that you want to query.
        self.fctrigger = fctrigger
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.fctrigger:
            self.fctrigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fctrigger is not None:
            result['FCTrigger'] = self.fctrigger.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FCTrigger') is not None:
            temp_model = DescribeFCTriggerResponseBodyFCTrigger()
            self.fctrigger = temp_model.from_map(m['FCTrigger'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFCTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpInfoRequest(TeaModel):
    def __init__(
        self,
        ip: str = None,
    ):
        # The IP address that you want to query. You can specify only one IP address in each request.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class DescribeIpInfoResponseBody(TeaModel):
    def __init__(
        self,
        cdn_ip: str = None,
        isp: str = None,
        isp_ename: str = None,
        region: str = None,
        region_ename: str = None,
        request_id: str = None,
    ):
        # Indicates whether the IP address belongs to an Alibaba Cloud CDN POP.
        # 
        # *   **True**\
        # *   **False**\
        self.cdn_ip = cdn_ip
        # The Chinese name of the ISP.
        self.isp = isp
        # The English name of the Internet service provider (ISP).
        self.isp_ename = isp_ename
        # The Chinese name of the region.
        self.region = region
        # The English name of the region.
        self.region_ename = region_ename
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_ip is not None:
            result['CdnIp'] = self.cdn_ip
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.region is not None:
            result['Region'] = self.region
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnIp') is not None:
            self.cdn_ip = m.get('CdnIp')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIpInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIpInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIpInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpStatusRequest(TeaModel):
    def __init__(
        self,
        ips: str = None,
    ):
        # The IP addresses that you want to query. Separate IP addresses with underscores (\_), such as Ips=ip1\_ip2.
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ips is not None:
            result['Ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        return self


class DescribeIpStatusResponseBodyIpStatus(TeaModel):
    def __init__(
        self,
        ip: str = None,
        status: str = None,
    ):
        # The IP address of the POP.
        self.ip = ip
        # The status.
        # 
        # *   **nonali**: not an Alibaba Cloud CDN POP
        # *   **normal**: an available Alibaba Cloud CDN POP
        # *   **abnormal**: an unavailable Alibaba Cloud CDN POP
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeIpStatusResponseBody(TeaModel):
    def __init__(
        self,
        ip_status: List[DescribeIpStatusResponseBodyIpStatus] = None,
        request_id: str = None,
    ):
        # The status of the IP addresses of the POPs.
        self.ip_status = ip_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ip_status:
            for k in self.ip_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpStatus'] = []
        if self.ip_status is not None:
            for k in self.ip_status:
                result['IpStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_status = []
        if m.get('IpStatus') is not None:
            for k in m.get('IpStatus'):
                temp_model = DescribeIpStatusResponseBodyIpStatus()
                self.ip_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIpStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIpStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIpStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeL2VipsByDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name in each request.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeL2VipsByDomainResponseBodyVips(TeaModel):
    def __init__(
        self,
        vip: List[str] = None,
    ):
        self.vip = vip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vip is not None:
            result['Vip'] = self.vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        return self


class DescribeL2VipsByDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        request_id: str = None,
        vips: DescribeL2VipsByDomainResponseBodyVips = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The ID of the request.
        self.request_id = request_id
        # The list of VIPs.
        self.vips = vips

    def validate(self):
        if self.vips:
            self.vips.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vips is not None:
            result['Vips'] = self.vips.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Vips') is not None:
            temp_model = DescribeL2VipsByDomainResponseBodyVips()
            self.vips = temp_model.from_map(m['Vips'])
        return self


class DescribeL2VipsByDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeL2VipsByDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeL2VipsByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePreloadDetailByIdRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribePreloadDetailByIdResponseBodyUrlDetailsUrls(TeaModel):
    def __init__(
        self,
        description: str = None,
        success: str = None,
        url: str = None,
    ):
        self.description = description
        self.success = success
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribePreloadDetailByIdResponseBodyUrlDetails(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        domain: str = None,
        end_time: str = None,
        process: str = None,
        ret_code: str = None,
        status: str = None,
        task_id: str = None,
        urls: List[DescribePreloadDetailByIdResponseBodyUrlDetailsUrls] = None,
    ):
        self.creation_time = creation_time
        self.domain = domain
        self.end_time = end_time
        self.process = process
        self.ret_code = ret_code
        self.status = status
        self.task_id = task_id
        self.urls = urls

    def validate(self):
        if self.urls:
            for k in self.urls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.process is not None:
            result['Process'] = self.process
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        result['Urls'] = []
        if self.urls is not None:
            for k in self.urls:
                result['Urls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        self.urls = []
        if m.get('Urls') is not None:
            for k in m.get('Urls'):
                temp_model = DescribePreloadDetailByIdResponseBodyUrlDetailsUrls()
                self.urls.append(temp_model.from_map(k))
        return self


class DescribePreloadDetailByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        url_details: List[DescribePreloadDetailByIdResponseBodyUrlDetails] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.url_details = url_details

    def validate(self):
        if self.url_details:
            for k in self.url_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UrlDetails'] = []
        if self.url_details is not None:
            for k in self.url_details:
                result['UrlDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.url_details = []
        if m.get('UrlDetails') is not None:
            for k in m.get('UrlDetails'):
                temp_model = DescribePreloadDetailByIdResponseBodyUrlDetails()
                self.url_details.append(temp_model.from_map(k))
        return self


class DescribePreloadDetailByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePreloadDetailByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePreloadDetailByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRangeDataByLocateAndIspServiceRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        end_time: str = None,
        isp_names: str = None,
        location_names: str = None,
        start_time: str = None,
    ):
        self.domain_names = domain_names
        self.end_time = end_time
        self.isp_names = isp_names
        self.location_names = location_names
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_names is not None:
            result['IspNames'] = self.isp_names
        if self.location_names is not None:
            result['LocationNames'] = self.location_names
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNames') is not None:
            self.isp_names = m.get('IspNames')
        if m.get('LocationNames') is not None:
            self.location_names = m.get('LocationNames')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRangeDataByLocateAndIspServiceResponseBody(TeaModel):
    def __init__(
        self,
        json_result: str = None,
        request_id: str = None,
    ):
        self.json_result = json_result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRangeDataByLocateAndIspServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRangeDataByLocateAndIspServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRangeDataByLocateAndIspServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRealtimeDeliveryAccRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        interval: str = None,
        log_store: str = None,
        project: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        # 
        # The end of the time range to query. The end time must be later than the start time.
        self.end_time = end_time
        # The time interval between the data entries. Unit: seconds. The value varies based on the values of the **StartTime** and **EndTime** parameters. Valid values:
        # 
        # *   If the time span between StartTime and EndTime is less than 3 days, valid values are **300**, **3600**, and **86400**. Default value: **300**.
        # *   If the time span between StartTime and EndTime is from 3 to 31 days (31 days excluded), valid values are **3600** and **86400**. Default value: **3600**.
        # *   If the time span between StartTime and EndTime is 31 days or longer, the valid value is **86400**. Default value: **86400**.
        self.interval = interval
        # The timestamp of the data.
        self.log_store = log_store
        # The name of the Log Service project that is used for real-time log delivery. By default, all projects are queried.
        self.project = project
        # The information about real-time log delivery.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData(TeaModel):
    def __init__(
        self,
        failed_num: int = None,
        success_num: int = None,
        time_stamp: str = None,
    ):
        # Queries the number of real-time log deliveries.
        self.failed_num = failed_num
        self.success_num = success_num
        # The name of the Logstore that collects log data from Alibaba Cloud Content Delivery Network (CDN) in real time. By default, all Logstores are queried.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num
        if self.success_num is not None:
            result['SuccessNum'] = self.success_num
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')
        if m.get('SuccessNum') is not None:
            self.success_num = m.get('SuccessNum')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData(TeaModel):
    def __init__(
        self,
        acc_data: List[DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData] = None,
    ):
        self.acc_data = acc_data

    def validate(self):
        if self.acc_data:
            for k in self.acc_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccData'] = []
        if self.acc_data is not None:
            for k in self.acc_data:
                result['AccData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acc_data = []
        if m.get('AccData') is not None:
            for k in m.get('AccData'):
                temp_model = DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData()
                self.acc_data.append(temp_model.from_map(k))
        return self


class DescribeRealtimeDeliveryAccResponseBody(TeaModel):
    def __init__(
        self,
        reat_time_delivery_acc_data: DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData = None,
        request_id: str = None,
    ):
        # The operation that you want to perform. Set the value to **DescribeRealtimeDeliveryAcc**.
        self.reat_time_delivery_acc_data = reat_time_delivery_acc_data
        # The number of failed attempts to deliver log data to Log Service.
        self.request_id = request_id

    def validate(self):
        if self.reat_time_delivery_acc_data:
            self.reat_time_delivery_acc_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reat_time_delivery_acc_data is not None:
            result['ReatTimeDeliveryAccData'] = self.reat_time_delivery_acc_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReatTimeDeliveryAccData') is not None:
            temp_model = DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData()
            self.reat_time_delivery_acc_data = temp_model.from_map(m['ReatTimeDeliveryAccData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRealtimeDeliveryAccResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRealtimeDeliveryAccResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRealtimeDeliveryAccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRefreshQuotaRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRefreshQuotaResponseBody(TeaModel):
    def __init__(
        self,
        block_quota: str = None,
        block_remain: str = None,
        dir_quota: str = None,
        dir_remain: str = None,
        ignore_params_quota: str = None,
        ignore_params_remain: str = None,
        preload_edge_quota: str = None,
        preload_edge_remain: str = None,
        preload_quota: str = None,
        preload_remain: str = None,
        regex_quota: str = None,
        regex_remain: str = None,
        request_id: str = None,
        url_quota: str = None,
        url_remain: str = None,
    ):
        # The maximum number of URLs that can be refreshed on the current day.
        self.block_quota = block_quota
        # The remaining number of times that you can prefetch content to L1 nodes on the current day.
        self.block_remain = block_remain
        # The remaining number of directories that can be refreshed on the current day.
        self.dir_quota = dir_quota
        # The operation that you want to perform. Set this parameter to **DescribeRefreshQuota**.
        self.dir_remain = dir_remain
        # 当天忽略参数刷新数量上限。
        self.ignore_params_quota = ignore_params_quota
        # 当天剩余忽略参数刷新数量。
        self.ignore_params_remain = ignore_params_remain
        # The maximum number of directories that can be refreshed on the current day.
        self.preload_edge_quota = preload_edge_quota
        # The maximum number of times that you can prefetch content to L2 nodes on the current day.
        self.preload_edge_remain = preload_edge_remain
        # The remaining number of times that you can use regular expressions to refresh directories or URLs on the current day.
        self.preload_quota = preload_quota
        # The maximum number of URLs and directories that can be blocked on the current day.
        self.preload_remain = preload_remain
        # The ID of the request
        self.regex_quota = regex_quota
        # The remaining number of times that you can prefetch content to L2 nodes on the current day.
        self.regex_remain = regex_remain
        # The remaining number of URLs that can be refreshed on the current day.
        self.request_id = request_id
        # The maximum number of times that you can prefetch content to L1 nodes on the current day.
        self.url_quota = url_quota
        # The maximum number of times that you can use regular expressions to refresh directories or URLs on the current day.
        self.url_remain = url_remain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.block_remain is not None:
            result['BlockRemain'] = self.block_remain
        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota
        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain
        if self.ignore_params_quota is not None:
            result['IgnoreParamsQuota'] = self.ignore_params_quota
        if self.ignore_params_remain is not None:
            result['IgnoreParamsRemain'] = self.ignore_params_remain
        if self.preload_edge_quota is not None:
            result['PreloadEdgeQuota'] = self.preload_edge_quota
        if self.preload_edge_remain is not None:
            result['PreloadEdgeRemain'] = self.preload_edge_remain
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.regex_quota is not None:
            result['RegexQuota'] = self.regex_quota
        if self.regex_remain is not None:
            result['RegexRemain'] = self.regex_remain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota
        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')
        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')
        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')
        if m.get('IgnoreParamsQuota') is not None:
            self.ignore_params_quota = m.get('IgnoreParamsQuota')
        if m.get('IgnoreParamsRemain') is not None:
            self.ignore_params_remain = m.get('IgnoreParamsRemain')
        if m.get('PreloadEdgeQuota') is not None:
            self.preload_edge_quota = m.get('PreloadEdgeQuota')
        if m.get('PreloadEdgeRemain') is not None:
            self.preload_edge_remain = m.get('PreloadEdgeRemain')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RegexQuota') is not None:
            self.regex_quota = m.get('RegexQuota')
        if m.get('RegexRemain') is not None:
            self.regex_remain = m.get('RegexRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')
        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')
        return self


class DescribeRefreshQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRefreshQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRefreshQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRefreshTaskByIdRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The path of the object refreshed by the refresh task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeRefreshTaskByIdResponseBodyTasks(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        object_path: str = None,
        object_type: str = None,
        process: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The progress of the task, in percentage.
        self.creation_time = creation_time
        # The ID of the task.
        self.description = description
        # Queries the status of refresh or prefetch tasks by ID for an accelerated domain name.
        self.object_path = object_path
        # The ID of the request.
        self.object_type = object_type
        # The operation that you want to perform. Set the value to **DescribeRefreshTaskById**.
        self.process = process
        # The time when the task was created. The time is displayed in UTC.
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeRefreshTaskByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[DescribeRefreshTaskByIdResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # The ID of the task that you want to query.
        # 
        # You can call the [RefreshObjectCaches](~~91164~~) operation to query task IDs. Then, you can use the task IDs to query task status.
        # 
        # You can specify up to 10 task IDs. Separate task IDs with commas (,).
        self.request_id = request_id
        # The error returned when the refresh or prefetch task failed. Valid values:
        # 
        # *   **Internal Error**: An internal error occurred.
        # *   **Origin Timeout**: The response from the origin server timed out.
        # *   **Origin Return StatusCode 5XX**: The origin server returned a 5XX error.
        self.tasks = tasks
        # The total number of tasks.
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribeRefreshTaskByIdResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRefreshTaskByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRefreshTaskByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRefreshTaskByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRefreshTasksRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        object_path: str = None,
        object_type: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        security_token: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.object_path = object_path
        self.object_type = object_type
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.security_token = security_token
        self.start_time = start_time
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeRefreshTasksResponseBodyTasksCDNTask(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        object_path: str = None,
        object_type: str = None,
        process: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.object_path = object_path
        self.object_type = object_type
        self.process = process
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeRefreshTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        cdntask: List[DescribeRefreshTasksResponseBodyTasksCDNTask] = None,
    ):
        self.cdntask = cdntask

    def validate(self):
        if self.cdntask:
            for k in self.cdntask:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CDNTask'] = []
        if self.cdntask is not None:
            for k in self.cdntask:
                result['CDNTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cdntask = []
        if m.get('CDNTask') is not None:
            for k in m.get('CDNTask'):
                temp_model = DescribeRefreshTasksResponseBodyTasksCDNTask()
                self.cdntask.append(temp_model.from_map(k))
        return self


class DescribeRefreshTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: DescribeRefreshTasksResponseBodyTasks = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tasks') is not None:
            temp_model = DescribeRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRefreshTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRefreshTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRefreshTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStagingIpResponseBodyIPV4s(TeaModel):
    def __init__(
        self,
        ipv4: List[str] = None,
    ):
        self.ipv4 = ipv4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv4 is not None:
            result['IPV4'] = self.ipv4
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPV4') is not None:
            self.ipv4 = m.get('IPV4')
        return self


class DescribeStagingIpResponseBody(TeaModel):
    def __init__(
        self,
        ipv4s: DescribeStagingIpResponseBodyIPV4s = None,
        request_id: str = None,
    ):
        self.ipv4s = ipv4s
        # Queries node IP addresses in the staging environment.
        self.request_id = request_id

    def validate(self):
        if self.ipv4s:
            self.ipv4s.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv4s is not None:
            result['IPV4s'] = self.ipv4s.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPV4s') is not None:
            temp_model = DescribeStagingIpResponseBodyIPV4s()
            self.ipv4s = temp_model.from_map(m['IPV4s'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeStagingIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStagingIpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeStagingIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeTagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[DescribeTagResourcesRequestTag] = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBodyTagResourcesTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        tag: List[DescribeTagResourcesResponseBodyTagResourcesTag] = None,
    ):
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeTagResourcesResponseBodyTagResourcesTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_resources: List[DescribeTagResourcesResponseBodyTagResources] = None,
    ):
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = DescribeTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopDomainsByFlowRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        limit: int = None,
        start_time: str = None,
    ):
        # The maximum number of domain names to query. Valid values: **1** to **100**. Default value: **20**.
        self.end_time = end_time
        # The total number of accelerated domain names that are in the **Enabled** state within the current Alibaba Cloud account.
        self.limit = limit
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        max_bps: float = None,
        max_bps_time: str = None,
        rank: int = None,
        total_access: int = None,
        total_traffic: str = None,
        traffic_percent: str = None,
    ):
        # The total number of accelerated domain names that belong to the current Alibaba Cloud account.
        self.domain_name = domain_name
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  Set StartTime to UTC time in the yyyy-MM-ddTHH:mm:ssZ format. For example, if the local time is 00:00, June 1, 2021, set StartTime to 2021-05-31T16:00:00Z.
        self.max_bps = max_bps
        # Queries the top N domain names ranked by network traffic. You can query data collected within the last 30 days.
        self.max_bps_time = max_bps_time
        # The time when the bandwidth reached the peak value.
        self.rank = rank
        # The top N domain names ranked by network traffic.
        self.total_access = total_access
        # The ID of the request.
        self.total_traffic = total_traffic
        # The beginning of the time range during which data was queried.
        self.traffic_percent = traffic_percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.traffic_percent is not None:
            result['TrafficPercent'] = self.traffic_percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('TrafficPercent') is not None:
            self.traffic_percent = m.get('TrafficPercent')
        return self


class DescribeTopDomainsByFlowResponseBodyTopDomains(TeaModel):
    def __init__(
        self,
        top_domain: List[DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain] = None,
    ):
        self.top_domain = top_domain

    def validate(self):
        if self.top_domain:
            for k in self.top_domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopDomain'] = []
        if self.top_domain is not None:
            for k in self.top_domain:
                result['TopDomain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.top_domain = []
        if m.get('TopDomain') is not None:
            for k in m.get('TopDomain'):
                temp_model = DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k))
        return self


class DescribeTopDomainsByFlowResponseBody(TeaModel):
    def __init__(
        self,
        domain_count: int = None,
        domain_online_count: int = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        top_domains: DescribeTopDomainsByFlowResponseBodyTopDomains = None,
    ):
        # The number of visits to the accelerated domain name.
        self.domain_count = domain_count
        # The ranking of the accelerated domain name.
        self.domain_online_count = domain_online_count
        # The operation that you want to perform. Set the value to **DescribeTopDomainsByFlow**.
        self.end_time = end_time
        # The proportion of the amount of network traffic consumed for visiting the web page.
        self.request_id = request_id
        # The total amount of network traffic.
        self.start_time = start_time
        # The end of the time range during which data was queried.
        self.top_domains = top_domains

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.domain_online_count is not None:
            result['DomainOnlineCount'] = self.domain_online_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('DomainOnlineCount') is not None:
            self.domain_online_count = m.get('DomainOnlineCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TopDomains') is not None:
            temp_model = DescribeTopDomainsByFlowResponseBodyTopDomains()
            self.top_domains = temp_model.from_map(m['TopDomains'])
        return self


class DescribeTopDomainsByFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTopDomainsByFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTopDomainsByFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserCertificateExpireCountResponseBody(TeaModel):
    def __init__(
        self,
        expire_within_30days_count: int = None,
        expired_count: int = None,
        request_id: str = None,
    ):
        # The ID of the request.
        self.expire_within_30days_count = expire_within_30days_count
        self.expired_count = expired_count
        # The number of domain names whose SSL certificates have already expired.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_within_30days_count is not None:
            result['ExpireWithin30DaysCount'] = self.expire_within_30days_count
        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireWithin30DaysCount') is not None:
            self.expire_within_30days_count = m.get('ExpireWithin30DaysCount')
        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserCertificateExpireCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserCertificateExpireCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserCertificateExpireCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserConfigsRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The feature whose configurations you want to query. You can specify only one feature in each request. Valid values: oss, green_manager, waf, cc_rule, ddos_dispatch, edge_safe, blocked_regions, http_acl_policy, bot_manager, and ip_reputation.
        self.config = config
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUserConfigsResponseBodyConfigsOssLogConfig(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        enable: str = None,
        prefix: str = None,
    ):
        # The name of the bucket.
        self.bucket = bucket
        # Indicates whether the OSS bucket is enabled.
        self.enable = enable
        # The prefix.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class DescribeUserConfigsResponseBodyConfigsWafConfig(TeaModel):
    def __init__(
        self,
        enable: str = None,
    ):
        # Indicates whether WAF is enabled.
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeUserConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        oss_log_config: DescribeUserConfigsResponseBodyConfigsOssLogConfig = None,
        waf_config: DescribeUserConfigsResponseBodyConfigsWafConfig = None,
    ):
        # The configurations of Object Storage Service (OSS).
        self.oss_log_config = oss_log_config
        # The configurations of Web Application Firewall (WAF).
        self.waf_config = waf_config

    def validate(self):
        if self.oss_log_config:
            self.oss_log_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_log_config is not None:
            result['OssLogConfig'] = self.oss_log_config.to_map()
        if self.waf_config is not None:
            result['WafConfig'] = self.waf_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssLogConfig') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigsOssLogConfig()
            self.oss_log_config = temp_model.from_map(m['OssLogConfig'])
        if m.get('WafConfig') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigsWafConfig()
            self.waf_config = temp_model.from_map(m['WafConfig'])
        return self


class DescribeUserConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: DescribeUserConfigsResponseBodyConfigs = None,
        request_id: str = None,
    ):
        # The configurations of the specified feature.
        self.configs = configs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['Configs'] = self.configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigs()
            self.configs = temp_model.from_map(m['Configs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserDomainsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of a tag.
        # 
        # By default, all tag keys are queried.
        self.key = key
        # The value of the tag.
        # 
        # By default, all tag values are queried.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeUserDomainsRequest(TeaModel):
    def __init__(
        self,
        cdn_type: str = None,
        change_end_time: str = None,
        change_start_time: str = None,
        check_domain_show: bool = None,
        coverage: str = None,
        domain_name: str = None,
        domain_search_type: str = None,
        domain_status: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        security_token: str = None,
        source: str = None,
        tag: List[DescribeUserDomainsRequestTag] = None,
    ):
        # The type of workload accelerated by Alibaba Cloud CDN. Separate types with commas (,). Valid values:
        # 
        # *   **web**: images and small files
        # *   **download**: large files
        # *   **video**: on-demand video and audio streaming
        # 
        # If you do not set this parameter, all service types are queried.
        self.cdn_type = cdn_type
        # The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.change_end_time = change_end_time
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.change_start_time = change_start_time
        # Specifies whether to display domain names that are under review, failed the review, or failed to be configured. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.check_domain_show = check_domain_show
        # The acceleration region. By default, all acceleration regions are queried. Valid values:
        # 
        # *   **domestic**: Chinese mainland
        # *   **global**: global
        # *   **overseas**: outside the Chinese mainland
        self.coverage = coverage
        # The accelerated domain. If you do not set this parameter, all domain names that match the conditions are returned.
        self.domain_name = domain_name
        # The search mode. Valid values:
        # 
        # *   **fuzzy_match**: fuzzy match
        # *   **pre_match**: prefix match
        # *   **suf_match**: suffix match
        # *   **full_match** (default): exact match
        # 
        # > If you specify the domain names to query but do not set the DomainSearchType parameter, the exact match mode is used.
        self.domain_search_type = domain_search_type
        # The status of the domain name. Valid values:
        # 
        # *   **online**\
        # *   **offline**\
        # *   **configuring**\
        # *   **configure_failed**\
        # *   **checking**\
        # *   **check_failed**\
        # *   **stopping**\
        # *   **deleting**\
        # 
        # If you do not set this parameter, domain names in all states are queried.
        self.domain_status = domain_status
        self.owner_id = owner_id
        # The number of the page to return. Valid values: **1** to **100000**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **1 to 50**. Default value: **20**. Maximum value: **50**.
        self.page_size = page_size
        # The ID of the resource group. By default, all IDs are queried.
        self.resource_group_id = resource_group_id
        self.security_token = security_token
        # The information about the origin server.
        self.source = source
        # The list of tags. Maximum number of elements in the list: 20
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.source is not None:
            result['Source'] = self.source
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(
        self,
        content: str = None,
        port: int = None,
        priority: str = None,
        type: str = None,
        weight: str = None,
    ):
        # The address of the origin server.
        self.content = content
        # The port of the origin server.
        self.port = port
        # The priority.
        self.priority = priority
        # The type of the origin server.
        self.type = type
        # The weight of the origin server if multiple origin servers have been specified.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(
        self,
        cdn_type: str = None,
        cname: str = None,
        coverage: str = None,
        description: str = None,
        domain_id: int = None,
        domain_name: str = None,
        domain_status: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        resource_group_id: str = None,
        sandbox: str = None,
        sources: DescribeUserDomainsResponseBodyDomainsPageDataSources = None,
        ssl_protocol: str = None,
    ):
        # The type of the workload accelerated by Alibaba Cloud CDN. Valid values:
        # 
        # *   **web**: images and small files
        # *   **download**: large files
        # *   **video**: on-demand video and audio streaming
        self.cdn_type = cdn_type
        # The CNAME assigned to the accelerated domain name.
        self.cname = cname
        # The acceleration region. Valid values:
        # 
        # *   **domestic**: Chinese mainland
        # *   **global**: global
        # *   **overseas**: outside the Chinese mainland
        self.coverage = coverage
        # The information about Internet Content Provider (ICP) filing.
        self.description = description
        # The ID of the accelerated domain name.
        self.domain_id = domain_id
        # The accelerated domain.
        self.domain_name = domain_name
        # The status of the accelerated domain name. Valid values:
        # 
        # *   **online**\
        # *   **offline**\
        # *   **configuring**\
        # *   **configure_failed**\
        # *   **checking**\
        # *   **check_failed**\
        # *   **stopping**\
        # *   **deleting**\
        self.domain_status = domain_status
        # The time when the accelerated domain name was added.
        self.gmt_created = gmt_created
        # The time when the accelerated domain name was modified.
        self.gmt_modified = gmt_modified
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether the accelerated domain name is in a sandbox.
        self.sandbox = sandbox
        # The information about the origin server.
        self.sources = sources
        # Indicates whether HTTPS is enabled. Valid values:
        # 
        # *   **on**\
        # *   **off**\
        self.ssl_protocol = ssl_protocol

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('Sources') is not None:
            temp_model = DescribeUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        return self


class DescribeUserDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        page_data: List[DescribeUserDomainsResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = DescribeUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeUserDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domains: DescribeUserDomainsResponseBodyDomains = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of the accelerated domain names returned.
        self.domains = domains
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = DescribeUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUserDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The value of the tag.
        self.key = key
        # The ID of the request.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeUserTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[DescribeUserTagsResponseBodyTags] = None,
    ):
        # The list of tags returned.
        self.request_id = request_id
        # The key of the tag.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeUserTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeUserTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserUsageDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
    ):
        # The name of the task.
        self.page_number = page_number
        # The usage details returned per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # The ID of the request.
        self.end_time = end_time
        # The last time when the task was modified.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        download_url: str = None,
        status: str = None,
        task_config: DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig = None,
        task_id: str = None,
        task_name: str = None,
        update_time: str = None,
    ):
        # The download URL.
        self.create_time = create_time
        # The configurations of the task.
        self.download_url = download_url
        # The time when the task was created.
        self.status = status
        # The total number of entries returned.
        self.task_config = task_config
        # The number of the current page.
        self.task_id = task_id
        # The number of entries to return on each page. Default value: **20**. Maximum value: **50**.
        # 
        # Valid values: **1** to **50**.
        self.task_name = task_name
        # The operation that you want to perform. Set the value to **DescribeUserUsageDataExportTask**.
        self.update_time = update_time

    def validate(self):
        if self.task_config:
            self.task_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.status is not None:
            result['Status'] = self.status
        if self.task_config is not None:
            result['TaskConfig'] = self.task_config.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskConfig') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig()
            self.task_config = temp_model.from_map(m['TaskConfig'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData(TeaModel):
    def __init__(
        self,
        data_item: List[DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem] = None,
    ):
        self.data_item = data_item

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataItem'] = []
        if self.data_item is not None:
            for k in self.data_item:
                result['DataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k in m.get('DataItem'):
                temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem()
                self.data_item.append(temp_model.from_map(k))
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage(TeaModel):
    def __init__(
        self,
        data: DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The status of the task.
        # 
        # *   created: The task is being created.
        # *   success: The task has been created.
        # *   failed: The creation of the task failed.
        self.data = data
        # The number of the page to return. Valid values: **1** to **100000**.
        self.page_number = page_number
        # The description of the task.
        self.page_size = page_size
        # The start of the time range that was queried.
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUserUsageDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_data_per_page: DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage = None,
    ):
        # The ID of the task.
        self.request_id = request_id
        # The end of the time range that was queried.
        self.usage_data_per_page = usage_data_per_page

    def validate(self):
        if self.usage_data_per_page:
            self.usage_data_per_page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usage_data_per_page is not None:
            result['UsageDataPerPage'] = self.usage_data_per_page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsageDataPerPage') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage()
            self.usage_data_per_page = temp_model.from_map(m['UsageDataPerPage'])
        return self


class DescribeUserUsageDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserUsageDataExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserUsageDetailDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
    ):
        # The name of the task.
        self.page_number = page_number
        # The usage details returned per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # refresh
        self.end_time = end_time
        # The ID of the request.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        download_url: str = None,
        status: str = None,
        task_config: DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig = None,
        task_id: str = None,
        task_name: str = None,
        update_time: str = None,
    ):
        # The download URL.
        self.create_time = create_time
        # The configurations of the task.
        self.download_url = download_url
        # The time when the task was created.
        self.status = status
        # The total number of entries returned.
        self.task_config = task_config
        # The number of the page returned.
        self.task_id = task_id
        # The number of entries to return on each page. Default value: **20**. Maximum value: **50**.
        # 
        # Valid values: **1** to **50**.
        self.task_name = task_name
        # The operation that you want to perform. Set the value to **DescribeUserUsageDetailDataExportTask**.
        self.update_time = update_time

    def validate(self):
        if self.task_config:
            self.task_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.status is not None:
            result['Status'] = self.status
        if self.task_config is not None:
            result['TaskConfig'] = self.task_config.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskConfig') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig()
            self.task_config = temp_model.from_map(m['TaskConfig'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData(TeaModel):
    def __init__(
        self,
        data_item: List[DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem] = None,
    ):
        self.data_item = data_item

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataItem'] = []
        if self.data_item is not None:
            for k in self.data_item:
                result['DataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k in m.get('DataItem'):
                temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem()
                self.data_item.append(temp_model.from_map(k))
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage(TeaModel):
    def __init__(
        self,
        data: DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The status of the task.
        self.data = data
        # The number of the page to return. Valid values: **1** to **100000**.
        self.page_number = page_number
        # The description of the task.
        self.page_size = page_size
        # The start of the time range that was queried.
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_data_per_page: DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage = None,
    ):
        # The ID of the task.
        self.request_id = request_id
        # The end of the time range that was queried.
        self.usage_data_per_page = usage_data_per_page

    def validate(self):
        if self.usage_data_per_page:
            self.usage_data_per_page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usage_data_per_page is not None:
            result['UsageDataPerPage'] = self.usage_data_per_page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsageDataPerPage') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage()
            self.usage_data_per_page = temp_model.from_map(m['UsageDataPerPage'])
        return self


class DescribeUserUsageDetailDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserUsageDetailDataExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserVipsByDomainRequest(TeaModel):
    def __init__(
        self,
        available: str = None,
        domain_name: str = None,
    ):
        # The virtual IP address.
        self.available = available
        # A list of virtual IP addresses.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeUserVipsByDomainResponseBodyVips(TeaModel):
    def __init__(
        self,
        vip: List[str] = None,
    ):
        self.vip = vip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vip is not None:
            result['Vip'] = self.vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        return self


class DescribeUserVipsByDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        request_id: str = None,
        vips: DescribeUserVipsByDomainResponseBodyVips = None,
    ):
        # >  The maximum number of times that each user can call this operation per second is 30.
        self.domain_name = domain_name
        # A list of virtual IP addresses.
        self.request_id = request_id
        # The accelerated domain name. You can specify only one domain name.
        self.vips = vips

    def validate(self):
        if self.vips:
            self.vips.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vips is not None:
            result['Vips'] = self.vips.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Vips') is not None:
            temp_model = DescribeUserVipsByDomainResponseBodyVips()
            self.vips = temp_model.from_map(m['Vips'])
        return self


class DescribeUserVipsByDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserVipsByDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserVipsByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyContentRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVerifyContentResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVerifyContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVerifyContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVerifyContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # The accelerated domain name for which you want to disable real-time log delivery. You can specify multiple domain names and separate them with commas (,).
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableRealtimeLogDeliveryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # The accelerated domain name for which you want to enable real-time log delivery. You can specify multiple domain names and separate them with commas (,).
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableRealtimeLogDeliveryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsByLogConfigIdRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
    ):
        # >  The maximum number of times that each user can call this operation per second is 100.
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class ListDomainsByLogConfigIdResponseBodyDomains(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
    ):
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class ListDomainsByLogConfigIdResponseBody(TeaModel):
    def __init__(
        self,
        domains: ListDomainsByLogConfigIdResponseBodyDomains = None,
        request_id: str = None,
    ):
        # The ID of the request.
        self.domains = domains
        # The ID of the custom configuration.
        self.request_id = request_id

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = ListDomainsByLogConfigIdResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDomainsByLogConfigIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDomainsByLogConfigIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDomainsByLogConfigIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFCTriggerRequest(TeaModel):
    def __init__(
        self,
        event_meta_name: str = None,
        event_meta_version: str = None,
    ):
        # The name of the event. You can specify only one name.
        self.event_meta_name = event_meta_name
        # The version number of the event. You can specify only one version number.
        self.event_meta_version = event_meta_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        return self


class ListFCTriggerResponseBodyFCTriggers(TeaModel):
    def __init__(
        self,
        event_meta_name: str = None,
        event_meta_version: str = None,
        notes: str = None,
        role_arn: str = None,
        source_arn: str = None,
        trigger_arn: str = None,
    ):
        # The name of the event.
        self.event_meta_name = event_meta_name
        # The version of the event.
        self.event_meta_version = event_meta_version
        # The remarks.
        self.notes = notes
        # The Resource Access Management (RAM) role.
        self.role_arn = role_arn
        # The resources and filters for event listening.
        self.source_arn = source_arn
        # The trigger that corresponds to the Function Compute service.
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class ListFCTriggerResponseBody(TeaModel):
    def __init__(
        self,
        fctriggers: List[ListFCTriggerResponseBodyFCTriggers] = None,
        request_id: str = None,
    ):
        # The Function Compute triggers that are set for Alibaba Cloud CDN events.
        self.fctriggers = fctriggers
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.fctriggers:
            for k in self.fctriggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FCTriggers'] = []
        if self.fctriggers is not None:
            for k in self.fctriggers:
                result['FCTriggers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fctriggers = []
        if m.get('FCTriggers') is not None:
            for k in m.get('FCTriggers'):
                temp_model = ListFCTriggerResponseBodyFCTriggers()
                self.fctriggers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFCTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRealtimeLogDeliveryDomainsRequest(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region: str = None,
    ):
        # The name of the Logstore that collects log data from Alibaba Cloud CDN in real time. You can specify multiple Logstore names and separate them with commas (,).
        self.logstore = logstore
        # The name of the Log Service project that is used for real-time log delivery. You can specify multiple project names and separate them with commas (,).
        self.project = project
        # The ID of the region where the Log Service project is deployed. You can specify multiple region IDs and separate them with commas (,).
        # 
        # For more information about regions, see [Regions that support real-time log delivery](~~144883~~).
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ListRealtimeLogDeliveryDomainsResponseBodyContentDomains(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        status: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The status. Valid values:
        # 
        # *   **online**: enabled
        # *   **offline**: disabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListRealtimeLogDeliveryDomainsResponseBodyContent(TeaModel):
    def __init__(
        self,
        domains: List[ListRealtimeLogDeliveryDomainsResponseBodyContentDomains] = None,
    ):
        self.domains = domains

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = ListRealtimeLogDeliveryDomainsResponseBodyContentDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class ListRealtimeLogDeliveryDomainsResponseBody(TeaModel):
    def __init__(
        self,
        content: ListRealtimeLogDeliveryDomainsResponseBodyContent = None,
        request_id: str = None,
    ):
        # The information about the accelerated domain names.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = ListRealtimeLogDeliveryDomainsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRealtimeLogDeliveryDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRealtimeLogDeliveryDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRealtimeLogDeliveryDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region: str = None,
    ):
        # The name of the Logstore that collects log data from Alibaba Cloud CDN in real time.
        self.logstore = logstore
        # The name of the Log Service project that is used for real-time log delivery.
        self.project = project
        # The ID of the region where the Log Service project is deployed. For more information, see [Regions that support real-time log delivery](~~144883~~).
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ListRealtimeLogDeliveryInfosResponseBodyContent(TeaModel):
    def __init__(
        self,
        realtime_log_delivery_infos: List[ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos] = None,
    ):
        self.realtime_log_delivery_infos = realtime_log_delivery_infos

    def validate(self):
        if self.realtime_log_delivery_infos:
            for k in self.realtime_log_delivery_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RealtimeLogDeliveryInfos'] = []
        if self.realtime_log_delivery_infos is not None:
            for k in self.realtime_log_delivery_infos:
                result['RealtimeLogDeliveryInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.realtime_log_delivery_infos = []
        if m.get('RealtimeLogDeliveryInfos') is not None:
            for k in m.get('RealtimeLogDeliveryInfos'):
                temp_model = ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos()
                self.realtime_log_delivery_infos.append(temp_model.from_map(k))
        return self


class ListRealtimeLogDeliveryInfosResponseBody(TeaModel):
    def __init__(
        self,
        content: ListRealtimeLogDeliveryInfosResponseBodyContent = None,
        request_id: str = None,
    ):
        # The information about real-time log delivery.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = ListRealtimeLogDeliveryInfosResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRealtimeLogDeliveryInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRealtimeLogDeliveryInfosResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRealtimeLogDeliveryInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserCustomLogConfigResponseBodyConfigIds(TeaModel):
    def __init__(
        self,
        config_id: List[str] = None,
    ):
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class ListUserCustomLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        config_ids: ListUserCustomLogConfigResponseBodyConfigIds = None,
        request_id: str = None,
    ):
        # The ID of the request.
        self.config_ids = config_ids
        # The ID of the log configuration.
        self.request_id = request_id

    def validate(self):
        if self.config_ids:
            self.config_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_ids is not None:
            result['ConfigIds'] = self.config_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigIds') is not None:
            temp_model = ListUserCustomLogConfigResponseBodyConfigIds()
            self.config_ids = temp_model.from_map(m['ConfigIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserCustomLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserCustomLogConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCdnDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        security_token: str = None,
        sources: str = None,
        top_level_domain: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name in each request.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.security_token = security_token
        # The information about the addresses of origin servers.
        # 
        # > Do not set **Sources** and **TopLevelDomain** at the same time. If you set **Sources** and **TopLevelDomain** at the same time, **TopLevelDomain** does not take effect.
        self.sources = sources
        # The root domain. To add a root domain name, you must be added to the whitelist specified by the CDN_TOP_LEVEL_DOMAIN_GREY_USER_LIST parameter.
        # 
        # > Do not set **Sources** and **TopLevelDomain** at the same time. If you set **Sources** and **TopLevelDomain** at the same time, **TopLevelDomain** does not take effect.
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class ModifyCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCdnDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCdnDomainSchdmByPropertyRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        property: str = None,
    ):
        # The operation that you want to perform. Set the value to **ModifyCdnDomainSchdmByProperty**.
        self.domain_name = domain_name
        # The accelerated region. Valid values for coverage:
        # 
        # *   **domestic**: Chinese mainland
        # *   **overseas**: global (excluding the Chinese mainland)
        # *   **global**: global
        self.property = property

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.property is not None:
            result['Property'] = self.property
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        return self


class ModifyCdnDomainSchdmByPropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCdnDomainSchdmByPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCdnDomainSchdmByPropertyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyCdnDomainSchdmByPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        logstore: str = None,
        project: str = None,
        region: str = None,
    ):
        # The ID of the request.
        self.domain = domain
        # The accelerated domain name for which you want to modify the configurations of real-time log delivery. Only one domain name is supported.
        self.logstore = logstore
        # The ID of the region where the Log Service project is deployed. For more information, see [Regions that support real-time log delivery](~~144883~~).
        self.project = project
        # The name of the Log Service project that is used for real-time log delivery.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ModifyRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The operation that you want to perform. Set the value to **ModifyRealtimeLogDelivery**.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyRealtimeLogDeliveryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCdnServiceRequest(TeaModel):
    def __init__(
        self,
        internet_charge_type: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The metering method of Alibaba Cloud CDN. A value of **PayByTraffic** indicates that the metering method is pay-by-data-transfer.
        self.internet_charge_type = internet_charge_type
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class OpenCdnServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenCdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenCdnServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenCdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishStagingConfigToProductionRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class PublishStagingConfigToProductionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishStagingConfigToProductionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishStagingConfigToProductionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishStagingConfigToProductionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushObjectCacheRequest(TeaModel):
    def __init__(
        self,
        area: str = None,
        l_2preload: bool = None,
        object_path: str = None,
        owner_id: int = None,
        security_token: str = None,
        with_header: str = None,
    ):
        # The accelerated region where content is to be prefetched. Valid values:
        # 
        # *   **domestic****: Chinese mainland**\
        # *   **overseas****: regions outside the Chinese mainland**\
        # 
        # If you do not set this parameter, content in the accelerated region of the domain name is prefetched.
        # 
        # *   If the accelerated region is set to **Mainland China Only**, content in regions in the Chinese mainland is prefetched.
        # *   If the accelerated region is set to **Global**, content in all regions is prefetched.
        # *   If the accelerated region is set to **Global (Excluding Mainland China)**, content in regions outside the Chinese mainland is prefetched.
        self.area = area
        # Specifies whether to prefetch content to POPs. Valid values:
        # 
        # *   **true**: prefetches content to POPs.
        # *   **false**: prefetches content to regular POPs. Regular POPs can be L2 POPs or L3 POPs. Default value: **false**.
        self.l_2preload = l_2preload
        # The URLs based on which content is prefetched. Format: **accelerated domain name/files to be prefetched**.
        # 
        # > Separate URLs with line feeds (\n or \r\n). Each object path can be up to 1,024 characters in length.
        self.object_path = object_path
        self.owner_id = owner_id
        self.security_token = security_token
        # The custom header for prefetch in the JSON format.
        self.with_header = with_header

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.l_2preload is not None:
            result['L2Preload'] = self.l_2preload
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.with_header is not None:
            result['WithHeader'] = self.with_header
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('L2Preload') is not None:
            self.l_2preload = m.get('L2Preload')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('WithHeader') is not None:
            self.with_header = m.get('WithHeader')
        return self


class PushObjectCacheResponseBody(TeaModel):
    def __init__(
        self,
        push_task_id: str = None,
        request_id: str = None,
    ):
        # The ID of the prefetch task. If multiple tasks are returned, the IDs are separated by commas (,). The task IDs are merged based on the following rules:
        # 
        # *   If the tasks are set for the same accelerated domain name, submitted within the same second, and prefetch content from URLs instead of directories, the tasks IDs are merged into the same task ID (RushTaskId).
        # *   If the number of tasks that are set for the same accelerated domain name, submitted within the same second, and prefetch content from URLs instead of directories exceeds 500, every 500 task IDs are merged into the same task ID (RushTaskId).
        self.push_task_id = push_task_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_task_id is not None:
            result['PushTaskId'] = self.push_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushTaskId') is not None:
            self.push_task_id = m.get('PushTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushObjectCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushObjectCacheResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushObjectCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshObjectCachesRequest(TeaModel):
    def __init__(
        self,
        object_path: str = None,
        object_type: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.object_path = object_path
        self.object_type = object_type
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RefreshObjectCachesResponseBody(TeaModel):
    def __init__(
        self,
        refresh_task_id: str = None,
        request_id: str = None,
    ):
        self.refresh_task_id = refresh_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_task_id is not None:
            result['RefreshTaskId'] = self.refresh_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshTaskId') is not None:
            self.refresh_task_id = m.get('RefreshTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshObjectCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshObjectCachesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RefreshObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackStagingConfigRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # The ID of the request.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class RollbackStagingConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The operation that you want to perform. Set the value to **RollbackStagingConfig**.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RollbackStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RollbackStagingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RollbackStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCdnDomainCSRCertificateRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        server_certificate: str = None,
    ):
        # The ID of the request.
        self.domain_name = domain_name
        # The content of the certificate. The certificate must match the certificate signing request (CSR) created by calling the [CreateCdnCertificateSigningRequest](~~144478~~) operation. Make sure that the certificate is in the PEM format, and the content of the certificate is encoded in Base64 and then encoded by encodeURIComponent.
        self.server_certificate = server_certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        return self


class SetCdnDomainCSRCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The operation that you want to perform. Set the value to **SetCdnDomainCSRCertificate**.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetCdnDomainCSRCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetCdnDomainCSRCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetCdnDomainCSRCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCdnDomainSMCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        domain_name: str = None,
        owner_id: int = None,
        sslprotocol: str = None,
        security_token: str = None,
    ):
        # The ID of the SM certificate that you want to configure. The identifier of the certificate. The value is Certificate ID-cn-hangzhou. For example, if the certificate ID is 123, set the value of this parameter to 123-cn-hangzhou.
        self.cert_identifier = cert_identifier
        # The accelerated domain name for which you want to configure the SM certificate.
        # 
        # > The domain name must use HTTPS acceleration.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # Specifies whether to enable the SSL certificate. Valid values:
        # 
        # *   **on**\
        # *   **off**\
        self.sslprotocol = sslprotocol
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetCdnDomainSMCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetCdnDomainSMCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetCdnDomainSMCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetCdnDomainSMCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCdnDomainSSLCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_id: int = None,
        cert_name: str = None,
        cert_region: str = None,
        cert_type: str = None,
        domain_name: str = None,
        owner_id: int = None,
        sslpri: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        security_token: str = None,
    ):
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.cert_region = cert_region
        self.cert_type = cert_type
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.sslpri = sslpri
        self.sslprotocol = sslprotocol
        self.sslpub = sslpub
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetCdnDomainSSLCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetCdnDomainSSLCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetCdnDomainSSLCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetCdnDomainSSLCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCdnDomainStagingConfigRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        functions: str = None,
    ):
        self.domain_name = domain_name
        self.functions = functions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.functions is not None:
            result['Functions'] = self.functions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        return self


class SetCdnDomainStagingConfigResponseBodyDomainConfigList(TeaModel):
    def __init__(
        self,
        config_id: int = None,
        domain_name: str = None,
        function_name: str = None,
    ):
        self.config_id = config_id
        self.domain_name = domain_name
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class SetCdnDomainStagingConfigResponseBody(TeaModel):
    def __init__(
        self,
        domain_config_list: List[SetCdnDomainStagingConfigResponseBodyDomainConfigList] = None,
        request_id: str = None,
    ):
        self.domain_config_list = domain_config_list
        self.request_id = request_id

    def validate(self):
        if self.domain_config_list:
            for k in self.domain_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfigList'] = []
        if self.domain_config_list is not None:
            for k in self.domain_config_list:
                result['DomainConfigList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_config_list = []
        if m.get('DomainConfigList') is not None:
            for k in m.get('DomainConfigList'):
                temp_model = SetCdnDomainStagingConfigResponseBodyDomainConfigList()
                self.domain_config_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetCdnDomainStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetCdnDomainStagingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetCdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainServerCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_type: str = None,
        domain_name: str = None,
        force_set: str = None,
        owner_id: int = None,
        private_key: str = None,
        security_token: str = None,
        server_certificate: str = None,
        server_certificate_status: str = None,
    ):
        # Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate that uses the same name.
        self.cert_name = cert_name
        # The ID of the request.
        self.cert_type = cert_type
        # The private key. Specify the private key only if you want to enable the SSL certificate.
        self.domain_name = domain_name
        # Specifies whether to enable the SSL certificate. Valid values:
        # 
        # *   **on**: enables the SSL certificate.
        # *   **off**: disables the SSL certificate. This is the default value.
        self.force_set = force_set
        self.owner_id = owner_id
        # Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate that uses the same name.
        self.private_key = private_key
        self.security_token = security_token
        # The type of the SSL certificate. Valid values:
        # 
        # *   **upload**: a user-uploaded SSL certificate.
        # *   **cas**: an SSL certificate that is issued by Alibaba Cloud SSL Certificates Service.
        # *   **free**: a free SSL certificate.
        # 
        # >  If this parameter is set to **cas**, the **PrivateKey** parameter is optional.
        self.server_certificate = server_certificate
        # The name of the SSL certificate. You can specify only one name.
        self.server_certificate_status = server_certificate_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.force_set is not None:
            result['ForceSet'] = self.force_set
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        return self


class SetDomainServerCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDomainServerCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDomainServerCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetDomainServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetReqHeaderConfigRequest(TeaModel):
    def __init__(
        self,
        config_id: int = None,
        domain_name: str = None,
        key: str = None,
        owner_id: int = None,
        security_token: str = None,
        value: str = None,
    ):
        # The ID of the configuration.
        self.config_id = config_id
        # The accelerated domain name. Separate multiple domain names with commas (,).
        self.domain_name = domain_name
        # The name of the custom header.
        self.key = key
        self.owner_id = owner_id
        self.security_token = security_token
        # The value of the custom header.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key is not None:
            result['Key'] = self.key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetReqHeaderConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetReqHeaderConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetReqHeaderConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetReqHeaderConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetWaitingRoomConfigRequest(TeaModel):
    def __init__(
        self,
        allow_pct: int = None,
        domain_name: str = None,
        gap_time: int = None,
        max_time_wait: int = None,
        wait_uri: str = None,
        wait_url: str = None,
    ):
        # The percentage of requests that are allowed to be redirected to the origin server. Valid values: **0** to **100**.
        self.allow_pct = allow_pct
        # The accelerated domain name. You can specify only one domain name.
        self.domain_name = domain_name
        # The length of waiting time to skip after an exit from the queue. Unit: seconds.
        self.gap_time = gap_time
        # The maximum length of waiting time in the queue. Unit: seconds.
        self.max_time_wait = max_time_wait
        # The regular expression that is used to match URI strings for which the virtual waiting room feature is enabled.
        self.wait_uri = wait_uri
        # The URL of the waiting page.
        self.wait_url = wait_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_pct is not None:
            result['AllowPct'] = self.allow_pct
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gap_time is not None:
            result['GapTime'] = self.gap_time
        if self.max_time_wait is not None:
            result['MaxTimeWait'] = self.max_time_wait
        if self.wait_uri is not None:
            result['WaitUri'] = self.wait_uri
        if self.wait_url is not None:
            result['WaitUrl'] = self.wait_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPct') is not None:
            self.allow_pct = m.get('AllowPct')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GapTime') is not None:
            self.gap_time = m.get('GapTime')
        if m.get('MaxTimeWait') is not None:
            self.max_time_wait = m.get('MaxTimeWait')
        if m.get('WaitUri') is not None:
            self.wait_uri = m.get('WaitUri')
        if m.get('WaitUrl') is not None:
            self.wait_url = m.get('WaitUrl')
        return self


class SetWaitingRoomConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetWaitingRoomConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetWaitingRoomConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetWaitingRoomConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCdnDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name in each request.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class StartCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartCdnDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCdnDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The accelerated domain name that you want to disable. You can specify only one domain name in each request.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class StopCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopCdnDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The ID of the request.
        self.key = key
        # The operation that you want to perform. Set the value to **TagResources**.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The ID of the resource. Valid values of N: **1** to **50**.
        self.resource_id = resource_id
        # >  The maximum number of times that each user can call this operation per second is 100.
        self.resource_type = resource_type
        # The type of resource. The resource type. Set the value to **DOMAIN**.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Adds tags to a resource.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # The operation that you want to perform. Set the value to **UntagResources**.
        self.all = all
        # Removes tags from a resource.
        self.resource_id = resource_id
        # The ID of the request.
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCdnDeliverTaskRequest(TeaModel):
    def __init__(
        self,
        deliver: str = None,
        deliver_id: int = None,
        domain_name: str = None,
        name: str = None,
        reports: str = None,
        schedule: str = None,
    ):
        # \[{\\"reportId\\":1,\\"conditions\\":\[{\\"field\\":\\"prov\\",\\"op\\":\\"in\\",\\"value\\":\[\\"Heilongjiang\\",\\"Beijing\\"]}]}]
        self.deliver = deliver
        # > You can call this operation up to three times per second per account.
        self.deliver_id = deliver_id
        # The operations reports that are tracked by the task. The data must be escaped in JSON.
        self.domain_name = domain_name
        # **Fields in the ReDatas parameter**\
        # 
        # |Field|Type|Required|Description|
        # |---|---|---|---|
        # |reportId|String|Yes|The ID of the report.|
        # |conditions|ConDatas\[\]|No|The filter conditions for the report.|
        # 
        # **Fields in the ConDatas parameter**\
        # 
        # |Field|Type|Required|Description|
        # |---|---|---|---|
        # |field|String|No|The filter field.|
        # |op|String|No|The filter operation.|
        # |value|String\[\]|No|The array of field values.|
        # 
        # 
        # **Fields in the email parameter**\
        # 
        # |Field|Type|Required|Description|
        # |---|---|---|---|
        # |subject|String|Yes|The email subject.|
        # |to|String\[\]|Yes|The email addresses to which operations reports are sent.|
        # 
        # 
        # **Fields in the Deliver parameter**\
        # 
        # |Field|Type|Required|Description|
        # |---|---|---|---|
        # |subject|String|No|The email subject.|
        # |to|String\[\]|Yes|The email addresses to which operations reports are sent.|
        # 
        # 
        # **Fields in the Schedule parameter**\
        # 
        # |Field|Type|Required|Description|
        # |---|---|---|---|
        # |schedName|String|No|The name of the tracking task.|
        # |description|String|No|The description of the tracking task.|
        # |crontab|String|Yes|Specifies the cycle in which the tracking task is scheduled to run.|
        # |frequency|String|Yes|The interval at which the reports are sent. Valid values:<br />**h**: by hour<br />**d**: by day<br />**w**: by week|
        # |status|String|No|The status of the tracking task. Valid values:<br />**enable**<br />**disable**|
        # |effectiveFrom|String|No|The start time of the tracking task.|
        # |effectiveEnd|String|No|The end time of the tracking task.|
        self.name = name
        # The name of the tracking task.
        self.reports = reports
        # The method that is used to send operations reports. Operations reports are sent to you only by email. The settings must be escaped in JSON.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deliver is not None:
            result['Deliver'] = self.deliver
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.name is not None:
            result['Name'] = self.name
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class UpdateCdnDeliverTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The parameters that specify the time interval at which the tracking task sends operations reports. The settings must be escaped in JSON.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCdnDeliverTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCdnDeliverTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCdnSubTaskRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        report_ids: str = None,
        start_time: str = None,
    ):
        # The ID of the request.
        self.domain_name = domain_name
        # The domain names that you want to track. You can specify multiple domain names and separate them with commas (,). You can specify at most 500 domain names in each call.
        # 
        # If you do not specify a domain name, the task collects data from all domain names that belong to your Alibaba Cloud account.
        self.end_time = end_time
        # The IDs of operations reports that you want to update. Separate IDs with commas (,).
        self.report_ids = report_ids
        # The operation that you want to perform. Set the value to **UpdateCdnSubTask**.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class UpdateCdnSubTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCdnSubTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCdnSubTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFCTriggerRequest(TeaModel):
    def __init__(
        self,
        function_arn: str = None,
        notes: str = None,
        role_arn: str = None,
        source_arn: str = None,
        trigger_arn: str = None,
    ):
        # The feature trigger.
        self.function_arn = function_arn
        # The remarks.
        self.notes = notes
        # The assigned RAM role.
        self.role_arn = role_arn
        # The resources and filters for event listening.
        self.source_arn = source_arn
        # The trigger that corresponds to the Function Compute service.
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_arn is not None:
            result['FunctionARN'] = self.function_arn
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceARN'] = self.source_arn
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionARN') is not None:
            self.function_arn = m.get('FunctionARN')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceARN') is not None:
            self.source_arn = m.get('SourceARN')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class UpdateFCTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFCTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyDomainOwnerRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        global_resource_plan: str = None,
        verify_type: str = None,
    ):
        self.domain_name = domain_name
        self.global_resource_plan = global_resource_plan
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.global_resource_plan is not None:
            result['GlobalResourcePlan'] = self.global_resource_plan
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GlobalResourcePlan') is not None:
            self.global_resource_plan = m.get('GlobalResourcePlan')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class VerifyDomainOwnerResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyDomainOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyDomainOwnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


