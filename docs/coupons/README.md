# coupons

## Overview

Everything about Coupon collection

Find out more
<https://doc.getlago.com/docs/api/coupons/coupon-object>
### Available Operations

* [applied_coupons](#applied_coupons) - Find Applied Coupons
* [apply](#apply) - Apply a coupon to a customer
* [create](#create) - Create a new coupon
* [destroy](#destroy) - Delete a coupon
* [find](#find) - Find coupon by code
* [find_all](#find_all) - Find Coupons
* [update](#update) - Update an existing coupon

## applied_coupons

Find all applied coupons

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindAllAppliedCouponsRequest(
    external_customer_id='12345',
    page=2,
    per_page=20,
    status=operations.FindAllAppliedCouponsStatusEnum.ACTIVE,
)

res = s.coupons.applied_coupons(req)

if res.applied_coupons is not None:
    # handle response
```

## apply

Apply a coupon to a customer

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.AppliedCouponInput(
    applied_coupon=shared.AppliedCouponInputAppliedCoupon(
        amount_cents=1200,
        amount_currency='EUR',
        coupon_code='example_code',
        external_customer_id='123456',
        frequency=shared.AppliedCouponInputAppliedCouponFrequencyEnum.ONCE,
        frequency_duration=3,
        percentage_rate=25,
    ),
)

res = s.coupons.apply(req)

if res.applied_coupon is not None:
    # handle response
```

## create

Create a new coupon

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

req = shared.CouponInput(
    coupon=shared.CouponInputCoupon(
        amount_cents=1200,
        amount_currency='EUR',
        applies_to=shared.CouponInputCouponAppliesTo(
            plan_codes=[
                'code1',
                'code1',
                'code1',
                'code1',
            ],
        ),
        code='example_code',
        coupon_type=shared.CouponInputCouponCouponTypeEnum.PERCENTAGE,
        expiration=shared.CouponInputCouponExpirationEnum.TIME_LIMIT,
        expiration_at=dateutil.parser.isoparse('2022-09-14T23:59:59Z'),
        frequency=shared.CouponInputCouponFrequencyEnum.ONCE,
        frequency_duration=3,
        name='coupon1',
        percentage_rate=25,
        reusable=True,
    ),
)

res = s.coupons.create(req)

if res.coupon is not None:
    # handle response
```

## destroy

Delete a coupon

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DestroyCouponRequest(
    code='example_code',
)

res = s.coupons.destroy(req)

if res.coupon is not None:
    # handle response
```

## find

Return a single coupon

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindCouponRequest(
    code='example_code',
)

res = s.coupons.find(req)

if res.coupon is not None:
    # handle response
```

## find_all

Find all coupons in certain organisation

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindAllCouponsRequest(
    page=2,
    per_page=20,
)

res = s.coupons.find_all(req)

if res.coupons is not None:
    # handle response
```

## update

Update an existing coupon by code

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

req = operations.UpdateCouponRequest(
    coupon_input=shared.CouponInput(
        coupon=shared.CouponInputCoupon(
            amount_cents=1200,
            amount_currency='EUR',
            applies_to=shared.CouponInputCouponAppliesTo(
                plan_codes=[
                    'code1',
                    'code1',
                    'code1',
                    'code1',
                ],
            ),
            code='example_code',
            coupon_type=shared.CouponInputCouponCouponTypeEnum.PERCENTAGE,
            expiration=shared.CouponInputCouponExpirationEnum.TIME_LIMIT,
            expiration_at=dateutil.parser.isoparse('2022-09-14T23:59:59Z'),
            frequency=shared.CouponInputCouponFrequencyEnum.ONCE,
            frequency_duration=3,
            name='coupon1',
            percentage_rate=25,
            reusable=True,
        ),
    ),
    code='example_code',
)

res = s.coupons.update(req)

if res.coupon is not None:
    # handle response
```
