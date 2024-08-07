# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from pydantic import validate_call, StrictFloat
from typing import Dict, Tuple, Union

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from cobo_waas2.models.get_token200_response import GetToken200Response
from cobo_waas2.models.refresh_token_request import RefreshTokenRequest

from cobo_waas2.api_client import ApiClient, RequestSerialized
from cobo_waas2.api_response import ApiResponse
from cobo_waas2.rest import RESTResponseType


class OAuthApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client: ApiClient = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_token(
        self,
        client_id: Annotated[StrictStr, Field(description="The App ID, a unique identifier to distinguish Cobo Portal Apps. You can get the App ID by retrieving the Manifest file after receiving the notification of app launch approval.")],
        org_id: Annotated[StrictStr, Field(description="Org ID, a unique identifier to distinguish different organizations. You can get the Org ID by retrieving the Manifest file after receiving the notification of app launch approval.")],
        grant_type: Annotated[StrictStr, Field(description="The type of the permission granting. To get an access token, you need to set the value as `org_implicit`.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> GetToken200Response:
        """Get Access Token

        <Note>This operation is only applicable to Cobo Portal App developers. To call this operation, you need to use the OAuth authentication method that requires an App Key.</Note> This operation allows Cobo Portal Apps to get an access token and a refresh token with a specified App ID, Org ID, and grant type.   Access tokens allow the app to signal to the WaaS service that it has received permission from the organization admin to access specific resources. Once the app has been granted permission by an organization admin, it can use this operation to obtain both an access token and a refresh token.  For security purposes, access tokens expire after a certain period. Once they expire, the app need to [Refresh token](/v2/api-references/oauth/refresh-access-token) to get a new access token and a new fresh token. 

        :param client_id: The App ID, a unique identifier to distinguish Cobo Portal Apps. You can get the App ID by retrieving the Manifest file after receiving the notification of app launch approval. (required)
        :type client_id: str
        :param org_id: Org ID, a unique identifier to distinguish different organizations. You can get the Org ID by retrieving the Manifest file after receiving the notification of app launch approval. (required)
        :type org_id: str
        :param grant_type: The type of the permission granting. To get an access token, you need to set the value as `org_implicit`. (required)
        :type grant_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_token_serialize(
            client_id=client_id,
            org_id=org_id,
            grant_type=grant_type,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetToken200Response",
            '4XX': "GetToken4XXResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_token_with_http_info(
        self,
        client_id: Annotated[StrictStr, Field(description="The App ID, a unique identifier to distinguish Cobo Portal Apps. You can get the App ID by retrieving the Manifest file after receiving the notification of app launch approval.")],
        org_id: Annotated[StrictStr, Field(description="Org ID, a unique identifier to distinguish different organizations. You can get the Org ID by retrieving the Manifest file after receiving the notification of app launch approval.")],
        grant_type: Annotated[StrictStr, Field(description="The type of the permission granting. To get an access token, you need to set the value as `org_implicit`.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> ApiResponse[GetToken200Response]:
        """Get Access Token

        <Note>This operation is only applicable to Cobo Portal App developers. To call this operation, you need to use the OAuth authentication method that requires an App Key.</Note> This operation allows Cobo Portal Apps to get an access token and a refresh token with a specified App ID, Org ID, and grant type.   Access tokens allow the app to signal to the WaaS service that it has received permission from the organization admin to access specific resources. Once the app has been granted permission by an organization admin, it can use this operation to obtain both an access token and a refresh token.  For security purposes, access tokens expire after a certain period. Once they expire, the app need to [Refresh token](/v2/api-references/oauth/refresh-access-token) to get a new access token and a new fresh token. 

        :param client_id: The App ID, a unique identifier to distinguish Cobo Portal Apps. You can get the App ID by retrieving the Manifest file after receiving the notification of app launch approval. (required)
        :type client_id: str
        :param org_id: Org ID, a unique identifier to distinguish different organizations. You can get the Org ID by retrieving the Manifest file after receiving the notification of app launch approval. (required)
        :type org_id: str
        :param grant_type: The type of the permission granting. To get an access token, you need to set the value as `org_implicit`. (required)
        :type grant_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_token_serialize(
            client_id=client_id,
            org_id=org_id,
            grant_type=grant_type,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetToken200Response",
            '4XX': "GetToken4XXResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_token_without_preload_content(
        self,
        client_id: Annotated[StrictStr, Field(description="The App ID, a unique identifier to distinguish Cobo Portal Apps. You can get the App ID by retrieving the Manifest file after receiving the notification of app launch approval.")],
        org_id: Annotated[StrictStr, Field(description="Org ID, a unique identifier to distinguish different organizations. You can get the Org ID by retrieving the Manifest file after receiving the notification of app launch approval.")],
        grant_type: Annotated[StrictStr, Field(description="The type of the permission granting. To get an access token, you need to set the value as `org_implicit`.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> RESTResponseType:
        """Get Access Token

        <Note>This operation is only applicable to Cobo Portal App developers. To call this operation, you need to use the OAuth authentication method that requires an App Key.</Note> This operation allows Cobo Portal Apps to get an access token and a refresh token with a specified App ID, Org ID, and grant type.   Access tokens allow the app to signal to the WaaS service that it has received permission from the organization admin to access specific resources. Once the app has been granted permission by an organization admin, it can use this operation to obtain both an access token and a refresh token.  For security purposes, access tokens expire after a certain period. Once they expire, the app need to [Refresh token](/v2/api-references/oauth/refresh-access-token) to get a new access token and a new fresh token. 

        :param client_id: The App ID, a unique identifier to distinguish Cobo Portal Apps. You can get the App ID by retrieving the Manifest file after receiving the notification of app launch approval. (required)
        :type client_id: str
        :param org_id: Org ID, a unique identifier to distinguish different organizations. You can get the Org ID by retrieving the Manifest file after receiving the notification of app launch approval. (required)
        :type org_id: str
        :param grant_type: The type of the permission granting. To get an access token, you need to set the value as `org_implicit`. (required)
        :type grant_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_token_serialize(
            client_id=client_id,
            org_id=org_id,
            grant_type=grant_type,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetToken200Response",
            '4XX': "GetToken4XXResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_token_serialize(
        self,
        client_id,
        org_id,
        grant_type,
    ) -> RequestSerialized:
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if client_id is not None:
            
            _query_params.append(('client_id', client_id))
            
        if org_id is not None:
            
            _query_params.append(('org_id', org_id))
            
        if grant_type is not None:
            
            _query_params.append(('grant_type', grant_type))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/oauth/token',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
        )

    @validate_call
    def refresh_token(
        self,
        refresh_token_request: Annotated[RefreshTokenRequest, Field(description="The request body for refreshing an access token.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> GetToken200Response:
        """Refresh Access Token

        <Note>This operation is only applicable to Cobo Portal Apps developers. To call this operation, you need to use the OAuth authentication method that requires an App Key.</Note> This operation allows Cobo Portal Apps to obtain a new access token with a specified App ID, grant type and a refresh token. For security purposes, access tokens expire after a certain period. Once they expire, the app need to use this operation to get a new access token and a new fresh token. 

        :param refresh_token_request: The request body for refreshing an access token. (required)
        :type refresh_token_request: RefreshTokenRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._refresh_token_serialize(
            refresh_token_request=refresh_token_request,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetToken200Response",
            '4XX': "GetToken4XXResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def refresh_token_with_http_info(
        self,
        refresh_token_request: Annotated[RefreshTokenRequest, Field(description="The request body for refreshing an access token.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> ApiResponse[GetToken200Response]:
        """Refresh Access Token

        <Note>This operation is only applicable to Cobo Portal Apps developers. To call this operation, you need to use the OAuth authentication method that requires an App Key.</Note> This operation allows Cobo Portal Apps to obtain a new access token with a specified App ID, grant type and a refresh token. For security purposes, access tokens expire after a certain period. Once they expire, the app need to use this operation to get a new access token and a new fresh token. 

        :param refresh_token_request: The request body for refreshing an access token. (required)
        :type refresh_token_request: RefreshTokenRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._refresh_token_serialize(
            refresh_token_request=refresh_token_request,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetToken200Response",
            '4XX': "GetToken4XXResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def refresh_token_without_preload_content(
        self,
        refresh_token_request: Annotated[RefreshTokenRequest, Field(description="The request body for refreshing an access token.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> RESTResponseType:
        """Refresh Access Token

        <Note>This operation is only applicable to Cobo Portal Apps developers. To call this operation, you need to use the OAuth authentication method that requires an App Key.</Note> This operation allows Cobo Portal Apps to obtain a new access token with a specified App ID, grant type and a refresh token. For security purposes, access tokens expire after a certain period. Once they expire, the app need to use this operation to get a new access token and a new fresh token. 

        :param refresh_token_request: The request body for refreshing an access token. (required)
        :type refresh_token_request: RefreshTokenRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._refresh_token_serialize(
            refresh_token_request=refresh_token_request,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetToken200Response",
            '4XX': "GetToken4XXResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response

    def _refresh_token_serialize(
        self,
        refresh_token_request,
    ) -> RequestSerialized:
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if refresh_token_request is not None:
            _body_params = refresh_token_request

        # set the HTTP header `Accept`
        _header_params = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/oauth/token',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
        )
