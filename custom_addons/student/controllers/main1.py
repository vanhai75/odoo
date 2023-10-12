from odoo import http
from odoo.addons.student.controllers.main import MountainController
import werkzeug

class MountainController(MountainController):

    @http.route('/mountain')
    def mountain_check(self):
        super(MountainController, self).mountain_check()
        return werkzeug.utils.redirect('https://www.google.com')