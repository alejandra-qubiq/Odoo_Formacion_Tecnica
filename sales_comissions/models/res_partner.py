# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, exceptions


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_sales_person = fields.Boolean(
        string='Sales Person'
    )
    sales_number = fields.Integer(
        string='Sales number: '
    )
    commission = fields.Float(
        string='commission', default=10
    )
    _sql_constraints = [
        ('unique_sales_number',
         'unique(sales_number)',
         'Sales number must be unique.'),
    ]

    @api.constrains('is_sales_person', 'sales_number')
    def _check_sales_number_constraint(self):
        for record in self:
            if record.is_sales_person and not record.sales_number:
                raise exceptions.ValidationError(
                    'Sales person must have a sales number.'
                    )

    def unlink(self):
        for record in self:
            if record.is_sales_person and record.sales_number:
                raise exceptions.ValidationError(
                    'Cannot delete a sales person with sales numbers.'
                    )
        return super(ResPartner, self).unlink()
