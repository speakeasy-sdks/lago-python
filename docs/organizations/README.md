# organizations

## Overview

Everything about Organization collection

Find out more
<https://doc.getlago.com/docs/api/organizations/organization-object>
### Available Operations

* [update](#update) - Update an existing Organization

## update

Update an existing organization

### Example Usage

```python
import lago
from lago.models import shared

s = lago.Lago(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.OrganizationInput(
    organization=shared.OrganizationInputOrganization(
        address_line1='address1',
        address_line2='address2',
        billing_configuration=shared.BillingConfigurationOrganization(
            document_locale='fr',
            invoice_footer='text',
            invoice_grace_period=5,
            vat_rate=25,
        ),
        city='City',
        country='CZ',
        email='example@example.com',
        email_settings=[
            shared.OrganizationInputOrganizationEmailSettingsEnum.INVOICE_FINALIZED,
            shared.OrganizationInputOrganizationEmailSettingsEnum.CREDIT_NOTE_CREATED,
            shared.OrganizationInputOrganizationEmailSettingsEnum.CREDIT_NOTE_CREATED,
        ],
        legal_name='name1',
        legal_number='10000',
        state='state1',
        timezone='Europe/Paris',
        webhook_url='https://example.com',
        zipcode='10000',
    ),
)

res = s.organizations.update(req)

if res.organization is not None:
    # handle response
```
