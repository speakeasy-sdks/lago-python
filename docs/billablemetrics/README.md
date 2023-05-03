# billable_metrics

## Overview

Everything about Billable metric collection

Find out more
<https://doc.getlago.com/docs/api/billable_metrics/billable-metric-object>
### Available Operations

* [create](#create) - Create a new billable metric
* [destroy](#destroy) - Delete a billable metric
* [find](#find) - Find billable metric by code
* [find_all](#find_all) - Find Billable metrics
* [find_all_groups](#find_all_groups) - Find Billable metric groups
* [update](#update) - Update an existing billable metric

## create

Create a new billable metric

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.BillableMetricInput(
    billable_metric=shared.BillableMetricInputBillableMetric(
        aggregation_type=shared.BillableMetricInputBillableMetricAggregationTypeEnum.MAX_AGG,
        code='example_code',
        description='description',
        field_name='amount',
        group=shared.BillableMetricGroup(
            key='region',
            values=[
                {
                    "unde": 'nulla',
                    "corrupti": 'illum',
                    "vel": 'error',
                    "deserunt": 'suscipit',
                },
                'magnam',
                {
                    "delectus": 'tempora',
                },
            ],
        ),
        name='bm1',
    ),
)

res = s.billable_metrics.create(req)

if res.billable_metric is not None:
    # handle response
```

## destroy

Delete a billable metric

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DestroyBillableMetricRequest(
    code='example_code',
)

res = s.billable_metrics.destroy(req)

if res.billable_metric is not None:
    # handle response
```

## find

Return a single billable metric

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindBillableMetricRequest(
    code='example_code',
)

res = s.billable_metrics.find(req)

if res.billable_metric is not None:
    # handle response
```

## find_all

Find all billable metrics in certain organisation

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindAllBillableMetricsRequest(
    page=2,
    per_page=20,
)

res = s.billable_metrics.find_all(req)

if res.billable_metrics is not None:
    # handle response
```

## find_all_groups

Find all billable metric groups in certain organisation

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindAllBillableMetricGroupsRequest(
    code='example_code',
    page=2,
    per_page=20,
)

res = s.billable_metrics.find_all_groups(req)

if res.groups is not None:
    # handle response
```

## update

Update an existing billable metric by code

### Example Usage

```python
import lago
from lago.models import operations, shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.UpdateBillableMetricRequest(
    billable_metric_input=shared.BillableMetricInput(
        billable_metric=shared.BillableMetricInputBillableMetric(
            aggregation_type=shared.BillableMetricInputBillableMetricAggregationTypeEnum.SUM_AGG,
            code='example_code',
            description='description',
            field_name='amount',
            group=shared.BillableMetricGroup(
                key='region',
                values=[
                    {
                        "voluptatum": 'iusto',
                        "excepturi": 'nisi',
                        "recusandae": 'temporibus',
                        "ab": 'quis',
                    },
                    'deserunt',
                ],
            ),
            name='bm1',
        ),
    ),
    code='example_code',
)

res = s.billable_metrics.update(req)

if res.billable_metric is not None:
    # handle response
```
