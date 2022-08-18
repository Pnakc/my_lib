from odoo import models, fields, api


class MlReaderHistory(models.Model):
    _name = "ml.reader.history"
    _description = "Lịch sử mượn sách"

    book_id = fields.Char("Mã sách")
    name = fields.Char("Tên sách", required=True)
    date_start = fields.Date("Ngày mượn")
    date_end = fields.Date("Ngày hẹn trả")
    date_real = fields.Date("Ngày trả")
    warning = fields.Char("Cảnh báo trả quá hạn")
    reader_id = fields.Many2one(comodel_name='ml.reader',
                                string='Lịch sử mượn sách')
