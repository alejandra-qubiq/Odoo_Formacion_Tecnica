# Copyright 2019 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Book Library",
    "summary": "Book Repository",
    "version": "17.0.1.0.0",
    "category": "Base",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['base', "product", "sale"],
    "data": [
        'security/ir.model.access.csv',
        'reports/layout.xml',
        'reports/reports.xml',
        'reports/report_book_custom.xml',
        'reports/sale_report_inherit.xml',
        'security/security.xml',
        'views/library_audit.xml',
        'views/res_partner.xml',
        'views/book_library.xml',
        'views/library_book_genre.xml',
        'views/library_book_component_line.xml',
        'views/book_library_menus.xml',
    ],
}
