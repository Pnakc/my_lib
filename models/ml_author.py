from odoo import models, fields, api


class MlAuthor(models.Model):
    _name = "ml.author"
    _description = "Tác giả"

    author_id = fields.Char("ID", required=True)
    name = fields.Char("Tên tác giả", required=True)
    date_birth = fields.Integer(string="Năm sinh")
    date_death = fields.Integer(string="Năm mất")
    country = fields.Char("Quốc tịch")
    achievement = fields.Text("Thành tựu")
    book = fields.Char("Tác phẩm", required=True)
    author_pic = fields.Binary("Hình ảnh", attachment=True)
    

    # @api.model
    # def year_selection(self):
    #     self.year_list = []
    #     for year in range(1800, 2100):
    #         self.year_list.append(year)
    #     return self.year_list
