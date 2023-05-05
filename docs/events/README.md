# events

## Overview

Everything about Event collection

Find out more
<https://doc.getlago.com/docs/api/events/event-object>
### Available Operations

* [estimate_fees](#estimate_fees) - Estimate fees for an instant charge
* [batch_create](#batch_create) - Create batch events
* [create](#create) - Create a new event
* [find](#find) - Find event by transaction ID

## estimate_fees

Estimate the fees that would be created after reception of an event for a billable metric attached to one or multiple instant charges

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.EventEstimateFeesInput(
    event=shared.EventEstimateFeesInputEvent(
        code='code',
        external_customer_id='654321',
        external_subscription_id='123456',
        properties={
            "hic": 'optio',
            "totam": 'beatae',
            "commodi": 'molestiae',
        },
    ),
)

res = s.events.estimate_fees(req)

if res.fees is not None:
    # handle response
```

## batch_create

Create batch events

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.BatchEventInput(
    event=shared.BatchEventInputEvent(
        code='code',
        external_customer_id='654321',
        external_subscription_ids=[
            'qui',
            'impedit',
        ],
        properties={
            "esse": 'ipsum',
            "excepturi": 'aspernatur',
            "perferendis": 'ad',
        },
        timestamp=1669823754,
        transaction_id='123456',
    ),
)

res = s.events.batch_create(req)

if res.status_code == 200:
    # handle response
```

## create

Create a new event

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.EventInput(
    event=shared.EventInputEvent(
        code='code',
        external_customer_id='654321',
        external_subscription_id='123456',
        properties={
            "sed": 'iste',
            "dolor": 'natus',
            "laboriosam": 'hic',
        },
        timestamp=1669823754,
        transaction_id='123456',
    ),
)

res = s.events.create(req)

if res.status_code == 200:
    # handle response
```

## find

Return a single event

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindEventRequest(
    id='12345',
)

res = s.events.find(req)

if res.event is not None:
    # handle response
```
