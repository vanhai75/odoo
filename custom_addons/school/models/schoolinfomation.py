from odoo import api, fields, models
class SchoolInformation(models.Model):
    _name = "school.information"
    _description = "School Information"

    name = fields.Char(string="Tên Trường")
    type = fields.Selection([("private", "Dân Lập"), ("public", "Công Lập")], default="public", string="Loại Trường")
    email = fields.Text(string="Email")
    address = fields.Text(string="Địa Chỉ")
    phoneNu = fields.Char(string="Số Điện Thoại")
    hasOnlineClass = fields.Boolean(string="Có lớp online Không")
    rank = fields.Integer(string="Xếp Hạng ")
    establishDay= fields.Date(string="Ngày thành lập ")
    document = fields.Binary(string="Tài liệu trường ")
    document_name=fields.Char(string="Tên tài liệu ")

