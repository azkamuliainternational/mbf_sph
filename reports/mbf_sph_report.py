from odoo import models

class ReportMbfSph(models.AbstractModel):
    _name = 'report.surat_penawaran_harga.report_mbf_sph'
    _description = 'Laporan Surat Penawaran Harga'

    def get_report_values(self, docids, data=None):
        docs = self.env['mbf.sph'].browse(docids)
        return {
            'docs': docs,
        }