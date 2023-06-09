"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .add_ons import AddOns
from .billable_metrics import BillableMetrics
from .coupons import Coupons
from .credit_notes import CreditNotes
from .customers import Customers
from .events import Events
from .fees import Fees
from .invoices import Invoices
from .organizations import Organizations
from .plans import Plans
from .subscriptions import Subscriptions
from .wallets import Wallets
from .webhooks import Webhooks
from lago.models import shared

SERVERS = [
    "https://api.getlago.com/api/v1",
]
"""Contains the list of servers available to the SDK"""

class Lago:
    r"""Lago API allows your application to push customer information and metrics (events) from your application to the billing application.
    https://github.com/getlago - Lago Github
    """
    add_ons: AddOns
    r"""Everything about Add-on collection
    https://doc.getlago.com/docs/api/add_ons/add-on-object - Find out more
    """
    billable_metrics: BillableMetrics
    r"""Everything about Billable metric collection
    https://doc.getlago.com/docs/api/billable_metrics/billable-metric-object - Find out more
    """
    coupons: Coupons
    r"""Everything about Coupon collection
    https://doc.getlago.com/docs/api/coupons/coupon-object - Find out more
    """
    credit_notes: CreditNotes
    r"""Everything about Credit notes collection"""
    customers: Customers
    r"""Everything about Customer collection
    https://doc.getlago.com/docs/api/customers/customer-object - Find out more
    """
    events: Events
    r"""Everything about Event collection
    https://doc.getlago.com/docs/api/events/event-object - Find out more
    """
    fees: Fees
    r"""Everything about Fees
    https://doc.getlago.com/docs/api/invoices/invoice-object#fee-object - Find out more
    """
    invoices: Invoices
    r"""Everything about Invoice collection
    https://doc.getlago.com/docs/api/invoices/invoice-object - Find out more
    """
    organizations: Organizations
    r"""Everything about Organization collection
    https://doc.getlago.com/docs/api/organizations/organization-object - Find out more
    """
    plans: Plans
    r"""Everything about Plan collection
    https://doc.getlago.com/docs/api/plans/plan-object - Find out more
    """
    subscriptions: Subscriptions
    r"""Everything about Subscription collection
    https://doc.getlago.com/docs/api/subscriptions/subscription-object - Find out more
    """
    wallets: Wallets
    r"""Everything about Wallet collection
    https://doc.getlago.com/docs/api/wallets/wallet-object - Find out more
    """
    webhooks: Webhooks
    r"""Everything about Webhooks
    https://doc.getlago.com/docs/api/webhooks/message-signature#1-retrieve-the-public-key - Find out more
    """

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.0.1"
    _gen_version: str = "2.17.8"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.add_ons = AddOns(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.billable_metrics = BillableMetrics(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.coupons = Coupons(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.credit_notes = CreditNotes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.customers = Customers(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.events = Events(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.fees = Fees(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.invoices = Invoices(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.organizations = Organizations(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.plans = Plans(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.subscriptions = Subscriptions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.wallets = Wallets(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.webhooks = Webhooks(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    