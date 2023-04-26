<div align="center">
    <img src="https://user-images.githubusercontent.com/6267663/230070609-43e6bc4c-e839-49ac-82b8-04ebc5ff3a89.svg" width="250">
    <h1>Python SDK</h1>
   <p>Open-source metering and usage-based billing</p>
   <a href="https://doc.getlago.com/docs/api/intro"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/lago-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/lago-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/lago-python/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/lago-python?sort=semver&style=for-the-badge" /></a>
</div>


<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install lago-billing
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindInvoiceRequest(
    id="1a901a90-1a90-1a90-1a90-1a901a901a90",
)

res = s.invoices.find(req)

if res.invoice is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [add_ons](docs/addons/README.md)

* [apply](docs/addons/README.md#apply) - Apply an add-on to a customer
* [create](docs/addons/README.md#create) - Create a new add-on
* [destroy](docs/addons/README.md#destroy) - Delete an add-on
* [find](docs/addons/README.md#find) - Find add-on by code
* [find_all](docs/addons/README.md#find_all) - Find add-ons
* [update](docs/addons/README.md#update) - Update an existing add-on

### [billable_metrics](docs/billablemetrics/README.md)

* [create](docs/billablemetrics/README.md#create) - Create a new billable metric
* [destroy](docs/billablemetrics/README.md#destroy) - Delete a billable metric
* [find](docs/billablemetrics/README.md#find) - Find billable metric by code
* [find_all](docs/billablemetrics/README.md#find_all) - Find Billable metrics
* [find_all_groups](docs/billablemetrics/README.md#find_all_groups) - Find Billable metric groups
* [update](docs/billablemetrics/README.md#update) - Update an existing billable metric

### [coupons](docs/coupons/README.md)

* [applied_coupons](docs/coupons/README.md#applied_coupons) - Find Applied Coupons
* [apply](docs/coupons/README.md#apply) - Apply a coupon to a customer
* [create](docs/coupons/README.md#create) - Create a new coupon
* [destroy](docs/coupons/README.md#destroy) - Delete a coupon
* [find](docs/coupons/README.md#find) - Find coupon by code
* [find_all](docs/coupons/README.md#find_all) - Find Coupons
* [update](docs/coupons/README.md#update) - Update an existing coupon

### [credit_notes](docs/creditnotes/README.md)

* [create](docs/creditnotes/README.md#create) - Create a new Credit note
* [download](docs/creditnotes/README.md#download) - Download an existing credit note
* [find](docs/creditnotes/README.md#find) - Find credit note
* [find_all](docs/creditnotes/README.md#find_all) - Find Credit notes
* [update](docs/creditnotes/README.md#update) - Update an existing credit note
* [void](docs/creditnotes/README.md#void) - Void existing credit note

### [customers](docs/customers/README.md)

* [create](docs/customers/README.md#create) - Create a customer
* [current_usage](docs/customers/README.md#current_usage) - Find customer current usage
* [delete_applied_coupon](docs/customers/README.md#delete_applied_coupon) - Delete customer's appplied coupon
* [destroy](docs/customers/README.md#destroy) - Delete a customer
* [find](docs/customers/README.md#find) - Find customer by external ID
* [find_all](docs/customers/README.md#find_all) - Find customers
* [portal_url](docs/customers/README.md#portal_url) - Get customer portal URL

### [events](docs/events/README.md)

* [estimate_fees](docs/events/README.md#estimate_fees) - Estimate fees for an instant charge
* [batch_create](docs/events/README.md#batch_create) - Create batch events
* [create](docs/events/README.md#create) - Create a new event
* [find](docs/events/README.md#find) - Find event by transaction ID

### [fees](docs/fees/README.md)

* [find](docs/fees/README.md#find) - Find fee by ID
* [find_all](docs/fees/README.md#find_all) - Find all fees
* [update](docs/fees/README.md#update) - Update an existing fee

### [invoices](docs/invoices/README.md)

* [download](docs/invoices/README.md#download) - Download an existing invoice
* [finalize](docs/invoices/README.md#finalize) - Finalize a draft invoice
* [find](docs/invoices/README.md#find) - Find invoice by ID
* [find_all](docs/invoices/README.md#find_all) - Find all invoices
* [retry](docs/invoices/README.md#retry) - Retry invoice payment
* [update](docs/invoices/README.md#update) - Update an existing invoice status
* [void](docs/invoices/README.md#void) - Refresh a draft invoice

### [organizations](docs/organizations/README.md)

* [update](docs/organizations/README.md#update) - Update an existing Organization

### [plans](docs/plans/README.md)

* [create](docs/plans/README.md#create) - Create a new plan
* [destroy](docs/plans/README.md#destroy) - Delete a plan
* [find](docs/plans/README.md#find) - Fin plan by code
* [find_all](docs/plans/README.md#find_all) - Find plans
* [update](docs/plans/README.md#update) - Update an existing plan

### [subscriptions](docs/subscriptions/README.md)

* [create](docs/subscriptions/README.md#create) - Assign a plan to a customer
* [destroy](docs/subscriptions/README.md#destroy) - Terminate a subscription
* [find_all](docs/subscriptions/README.md#find_all) - Find subscriptions
* [update](docs/subscriptions/README.md#update) - Update an existing subscription

### [wallets](docs/wallets/README.md)

* [create](docs/wallets/README.md#create) - Create a new wallet
* [create_transaction](docs/wallets/README.md#create_transaction) - Create a new wallet transaction
* [destroy](docs/wallets/README.md#destroy) - Delete a wallet
* [find](docs/wallets/README.md#find) - Find wallet
* [find_all](docs/wallets/README.md#find_all) - Find wallets
* [find_all_transactions](docs/wallets/README.md#find_all_transactions) - Find wallet transactions
* [update](docs/wallets/README.md#update) - Update an existing wallet

### [webhooks](docs/webhooks/README.md)

* [fetch_public_key](docs/webhooks/README.md#fetch_public_key) - Fetch webhook public key
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
