# -*- coding: utf-8 -*-
from odoo import http

class Openacademy(http.Controller):
     @http.route('/openacademy', auth='public',website=True)
     def index(self, **kw):
         Session = http.request.env['openacademy.session']
         return http.request.render('openacademy.index', {
             'sessions': Session.search([])
         })
     @http.route('/openacademy/<model("openacademy.session"):session>/', auth='public',
                 website=True)
     def session(self, session, **kw):
         return http.request.render('openacademy.get_session', {
             'session': session
         })

     @http.route('/openacademy/subscription', auth='public', website=True)
     def subscription(self, **kw):
         env = http.request.env
         user = http.request.env.user
         session_id = kw.get("session")
         session = env['openacademy.session'].browse(int(session_id))
         partner = user.partner_id
         #session.write({'attendee_ids': [(4,user['partner_id'].id)]})

         #registration
         registrations = env['openacademy.registration']

         registration = registrations.search([('partner_id', '=', partner.id), ('session_id','=',session.id)], limit=1)
         if registration:
            return http.request.render('openacademy.register_already_validated', {
                'registration': registration
            })
         registrations.create({'session_id': session.id, 'partner_id':partner.id})
         #Send mail
         context = {'test': 'hello world'}
         template = env.ref('openacademy.mail_template_registration_session')
         template.with_context(context).send_mail(partner.id)

         return http.request.render('openacademy.register_validated')



     @http.route('/openacademy/my_sessions', auth='public', website=True)
     def show_sessions(self, **kw):
         user = http.request.env.user
         print(user.partner_id)
         my_sessions = user.partner_id.session_ids
         # registrations = http.request.env['openacademy.registration'].search([('partner_id', '=', user.partner_id.id)])
         registrations = my_sessions.mapped("registration_ids")
         return http.request.render('openacademy.mysessions', {
             'sessions': my_sessions,
             'registrations':registrations,
         })







     # @http.route('/openacademy/openacademy/objects/', auth='public')
     # def list(self, **kw):
     #     return http.request.render('openacademy.listing', {
     #         'root': '/openacademy/openacademy',
     #         'objects': http.request.env['openacademy.openacademy'].search([]),
     #     })
     #
     # @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>/', auth='public')
     # def object(self, obj, **kw):
     #     return http.request.render('openacademy.object', {
     #         'object': obj
     #     })
