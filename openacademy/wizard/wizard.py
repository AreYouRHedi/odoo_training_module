from odoo import models, fields, api
from random import choices
import time


class Wizard(models.TransientModel) :
    _name = 'openacademy.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    def _default_sessions(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('openacademy.session',
                                 string="Sessions", required=True, default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def subscribe(self):
        #for session in self.session_ids:
        #    session.attendee_ids |= self.attendee_ids
        #return {}
        countries = ['France', 'United Kingdom', 'Spain', 'Afghanistan']

        #test 1
        start_time = time.time()
        country_db = self.env["res.country"].search([])
        for i in range(10000):
            if choices(countries)[0] in country_db:
                continue
        print("TEST 1:", time.time() - start_time)

        #test2
        start_time = time.time()
        for i in range(10000):
            name = self.env["res.country"].search([("name", "=", choices(countries)[0])])
            if name:
                continue
        print("TEST 2:", time.time() - start_time)

