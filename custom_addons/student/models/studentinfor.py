from odoo import api,fields,models
class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student Managent"
    name = fields.Char(string='Họ Và Tên',required=True)
    birthday = fields.Date(string="Ngày Sinh ",required=True)
    class_id = fields.Many2one("class.information", string='Lớp')

class ClassInformation(models.Model):
    _inherit='class.information'
    student_list= fields.One2many('student.information','class_id',string='Danh sach')
