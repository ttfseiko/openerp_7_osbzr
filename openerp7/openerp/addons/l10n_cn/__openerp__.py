# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': '中国会计科目表',
    'version': '7.0',
    'category': 'Localization/Account Charts',
    'author': 'www.openerp-china.org',
    'maintainer':'www.openerp-china.org',
    'website':'http://openerp-china.org',
    'url': 'http://www.openerp-china.org/index.php?page=l10n_cn',
    'description': """
科目类型\会计科目表模板\增值税\辅助核算类别\管理会计凭证簿\财务会计凭证簿

添加中文省份数据

增加小企业会计科目表
    """,
    'depends': ['base','account'],
    'demo': [],
    'data': [
        'account_tax.xml',
        'account_chart_type.xml',
        'account_chart_template.xml',
        'account_chart_small_business_template.xml',
        'l10n_chart_cn_wizard.xml',
        'base_data.xml',
    ],
    'license': 'GPL-3',
    'auto_install': False,
    'installable': True,
    'images': ['images/config_chart_l10n_cn.jpeg','images/l10n_cn_chart.jpeg'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

