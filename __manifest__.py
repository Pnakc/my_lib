# -*- coding: utf-8 -*-
{
    'name': "My Library",
    'summary': """Thư viện""",
    'description': """Quản lý thư viện""",
    'author': "Nguyễn Hưng",
    'website': "",
    'category': 'Uncategorized',
    'version': '1',
    'depends': [
        'product',
    ],
    'data': [
        'views/ml_books.xml',
        'views/menu.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}