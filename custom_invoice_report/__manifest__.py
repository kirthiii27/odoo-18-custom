{
    'name': 'Custom Invoice Report',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Custom invoice report with outstanding credits and PD cheques',
    'description': 'This module customizes the invoice report to include outstanding credits and post-dated cheques.',
    'author': 'Your Name',
    'depends': ['account', 'base', 'sale','web'],
    'data': [
        'report/custom_invoice_report.xml',
        'report/custom_ipos_nvoice_report.xml',
        'views/custom_views.xml'

    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'custom_invoice_report/static/src/js/print_invoice.js',  # Path to your JavaScript file
    #     ],
    #     'web.report_assets_common': [
    #             ],
    # },
    'installable': True,
    'application': False,
    'auto_install': False,
}
