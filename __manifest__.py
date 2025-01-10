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
        # 'reports/mbf_sph_report.xml',
        
        
    ],
    'installable': True,
    'application': True,
}