from odoo import models, fields     
class plane_vol(models.Model): 
    _name = 'plane.vol' 
    codi = fields.Integer('Codi', required=True) 
    passatgers = fields.Integer('Passatgers')     
    dataSortida = fields.Date('Data de sortida')     
    dataArribada = fields.Date('Data d''arribada')