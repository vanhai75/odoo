{
    'name': "My pet",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': '',
    'website': '',
    'category': 'Uncategorized',
    'version': '0.1',
    'assets': {
        'web.assets_backend': [
            '/mypet/static/src/js/bold.js',
        ],
    },
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_views.xml',
        'wizard/batch_update.xml',
        'views/res_config_settings_views.xml',

    ],
    'qweb': [
        # 'static/src/xml/templates.xml',
        'mypet/static/src/xml/button_recover_debt.xml',
    ],
'assets': {
        'web.assets_qweb': [
            'mypet/static/src/js/button_recover_debt.js',
        ],
        'web.assets_backend': [
            'mypet/static/src/xml/button_recover_debt.xml',
        ],
},
    'installable': True,
    'application': True,
}
