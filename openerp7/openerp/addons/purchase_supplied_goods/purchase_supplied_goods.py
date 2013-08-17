# -*- coding: utf-8 -*-
##############################################################################
#
#    Purchase Supplied Goods - OpenERP Module
#    Copyright (C) 2013 Shine IT (<http://www.openerp.cn).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv

class ProductProduct(osv.osv):
    _inherit = 'product.product'

    def search(self, cr, uid, args, offset=0, limit=None, order=None,
            context=None, count=False):
        context = context or {}
        if context.get('partner_id'):
            supplier_info_obj = self.pool.get('product.supplierinfo')
            supplierinfo_ids = supplier_info_obj.search(cr, uid, 
                    [('name', '=', context['partner_id'])], context=context)
            if supplierinfo_ids:
                supplied_products = supplier_info_obj.read(cr, uid,
                        supplierinfo_ids, ['product_id'], context=context)
                product_ids = map(lambda x: x['product_id'][0],
                        supplied_products)
                args.extend(( '|',('id', 'in', product_ids),
                    ('seller_ids', '=', None) ))
        return super(ProductProduct, self).search(cr, uid, args, offset, limit,
                order, context, count)



            

