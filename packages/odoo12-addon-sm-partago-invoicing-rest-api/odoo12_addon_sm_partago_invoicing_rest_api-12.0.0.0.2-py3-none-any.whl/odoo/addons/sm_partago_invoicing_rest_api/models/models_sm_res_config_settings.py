from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # INVOICING
    cs_app_api_payment_mode_id = fields.Many2one(
        related='company_id.cs_app_api_payment_mode_id',
        string=_("Payment mode (for prepayment invoices generated from APP)"),
        readonly=False)
