# Copyright 2026
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountPaymentMethodLine(models.Model):
    _inherit = "account.payment.method.line"

    show_in_advance_payment = fields.Boolean(
        string="Show in Advance Payment",
        default=False,
        help="If checked, this payment method will be available in the advance payment wizard",
    )
