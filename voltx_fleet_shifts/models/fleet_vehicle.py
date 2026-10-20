from odoo import models, fields, _

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    driver_ids = fields.Many2many('res.partner', 'fleet_vehicle_driver_rel', 'vehicle_id', 'driver_id', string='Drivers')

    def action_view_assignation_logs(self):
        self.ensure_one()
        return {
            'name': _('Assignment History'),
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'fleet.vehicle.assignation.log',
            'domain': [('vehicle_id', '=', self.id)],
            'context': {'default_vehicle_id': self.id}
        }
