
from odoo import fields, models


class ProjectTask(models.Model):

    _inherit = "project.task"


    successor_id = fields.Many2one("project.task", "Successor")