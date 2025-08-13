from odoo import models


class AccountingCleanupWizard(models.TransientModel):
    _name = "accounting.cleanup.wizard"
    _description = "Accounting Cleanup Wizard"

    def action_cleanup_accounting_data(self):
        invoices = self.env["account.move"].search([("move_type", "=", "out_invoice")])
        references = [invoice.name for invoice in invoices]
        invoices.filtered(lambda m: m.state != "draft").button_draft()
        invoices.unlink()

        entries = self.env["account.move"].search([("ref", "in", references)])
        entries.filtered(lambda m: m.state != "draft").button_draft()
        entries.unlink()

        payments = self.env["account.payment"].search([("ref", "in", references)])
        payments.filtered(lambda p: p.state != "cancel").action_draft()
        payments.unlink()
