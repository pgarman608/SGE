# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medicamento(models.Model):
    _name = 'inventariofarmacia.medicamento'
    _description = 'Medicamento'

    name = fields.Integer('Codigo del Medicamento',required=True)
    nombre = fields.Char(string='Nombre',required=True)
    fabricante = fields.Char(string='Fabricante',required=True)
    forma = fields.Char(string='Forma farmacéutica',required=True)
    numlote = fields.Integer('Numero del lote',required=True)
    precio = fields.Integer('Precio',required=True)

    factura_id = fields.Many2one('inventariofarmacia.factura', 'medicamentos_ids')
    pedido_id = fields.Many2one('inventariofarmacia.pedido', 'medicamentos_ids')

class factura(models.Model):
	_name = 'inventariofarmacia.factura'
	_description = 'Factura'

	name = fields.Integer('Codigo de la factura',required=True)
	nombre_cliente = fields.Char(string='Nombre del cliente', required=True)
	precio_total = fields.Integer('Precio',required=True)
	fecha_factura = fields.Date('Fecha',required=True)

	medicamentos_ids = fields.One2many('inventariofarmacia.medicamento','factura_id',string='Medicamentos')
	
class pedido(models.Model):
    _name = 'inventariofarmacia.pedido'
    _description = 'Pedido'

    name = fields.Integer('Codigo del pedido',required=True)
    nombre_empresa = fields.Char(string='Nombre de la empresa',required=True)
    precio_total = fields.Integer('Precio total',required=True)
    fecha_pedido = fields.Date('Fecha',required=True)

    medicamentos_ids = fields.One2many('inventariofarmacia.medicamento','pedido_id', string='Medicamentos')

#	nombre, fabricante, dosis, forma farmacéutica y número de lote
# class inventariofarmacia(models.Model):
#     _name = 'inventariofarmacia.inventariofarmacia'
#     _description = 'inventariofarmacia.inventariofarmacia'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
