# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Agregamos 2 nuevas variable exento_de_impuestos y exento_de_impuestos_char
    # exento_de_impuestos es para marcar en el formulario
    # exento_de_impuestos_char es para mostrar en la lista tree

    exento_de_impuestos = fields.Boolean(string='Exento de Impuestos')
    exento_de_impuestos_char = fields.Char(size=2, string="Exento de Impuestos")

    @api.model
    def create(self, values):
        if 'exento_de_impuestos' in values:
            if values['exento_de_impuestos']:
                values['exento_de_impuestos_char'] = 'Si'
            else:
                values['exento_de_impuestos_char'] = 'No'
        else:
            values['exento_de_impuestos_char'] = 'No'
        new_record = super(ResPartner, self).create(values)
        return new_record

    @api.model
    def write(self, values):
        if 'exento_de_impuestos' in values:
            if values['exento_de_impuestos']:
                values['exento_de_impuestos_char'] = 'Si'
            else:
                values['exento_de_impuestos_char'] = 'No'
        else:
            values['exento_de_impuestos_char'] = 'No'
        result = super(ResPartner, self).write(values)
        return result

