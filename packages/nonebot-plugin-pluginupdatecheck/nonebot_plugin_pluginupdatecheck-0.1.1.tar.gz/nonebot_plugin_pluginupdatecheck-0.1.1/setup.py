# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_pluginupdatecheck']

package_data = \
{'': ['*']}

install_requires = \
['nonebot2>=2.0.0rc2,<3.0.0', 'numpy>=1.24.3,<2.0.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'nonebot-plugin-pluginupdatecheck',
    'version': '0.1.1',
    'description': 'A plugin of chatbot based on nonebot2 framework,it can check the updateable plugins already installed.Also can install new plugins.',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# nonebot_plugin_pluginupdatecheck\n\nnonebot2便携插件安装器\n\n</div>\n\n## 💬 前言\n\n一个nonebot2的插件便捷安装和升级插件（基于nb-cli和pip)\n\n## 📖 介绍\n\n为了方便我在手机上直接控制bot安装和更新插件而开发的一款插件\n\n## 💿 安装\n\n<details>\n<summary>nb-cli安装</summary>\n在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装\n  \n    nb plugin install nonebot-plugin-pluginupdatecheck\n\n</details>\n\n<details>\n<summary>pip安装</summary>\n  \n    pip install nonebot-plugin-pluginupdatecheck\n\n</details>\n\n## 🎉 使用\n\n检测插件更新：输入检测插件更新、检查插件更新\n\n![image](https://github.com/xi-yue-233/nonebot-plugin-pluginupdatecheck/assets/58218656/f6defd18-6279-45f4-a009-83cfda529e2d)\n![20230516225101](https://github.com/xi-yue-233/nonebot-plugin-pluginupdatecheck/assets/58218656/8d26d5d0-ef2b-458b-803e-0aa0afc5fa41)\n\n更新指定插件：输入更新插件“你指定的插件”空格后加的数字编号代表python源（默认清华源）\n\n![20230516225504](https://github.com/xi-yue-233/nonebot-plugin-pluginupdatecheck/assets/58218656/74707dc0-2bd8-46b9-b143-2a23e885ad39)\n\n\n安装指定插件：输入安装插件“你指定的插件”空格后加的数字编号代表python源（默认清华源）\n\n![20230516225647](https://github.com/xi-yue-233/nonebot-plugin-pluginupdatecheck/assets/58218656/aa60add9-93e2-4da6-8eff-fcd3085441cd)\n\n查看源：查看可以用的python源，前面的数字编号可以在插件安装的时候使用\n\n![20230516225748](https://github.com/xi-yue-233/nonebot-plugin-pluginupdatecheck/assets/58218656/e6e7f048-f75e-4a2f-9c9c-eb2ec8cec271)\n\n添加env环境变量：输入添加env后接要加的变量\n\n![20230516225930](https://github.com/xi-yue-233/nonebot-plugin-pluginupdatecheck/assets/58218656/c424be62-b99b-486b-83a3-4b458be6c086)\n![20230516230020](https://github.com/xi-yue-233/nonebot-plugin-pluginupdatecheck/assets/58218656/ce09af1d-72e3-448a-8c42-65f902d48f08)\n',
    'author': 'xi-yue-233',
    'author_email': '1004514855@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
