from odoo import api,fields,models
class ClassInformation(models.Model):
    _name = "student.information"
    _description = "Student Managent"
    name = fields.Char(string='Ho Va Teen',required=True)
    birthday = fields.Date(string="Ngay Sinh",required=True)
    class_id = fields.Many2one("class.information",string='Lop',required = True)
