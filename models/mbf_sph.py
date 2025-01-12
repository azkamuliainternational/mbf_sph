from odoo import models, fields, api
from datetime import date



class MbfSph(models.Model):
    _name = 'mbf.sph'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']  # Include necessary mixins

    _description = 'Surat Penawaran Harga'
    _order = 'date_penawaran desc'

    name = fields.Char(string='Nomor Surat Penawaran',  required=True, copy=False, readonly=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('mbf.sph'))
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    date_penawaran = fields.Date(string='Tanggal Penawaran',  default=lambda self: date.today(), required=True)
    date_berlaku = fields.Date(string='Tanggal Berlaku')
    user_id = fields.Many2one('res.users', string='User ', default=lambda self: self.env.user)
    masa_berlaku = fields.Integer(string='Masa Berlaku (Hari)')
    perihal = fields.Char(required=True,string='Perihal', track_visibility='onchange')
    header = fields.Text(required=True,string='Header Surat', track_visibility='onchange')
    footer = fields.Text(required=True,string='Footer Surat', track_visibility='onchange')
    note = fields.Text(required=True,string='Note')
    
    cara_pengiriman =  fields.Char(string='Cara Pengiriman')
    tgl_pengiriman = fields.Date(string='Tanggal Pengiriman')
    alamat_pengiriman= fields.Char(string='Alamat Pengiriman')
    respon= fields.Text(string='Catatan Customer')
    state= fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Terkirim'), ('done', 'Berhasil'), ('cancel', 'Gagal')],
        string='State',
        default='draft',
        required=True,
        track_visibility='onchange'
    )
    
    

    line_ids = fields.One2many('mbf.sph.line', 'sph_id', string='Detail Produk')
    def print_sph_report(self):
        """
        Method to generate and print the report for Surat Penawaran.
        Replace this logic with your custom report action.
        """
        # This assumes you have a report action defined (replace `report_name` with your actual report)
        return self.env.ref('mbf_sph.action_report_mbf_sph').report_action(self)
    
    
    @api.multi
    def action_confirm(self):
        for record in self:
            record.state = 'confirm'

    @api.multi
    def action_done(self):
        for record in self:
            record.state = 'done'
    @api.multi
    def action_cancel(self):
        for record in self:
            record.state = 'cancel'
    @api.multi
    def action_reset_to_draft(self):
        for record in self:
            record.state = 'draft'    

class MbfSphLine(models.Model):
    _name = 'mbf.sph.line'
    _description = 'Detail Produk Surat Penawaran'

    sph_id = fields.Many2one('mbf.sph', string='Surat Penawaran', required=True)
    product_id = fields.Many2one('product.product', string='Product', domain=[('sale_ok', '=', True)], change_default=True, ondelete='restrict')
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure')
    price_unit = fields.Float('Unit Price', required=True,default=0.0)
    discount = fields.Float(string='Discount (%)',  default=0.0)
    price_net = fields.Float(string='Harga Setelah Disc', compute='_compute_price_net', store=True)
    
    @api.depends('price_unit', 'discount')
    def _compute_price_net(self):
        """
        Compute the price after applying the discount.
        """
        for line in self:
            discount_factor = (100 - line.discount) / 100.0
            line.price_net = line.price_unit * discount_factor
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        """
        Set price_unit to the product's list_price when a product is selected.
        """
        if self.product_id:
            self.price_unit = self.product_id.list_price
             # Set the product_uom from the product template's uom_id
            self.product_uom = self.product_id.uom_id
        else:
            self.price_unit = 0.0
            self.product_uom = False