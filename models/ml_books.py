from odoo import models, fields, api


class MlBooks(models.Model):
    _name = "ml.books"
    _description = "Sách"

    book_id = fields.Char("Mã sách", required=True)
    name = fields.Char("Tên sách", required=True)
    author = fields.Char("Tên tác giả")
    year = fields.Integer(string="Năm xuất bản")
    type = fields.Selection([('1', 'Kinh dị'), ('2', 'Trinh thám'), ('3', 'Tâm lý')], string="Thể loại")
    publisher = fields.Char("Nhà xuất bản")
    amount = fields.Integer("Số sách còn trong kho")
    book_pic = fields.Binary("Hình ảnh", attachment=True)

    # def __init__(self):
    #     self.year_list = []
    #
    # @api.model
    # def year_selection(self):
    #     for year in range(1800, 2100):
    #         self.year_list.append(year)
    #     return self.year_list
