from odoo import models, fields

class FleetWorkShift(models.Model):
    _name = 'fleet.work.shift'
    _description = 'Fleet Work Shift'

    name = fields.Char(string='Shift Name', required=True, translate=True)
    hours_per_day = fields.Float(string='Hours per Day', required=True)
    start_time = fields.Float(string='Start Time (HH:MM)', required=True, default=6.0, help="Shift start time in decimal format (e.g., 6.5 = 06:30 AM)")
    end_time = fields.Float(string='End Time (HH:MM)', required=True, default=16.0, help="Shift end time in decimal format (e.g., 16.5 = 04:30 PM)")
    active = fields.Boolean(default=True)
