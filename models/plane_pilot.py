from odoo import models, fields     
class plane_pilot(models.Model): 
    _name = 'plane.pilot' 
    codi = fields. Integer('Codi', required=True) 
    nom = fields.Char('Nom', required=True)     
    cognoms = fields.Char('Cognoms')     
    nif = fields.Char('NIF')   
    telf = fields.Char('Telefon')
    email = fields.Char('Email')