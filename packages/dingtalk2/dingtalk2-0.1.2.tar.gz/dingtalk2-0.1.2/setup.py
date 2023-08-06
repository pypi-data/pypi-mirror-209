# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dingtalk2']

package_data = \
{'': ['*']}

install_requires = \
['asyncio>=3.4.3,<4.0.0', 'httpx>=0.24.0,<0.25.0', 'loguru>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'dingtalk2',
    'version': '0.1.2',
    'description': '',
    'long_description': '# DingTalk2 介绍\n\n[![image](https://img.shields.io/pypi/v/dingtalk2.svg)](https://pypi.python.org/pypi/dingtalk2)\n[![image](https://img.shields.io/travis/bopo/dingtalk2.svg)](https://travis-ci.com/bopo/dingtalk2)\n[![Documentation Status](https://readthedocs.org/projects/dingtalk2/badge/?version=latest)](https://dingtalk2.readthedocs.io/en/latest/?version=latest)\n\n钉钉支持 Webhook 模式接入事件推送、机器人收消息以及卡片回调等\n\n-   开源协议: MIT license\n-   使用文档: <https://dingtalk2.readthedocs.io>.\n\n## 快速开始\n\n### 准备工作\n\n* Python3 开发环境，https://www.python.org/\n* 钉钉机器人的 token\n\n### 快速开始指南\n\n1、安装 dingtalk2\n\n```Shell\npython -m pip install dingtalk2\n```\n\n2、使用 dingtalk2\n\n```python\nfrom dingtalk2 import dingtalk\n\naccess = \'6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfcxxxxxxx\'\nsecret = \'SEC0ed50da84fca5e37491b032a660dcfd2fd6aef8e2dcb74caa39ddxxxxxxxxxx\'\n\nclient = dingtalk.DingTalk(access=access, secret=secret)\n\nclient.text("hello")\nclient.image(pic_url=\'http://uc-test-manage-00.umlife.net/jenkins/pic/flake8.png\')\n\n```\n\n\n### 技术支持\n\n可以搜索共创群，答疑交流。\n\n共创群ID：xxx （钉钉搜索群号入群）；\n\n也可以扫码入群：\n\n',
    'author': 'bopo',
    'author_email': 'ibopo@126.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
