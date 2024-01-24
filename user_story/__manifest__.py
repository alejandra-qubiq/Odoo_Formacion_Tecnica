# Copyright 2019 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "User Story",
    "summary": "User Stories",
    "version": "17.0.1.0.0",
    "category": "Base",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['base', 'sale'],
    "data": [
        'views/res_partner.xml',
        'views/report_sales.xml',
        'views/sale_order.xml',
        "security/ir.model.access.csv",
    ],
}
