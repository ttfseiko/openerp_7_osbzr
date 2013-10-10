基于 OpenERP20130721

持续跟进三个官方库

  http://bazaar.launchpad.net/~openerp/openobject-addons/7.0/changes
  
  http://bazaar.launchpad.net/~openerp/openobject-server/7.0/changes
  
  http://bazaar.launchpad.net/~openerp/openerp-web/7.0/changes
  
增加有用的社区模块

合并官方未接受的合并请求

管理中文社区发现的bug和提交的patch

如何参与开发：
-------------
1 // 添加 osbzr 的 remote 只需要做一次
git remote add osbzr http://git.oschina.net/osbzr/openerp_7_osbzr.git

2 // 拉 主干代码到本地
git fetch osbzr

3 // 合并 主干代码到本地
git merge osbzr/master

4 // 推送 本地合并后的代码到 fork 项目
git push origin master

5// 向主项目提交合并请求
