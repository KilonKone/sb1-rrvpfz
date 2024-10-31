{
    'name': 'Math Captcha Login',
    'version': '16.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Add math captcha to login form',
    'description': """
        This module adds a simple math captcha to the login form.
        Users need to solve a simple math problem to login.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'web'],
    'data': [
        'views/login_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}