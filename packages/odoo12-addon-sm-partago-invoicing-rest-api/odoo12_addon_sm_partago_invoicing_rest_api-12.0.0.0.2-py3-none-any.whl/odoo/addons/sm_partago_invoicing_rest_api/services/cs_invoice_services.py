import json
from . import schemas
from odoo.http import Response
from odoo.tools.translate import _
from odoo.addons.component.core import Component
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils


class CsInvoiceService(Component):
    _inherit = "base.rest.private_abstract_service"
    _name = "cs.invoice.service"
    _usage = "cs-invoice"
    _description = """
        Invoice Services
    """

    def create(self, **params):
        create_dict = self._prepare_create(params)
        invoice = self.env['account.invoice'].create(create_dict)
        if invoice.partner_id:
            invoice.action_invoice_open()
        else:
            error_subject = _("Carsharing prepayment invoice creation error.")
            error = _("Can't validate invoice without associated partner.")
            overwrite_project_id = 9
            sm_utils.create_system_task_csinvoice(
                self,
                error_subject,
                error,
                invoice.id,
                overwrite_project_id
            )
        invoice.message_post(
            subject="Cs prepayment invoice created from APP",
            body=str(params),
            message_type="notification"
        )
        return Response(
            json.dumps({
                'message': _("Creation ok"),
                'id': invoice.id
            }),
            status=200,
            content_type="application/json"
        )

    def _validator_create(self):
        return schemas.S_CS_INVOICE_CREATE

    def _prepare_create(self, params):
        company = self.env.user.company_id
        # TODO: Conditional setup payment mode based on params when it's clear.
        create_dict = {
            'amount_tax': 5,
            'state': 'draft',
            'type': 'out_invoice',
            'journal_id': company.cs_invoice_journal_id.id,
            'invoice_email_sent': False,
            'invoice_template': 'cs_app_invoice',
            'payment_mode_id': company.cs_app_api_payment_mode_id.id
        }
        customer = params.get('customer', False)
        cs_person_index = customer.get('reference', False)
        related_partners = self.env['res.partner'].search(
            [('cs_person_index', '=', cs_person_index)])
        if len(related_partners) == 1:
            create_dict['partner_id'] = related_partners[0].id
        items = params.get('items', False)
        if items:
            lines_list = []
            for item in items:
                lines_list.append((0, 0, {
                    'product_id': company.cs_carsharing_product_id.id,
                    'name': item['description'],
                    'price_unit': item['price'],
                    'quantity': item['quantity'],
                    'account_id': company.cs_carsharing_product_id.property_account_income_id.id,
                    'line_type': 'default'
                }))
            create_dict['invoice_line_ids'] = lines_list
        create_dict['date_invoice'] = params.get('date')
        return create_dict
