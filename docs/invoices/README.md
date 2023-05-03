# invoices

## Overview

Everything about Invoice collection

Find out more
<https://doc.getlago.com/docs/api/invoices/invoice-object>
### Available Operations

* [download](#download) - Download an existing invoice
* [finalize](#finalize) - Finalize a draft invoice
* [find](#find) - Find invoice by ID
* [find_all](#find_all) - Find all invoices
* [retry](#retry) - Retry invoice payment
* [update](#update) - Update an existing invoice status
* [void](#void) - Refresh a draft invoice

## download

Download an existing invoice

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DownloadInvoiceRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.download(req)

if res.invoice is not None:
    # handle response
```

## finalize

Finalize a draft invoice

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FinalizeInvoiceRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.finalize(req)

if res.invoice is not None:
    # handle response
```

## find

Return a single invoice

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindInvoiceRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.find(req)

if res.invoice is not None:
    # handle response
```

## find_all

Find all invoices in certain organisation

### Example Usage

```python
import lago
import dateutil.parser
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindAllInvoicesRequest(
    external_customer_id='12345',
    issuing_date_from=dateutil.parser.parse('2022-07-08').date(),
    issuing_date_to=dateutil.parser.parse('2022-08-09').date(),
    page=2,
    per_page=20,
    status=operations.FindAllInvoicesStatusEnum.FINALIZED,
)

res = s.invoices.find_all(req)

if res.invoices is not None:
    # handle response
```

## retry

Retry invoice payment

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RetryPaymentRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.retry(req)

if res.status_code == 200:
    # handle response
```

## update

Update an existing invoice

### Example Usage

```python
import lago
from lago.models import operations, shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.UpdateInvoiceRequest(
    invoice_input=shared.InvoiceInput(
        invoice=shared.InvoiceInputInvoice(
            metadata=[
                shared.InvoiceInputInvoiceMetadata(
                    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
                    key='name',
                    value='John',
                ),
                shared.InvoiceInputInvoiceMetadata(
                    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
                    key='name',
                    value='John',
                ),
            ],
            payment_status=shared.InvoiceInputInvoicePaymentStatusEnum.SUCCEEDED,
        ),
    ),
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.update(req)

if res.invoice is not None:
    # handle response
```

## void

Refresh a draft invoice

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RefreshInvoiceRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.void(req)

if res.invoice is not None:
    # handle response
```
