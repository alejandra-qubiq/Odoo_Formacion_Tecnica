# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    component_line_ids = fields.One2many(
        comodel_name='product.pack.lines',
        string='Pack Components Lines',
        inverse_name='product_id',
    )

    is_pack = fields.Boolean(string='Pack')

    price_pack_method = fields.Selection(
        string='Cost Calculation',
        selection=[('normal_price', 'Normal Price'),
                   ('component_total', 'Sum Components')],
        default="normal_price")

    total_price = fields.Float(
        compute="_compute_price",
        store=True,
        readonly=False,
        )

    @api.depends('price_pack_method', 'component_line_ids')
    def _compute_price(self):
        for line in self:
            if line.price_pack_method == "component_total":
                line.total_price = self.list_price
                for component in line.component_line_ids:
                    line.total_price += component.price
            else:
                line.total_price = line.list_price
