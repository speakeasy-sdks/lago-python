# plans

## Overview

Everything about Plan collection

Find out more
<https://doc.getlago.com/docs/api/plans/plan-object>
### Available Operations

* [create](#create) - Create a new plan
* [destroy](#destroy) - Delete a plan
* [find](#find) - Fin plan by code
* [find_all](#find_all) - Find plans
* [update](#update) - Update an existing plan

## create

Create a new plan

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.PlanInput(
    plan=shared.PlanInputPlan(
        amount_cents=1200,
        amount_currency="EUR",
        bill_charges_monthly=False,
        charges=[
            shared.PlanInputPlanCharges(
                billable_metric_id="1a901a90-1a90-1a90-1a90-1a901a901a90",
                charge_model="standard",
                group_properties=[
                    shared.PlanInputPlanChargesGroupProperties(
                        group_id="123456",
                        values={
                            "mollitia": "laborum",
                            "dolores": "dolorem",
                            "corporis": "explicabo",
                        },
                    ),
                    shared.PlanInputPlanChargesGroupProperties(
                        group_id="123456",
                        values={
                            "enim": "omnis",
                            "nemo": "minima",
                            "excepturi": "accusantium",
                            "iure": "culpa",
                        },
                    ),
                    shared.PlanInputPlanChargesGroupProperties(
                        group_id="123456",
                        values={
                            "sapiente": "architecto",
                            "mollitia": "dolorem",
                            "culpa": "consequuntur",
                            "repellat": "mollitia",
                        },
                    ),
                    shared.PlanInputPlanChargesGroupProperties(
                        group_id="123456",
                        values={
                            "numquam": "commodi",
                            "quam": "molestiae",
                            "velit": "error",
                        },
                    ),
                ],
                id="1a901a90-1a90-1a90-1a90-1a901a901a90",
                instant=False,
                properties={
                    "quis": "vitae",
                },
            ),
        ],
        code="example_code",
        description="description",
        interval="yearly",
        name="example name",
        pay_in_advance=True,
        trial_period=2,
    ),
)

res = s.plans.create(req)

if res.plan is not None:
    # handle response
```

## destroy

Delete a plan

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DestroyPlanRequest(
    code="example_code",
)

res = s.plans.destroy(req)

if res.plan is not None:
    # handle response
```

## find

Return a single plan

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindPlanRequest(
    code="example_code",
)

res = s.plans.find(req)

if res.plan is not None:
    # handle response
```

## find_all

Find all plans in certain organisation

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindAllPlansRequest(
    page=2,
    per_page=20,
)

res = s.plans.find_all(req)

if res.plans is not None:
    # handle response
```

## update

Update an existing plan by code

### Example Usage

```python
import lago
from lago.models import operations, shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.UpdatePlanRequest(
    plan_input=shared.PlanInput(
        plan=shared.PlanInputPlan(
            amount_cents=1200,
            amount_currency="EUR",
            bill_charges_monthly=False,
            charges=[
                shared.PlanInputPlanCharges(
                    billable_metric_id="1a901a90-1a90-1a90-1a90-1a901a901a90",
                    charge_model="graduated",
                    group_properties=[
                        shared.PlanInputPlanChargesGroupProperties(
                            group_id="123456",
                            values={
                                "sequi": "tenetur",
                                "ipsam": "id",
                                "possimus": "aut",
                                "quasi": "error",
                            },
                        ),
                    ],
                    id="1a901a90-1a90-1a90-1a90-1a901a901a90",
                    instant=False,
                    properties={
                        "laborum": "quasi",
                        "reiciendis": "voluptatibus",
                        "vero": "nihil",
                        "praesentium": "voluptatibus",
                    },
                ),
                shared.PlanInputPlanCharges(
                    billable_metric_id="1a901a90-1a90-1a90-1a90-1a901a901a90",
                    charge_model="standard",
                    group_properties=[
                        shared.PlanInputPlanChargesGroupProperties(
                            group_id="123456",
                            values={
                                "cum": "perferendis",
                                "doloremque": "reprehenderit",
                            },
                        ),
                        shared.PlanInputPlanChargesGroupProperties(
                            group_id="123456",
                            values={
                                "maiores": "dicta",
                                "corporis": "dolore",
                            },
                        ),
                        shared.PlanInputPlanChargesGroupProperties(
                            group_id="123456",
                            values={
                                "dicta": "harum",
                                "enim": "accusamus",
                            },
                        ),
                    ],
                    id="1a901a90-1a90-1a90-1a90-1a901a901a90",
                    instant=False,
                    properties={
                        "repudiandae": "quae",
                        "ipsum": "quidem",
                    },
                ),
                shared.PlanInputPlanCharges(
                    billable_metric_id="1a901a90-1a90-1a90-1a90-1a901a901a90",
                    charge_model="package",
                    group_properties=[
                        shared.PlanInputPlanChargesGroupProperties(
                            group_id="123456",
                            values={
                                "modi": "praesentium",
                                "rem": "voluptates",
                                "quasi": "repudiandae",
                                "sint": "veritatis",
                            },
                        ),
                        shared.PlanInputPlanChargesGroupProperties(
                            group_id="123456",
                            values={
                                "incidunt": "enim",
                                "consequatur": "est",
                                "quibusdam": "explicabo",
                                "deserunt": "distinctio",
                            },
                        ),
                        shared.PlanInputPlanChargesGroupProperties(
                            group_id="123456",
                            values={
                                "labore": "modi",
                                "qui": "aliquid",
                                "cupiditate": "quos",
                                "perferendis": "magni",
                            },
                        ),
                    ],
                    id="1a901a90-1a90-1a90-1a90-1a901a901a90",
                    instant=False,
                    properties={
                        "ipsam": "alias",
                        "fugit": "dolorum",
                        "excepturi": "tempora",
                        "facilis": "tempore",
                    },
                ),
            ],
            code="example_code",
            description="description",
            interval="weekly",
            name="example name",
            pay_in_advance=True,
            trial_period=2,
        ),
    ),
    code="example_code",
)

res = s.plans.update(req)

if res.plan is not None:
    # handle response
```
