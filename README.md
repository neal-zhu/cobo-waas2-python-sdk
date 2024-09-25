# cobo-waas2-python-sdk
The Cobo Wallet-as-a-Service (WaaS) 2.0 API is the latest version of Cobo’s WaaS API offering. It enables you to access Cobo’s full suite of crypto wallet technologies with powerful and flexible access controls. By encapsulating complex security protocols and streamlining blockchain interactions, this API allows you to concentrate on your core business activities without worrying about the safety of your assets. The WaaS 2.0 API presents the following key features:

- A unified API for Cobo’s [all four wallet types](https://manuals.cobo.com/en/portal/introduction#an-all-in-one-wallet-platform)
- Support for 80+ chains and 3000+ tokens
- A comprehensive selection of webhook events
- Flexible usage models for MPC Wallets, including [Organization-Controlled Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/introduction) and [User-Controlled Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/ucw/introduction)
- Programmatic control of smart contract wallets such as Safe{Wallet} with fine-grained access controls
- Seamlessly transfer funds across multiple exchanges, including Binance, OKX, Bybit, Deribit, and more

For more information about the WaaS 2.0 API, see [Introduction to WaaS 2.0](https://www.cobo.com/developers/v2/guides/overview/introduction).


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2
- Package version: 1.4.0
- Generator version: 7.6.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.cobo.com/waas](https://www.cobo.com/waas)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

```sh
pip install cobo-waas2==1.4.0
```

Then import the package:
```python
import cobo_waas2
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import cobo_waas2
from pprint import pprint
# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)

# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_type = cobo_waas2.WalletType.CUSTODIAL
    wallet_subtype = cobo_waas2.WalletSubtype.ASSET
    chain_ids = 'BTC,ETH'
    limit = 10
    before = ''
    after = ''

    try:
        # List supported chains
        api_response = api_instance.list_supported_chains(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_supported_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_supported_chains: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.dev.cobo.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DevelopersWebhooksApi* | [**create_webhook_endpoint**](docs/DevelopersWebhooksApi.md#create_webhook_endpoint) | **POST** /webhooks/endpoints | Register webhook endpoint
*DevelopersWebhooksApi* | [**get_webhook_endpoint_by_id**](docs/DevelopersWebhooksApi.md#get_webhook_endpoint_by_id) | **GET** /webhooks/endpoints/{endpoint_id} | Get webhook endpoint information
*DevelopersWebhooksApi* | [**get_webhook_event_by_id**](docs/DevelopersWebhooksApi.md#get_webhook_event_by_id) | **GET** /webhooks/endpoints/{endpoint_id}/events/{event_id} | Retrieve event information
*DevelopersWebhooksApi* | [**list_webhook_endpoints**](docs/DevelopersWebhooksApi.md#list_webhook_endpoints) | **GET** /webhooks/endpoints | List webhook endpoints
*DevelopersWebhooksApi* | [**list_webhook_event_definitions**](docs/DevelopersWebhooksApi.md#list_webhook_event_definitions) | **GET** /webhooks/events/definitions | Get webhook event types
*DevelopersWebhooksApi* | [**list_webhook_event_logs**](docs/DevelopersWebhooksApi.md#list_webhook_event_logs) | **GET** /webhooks/endpoints/{endpoint_id}/events/{event_id}/logs | List webhook event logs
*DevelopersWebhooksApi* | [**list_webhook_events**](docs/DevelopersWebhooksApi.md#list_webhook_events) | **GET** /webhooks/endpoints/{endpoint_id}/events | List all webhook events
*DevelopersWebhooksApi* | [**retry_webhook_event_by_id**](docs/DevelopersWebhooksApi.md#retry_webhook_event_by_id) | **POST** /webhooks/endpoints/{endpoint_id}/events/{event_id}/retry | Retry event
*DevelopersWebhooksApi* | [**update_webhook_endpoint_by_id**](docs/DevelopersWebhooksApi.md#update_webhook_endpoint_by_id) | **PUT** /webhooks/endpoints/{endpoint_id} | Update webhook endpoint
*OAuthApi* | [**get_token**](docs/OAuthApi.md#get_token) | **GET** /oauth/token | Get Org Access Token
*OAuthApi* | [**refresh_token**](docs/OAuthApi.md#refresh_token) | **POST** /oauth/token | Refresh Org Access Token
*StakingsApi* | [**create_stake_activity**](docs/StakingsApi.md#create_stake_activity) | **POST** /stakings/activities/stake | Create stake activity
*StakingsApi* | [**create_unstake_activity**](docs/StakingsApi.md#create_unstake_activity) | **POST** /stakings/activities/unstake | Create unstake activity
*StakingsApi* | [**create_withdraw_activity**](docs/StakingsApi.md#create_withdraw_activity) | **POST** /stakings/activities/withdraw | Create withdraw activity
*StakingsApi* | [**get_staking_activity_by_id**](docs/StakingsApi.md#get_staking_activity_by_id) | **GET** /stakings/activities/{activity_id} | Get staking activity details
*StakingsApi* | [**get_staking_by_id**](docs/StakingsApi.md#get_staking_by_id) | **GET** /stakings/{staking_id} | Get staking position details
*StakingsApi* | [**get_staking_estimation_fee**](docs/StakingsApi.md#get_staking_estimation_fee) | **POST** /stakings/estimate_fee | Estimate staking fees
*StakingsApi* | [**get_staking_pool_by_id**](docs/StakingsApi.md#get_staking_pool_by_id) | **GET** /stakings/pools/{pool_id} | Get staking pool details
*StakingsApi* | [**list_staking_activities**](docs/StakingsApi.md#list_staking_activities) | **GET** /stakings/activities | List staking activities
*StakingsApi* | [**list_staking_pools**](docs/StakingsApi.md#list_staking_pools) | **GET** /stakings/pools | List staking pools
*StakingsApi* | [**list_stakings**](docs/StakingsApi.md#list_stakings) | **GET** /stakings | List staking positions
*TransactionsApi* | [**broadcast_signed_transactions**](docs/TransactionsApi.md#broadcast_signed_transactions) | **POST** /transactions/broadcast | Broadcast signed transactions
*TransactionsApi* | [**cancel_transaction_by_id**](docs/TransactionsApi.md#cancel_transaction_by_id) | **POST** /transactions/{transaction_id}/cancel | Cancel transaction
*TransactionsApi* | [**check_loop_transfers**](docs/TransactionsApi.md#check_loop_transfers) | **GET** /transactions/check_loop_transfers | Check Loop transfers
*TransactionsApi* | [**create_contract_call_transaction**](docs/TransactionsApi.md#create_contract_call_transaction) | **POST** /transactions/contract_call | Call smart contract
*TransactionsApi* | [**create_message_sign_transaction**](docs/TransactionsApi.md#create_message_sign_transaction) | **POST** /transactions/message_sign | Sign message
*TransactionsApi* | [**create_transfer_transaction**](docs/TransactionsApi.md#create_transfer_transaction) | **POST** /transactions/transfer | Transfer token
*TransactionsApi* | [**drop_transaction_by_id**](docs/TransactionsApi.md#drop_transaction_by_id) | **POST** /transactions/{transaction_id}/drop | Drop transaction
*TransactionsApi* | [**estimate_fee**](docs/TransactionsApi.md#estimate_fee) | **POST** /transactions/estimate_fee | Estimate transaction fee
*TransactionsApi* | [**get_transaction_by_id**](docs/TransactionsApi.md#get_transaction_by_id) | **GET** /transactions/{transaction_id} | Get transaction information
*TransactionsApi* | [**list_transactions**](docs/TransactionsApi.md#list_transactions) | **GET** /transactions | List all transactions
*TransactionsApi* | [**resend_transaction_by_id**](docs/TransactionsApi.md#resend_transaction_by_id) | **POST** /transactions/{transaction_id}/resend | Resend transaction
*TransactionsApi* | [**speedup_transaction_by_id**](docs/TransactionsApi.md#speedup_transaction_by_id) | **POST** /transactions/{transaction_id}/speedup | Speed up transaction
*WalletsApi* | [**check_address_validity**](docs/WalletsApi.md#check_address_validity) | **GET** /wallets/check_address_validity | Check address validity
*WalletsApi* | [**check_addresses_validity**](docs/WalletsApi.md#check_addresses_validity) | **GET** /wallets/check_addresses_validity | Check addresses validity
*WalletsApi* | [**create_address**](docs/WalletsApi.md#create_address) | **POST** /wallets/{wallet_id}/addresses | Create addresses in wallet
*WalletsApi* | [**create_wallet**](docs/WalletsApi.md#create_wallet) | **POST** /wallets | Create wallet
*WalletsApi* | [**delete_wallet_by_id**](docs/WalletsApi.md#delete_wallet_by_id) | **POST** /wallets/{wallet_id}/delete | Delete wallet
*WalletsApi* | [**get_address**](docs/WalletsApi.md#get_address) | **GET** /wallets/{wallet_id}/addresses/{address} | Get address information
*WalletsApi* | [**get_chain_by_id**](docs/WalletsApi.md#get_chain_by_id) | **GET** /wallets/chains/{chain_id} | Get chain information
*WalletsApi* | [**get_max_transferable_value**](docs/WalletsApi.md#get_max_transferable_value) | **GET** /wallets/{wallet_id}/max_transferable_value | Get maximum transferable value
*WalletsApi* | [**get_token_by_id**](docs/WalletsApi.md#get_token_by_id) | **GET** /wallets/tokens/{token_id} | Get token information
*WalletsApi* | [**get_wallet_by_id**](docs/WalletsApi.md#get_wallet_by_id) | **GET** /wallets/{wallet_id} | Get wallet information
*WalletsApi* | [**list_addresses**](docs/WalletsApi.md#list_addresses) | **GET** /wallets/{wallet_id}/addresses | List wallet addresses
*WalletsApi* | [**list_enabled_chains**](docs/WalletsApi.md#list_enabled_chains) | **GET** /wallets/enabled_chains | List enabled chains
*WalletsApi* | [**list_enabled_tokens**](docs/WalletsApi.md#list_enabled_tokens) | **GET** /wallets/enabled_tokens | List enabled tokens
*WalletsApi* | [**list_supported_chains**](docs/WalletsApi.md#list_supported_chains) | **GET** /wallets/chains | List supported chains
*WalletsApi* | [**list_supported_tokens**](docs/WalletsApi.md#list_supported_tokens) | **GET** /wallets/tokens | List supported tokens
*WalletsApi* | [**list_token_balances_for_address**](docs/WalletsApi.md#list_token_balances_for_address) | **GET** /wallets/{wallet_id}/addresses/{address}/tokens | List token balances by address
*WalletsApi* | [**list_token_balances_for_wallet**](docs/WalletsApi.md#list_token_balances_for_wallet) | **GET** /wallets/{wallet_id}/tokens | List token balances by wallet
*WalletsApi* | [**list_utxos**](docs/WalletsApi.md#list_utxos) | **GET** /wallets/{wallet_id}/utxos | List UTXOs
*WalletsApi* | [**list_wallets**](docs/WalletsApi.md#list_wallets) | **GET** /wallets | List all wallets
*WalletsApi* | [**lock_utxos**](docs/WalletsApi.md#lock_utxos) | **POST** /wallets/{wallet_id}/utxos/lock | Lock UTXOs
*WalletsApi* | [**unlock_utxos**](docs/WalletsApi.md#unlock_utxos) | **POST** /wallets/{wallet_id}/utxos/unlock | Unlock UTXOs
*WalletsApi* | [**update_wallet_by_id**](docs/WalletsApi.md#update_wallet_by_id) | **PUT** /wallets/{wallet_id} | Update wallet
*WalletsExchangeWalletApi* | [**list_asset_balances_for_exchange_wallet**](docs/WalletsExchangeWalletApi.md#list_asset_balances_for_exchange_wallet) | **GET** /wallets/{wallet_id}/exchanges/assets | List asset balances
*WalletsExchangeWalletApi* | [**list_exchanges**](docs/WalletsExchangeWalletApi.md#list_exchanges) | **GET** /wallets/exchanges | List supported exchanges
*WalletsExchangeWalletApi* | [**list_supported_assets_for_exchange**](docs/WalletsExchangeWalletApi.md#list_supported_assets_for_exchange) | **GET** /wallets/exchanges/{exchange_id}/assets | List supported assets
*WalletsExchangeWalletApi* | [**list_supported_chains_for_exchange**](docs/WalletsExchangeWalletApi.md#list_supported_chains_for_exchange) | **GET** /wallets/exchanges/{exchange_id}/assets/{asset_id}/chains | List supported chains
*WalletsMPCWalletsApi* | [**cancel_tss_request_by_id**](docs/WalletsMPCWalletsApi.md#cancel_tss_request_by_id) | **POST** /wallets/mpc/vaults/{vault_id}/tss_requests/{tss_request_id}/cancel | Cancel TSS request
*WalletsMPCWalletsApi* | [**create_key_share_holder_group**](docs/WalletsMPCWalletsApi.md#create_key_share_holder_group) | **POST** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups | Create key share holder group
*WalletsMPCWalletsApi* | [**create_mpc_project**](docs/WalletsMPCWalletsApi.md#create_mpc_project) | **POST** /wallets/mpc/projects | Create project
*WalletsMPCWalletsApi* | [**create_mpc_vault**](docs/WalletsMPCWalletsApi.md#create_mpc_vault) | **POST** /wallets/mpc/vaults | Create vault
*WalletsMPCWalletsApi* | [**create_tss_request**](docs/WalletsMPCWalletsApi.md#create_tss_request) | **POST** /wallets/mpc/vaults/{vault_id}/tss_requests | Create TSS request
*WalletsMPCWalletsApi* | [**delete_key_share_holder_group_by_id**](docs/WalletsMPCWalletsApi.md#delete_key_share_holder_group_by_id) | **POST** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups/{key_share_holder_group_id}/delete | Delete key share holder group
*WalletsMPCWalletsApi* | [**get_key_share_holder_group_by_id**](docs/WalletsMPCWalletsApi.md#get_key_share_holder_group_by_id) | **GET** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups/{key_share_holder_group_id} | Get key share holder group information
*WalletsMPCWalletsApi* | [**get_mpc_project_by_id**](docs/WalletsMPCWalletsApi.md#get_mpc_project_by_id) | **GET** /wallets/mpc/projects/{project_id} | Get project information
*WalletsMPCWalletsApi* | [**get_mpc_vault_by_id**](docs/WalletsMPCWalletsApi.md#get_mpc_vault_by_id) | **GET** /wallets/mpc/vaults/{vault_id} | Get vault information
*WalletsMPCWalletsApi* | [**get_tss_request_by_id**](docs/WalletsMPCWalletsApi.md#get_tss_request_by_id) | **GET** /wallets/mpc/vaults/{vault_id}/tss_requests/{tss_request_id} | Get TSS request
*WalletsMPCWalletsApi* | [**list_cobo_key_holders**](docs/WalletsMPCWalletsApi.md#list_cobo_key_holders) | **GET** /wallets/mpc/cobo_key_share_holders | List all Cobo key share holders
*WalletsMPCWalletsApi* | [**list_key_share_holder_groups**](docs/WalletsMPCWalletsApi.md#list_key_share_holder_groups) | **GET** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups | List all key share holder groups
*WalletsMPCWalletsApi* | [**list_mpc_projects**](docs/WalletsMPCWalletsApi.md#list_mpc_projects) | **GET** /wallets/mpc/projects | List all projects
*WalletsMPCWalletsApi* | [**list_mpc_vaults**](docs/WalletsMPCWalletsApi.md#list_mpc_vaults) | **GET** /wallets/mpc/vaults | List all vaults
*WalletsMPCWalletsApi* | [**list_tss_requests**](docs/WalletsMPCWalletsApi.md#list_tss_requests) | **GET** /wallets/mpc/vaults/{vault_id}/tss_requests | List TSS requests
*WalletsMPCWalletsApi* | [**update_key_share_holder_group_by_id**](docs/WalletsMPCWalletsApi.md#update_key_share_holder_group_by_id) | **PUT** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups/{key_share_holder_group_id} | Update key share holder group
*WalletsMPCWalletsApi* | [**update_mpc_project_by_id**](docs/WalletsMPCWalletsApi.md#update_mpc_project_by_id) | **PUT** /wallets/mpc/projects/{project_id} | Update project name
*WalletsMPCWalletsApi* | [**update_mpc_vault_by_id**](docs/WalletsMPCWalletsApi.md#update_mpc_vault_by_id) | **PUT** /wallets/mpc/vaults/{vault_id} | Update vault name


## Documentation For Models

 - [Activity](docs/Activity.md)
 - [ActivityAction](docs/ActivityAction.md)
 - [ActivityInitiator](docs/ActivityInitiator.md)
 - [ActivityStatus](docs/ActivityStatus.md)
 - [ActivityTimeline](docs/ActivityTimeline.md)
 - [ActivityType](docs/ActivityType.md)
 - [AddressBook](docs/AddressBook.md)
 - [AddressEncoding](docs/AddressEncoding.md)
 - [AddressInfo](docs/AddressInfo.md)
 - [AddressTransferDestination](docs/AddressTransferDestination.md)
 - [AddressTransferDestinationAccountOutput](docs/AddressTransferDestinationAccountOutput.md)
 - [AddressTransferDestinationUtxoOutputsInner](docs/AddressTransferDestinationUtxoOutputsInner.md)
 - [AmountDetailsInner](docs/AmountDetailsInner.md)
 - [AmountStatus](docs/AmountStatus.md)
 - [AssetBalance](docs/AssetBalance.md)
 - [AssetInfo](docs/AssetInfo.md)
 - [BabylonStakeExtra](docs/BabylonStakeExtra.md)
 - [BabylonStakingExtra](docs/BabylonStakingExtra.md)
 - [BabylonValidator](docs/BabylonValidator.md)
 - [BaseContractCallSource](docs/BaseContractCallSource.md)
 - [BaseEstimateStakingFee](docs/BaseEstimateStakingFee.md)
 - [BaseStakeExtra](docs/BaseStakeExtra.md)
 - [BaseStakeSource](docs/BaseStakeSource.md)
 - [BookkeepingRecord](docs/BookkeepingRecord.md)
 - [BookkeepingSummary](docs/BookkeepingSummary.md)
 - [BroadcastSignedTransactions201ResponseInner](docs/BroadcastSignedTransactions201ResponseInner.md)
 - [BroadcastSignedTransactionsRequest](docs/BroadcastSignedTransactionsRequest.md)
 - [ChainInfo](docs/ChainInfo.md)
 - [CheckAddressValidity200Response](docs/CheckAddressValidity200Response.md)
 - [CheckAddressesValidity200ResponseInner](docs/CheckAddressesValidity200ResponseInner.md)
 - [CheckLoopTransfers200ResponseInner](docs/CheckLoopTransfers200ResponseInner.md)
 - [CoboSafeDelegate](docs/CoboSafeDelegate.md)
 - [CoboSafeDelegateType](docs/CoboSafeDelegateType.md)
 - [ContractCallDestination](docs/ContractCallDestination.md)
 - [ContractCallDestinationType](docs/ContractCallDestinationType.md)
 - [ContractCallParams](docs/ContractCallParams.md)
 - [ContractCallSource](docs/ContractCallSource.md)
 - [ContractCallSourceType](docs/ContractCallSourceType.md)
 - [CreateAddressRequest](docs/CreateAddressRequest.md)
 - [CreateCustodialWalletParams](docs/CreateCustodialWalletParams.md)
 - [CreateExchangeWalletParams](docs/CreateExchangeWalletParams.md)
 - [CreateKeyShareHolder](docs/CreateKeyShareHolder.md)
 - [CreateKeyShareHolderGroupRequest](docs/CreateKeyShareHolderGroupRequest.md)
 - [CreateMpcProjectRequest](docs/CreateMpcProjectRequest.md)
 - [CreateMpcVaultRequest](docs/CreateMpcVaultRequest.md)
 - [CreateMpcWalletParams](docs/CreateMpcWalletParams.md)
 - [CreateSafeWalletParams](docs/CreateSafeWalletParams.md)
 - [CreateSmartContractWalletParams](docs/CreateSmartContractWalletParams.md)
 - [CreateStakeActivity](docs/CreateStakeActivity.md)
 - [CreateStakeActivity201Response](docs/CreateStakeActivity201Response.md)
 - [CreateStakeActivityExtra](docs/CreateStakeActivityExtra.md)
 - [CreateStakeActivityRequest](docs/CreateStakeActivityRequest.md)
 - [CreateTransferTransaction201Response](docs/CreateTransferTransaction201Response.md)
 - [CreateTssRequestRequest](docs/CreateTssRequestRequest.md)
 - [CreateUnstakeActivity](docs/CreateUnstakeActivity.md)
 - [CreateUnstakeActivityRequest](docs/CreateUnstakeActivityRequest.md)
 - [CreateWalletParams](docs/CreateWalletParams.md)
 - [CreateWebhookEndpointRequest](docs/CreateWebhookEndpointRequest.md)
 - [CreateWithdrawActivity](docs/CreateWithdrawActivity.md)
 - [CreateWithdrawActivityRequest](docs/CreateWithdrawActivityRequest.md)
 - [CreatedWalletInfo](docs/CreatedWalletInfo.md)
 - [CurveType](docs/CurveType.md)
 - [CustodialTransferSource](docs/CustodialTransferSource.md)
 - [CustodialWalletInfo](docs/CustodialWalletInfo.md)
 - [DeleteKeyShareHolderGroupById201Response](docs/DeleteKeyShareHolderGroupById201Response.md)
 - [DeleteWalletById201Response](docs/DeleteWalletById201Response.md)
 - [EigenLayerLstStakeExtra](docs/EigenLayerLstStakeExtra.md)
 - [EigenLayerNativeStakeExtra](docs/EigenLayerNativeStakeExtra.md)
 - [EigenlayerValidator](docs/EigenlayerValidator.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [EstimateContractCallFeeParams](docs/EstimateContractCallFeeParams.md)
 - [EstimateFeeParams](docs/EstimateFeeParams.md)
 - [EstimateFeeRequestType](docs/EstimateFeeRequestType.md)
 - [EstimateStakeFee](docs/EstimateStakeFee.md)
 - [EstimateTransferFeeParams](docs/EstimateTransferFeeParams.md)
 - [EstimateUnstakeFee](docs/EstimateUnstakeFee.md)
 - [EstimateWithdrawFee](docs/EstimateWithdrawFee.md)
 - [EstimatedEvmEip1559Fee](docs/EstimatedEvmEip1559Fee.md)
 - [EstimatedEvmEip1559FeeSlow](docs/EstimatedEvmEip1559FeeSlow.md)
 - [EstimatedEvmLegacyFee](docs/EstimatedEvmLegacyFee.md)
 - [EstimatedEvmLegacyFeeSlow](docs/EstimatedEvmLegacyFeeSlow.md)
 - [EstimatedFee](docs/EstimatedFee.md)
 - [EstimatedFixedFee](docs/EstimatedFixedFee.md)
 - [EstimatedUtxoFee](docs/EstimatedUtxoFee.md)
 - [EstimatedUtxoFeeSlow](docs/EstimatedUtxoFeeSlow.md)
 - [EvmContractCallDestination](docs/EvmContractCallDestination.md)
 - [EvmEIP191MessageSignDestination](docs/EvmEIP191MessageSignDestination.md)
 - [EvmEIP712MessageSignDestination](docs/EvmEIP712MessageSignDestination.md)
 - [EvmEip1559FeeBasePrice](docs/EvmEip1559FeeBasePrice.md)
 - [EvmEip1559FeeRate](docs/EvmEip1559FeeRate.md)
 - [EvmLegacyFeeBasePrice](docs/EvmLegacyFeeBasePrice.md)
 - [EvmLegacyFeeRate](docs/EvmLegacyFeeRate.md)
 - [ExchangeId](docs/ExchangeId.md)
 - [ExchangeTransferDestination](docs/ExchangeTransferDestination.md)
 - [ExchangeTransferSource](docs/ExchangeTransferSource.md)
 - [ExchangeWalletInfo](docs/ExchangeWalletInfo.md)
 - [ExtendedTokenInfo](docs/ExtendedTokenInfo.md)
 - [FeeAmount](docs/FeeAmount.md)
 - [FeeGasLimit](docs/FeeGasLimit.md)
 - [FeeRate](docs/FeeRate.md)
 - [FeeType](docs/FeeType.md)
 - [FixedFeeRate](docs/FixedFeeRate.md)
 - [GetStakingEstimationFee201Response](docs/GetStakingEstimationFee201Response.md)
 - [GetStakingEstimationFeeRequest](docs/GetStakingEstimationFeeRequest.md)
 - [GetToken200Response](docs/GetToken200Response.md)
 - [GetToken4XXResponse](docs/GetToken4XXResponse.md)
 - [KeyShareHolder](docs/KeyShareHolder.md)
 - [KeyShareHolderGroup](docs/KeyShareHolderGroup.md)
 - [KeyShareHolderGroupStatus](docs/KeyShareHolderGroupStatus.md)
 - [KeyShareHolderGroupType](docs/KeyShareHolderGroupType.md)
 - [KeyShareHolderStatus](docs/KeyShareHolderStatus.md)
 - [KeyShareHolderType](docs/KeyShareHolderType.md)
 - [ListAddresses200Response](docs/ListAddresses200Response.md)
 - [ListAssetBalancesForExchangeWallet200Response](docs/ListAssetBalancesForExchangeWallet200Response.md)
 - [ListExchanges200ResponseInner](docs/ListExchanges200ResponseInner.md)
 - [ListKeyShareHolderGroups200Response](docs/ListKeyShareHolderGroups200Response.md)
 - [ListMpcProjects200Response](docs/ListMpcProjects200Response.md)
 - [ListMpcVaults200Response](docs/ListMpcVaults200Response.md)
 - [ListStakingActivities200Response](docs/ListStakingActivities200Response.md)
 - [ListStakingPools200Response](docs/ListStakingPools200Response.md)
 - [ListStakings200Response](docs/ListStakings200Response.md)
 - [ListSupportedAssetsForExchange200Response](docs/ListSupportedAssetsForExchange200Response.md)
 - [ListSupportedChains200Response](docs/ListSupportedChains200Response.md)
 - [ListSupportedTokens200Response](docs/ListSupportedTokens200Response.md)
 - [ListTokenBalancesForAddress200Response](docs/ListTokenBalancesForAddress200Response.md)
 - [ListTransactions200Response](docs/ListTransactions200Response.md)
 - [ListTssRequests200Response](docs/ListTssRequests200Response.md)
 - [ListUtxos200Response](docs/ListUtxos200Response.md)
 - [ListWallets200Response](docs/ListWallets200Response.md)
 - [ListWebhookEndpoints200Response](docs/ListWebhookEndpoints200Response.md)
 - [ListWebhookEventDefinitions200ResponseInner](docs/ListWebhookEventDefinitions200ResponseInner.md)
 - [ListWebhookEventLogs200Response](docs/ListWebhookEventLogs200Response.md)
 - [ListWebhookEvents200Response](docs/ListWebhookEvents200Response.md)
 - [LockUtxos201Response](docs/LockUtxos201Response.md)
 - [LockUtxosRequest](docs/LockUtxosRequest.md)
 - [LockUtxosRequestUtxosInner](docs/LockUtxosRequestUtxosInner.md)
 - [MPCDelegate](docs/MPCDelegate.md)
 - [MPCProject](docs/MPCProject.md)
 - [MPCVault](docs/MPCVault.md)
 - [MPCVaultType](docs/MPCVaultType.md)
 - [MPCWalletInfo](docs/MPCWalletInfo.md)
 - [MaxFeeAmount](docs/MaxFeeAmount.md)
 - [MaxTransferableValue](docs/MaxTransferableValue.md)
 - [MessageSignDestination](docs/MessageSignDestination.md)
 - [MessageSignDestinationType](docs/MessageSignDestinationType.md)
 - [MessageSignParams](docs/MessageSignParams.md)
 - [MessageSignSource](docs/MessageSignSource.md)
 - [MessageSignSourceType](docs/MessageSignSourceType.md)
 - [MpcContractCallSource](docs/MpcContractCallSource.md)
 - [MpcMessageSignSource](docs/MpcMessageSignSource.md)
 - [MpcSigningGroup](docs/MpcSigningGroup.md)
 - [MpcStakeSource](docs/MpcStakeSource.md)
 - [MpcTransferSource](docs/MpcTransferSource.md)
 - [Pagination](docs/Pagination.md)
 - [PoolDetails](docs/PoolDetails.md)
 - [PoolDetailsAllOfValidatorsInfo](docs/PoolDetailsAllOfValidatorsInfo.md)
 - [PoolSummary](docs/PoolSummary.md)
 - [RawMessageSignDestination](docs/RawMessageSignDestination.md)
 - [RefreshToken200Response](docs/RefreshToken200Response.md)
 - [RefreshTokenRequest](docs/RefreshTokenRequest.md)
 - [ReplaceType](docs/ReplaceType.md)
 - [RetryWebhookEventById201Response](docs/RetryWebhookEventById201Response.md)
 - [RootPubkey](docs/RootPubkey.md)
 - [SafeContractCallSource](docs/SafeContractCallSource.md)
 - [SafeTransferSource](docs/SafeTransferSource.md)
 - [SafeWallet](docs/SafeWallet.md)
 - [SmartContractInitiator](docs/SmartContractInitiator.md)
 - [SmartContractWalletInfo](docs/SmartContractWalletInfo.md)
 - [SmartContractWalletOperationType](docs/SmartContractWalletOperationType.md)
 - [SmartContractWalletType](docs/SmartContractWalletType.md)
 - [SourceGroup](docs/SourceGroup.md)
 - [StakeSourceType](docs/StakeSourceType.md)
 - [StakingPoolType](docs/StakingPoolType.md)
 - [StakingSource](docs/StakingSource.md)
 - [Stakings](docs/Stakings.md)
 - [StakingsExtra](docs/StakingsExtra.md)
 - [StakingsValidatorInfo](docs/StakingsValidatorInfo.md)
 - [SubWalletAssetBalance](docs/SubWalletAssetBalance.md)
 - [TSSGroups](docs/TSSGroups.md)
 - [TSSRequest](docs/TSSRequest.md)
 - [TSSRequestStatus](docs/TSSRequestStatus.md)
 - [TSSRequestType](docs/TSSRequestType.md)
 - [TSSRequestWebhookEventData](docs/TSSRequestWebhookEventData.md)
 - [TokenBalance](docs/TokenBalance.md)
 - [TokenBalanceBalance](docs/TokenBalanceBalance.md)
 - [TokenInfo](docs/TokenInfo.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionApprover](docs/TransactionApprover.md)
 - [TransactionBlockInfo](docs/TransactionBlockInfo.md)
 - [TransactionCustodialAssetWalletSource](docs/TransactionCustodialAssetWalletSource.md)
 - [TransactionDepositFromAddressSource](docs/TransactionDepositFromAddressSource.md)
 - [TransactionDepositFromLoopSource](docs/TransactionDepositFromLoopSource.md)
 - [TransactionDepositFromWalletSource](docs/TransactionDepositFromWalletSource.md)
 - [TransactionDepositToAddressDestination](docs/TransactionDepositToAddressDestination.md)
 - [TransactionDepositToWalletDestination](docs/TransactionDepositToWalletDestination.md)
 - [TransactionDestination](docs/TransactionDestination.md)
 - [TransactionDestinationType](docs/TransactionDestinationType.md)
 - [TransactionDetail](docs/TransactionDetail.md)
 - [TransactionDetails](docs/TransactionDetails.md)
 - [TransactionEvmContractDestination](docs/TransactionEvmContractDestination.md)
 - [TransactionEvmEip1559Fee](docs/TransactionEvmEip1559Fee.md)
 - [TransactionEvmLegacyFee](docs/TransactionEvmLegacyFee.md)
 - [TransactionExchangeWalletSource](docs/TransactionExchangeWalletSource.md)
 - [TransactionFee](docs/TransactionFee.md)
 - [TransactionFeeStationWalletSource](docs/TransactionFeeStationWalletSource.md)
 - [TransactionFixedFee](docs/TransactionFixedFee.md)
 - [TransactionInitiatorType](docs/TransactionInitiatorType.md)
 - [TransactionMPCWalletSource](docs/TransactionMPCWalletSource.md)
 - [TransactionMessageSignEIP191Destination](docs/TransactionMessageSignEIP191Destination.md)
 - [TransactionMessageSignEIP712Destination](docs/TransactionMessageSignEIP712Destination.md)
 - [TransactionRawTxInfo](docs/TransactionRawTxInfo.md)
 - [TransactionRbf](docs/TransactionRbf.md)
 - [TransactionRbfSource](docs/TransactionRbfSource.md)
 - [TransactionReplacement](docs/TransactionReplacement.md)
 - [TransactionRequestEvmEip1559Fee](docs/TransactionRequestEvmEip1559Fee.md)
 - [TransactionRequestEvmLegacyFee](docs/TransactionRequestEvmLegacyFee.md)
 - [TransactionRequestFee](docs/TransactionRequestFee.md)
 - [TransactionRequestFixedFee](docs/TransactionRequestFixedFee.md)
 - [TransactionRequestUtxoFee](docs/TransactionRequestUtxoFee.md)
 - [TransactionResend](docs/TransactionResend.md)
 - [TransactionResult](docs/TransactionResult.md)
 - [TransactionResultType](docs/TransactionResultType.md)
 - [TransactionSignatureResult](docs/TransactionSignatureResult.md)
 - [TransactionSigner](docs/TransactionSigner.md)
 - [TransactionSmartContractSafeWalletSource](docs/TransactionSmartContractSafeWalletSource.md)
 - [TransactionSource](docs/TransactionSource.md)
 - [TransactionSourceType](docs/TransactionSourceType.md)
 - [TransactionStatus](docs/TransactionStatus.md)
 - [TransactionSubStatus](docs/TransactionSubStatus.md)
 - [TransactionTimeline](docs/TransactionTimeline.md)
 - [TransactionTokeApproval](docs/TransactionTokeApproval.md)
 - [TransactionTokenAmount](docs/TransactionTokenAmount.md)
 - [TransactionTransferToAddressDestination](docs/TransactionTransferToAddressDestination.md)
 - [TransactionTransferToAddressDestinationAccountOutput](docs/TransactionTransferToAddressDestinationAccountOutput.md)
 - [TransactionTransferToAddressDestinationUtxoOutputsInner](docs/TransactionTransferToAddressDestinationUtxoOutputsInner.md)
 - [TransactionTransferToWalletDestination](docs/TransactionTransferToWalletDestination.md)
 - [TransactionType](docs/TransactionType.md)
 - [TransactionUtxo](docs/TransactionUtxo.md)
 - [TransactionUtxoFee](docs/TransactionUtxoFee.md)
 - [TransactionWebhookEventData](docs/TransactionWebhookEventData.md)
 - [TransferDestination](docs/TransferDestination.md)
 - [TransferDestinationType](docs/TransferDestinationType.md)
 - [TransferParams](docs/TransferParams.md)
 - [TransferSource](docs/TransferSource.md)
 - [UTXO](docs/UTXO.md)
 - [UpdateCustodialWalletParams](docs/UpdateCustodialWalletParams.md)
 - [UpdateExchangeWalletParams](docs/UpdateExchangeWalletParams.md)
 - [UpdateGroupAction](docs/UpdateGroupAction.md)
 - [UpdateKeyShareHolderGroupByIdRequest](docs/UpdateKeyShareHolderGroupByIdRequest.md)
 - [UpdateMpcProjectByIdRequest](docs/UpdateMpcProjectByIdRequest.md)
 - [UpdateMpcVaultByIdRequest](docs/UpdateMpcVaultByIdRequest.md)
 - [UpdateMpcWalletParams](docs/UpdateMpcWalletParams.md)
 - [UpdateSmartContractWalletParams](docs/UpdateSmartContractWalletParams.md)
 - [UpdateWalletParams](docs/UpdateWalletParams.md)
 - [UpdateWebhookEndpointByIdRequest](docs/UpdateWebhookEndpointByIdRequest.md)
 - [UtxoFeeBasePrice](docs/UtxoFeeBasePrice.md)
 - [UtxoFeeRate](docs/UtxoFeeRate.md)
 - [WalletBalanceSnapshot](docs/WalletBalanceSnapshot.md)
 - [WalletBalanceSnapshotRecord](docs/WalletBalanceSnapshotRecord.md)
 - [WalletInfo](docs/WalletInfo.md)
 - [WalletSubtype](docs/WalletSubtype.md)
 - [WalletType](docs/WalletType.md)
 - [WebhookEndpoint](docs/WebhookEndpoint.md)
 - [WebhookEndpointStatus](docs/WebhookEndpointStatus.md)
 - [WebhookEvent](docs/WebhookEvent.md)
 - [WebhookEventData](docs/WebhookEventData.md)
 - [WebhookEventDataType](docs/WebhookEventDataType.md)
 - [WebhookEventLog](docs/WebhookEventLog.md)
 - [WebhookEventStatus](docs/WebhookEventStatus.md)
 - [WebhookEventType](docs/WebhookEventType.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="CoboAuth"></a>
### CoboAuth

- **Type**: API key
- **API key parameter name**: BIZ-API-KEY
- **Location**: HTTP header

<a id="OAuth2"></a>
### OAuth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://auth.cobo.com/authorize
- **Scopes**: 
 - **custodial_asset_wallet:create**: Create access to custodial asset wallets
 - **custodial_asset_wallet:add**: Generate address access to custodial asset wallets
 - **custodial_asset_wallet:edit**: Change wallet name access to custodial asset wallets
 - **custodial_asset_wallet:withdraw**: Withdraw access to custodial asset wallets
 - **mpc_organization_controlled_wallet:create**: Create access to MPC organization-controlled wallets
 - **mpc_organization_controlled_wallet:add**: Generate address access to MPC organization-controlled wallets
 - **mpc_organization_controlled_wallet:edit**: Change wallet name access to MPC organization-controlled wallets
 - **mpc_organization_controlled_wallet:withdraw**: Withdraw access to MPC organization-controlled wallets
 - **mpc_organization_controlled_wallet:contract_call**: Contract call access to MPC organization-controlled wallets
 - **mpc_organization_controlled_wallet:message_sign**: Message sign access to MPC organization-controlled wallets
 - **mpc_organization_controlled_vault:manage**: Create/Edit access to MPC organization-controlled vaults
 - **mpc_organization_controlled_key_group:manage**: Create/Edit/Delete access to MPC organization-controlled key groups
 - **mpc_organization_controlled_tss_request:manage**: Create/Cancel access to MPC organization-controlled tss requests
 - **mpc_user_controlled_wallet:create**: Create access to MPC user-controlled wallets
 - **mpc_user_controlled_wallet:add**: Generate address access to MPC user-controlled wallets
 - **mpc_user_controlled_wallet:edit**: Change wallet name access to MPC user-controlled wallets
 - **mpc_user_controlled_wallet:withdraw**: Withdraw access to MPC user-controlled wallets
 - **mpc_user_controlled_wallet:contract_call**: Contract call access to MPC user-controlled wallets
 - **mpc_user_controlled_wallet:message_sign**: Message sign access to MPC user-controlled wallets
 - **mpc_user_controlled_project:manage**: Create/Edit access to MPC user-controlled projects
 - **mpc_user_controlled_vault:manage**: Create/Edit access to MPC user-controlled vaults
 - **mpc_user_controlled_key_group:manage**: Create/Edit/Delete access to MPC user-controlled key groups
 - **mpc_user_controlled_tss_request:manage**: Create/Cancel access to MPC user-controlled tss requests
 - **webhook:resend**: Resend access to webhook events
 - **webhook_url:edit**: Create/Edit access to webhook urls


## Author

help@cobo.com


