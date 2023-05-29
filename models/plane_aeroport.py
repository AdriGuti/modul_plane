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

    volsSortida_id = fields.One2many('plane.vol','origen_id',string='Vols de sortida')
    volsArribada_id = fields.One2many('plane.vol','desti_id',string='Vols d''arribada')