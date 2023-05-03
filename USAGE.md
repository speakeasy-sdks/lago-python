<!-- Start SDK Example Usage -->
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
<!-- End SDK Example Usage -->