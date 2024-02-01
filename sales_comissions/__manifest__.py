# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sales Comissions",
    "summary": "Module that adds sales comissions to sales orders",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['base', 'sale'],
    "data": [
        'views/res_partner.xml',
        # 'views/report_sales.xml',
        'views/sale_order.xml',
        "security/ir.model.access.csv",
    ],
}
