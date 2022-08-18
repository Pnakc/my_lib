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
        'product', 'base',
    ],
    'data': [
        # 'security/account_security.xml',
        # 'security/ir.model.access.csv',
        'views/ml_books.xml',
        'views/ml_author.xml',
        'views/ml_reader.xml',
        'views/ml_publisher.xml',
        'views/menu.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}