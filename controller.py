from odoo import http
from odoo.http import request

class TrackPemesanan(http.Controller):

    @http.route('/api/track_pemesanan/<int:pemesanan_id>', type='json', auth='public', methods=['GET'])
    def track_pemesanan(self, pemesanan_id):
        pemesanan = request.env['pemesanan.ruangan'].sudo().browse(pemesanan_id)
        if not pemesanan:
            return {'error': 'Pemesanan tidak ditemukan'}
        
        return {
            'nomor_pemesanan': pemesanan.nomor_pemesanan,
            'status_pemesanan': pemesanan.status_pemesanan,
            'tanggal_pemesanan': pemesanan.tanggal_pemesanan,
            'nama_pemesanan': pemesanan.nama_pemesanan
        }
