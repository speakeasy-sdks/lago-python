# fees

## Overview

Everything about Fees

Find out more
<https://doc.getlago.com/docs/api/invoices/invoice-object#fee-object>
### Available Operations

* [find](#find) - Find fee by ID
* [find_all](#find_all) - Find all fees
* [update](#update) - Update an existing fee

## find

Return a single fee

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindFeeRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.fees.find(req)

if res.fee_object is not None:
    # handle response
```

## find_all

Find all fees of an organization and filter them

### Example Usage

```python
import lago
import dateutil.parser
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindAllFeesRequest(
    billable_metric_code='bm_code',
    created_at_from=dateutil.parser.isoparse('2023-03-28T12:21:51Z'),
    created_at_to=dateutil.parser.isoparse('2023-03-28T12:21:51Z'),
    currency='EUR',
    external_customer_id='12345',
    external_subscription_id='12345',
    failed_at_from=dateutil.parser.isoparse('2023-03-28T12:21:51Z'),
    failed_at_to=dateutil.parser.isoparse('2023-03-28T12:21:51Z'),
    fee_type=operations.FindAllFeesFeeTypeEnum.CHARGE,
    page=2,
    payment_status=operations.FindAllFeesPaymentStatusEnum.SUCCEEDED,
    per_page=20,
    refunded_at_from=dateutil.parser.isoparse('2023-03-28T12:21:51Z'),
    refunded_at_to=dateutil.parser.isoparse('2023-03-28T12:21:51Z'),
    succeeded_at_from=dateutil.parser.isoparse('2023-03-28T12:21:51Z'),
    succeeded_at_to=dateutil.parser.isoparse('2023-03-28T12:21:51Z'),
)

res = s.fees.find_all(req)

if res.fees_paginated is not None:
    # handle response
```

## update

Update an existing fee

### Example Usage

```python
import lago
from lago.models import operations, shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateFeeRequest(
    fee_update_input=shared.FeeUpdateInput(
        invoice=shared.FeeUpdateInputInvoice(
            payment_status=shared.FeeUpdateInputInvoicePaymentStatusEnum.REFUNDED,
        ),
    ),
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.fees.update(req)

if res.fee_object is not None:
    # handle response
```
