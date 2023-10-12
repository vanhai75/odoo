from odoo import api, fields, models
class SchoolInformation(models.Model):
    _name = "school.information"
    _description = "School Management"

    name = fields.Char(string="Tên Trường")
    type = fields.Selection([("private", "Dân Lập"), ("public", "Công Lập")], default="public", string="Loại Trường")
    email = fields.Text(string="Email")
    address = fields.Text(string="Địa Chỉ")
    phoneNu = fields.Char(string="So dien thoai")
    hasOnlineClass = fields.Boolean(string="Co Lop Online Khoong")
    rank = fields.Integer(string="xep hang")
    establishDay= fields.Date(string="ngay thanh lap")
    document = fields.Binary(string="tai lieu truong")
    document_name=fields.Char(string="ten Tai Lieu")