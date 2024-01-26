# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models, api, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def _compute_name(self):
        res = super(SaleOrderLine, self)._compute_name()
        if self.product_id and self.product_id.is_pack:
            self.name += _('\n--Components--')
            for component in self.product_id.component_line_ids:
                self.name += '\n %s - %i' % (component.component_line_ids.name,
                                             component.quantity)
        return res
