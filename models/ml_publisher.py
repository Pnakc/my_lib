from odoo import models, fields, api


class MlPublisher(models.Model):
    _name = "ml.publisher"
    _description = "Nhà xuất bản"

    publisher_id = fields.Char("ID", required=True)
    name = fields.Char("Tên nhà xuất bản", required=True)
    date = fields.Integer(string="Năm thành lập")
    address = fields.Char("Địa chỉ trụ sở")
    book = fields.Char("Tác phẩm", required=True)
    publisher_pic = fields.Binary("Hình ảnh", attachment=True)

    # @api.model
    # def year_selection(self):
    #     self.year_list = []
    #     for year in range(1800, 2100):
    #         self.year_list.append(year)
    #     return self.year_list
