from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class AccountingCleanupWizard(models.TransientModel):
    _name = 'accounting.cleanup.wizard'
    _description = 'Accounting Cleanup Wizard'

    def action_cleanup_accounting_data(self):
        moves = self.env['account.move'].search([])
        payments = self.env['account.payment'].search([])

        # # Ensure everything is canceled before delete
        payments.filtered(lambda p: p.state != 'cancel').action_draft()
        payments.unlink()

        moves.filtered(lambda m: m.state != 'draft').button_draft()
        moves.unlink()