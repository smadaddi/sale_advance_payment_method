# Copyright 2026
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountVoucherWizard(models.TransientModel):
    _inherit = "account.voucher.wizard"

    payment_method_line_id = fields.Many2one(
        "account.payment.method.line",
        "Payment Method",
        domain="[('journal_id', '=', journal_id), ('show_in_advance_payment', '=', True), ('payment_type', '=', payment_type)]",
    )

    @api.onchange("journal_id", "payment_type")
    def _onchange_journal_payment_type(self):
        """Clear payment method line when journal or payment type changes"""
        self.payment_method_line_id = False

    def _prepare_payment_vals(self, sale):
        """Override to include payment_method_line_id if selected"""
        vals = super()._prepare_payment_vals(sale)
        
        # If a payment method line is selected, use it
        if self.payment_method_line_id:
            vals["payment_method_line_id"] = self.payment_method_line_id.id
        
        return vals
