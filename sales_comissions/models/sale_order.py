# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    commission_line_ids = fields.One2many(
        string='Commission lines',
        comodel_name='commission.lines',
        inverse_name='sale_order_id',
    )
    total_commission = fields.Float(
        string="Total commission",
        compute='_compute_commission')

    @api.depends('amount_total', 'commission_line_ids.commission')
    def _compute_commission(self):
        for record in self:
            record.total_commission = sum(
                record.amount_total * (commission_lines.commission / 100)
                for commission_lines in record.commission_line_ids
            ) or 0.0
