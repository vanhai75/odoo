from odoo import api,fields,models
class ClassInformation(models.Model):
    _name = "class.information"
    _description = "class Managent"
    name = fields.Char(string='Tên Lớp ')
    grade = fields.Char(string='Khối ')
    mainTeacher= fields.Char('Giáo viên chủ nhiệm')
    school_id = fields.Many2one("school.information", string="School")
class SchoolInformation(models.Model):
    _inherit='school.information'
    class_id= fields.One2many('class.information','school_id',string='Danh sach')
