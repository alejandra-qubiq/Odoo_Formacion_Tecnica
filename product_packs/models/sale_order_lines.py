# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models, api, fields, _


class SaleOrderLines(models.Model):
    _inherit = 'sale.order.line'
    contains_packs = fields.Boolean(string='Packs')

    @api.onchange('product_id')
    def _compute_name(self):
        super(SaleOrderLines, self)._compute_name()
        for rec in self:
            if rec.product_id and rec.product_id.is_pack:
                rec.name += _('\n--Components--')
                for component in rec.product_id.component_line_ids:
                    rec.name += '\n %s - %i' % (
                        component.component_id.name,
                        component.quantity
                    )
