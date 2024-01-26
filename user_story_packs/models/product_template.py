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

    list_price = fields.Float(
        compute="_compute_price",
        store=True,
        readonly=False,
        )

    @api.depends('price_pack_method')
    def _compute_price(self):
        for line in self:
            if line.price_pack_method == "component_total":
                total = 0.0
                for component in line.component_line_ids:
                    total += component.price
                line.list_price = total
            else:
                line.list_price = line.list_price


