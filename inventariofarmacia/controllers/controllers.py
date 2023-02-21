# -*- coding: utf-8 -*-
# from odoo import http


# class inventariofarmacia(http.Controller):
#     @http.route('/inventariofarmacia/inventariofarmacia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventariofarmacia/inventariofarmacia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventariofarmacia.listing', {
#             'root': '/inventariofarmacia/inventariofarmacia',
#             'objects': http.request.env['inventariofarmacia.inventariofarmacia'].search([]),
#         })

#     @http.route('/inventariofarmacia/inventariofarmacia/objects/<model("inventariofarmacia.inventariofarmacia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventariofarmacia.object', {
#             'object': obj
#         })
