# credit_notes

## Overview

Everything about Credit notes collection

### Available Operations

* [create](#create) - Create a new Credit note
* [download](#download) - Download an existing credit note
* [find](#find) - Find credit note
* [find_all](#find_all) - Find Credit notes
* [update](#update) - Update an existing credit note
* [void](#void) - Void existing credit note

## create

Create a new credit note

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.CreditNoteInput(
    credit_note=shared.CreditNoteInputCreditNote(
        credit_amount_cents=20,
        description='description',
        invoice_id='1a901a90-1a90-1a90-1a90-1a901a901a90',
        items=[
            shared.CreditNoteInputCreditNoteItems(
                amount_cents=20,
                fee_id='1a901a90-1a90-1a90-1a90-1a901a901a90',
            ),
            shared.CreditNoteInputCreditNoteItems(
                amount_cents=20,
                fee_id='1a901a90-1a90-1a90-1a90-1a901a901a90',
            ),
            shared.CreditNoteInputCreditNoteItems(
                amount_cents=20,
                fee_id='1a901a90-1a90-1a90-1a90-1a901a901a90',
            ),
            shared.CreditNoteInputCreditNoteItems(
                amount_cents=20,
                fee_id='1a901a90-1a90-1a90-1a90-1a901a901a90',
            ),
        ],
        reason=shared.CreditNoteInputCreditNoteReasonEnum.FRAUDULENT_CHARGE,
        refund_amount_cents=20,
    ),
)

res = s.credit_notes.create(req)

if res.credit_note is not None:
    # handle response
```

## download

Download an existing credit note

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DownloadCreditNoteRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.credit_notes.download(req)

if res.credit_note is not None:
    # handle response
```

## find

Return a single credit note

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindCreditNoteRequest(
    id='12345',
)

res = s.credit_notes.find(req)

if res.credit_note is not None:
    # handle response
```

## find_all

Find all credit notes in certain organisation

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.FindAllCreditNotesRequest(
    external_customer_id='12345',
    page=2,
    per_page=20,
)

res = s.credit_notes.find_all(req)

if res.credit_notes is not None:
    # handle response
```

## update

Update an existing credit note

### Example Usage

```python
import lago
from lago.models import operations, shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateCreditNoteRequest(
    credit_note_update_input=shared.CreditNoteUpdateInput(
        credit_note=shared.CreditNoteUpdateInputCreditNote(
            refund_status=shared.CreditNoteUpdateInputCreditNoteRefundStatusEnum.SUCCEEDED,
        ),
    ),
    id='12345',
)

res = s.credit_notes.update(req)

if res.credit_note is not None:
    # handle response
```

## void

Void an existing credit note

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.VoidCreditNoteRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.credit_notes.void(req)

if res.credit_note is not None:
    # handle response
```
