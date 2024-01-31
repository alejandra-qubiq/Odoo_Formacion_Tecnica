# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class CommissionLines(models.Model):
    _name = "commission.lines"
    _description = "Commission lines"

    partner_id = fields.Many2one(
        string='User',
        comodel_name='res.partner',
        domain=[("is_sales_person", "=", True)]
    )
    sale_order_id = fields.Many2one(
        string='Orders',
        comodel_name='sale.order',
    )
    commission = fields.Float(
        string='%',
        compute='_compute_field', readonly=False, store=True)

    @api.depends('partner_id')
    def _compute_field(self):
        for record in self:
            record.commission = record.partner_id.commission if record.partner_id else 0.0

