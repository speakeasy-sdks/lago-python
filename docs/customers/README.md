# customers

## Overview

Everything about Customer collection

Find out more
<https://doc.getlago.com/docs/api/customers/customer-object>
### Available Operations

* [create](#create) - Create a customer
* [current_usage](#current_usage) - Find customer current usage
* [delete_applied_coupon](#delete_applied_coupon) - Delete customer's appplied coupon
* [destroy](#destroy) - Delete a customer
* [find](#find) - Find customer by external ID
* [find_all](#find_all) - Find customers
* [portal_url](#portal_url) - Get customer portal URL

## create

Create a new customer

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.CustomerInput(
    customer=shared.CustomerInputCustomer(
        address_line1='address1',
        address_line2='address2',
        billing_configuration={
            "porro": 'dolorum',
            "dicta": 'nam',
            "officia": 'occaecati',
        },
        city='City',
        country='CZ',
        currency='EUR',
        email='example@example.com',
        external_id='12345',
        lago_url='https://lago.url',
        legal_name='name1',
        legal_number='10000',
        metadata=[
            shared.CustomerInputCustomerMetadata(
                display_in_invoice=False,
                id='1a901a90-1a90-1a90-1a90-1a901a901a90',
                key='name',
                value='John',
            ),
        ],
        name='John Doe',
        phone='+3551234567',
        state='state1',
        timezone='Europe/Paris',
        url='https://example.com',
        zipcode='10000',
    ),
)

res = s.customers.create(req)

if res.customer is not None:
    # handle response
```

## current_usage

Return a customer current usage

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindCustomerCurrentUsageRequest(
    customer_external_id='12345',
    external_subscription_id='54321',
)

res = s.customers.current_usage(req)

if res.customer_usage is not None:
    # handle response
```

## delete_applied_coupon

Delete customer's appplied coupon

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteAppliedCouponRequest(
    applied_coupon_id='54321',
    customer_external_id='12345',
)

res = s.customers.delete_applied_coupon(req)

if res.applied_coupon is not None:
    # handle response
```

## destroy

Return the deleted customer

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteCustomerRequest(
    external_id='12345',
)

res = s.customers.destroy(req)

if res.customer is not None:
    # handle response
```

## find

Return a single customer

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindCustomerRequest(
    external_id='12345',
)

res = s.customers.find(req)

if res.customer is not None:
    # handle response
```

## find_all

Find all customers in certain organisation

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindAllCustomersRequest(
    page=2,
    per_page=20,
)

res = s.customers.find_all(req)

if res.customers is not None:
    # handle response
```

## portal_url

Get customer portal URL

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetCustomerPortalURLRequest(
    customer_external_id='12345',
)

res = s.customers.portal_url(req)

if res.get_customer_portal_url_200_application_json_object is not None:
    # handle response
```
