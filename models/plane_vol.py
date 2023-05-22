from odoo import models, fields     
class plane_vol(models.Model): 
    _name = 'plane.vol' 
    codi = fields.Integer('Codi', required=True) 
    passatgers = fields.Integer('Passatgers')     
    dataSortida = fields.Date('Data de sortida')     
    dataArribada = fields.Date('Data d''arribada')
    
    origen_id = fields.Many2one('plane.aeroport',string='Origen')
    desti_id = fields.Many2one('plane.aeroport',string='Desti')

    avio_id = fields.Many2one('plane.avio',string='Avio')

    pilot_id = fields.Many2one('plane.pilot',string='pilot')