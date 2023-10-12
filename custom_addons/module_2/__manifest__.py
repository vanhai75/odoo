{
    'name': "Module_2",
    'summary': """player model""",
    'description': """Managing pet information""",
    'author': '',
    'website': '',
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
    ],
    'data': [
        'security/player_security.xml',
        'security/ir.model.access.csv',
        'views/player_view.xml',
        'demo/demo.xml',
        'data/account_data.xml',



    ],
    'qweb': [
        # 'static/src/xml/templates.xml',
        'static/src/xml/btn_tree_multi_update.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
