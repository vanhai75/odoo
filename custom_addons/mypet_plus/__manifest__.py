{
    'name': "My pet (+)",
    'summary': """My pet plus""",
    'description': """Managing pet information""",
    'author': "Hai",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'mypet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_plus_views.xml',
        'views/product_pet_views.xml',
        'views/my_pet_views.xml',
        # ' views/templates.xml'
    ],
    'qweb': [
# 'static/src/xml/btn_tree_multi_update.xml'
             ],
    'installable': True,
    'application': True,
}