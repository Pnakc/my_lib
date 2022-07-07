from odoo import models, fields, api


class MlBooks(models.Model):
    _name = "ml.books"
    _description = "Sách"

    name = fields.Char("Tên sách", required=True)
    author = fields.Char("Tên tác giả", required=True)
    year = fields.Integer("Năm xuất bản")
    publishing_company = fields.Char("Nhà xuất bản")
