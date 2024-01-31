# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models, api, fields, _


class SaleOrderLines(models.Model):
    _inherit = 'sale.order'
    contains_packs = fields.Boolean(
        string='Contains packs',
    )
    pack_id = fields.Many2one(
        comodel_name='product.template',
        string="Pack",
        domain="[('is_pack', '=', True)]"
    )

    @api.onchange('pack_id')
    def _onchange_pack_id(self):
        if self.contains_packs and self.pack_id:
            self.order_line = False
            for product in self.pack_id.component_line_ids:
                print('aqui', self.id)
                self.env['sale.order.line'].new({
                    'product_id': product.component_id.id,
                    'order_id': self.id,
                    'product_uom_qty': product.quantity
                })
                print(self.id)
