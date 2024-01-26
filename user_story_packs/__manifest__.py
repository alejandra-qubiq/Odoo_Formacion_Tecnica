# Copyright 2019 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "User Story Packs",
    "summary": "User Stories Packs",
    "version": "17.0.1.0.0",
    "category": "Base",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['sale'],
    "data": [
        'views/product_template.xml',
        "security/ir.model.access.csv",
        'views/product_pack_lines.xml',
        'reports/report_pack_template.xml',
        'reports/report.xml'
    ],
}
