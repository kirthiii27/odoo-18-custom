from odoo import models, fields, api

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    # Other fields and methods...

    def action_print_invoice(self):
        # You can use the action report method with the 'qweb-pdf' type and without forcing a download
        return self.env.ref('custom_invoice_report.action_report_pos_invoice').report_action(self)
    outstanding_credits = fields.Monetary(string="Outstanding Credits", compute="_compute_outstanding_credits")
    pd_cheques = fields.Monetary(string="PD Cheques", compute="_compute_pd_cheques")
    total_outstanding = fields.Monetary(string="Total Outstanding", compute="_compute_total_outstanding")

    # @api.depends('partner_id')
    def _compute_outstanding_credits(self):
        for record in self:
            outstanding_invoices = self.search([
                ('partner_id', '=', record.partner_id.id),
                ('move_type', '=', 'out_invoice'),
                ('state', '=', 'posted'),
                ('payment_state', '!=', 'paid')
            ])
            total_outstanding = sum(outstanding_invoices.mapped('amount_residual'))
            return {
                'invoices': outstanding_invoices,
                'total_outstanding': total_outstanding,
            }

    def _compute_outstanding_cheque(self):
        for record in self:
            outstanding_invoices = self.env['account.payment'].search([
                ('partner_id', '=', record.partner_id.id),
                ('payment_type', '=', 'inbound'),
                ('is_matched', '=', False),
                ('state', '=', 'in_process'),
                ('move_id.journal_id.name', '=', 'Cheque')
            ])
            total_outstanding = sum(outstanding_invoices.mapped('amount'))
            return {
                'invoices': outstanding_invoices,
                'total_outstanding': total_outstanding,
            }

    def action_post(self):
        """
        Override action_post to also automatically print the invoice after posting.
        """
        res = super(AccountMove, self).action_post()
        return self.action_print_invoice()  # Print invoice after posting
