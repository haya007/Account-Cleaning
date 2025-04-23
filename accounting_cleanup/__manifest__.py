# -*- coding: utf-8 -*-
{
    'name': "Accounting Cleanup",

    'summary': "Unlinking all records in Account Move and Account Payment",

    'description': """
This module provides a simple cleanup wizard for development and testing environments.

It allows you to:
- Cancel and delete all Customer Invoices, Vendor Bills, Credit Notes, and Journal Entries (`account.move`)

⚠️ Use this only in non-production environments (like Odoo.sh dev or staging branches).
    """,

    'author': "Hayagreeva Kasibhotla",
    'website': "https://www.byteeit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Cleaning',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'insurance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/accounting_cleanup_wizard.xml',
    ],
}
