# -*- coding: utf-8 -*-

{
    'name': 'MalPhi',
    'version': '1',
    'category': 'MalPhi',
    'summary': 'MalPhi system',
    'description': """
This application allows you to manage your customers for MalPhi.
    """,
    'depends': ['skyguyver_base'],
    'data': ['views/malphi_views.xml'
             ,'views/malphi_menus.xml'
            # ,'data/customer_acct_sequence.xml'
             ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto-install': False,
    'application': True,
}
