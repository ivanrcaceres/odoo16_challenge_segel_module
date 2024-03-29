# -*- coding: utf-8 -*-
{
    'name': "challenge_segel_module",

    'summary': """
        Modulo para evaluar conocimiento odoo 16""",

    'description': """
        Modulo para evaluar conocimiento odoo 16
    """,

    'author': "Ivan Caceres",
    'website': "https://www.linkedin.com/in/ivan-rodrigo-caceres-cartaman-b80a3b153/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_partner_extended_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
