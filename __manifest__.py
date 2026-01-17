# Copyright 2026
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Advance Payment Method Selection",
    "version": "18.0.1.0.0",
    "author": "Samad Alimadadi",
    "website": "https://artam-systems.com",
    "category": "Sales",
    "license": "AGPL-3",
    "summary": "Add payment method selection to advance payment wizard with journal filtering",
    "depends": ["sale_advance_payment"],
    "data": [
        "views/account_journal_view.xml",
        "wizard/sale_advance_payment_wzd_view.xml",
    ],
    "installable": True,
    "auto_install": False,
}
