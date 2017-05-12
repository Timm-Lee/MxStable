# 慕学在线稳定版



## 技术栈

本版本选取的技术栈为：Python 2.7 + Django 1.9 + 原生 Admin + 原生分页 + PyMySQL。

主要原因是：

* Python 2.7：因为 Python3 取消了 reload() 方法，因此无法通过 reload() 修改系统默认编码，进而会导致在 Ubuntu 14.04 上的 Python 3.4 中安装 django-pure-pagination 是会出现解码错误。
* Django 1.9：Django 1.8 -1.10 的改动幅度较小。但是 Django 1.11 修改了某些插件的渲染方式，改动较大。
* 原生 Admin：Django 自带，稳定性好，不用考虑 Python 兼容性等问题。
* 原生分页：同上。
* PyMySQL：Python 编写的数据库接口，目前尚未发现兼容性或其它问题。相比而言，MySQL-python 和 mysqlclient 两个包需要解决在 Mac OS 10.11.6 上出现的 `image not found` 的问题（可以通过软连接解决）。






