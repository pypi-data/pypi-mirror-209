# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_adbc', 'async_adbc.plugins', 'async_adbc.service']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.7,<0.6.0']

setup_kwargs = {
    'name': 'async-adbc',
    'version': '1.0.5',
    'description': '',
    'long_description': '# ADBC\n\nADBC是ADB Client的纯python异步实现，ADBC直接跟ADB Server通信不需要靠进程调用命令行来执行ADB命令。\n有以下特性：\n1. 支持async/await和同步调用\n2. 封装了一些性能测试有用的接口，供性能采集工具使用\n\n## 参考\n1. adb协议 https://github.com/kaluluosi/adbDocumentation/blob/master/README.zh-cn.md\n2. ppadb https://github.com/Swind/pure-python-adb',
    'author': 'kaluluosi',
    'author_email': 'kaluluosi@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
