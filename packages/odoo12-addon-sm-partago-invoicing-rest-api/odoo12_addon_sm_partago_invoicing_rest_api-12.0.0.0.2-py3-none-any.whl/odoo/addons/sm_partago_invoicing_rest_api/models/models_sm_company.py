# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class sm_company(models.Model):
    _inherit = 'res.company'

    cs_app_api_payment_mode_id = fields.Many2one(
        'account.payment.mode',
        string=_("Payment mode (for prepayment invoices generated from APP)")
    )
