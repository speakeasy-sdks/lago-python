# add_ons

## Overview

Everything about Add-on collection

Find out more
<https://doc.getlago.com/docs/api/add_ons/add-on-object>
### Available Operations

* [apply](#apply) - Apply an add-on to a customer
* [create](#create) - Create a new add-on
* [destroy](#destroy) - Delete an add-on
* [find](#find) - Find add-on by code
* [find_all](#find_all) - Find add-ons
* [update](#update) - Update an existing add-on

## apply

Apply an add-on to a customer

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.AppliedAddOnInput(
    applied_add_on=shared.AppliedAddOnInputAppliedAddOn(
        add_on_code='code',
        amount_cents=1200,
        amount_currency='EUR',
        external_customer_id='1234567',
    ),
)

res = s.add_ons.apply(req)

if res.applied_add_on is not None:
    # handle response
```

## create

Create a new add-on

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.AddOnInput(
    add_on=shared.AddOnInputAddOn(
        amount_cents=1200,
        amount_currency='EUR',
        code='example_code',
        description='description',
        name='example name',
    ),
)

res = s.add_ons.create(req)

if res.add_on is not None:
    # handle response
```

## destroy

Delete an add-on

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DestroyAddOnRequest(
    code='example_code',
)

res = s.add_ons.destroy(req)

if res.add_on is not None:
    # handle response
```

## find

Return a single add-on

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindAddOnRequest(
    code='example_code',
)

res = s.add_ons.find(req)

if res.add_on is not None:
    # handle response
```

## find_all

Find all add-ons in certain organisation

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindAllAddOnsRequest(
    page=2,
    per_page=20,
)

res = s.add_ons.find_all(req)

if res.add_ons is not None:
    # handle response
```

## update

Update an existing add-on by code

### Example Usage

```python
import lago
from lago.models import operations, shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateAddOnRequest(
    add_on_input=shared.AddOnInput(
        add_on=shared.AddOnInputAddOn(
            amount_cents=1200,
            amount_currency='EUR',
            code='example_code',
            description='description',
            name='example name',
        ),
    ),
    code='example_code',
)

res = s.add_ons.update(req)

if res.add_on is not None:
    # handle response
```
