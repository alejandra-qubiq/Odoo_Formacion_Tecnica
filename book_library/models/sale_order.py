from odoo import models, api
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains('partner_id')
    def _check_partner_is_partner(self):
        for record in self:
            if not record.partner_id.partner:
                raise UserError("You can only sell to members")
