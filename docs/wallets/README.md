# wallets

## Overview

Everything about Wallet collection

Find out more
<https://doc.getlago.com/docs/api/wallets/wallet-object>
### Available Operations

* [create](#create) - Create a new wallet
* [create_transaction](#create_transaction) - Create a new wallet transaction
* [destroy](#destroy) - Delete a wallet
* [find](#find) - Find wallet
* [find_all](#find_all) - Find wallets
* [find_all_transactions](#find_all_transactions) - Find wallet transactions
* [update](#update) - Update an existing wallet

## create

Create a new wallet

### Example Usage

```python
import lago
import dateutil.parser
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.WalletInput(
    wallet=shared.WalletInputWallet(
        currency='EUR',
        expiration_at=dateutil.parser.isoparse('2022-09-14T23:59:59Z'),
        external_customer_id='12345',
        granted_credits=10,
        name='Wallet name',
        paid_credits=500,
        rate_amount=2,
    ),
)

res = s.wallets.create(req)

if res.wallet is not None:
    # handle response
```

## create_transaction

Create a new wallet transaction

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.WalletTransactionInput(
    wallet_transaction=shared.WalletTransactionInputWalletTransaction(
        granted_credits=10,
        paid_credits=100,
        wallet_id='1a901a90-1a90-1a90-1a90-1a901a901a90',
    ),
)

res = s.wallets.create_transaction(req)

if res.wallet_transactions is not None:
    # handle response
```

## destroy

Delete a wallet

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DestroyWalletRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.wallets.destroy(req)

if res.wallet is not None:
    # handle response
```

## find

Return a wallet

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindWalletRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.wallets.find(req)

if res.wallet is not None:
    # handle response
```

## find_all

Find all wallets for certain customer

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindAllWalletsRequest(
    external_customer_id='12345',
    page=2,
    per_page=20,
)

res = s.wallets.find_all(req)

if res.wallets is not None:
    # handle response
```

## find_all_transactions

Find all wallet transactions for certain wallet

### Example Usage

```python
import lago
from lago.models import operations

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.FindAllWalletTransactionsRequest(
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
    page=2,
    per_page=20,
    status='pending',
    transaction_type='inbound',
)

res = s.wallets.find_all_transactions(req)

if res.wallet_transactions is not None:
    # handle response
```

## update

Update an existing wallet

### Example Usage

```python
import lago
import dateutil.parser
from lago.models import operations, shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.UpdateWalletRequest(
    wallet_update_input=shared.WalletUpdateInput(
        wallet=shared.WalletUpdateInputWallet(
            expiration_at=dateutil.parser.isoparse('2022-09-14T23:59:59Z'),
            name='Wallet name',
        ),
    ),
    id='1a901a90-1a90-1a90-1a90-1a901a901a90',
)

res = s.wallets.update(req)

if res.wallet is not None:
    # handle response
```
