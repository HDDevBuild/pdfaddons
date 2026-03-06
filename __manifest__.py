{
    'name': 'Custom PDF Download',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Generate PDFs via wkhtmltopdf and provide a simple download button',
    'author': 'Your Name',
    'depends': ['web'],  # depends on web for UI modifications
    'data': [
        'views/assets.xml',
        'views/custom_button.xml',
    ],
    'installable': True,
    'application': False,
}
