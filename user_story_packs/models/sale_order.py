# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def _compute_name(self):
        res = super()._compute_name()
        if self.product_id and self.product_id.is_pack and \
           self.product_id.component_line_ids:
            self.name += _('\n-- Components --')
            for line in self.product_id.component_line_ids:
                self.name += '\n %s - %i' % (line.component_id.name,
                                             line.quantity)
        return res