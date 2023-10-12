from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Player(models.Model):
    _name = 'player'
    _description = 'Player'

    number = fields.Char( string='Number')
    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Image', attachment=True)
    country = fields.Char(string='Country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    day_of_birth = fields.Datetime(string='Day of Birth')
    position = fields.Char(string='Position', groups='mo_football.group_player_manager')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')
    salary = fields.Float(string='Salary')
    tax = fields.Float(string='Tax')
    total_salary = fields.Float(string='Total Salary', compute='_compute_total_salary')
    sequence = fields.Integer(string='Sequence',)


    @api.depends('salary', 'tax')
    def _compute_total_salary(self):
        for record in self:
            record.total_salary = record.salary - (record.salary * (record.tax / 100))

    @api.constrains('salary')
    def _check_salary_positive(self):
        for record in self:
            if record.salary <= 0:
                raise ValidationError("Salary must be greater than zero")

    @api.model
    def create(self, vals):
        vals['sequence']=self.env['ir.sequence'].next_by_code('number.code')
        vals['number'] = f'PRL/{fields.Date.today().year}/{vals["sequence"]}'

        player = super(Player, self).create(vals)
        return player


