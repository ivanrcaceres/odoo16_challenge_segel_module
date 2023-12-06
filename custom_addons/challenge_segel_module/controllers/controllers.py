# -*- coding: utf-8 -*-
# from odoo import http


# class ChallengeSegelModule(http.Controller):
#     @http.route('/challenge_segel_module/challenge_segel_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/challenge_segel_module/challenge_segel_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('challenge_segel_module.listing', {
#             'root': '/challenge_segel_module/challenge_segel_module',
#             'objects': http.request.env['challenge_segel_module.challenge_segel_module'].search([]),
#         })

#     @http.route('/challenge_segel_module/challenge_segel_module/objects/<model("challenge_segel_module.challenge_segel_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('challenge_segel_module.object', {
#             'object': obj
#         })
