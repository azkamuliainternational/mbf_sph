{
    'name': 'Surat Penawaran Harga',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Modul untuk membuat surat penawaran harga',
    'depends': ['base', 'sale'],
    'data': [
         'security/ir.model.access.csv',
        'views/mbf_sph_views.xml',
        'views/report_mbf_sph_template.xml',
        'views/mbf_sph_report.xml',
          'data/sequence_data.xml',
        #    'views/external_layout_inherit.xml',
        # 'reports/mbf_sph_report.xml',
        
        
    ],
    'assets': {
        'web.assets_backend': [
            'mbf_sph/static/src/css/style_custom.css',  # Add the path to your CSS file here
        ],
    },
 
    'installable': True,
    'application': True,
}