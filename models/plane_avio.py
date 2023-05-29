from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    codi = fields.Integer('Codi', required=True)
    imatge = fields.Char('Imatge')
    marca = fields.Char('Marca')
    model = fields.Char('Model')
    maxVel = fields.Float('Maxima velocitat')

    vols_id = fields.One2many('plane.vol','avio_id',string='Vols')