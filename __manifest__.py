
{
    'name': 'Custom Picking Date',
    'version': '1.0',
    'category': 'Stock',
    'summary': 'Remove readonly restriction on date_done field in stock.picking',
    'description': """
        This module removes the readonly restriction on the date_done field in stock.picking model.
    """,
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
}
