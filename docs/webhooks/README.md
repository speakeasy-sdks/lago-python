# webhooks

## Overview

Everything about Webhooks

Find out more
<https://doc.getlago.com/docs/api/webhooks/message-signature#1-retrieve-the-public-key>
### Available Operations

* [fetch_public_key](#fetch_public_key) - Fetch webhook public key

## fetch_public_key

Webhook public key

### Example Usage

```python
import lago


s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.webhooks.fetch_public_key()

if res.fetch_public_key_200_text_plain_string is not None:
    # handle response
```
