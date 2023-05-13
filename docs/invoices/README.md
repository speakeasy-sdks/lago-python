# invoices

## Overview

Everything about Invoice collection

Find out more
<https://doc.getlago.com/docs/api/invoices/invoice-object>
### Available Operations

* [refresh](#refresh) - Refresh a draft invoice
* [retry](#retry) - Retry invoice payment
* [void](#void) - Finalize a draft invoice
* [void](#void) - Download an existing invoice
* [void](#void) - Update an existing invoice status
* [void](#void) - Find invoice by ID
* [void](#void) - Find all invoices

## refresh

Refresh a draft invoice

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.RefreshInvoiceRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.refresh(req)

if res.invoice is not None:
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.RetryPaymentRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.retry(req)

if res.status_code == 200:
    # handle response
```

## void

Finalize a draft invoice

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FinalizeInvoiceRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.void(req)

if res.invoice is not None:
    # handle response
```

## void

Download an existing invoice

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DownloadInvoiceRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.void(req)

if res.invoice is not None:
    # handle response
```

## void

Update an existing invoice

### Example Usage

```python
import lago
from lago.models import operations, shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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

res = s.invoices.void(req)

if res.invoice is not None:
    # handle response
```

## void

Return a single invoice

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindInvoiceRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.invoices.void(req)

if res.invoice is not None:
    # handle response
```

## void

Find all invoices in certain organisation

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

req = operations.FindAllInvoicesRequest(
    external_customer_id='12345',
    issuing_date_from=dateutil.parser.parse('2022-07-08').date(),
    issuing_date_to=dateutil.parser.parse('2022-08-09').date(),
    page=2,
    per_page=20,
    status=operations.FindAllInvoicesStatusEnum.DRAFT,
)

res = s.invoices.void(req)

if res.invoices is not None:
    # handle response
```
