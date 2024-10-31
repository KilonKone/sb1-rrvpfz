from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
import werkzeug

class MathCaptchaHome(Home):

    @http.route()
    def web_login(self, redirect=None, **kw):
        if request.httprequest.method == 'POST':
            user_answer = request.params.get('math_answer')
            if not user_answer or int(user_answer) != 4:  # 1 + 3 = 4
                request.params['login_success'] = False
                return request.render('web.login', {
                    'error': 'Incorrect math answer. Please try again.'
                })
        
        response = super(MathCaptchaHome, self).web_login(redirect=redirect, **kw)
        if request.params.get('login_success', False):
            return response
            
        return response