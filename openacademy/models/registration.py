from odoo import api, fields, models

class Registration(models.Model) :
    _name = "openacademy.registration"

    session_id = fields.Many2one('openacademy.session',ondelete="cascade",string='registration for a session',
                              required=True)
    partner_id = fields.Many2one('res.partner', ondelete="cascade",string='partner for a registration',
                              required=True)
    validated = fields.Boolean(default=False,required=True)

    @api.model
    def _auto_set_validation(self) :
        not_validated_registrations = self.search([('validated', '=', False)])
        not_validated_registrations.write({'validated': True})
        print("done")

    def write(self, vals):
        super().write(vals)

        if "validated" in vals and vals.get("validated"):
            # Send mail
            template = self.env.ref('openacademy.mail_template_registration_session')
            context = {'test': 'Register validated'}
            for record in self:
                template.with_context(context).send_mail(record.partner_id.id)
