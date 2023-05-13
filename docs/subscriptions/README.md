# subscriptions

## Overview

Everything about Subscription collection

Find out more
<https://doc.getlago.com/docs/api/subscriptions/subscription-object>
### Available Operations

* [create](#create) - Assign a plan to a customer
* [destroy](#destroy) - Terminate a subscription
* [find_all](#find_all) - Find subscriptions
* [update](#update) - Update an existing subscription

## create

Assign a plan to a customer

### Example Usage

```python
import lago
import dateutil.parser
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.SubscriptionCreateInput(
    subscription=shared.SubscriptionCreateInputSubscription(
        billing_time=shared.SubscriptionCreateInputSubscriptionBillingTimeEnum.ANNIVERSARY,
        external_customer_id='12345',
        external_id='54321',
        name='Test name',
        plan_code='example_code',
        subscription_at=dateutil.parser.isoparse('2022-08-08T00:00:00Z'),
    ),
)

res = s.subscriptions.create(req)

if res.subscription is not None:
    # handle response
```

## destroy

Terminate a subscription

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DestroySubscriptionRequest(
    external_id='example_id',
)

res = s.subscriptions.destroy(req)

if res.subscription is not None:
    # handle response
```

## find_all

Find all suscriptions for certain customer

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindAllSubscriptionsRequest(
    external_customer_id='12345',
    page=2,
    per_page=20,
)

res = s.subscriptions.find_all(req)

if res.subscriptions is not None:
    # handle response
```

## update

Update an existing subscription by external ID

### Example Usage

```python
import lago
import dateutil.parser
from lago.models import operations, shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateSubscriptionRequest(
    subscription_update_input=shared.SubscriptionUpdateInput(
        subscription=shared.SubscriptionUpdateInputSubscription(
            name='New name',
            subscription_at=dateutil.parser.isoparse('2022-08-08T00:00:00Z'),
        ),
    ),
    external_id='example_id',
)

res = s.subscriptions.update(req)

if res.subscription is not None:
    # handle response
```
