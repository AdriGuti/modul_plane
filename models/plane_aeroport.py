from odoo import models, fields     
class plane_aeroport(models.Model): 
    _name = 'plane.aeroport' 
    codi = fields. Integer('Codi', required=True) 
    nom = fields.Char('Nom', required=True)     
    imatge = fields.Char('Imatge')     
    ciutat = fields.Char('Ciutat')   
    pais = fields.Char('País')
    latitud = fields.Float('Latitud')
    longitud = fields.Float('Longitud')