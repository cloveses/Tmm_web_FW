WEB站点框架

已实现基本功能：默认页、注册、登录、登出、验证码等功能。
主要应用tornado+mako+mongoDB实现

manage.py web系统入口主文件
settings.py web系统配置文件
db 数据库模型定义及相关操作模块目录
lib 信赖模块目录（debian8_x86_64系统下可用）
managehdl 后台管理处理器目录
mylib 自定义相关功能模块
publichdl 公用处理器相关模块
sitehdl 前台处理器目录
views 视图目录
views\static  静态文件服务目录
views\templates  模板文件目录

依赖第三方模块：pymongo,mongoengine,torando,pillow,mako
