# import json
# import werkzeug
from odoo import http
from odoo.http import request

class MountainController(http.Controller):
    @http.route('/create', auth='public', type='http')
    def player_check(self):
        partner = request.env['player'].sudo().create({
            'name': 'Lionel Messi',
            'country': 'Argentina',
            'gender': 'male',
            'position': 'Forward',
            'height': 170.0,
            'weight': 72.0,
            'salary': 1000000.0,
            'tax': 20.0,
        })
        return 'create!!'
    @http.route('/update', auth='public', type='http')
    def player_update(self):

        player = request.env['player'].sudo().search([('name', '=', 'Lionel Messi')])

        if player:
            # Update the player's information
            player.write({
                'position': 'Midfielder',
                'salary': 1100000.0,
                'tax': 30.0,
            })
            return 'Player updated!'
        else:
            return 'Player not found!'
    # thay doi