{
    'name': 'flex landing orders',
    'version': '1.0',
    'summary': 'flex landing orders',
    'description': 'flex landing orders',
    'category': 'Uncategorized',
    'author': 'Abdalrahman Shahrour',
    'website': 'https://www.flex-ops.com',
    'license': 'AGPL-3',
    'depends': ['base', 'sale', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/landing_orders.xml',
        'report/report.xml',
        'views/sale_orders.xml',
        'views/contacts.xml',
    ],
    'installable': True,
    'auto_install': False,
}

# report_invoice_document
# t-name="account.report_invoice_with_payments"
