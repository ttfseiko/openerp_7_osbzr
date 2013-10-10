account_standard_costing
========================

修改自盎格鲁萨克森模块。已经实现标准成本下采购价格差异记账；生产成本差异记账待实现  https://github.com/oliverzgy/standard_costing

已实现 
------
采购价格差异记账

- 采购入库

  借 库存材料
  
  贷 材料采购

- 录入发票

  借 材料采购

  借 进项税额

  贷 应付账款

  借/贷 商品进销差价