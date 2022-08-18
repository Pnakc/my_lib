from odoo import models, fields, api


class MlReader(models.Model):
    _name = "ml.reader"
    _description = "Độc giả"

    reader_id = fields.Char("Mã độc giả", required=True)
    name = fields.Char("Tên độc giả", required=True)
    date_birth = fields.Date("Ngày sinh")
    ccid = fields.Char("CMND/CCCD")
    phone = fields.Char("Số điện thoại")
    address = fields.Text("Địa chỉ")
    time = fields.Date("Thời gian đăng kí")
    warning_card = fields.Char("Thẻ quá hạn")
    # history = fields.Char("Lịch sử mượn sách")
    history_ids = fields.One2many(
        comodel_name='ml.reader.history',
        inverse_name='reader_id',
        string='Lịch sử mượn sách',
        tracking=True,
        track_visibility='onchange',
        required=False)
