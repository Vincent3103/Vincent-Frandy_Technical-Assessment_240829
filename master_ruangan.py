from odoo import models, fields, api, exceptions

class MasterRuangan(models.Model):
    _name = 'master.ruangan'

    name = fields.Char(string='Nama Ruangan', required=True)
    tipe_ruangan = fields.Selection([
        ('kecil', 'Meeting Room Kecil'),
        ('besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string='Tipe Ruangan', required=True)
    lokasi_ruangan = fields.Selection([
        ('1a', '1A'),
        ('1b', '1B'),
        ('1c', '1C'),
        ('2a', '2A'),
        ('2b', '2B'),
        ('2c', '2C')
    ], string='Lokasi Ruangan', required=True)
    foto_ruangan = fields.Binary(string='Foto Ruangan', required=True)
    kapasitas_ruangan = fields.Integer(string='Kapasitas Ruangan', required=True)
    keterangan = fields.Text(string='Keterangan')

class PemesananRuangan(models.Model):
    _name = 'pemesanan.ruangan'

    nomor_pemesanan = fields.Char(string='Nomor Pemesanan', required=True)
    ruangan_id = fields.Many2one('master.ruangan', string='Ruangan', required=True)
    nama_pemesanan = fields.Char(string='Nama Pemesanan', required=True)
    tanggal_pemesanan = fields.Date(string='Tanggal Pemesanan', required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')
    ], string='Status Pemesanan', default='draft')
    catatan_pemesanan = fields.Text(string='Catatan Pemesanan')

    @api.constrains('tanggal_pemesanan', 'ruangan_id')
    def check_room_availability(self):
        for record in self:
            exist = self.search([
                ('ruangan_id', '=', record.ruangan_id.id),
                ('tanggal_pemesanan', '=', record.tanggal_pemesanan),
                ('id', '!=', record.id)
            ])
            if exist:
                raise exceptions.ValidationError('Ruangan sudah dipesan pada tanggal ini.')

    def action_proses_pemesanan(self):
        for record in self:
            if record.status_pemesanan == 'draft':
                record.write({'status_pemesanan': 'ongoing'})
            elif record.status_pemesanan == 'ongoing':
                record.write({'status_pemesanan': 'done'})

    def action_draft(self):
        self.write({'status_pemesanan': 'draft'})

    def action_ongoing(self):
        self.write({'status_pemesanan': 'ongoing'})

    def action_done(self):
        self.write({'status_pemesanan': 'done'})

    def action_cancel(self):
        self.write({'status_pemesanan': 'cancel'})
