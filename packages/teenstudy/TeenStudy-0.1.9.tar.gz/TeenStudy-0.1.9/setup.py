# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['teenstudy',
 'teenstudy.models',
 'teenstudy.utils',
 'teenstudy.web',
 'teenstudy.web.api',
 'teenstudy.web.pages',
 'teenstudy.web.utils']

package_data = \
{'': ['*'], 'teenstudy': ['resource/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'Pillow>=9.4.0,<10.0.0',
 'amis-python>=1.0.7,<2.0.0',
 'anti-useragent>=1.0.10,<2.0.0',
 'beautifulsoup4>=4.11.2,<5.0.0',
 'bs4>=0.0.1,<0.0.2',
 'fastapi>=0.95.0,<0.96.0',
 'httpx>=0.23.3,<0.24.0',
 'lxml>=4.9.2,<5.0.0',
 'nonebot-adapter-onebot>=2.2.1,<3.0.0',
 'nonebot-plugin-apscheduler>=0.2.0,<0.3.0',
 'nonebot2>=2.0.0rc2,<3.0.0',
 'psutil>=5.9.4,<6.0.0',
 'python-jose>=3.3.0,<4.0.0',
 'qrcode>=7.4.2,<8.0.0',
 'tortoise-orm>=0.19.3,<0.20.0',
 'ujson>=5.7.0,<6.0.0',
 'uvicorn>=0.21.0,<0.22.0']

setup_kwargs = {
    'name': 'teenstudy',
    'version': '0.1.9',
    'description': '基于nonebot2异步框架的青年大学自动提交插件基于nonebot2的青年大学习自动提交插件，用于自动完成大学习，在后台留下记录，返回完成截图',
    'long_description': '<div align="center">\n    <img src="https://i.328888.xyz/2023/02/28/z23ho.png" alt="TeenStudy.png" border="0" width="500px" height="500px"/>\n    <h1>TeenStudy</h1>\n    <b>基于nonebot2和go-cqhttp的青年大学习自动提交插件，用于自动完成大学习，在后台留下记录，返回完成截图</b>\n    <br/>\n    <a href="https://github.com/ZM25XC/TeenStudy/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ZM25XC/TeenStudy?style=flat-square"></a>\n    <a href="https://github.com/ZM25XC/TeenStudy/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/ZM25XC/TeenStudy?style=flat-square"></a>\n    <a href="https://github.com/ZM25XC/TeenStudy/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/ZM25XC/TeenStudy?style=flat-square"></a>\n    <a href="https://pypi.python.org/pypi/TeenStudy"><img src="https://img.shields.io/pypi/v/TeenStudy?color=yellow" alt="pypi"></a>\n  \t<a href="https://pypi.python.org/pypi/TeenStudy">\n    <img src="https://img.shields.io/pypi/dm/TeenStudy" alt="pypi download"></a>\n\t  <a href="https://github.com/ZM25XC/TeenStudy/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ZM25XC/TeenStudy?style=flat-square"></a>\n    <a href="https://jq.qq.com/?_wv=1027&k=NGFEwXyS">\n    <img src="https://img.shields.io/badge/QQ%E7%BE%A4-511173803-orange?style=flat-square" alt="QQ Chat Group">\n  </a>\n  </div>\n\n## 说明\n\n- 本项目为[青年大学习提交](https://github.com/ZM25XC/nonebot_plugin_auto_teenstudy) `Web UI`版\n- 本项目基于[nonebot2](https://github.com/nonebot/nonebot2)和[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)，使用本插件前请先阅读以上两个项目的使用文档\n-  **启动插件之后，一定要登录后台在推送列表中添加需要开启大学习功能的群聊**\n-  **本项目无法在国外IP环境下使用，如有开启代理，请关闭或添加代理规则**\n- 需要抓包的地区，绑定后尽量别进官方公众号，避免token或cookie刷新导致无法提交\n- 本项目需要部署在公网可访问的容器中，并开放端口（nonebot2配置的port），否则大部分功能将出现异常\n- 欢迎加入[QQ群](https://jq.qq.com/?_wv=1027&k=NGFEwXyS)，交流讨论。\n- 时间精力有限，目前只维护湖北和江西两个地区，其他地区出问题请提交Issues,我找个时间修，需要增加地区请进群帮忙测试，个别地区没账号无法测试\n\n- 觉得项目不错，不妨点个stars.\n\n## 地区状态\n\n<details>\n\n| 共青团名称 | 开发状态 | 备注 |\n|:-----:|:----:|:----:|\n|青春湖北|支持|无需抓包|\n|江西共青团|支持|无需抓包|\n|安徽共青团|支持|无需抓包|\n|广东共青团|支持|无需抓包|\n|青春上海|支持|微信扫码绑定|\n|青春浙江|支持|微信扫码绑定|\n|江苏共青团|支持|需要自行抓包|\n|青春山东|支持|需要自行抓包|\n|重庆共青团|支持|需要自行抓包|\n|吉青飞扬|支持|需要自行抓包|\n|黑龙江共青团|支持|需要自行抓包，该地区上线测试中|\n|天府新青年|支持|不进入公众号token时效大于1周|\n|河南共青团|不支持|cookie时效小于1周|\n|广西青年圈|待开发||\n|青春湖南|待开发||\n|甘肃青年|待开发||\n|山西青年|待开发||\n|河北共青团|待开发||\n|福建共青团|待开发||\n|内蒙古青年|待开发||\n|云南共青团|待开发||\n|三秦青年|待开发||\n|青春北京|待开发||\n|海南共青团|待开发||\n|津彩青春|待开发||\n|青春黔言|待开发||\n|青春柳州|待开发||\n|辽宁共青团|待开发||\n|宁夏共青团|待开发||\n|新疆共青团|待开发||\n|西藏共青团|待开发||\n</details>\n\n\n##  安装及更新\n\n<details>\n<summary>第一种方式(不推荐)</summary>\n\n- 使用`git clone https://github.com/ZM25XC/TeenStudy.git`指令克隆本仓库或下载压缩包文件\n\n</details>\n\n<details>\n<summary>第二种方式(二选一)</summary>\n\n- 使用`pip install TeenStudy`来进行安装,使用`pip install TeenStudy -U`进行更新\n- 使用`nb plugin install TeenStudy`来进行安装,使用`nb plugin install TeenStudy -U`进行更新\n\n</details>\n\n\n## 导入插件\n\n<details>\n<summary>使用第一种方式安装看此方法</summary>\n\n- 将`TeenStudy`放在nb的`plugins`目录下，运行nb机器人即可\n\n- 文件结构如下\n\n    ```py\n    📦 AweSome-Bot\n    ├── 📂 awesome_bot\n    │   └── 📂 plugins\n    |       └── 📂 TeenStudy\n    |           └── 📜 __init__.py\n    ├── 📜 .env.prod\n    ├── 📜 .gitignore\n    ├── 📜 pyproject.toml\n    └── 📜 README.md\n    ```\n\n    \n\n</details>\n\n<details>\n<summary>使用第二种方式安装看此方法</summary>\n\n- 在`pyproject.toml`里的`[tool.nonebot]`中添加`plugins = ["TeenStudy"]`\n\n</details>\n\n## 机器人配置\n\n- 在nonebot的`.env` 或 `.env.prod`配置文件中修改nonebot2的`HOST`为`0.0.0.0`、设置好超管账号和公网IP\n\n  ```py\n  HOST = "0.0.0.0"  #nonebot2监听的IP\n  SUPERUSERS = [""] # 超级用户\n  COMMAND_START=[""] # 命令前缀,根据需要自行修改\n  DXX_IP = ""\n  ```\n\n## 使用方式\n\n- 启动nb,等待插件加载数据，加载完毕后登录后台，账号默认为`nonebot配置文件中的超管账号`，密码默认为：`admin`,开放端口（默认为.env中配置的port）\n- 在管理后台的推送列表中添加需要开启大学习使用的群聊\n\n## 功能列表\n|    指令    |               指令格式               |                               说明                               |\n| :--------: | :----------------------------------: | :--------------------------------------------------------------: |\n| 添加大学习 |           添加大学习`地区`           |                    添加大学习湖北 添加大学习                     |\n| 我的大学习 |              我的大学习              |                           查询个人信息                           |\n| 提交大学习 |         提交大学习 戳一戳Bot         |                        提交最新一期大学习                        |\n|   大学习   |     大学习答案、大学习、答案截图     |                    获取最新一期青年大学习答案                    |\n|  完成截图  | 完成截图、大学习截图、大学习完成截图 |            获取最新一期青年大学习完成截图（带状态栏）            |\n| 完成大学习 |        完成大学习、全员大学习        | 团支书可用，需要成员填写团支书ID，填写后团支书可发指令提交大学习 |\n|  重置配置  |          重置配置、刷新配置          |                   超管可用，刷新Web UI默认配置                   |\n|  重置密码  |               重置密码               |                   重置登录Web UI的密码为用户ID                   |\n|删除大学习|删除大学习|用户申请清除数据库的信息|\n|导出用户数据|导出用户数据、导出数据|将数据导出至TeenStudy目录下|\n|更新用户数据|更新用户数据、刷新用户数据|将用户数据导入到数据库|\n|更新资源数据|更新资源数据、刷新资源数据|更新数据库中的资源数据（江西共青团团支部数据）|\n\n\n## ToDo\n\n\n- [ ] 增加更多地区支持\n- [ ] 优化 Bot\n\n\n## 更新日志\n\n### 2023/05/21\n\n- 增加黑龙江地区，需要自行抓包，该地区上线测试中，请积极提issue反馈\n- 下版本为大版本更新，将添加新功能，优化功能，请积极提issue反馈或加交流群反馈\n\n<details>\n<summary>2023/05/11</summary> \n\n- 增加广东地区，无需抓包[#13](https://github.com/ZM25XC/TeenStudy/issues/13)，感谢[@neal240](https://github.com/neal240)提供账号测试\n\n</details>\n\n<details>\n<summary>2023/05/06</summary> \n\n- 增加吉林地区，需要自行抓包\n- 修复超管更改登录密码后用原密码能继续登录问题\n- 添加二维码转链接开关，需要自行在后台配置页面打开\n- 调整部分依赖\n\n</details>\n\n<details>\n<summary> 2023/04/12</summary> \n\n- 因河南地区cookie时效小于1周，移除河南地区\n- 添加`删除大学习`功能，用户可自行删除数据\n- 添加`导出用户数据`功能\n- 添加`更新用户数据`功能\n- 添加`更新资源数据`功能，江西地区更新后请使用下此功能刷新团支部数据\n- 添加戳一戳提交大学习开关，默认开启，请在Web UI后台配置页面进行修改\n- 添加大学习提醒开关，默认开启，支持修改时间，请在Web UI后台配置页面进行修改\n- 添加自动提交大学习开关，默认开启，支持修改时间，请在Web UI后台进行修改\n- 调整安徽地区添加方式[#9](https://github.com/ZM25XC/TeenStudy/issues/9)，无需抓包，感谢[@yhzcake](https://github.com/yhzcake)测试提供方法\n- 修复Web UI 首页公网IP显示异常\n- 修复浙江地区用户重复显示\n- 更新江西共青团团支部数据\n  \n</details>\n\n\n<details>\n<summary>2023/03/18</summary>\n\n- 适配河南地区，需要自行抓包\n- 适配四川地区，需要自行抓包\n- 适配山东地区，需要自行抓包\n- 适配重庆地区，需要自行抓包\n- 添加自动获取公网IP功能，别再问如何配置公网IP啦\n- 添加重置密码功能，指令`重置密码`\n- 添加重置配置功能，指令`重置配置`，`刷新配置`\n- 添加完成大学习功能，团支书可一次性提交全班的大学习，指令`完成大学习`，`全员大学习`\n- 管理后台开放添加用户权限（浙江，上海地区无法添加）\n- 优化用户信息页\n- 优化登录界面提示\n- 将添加链接，登录链接转化成二维码，减少公网IP暴露，没啥用，样式好看一些\n- 修复Ubuntu系统导入资源失败BUG\n  \n</details>\n\n<details>\n\n<summary>2023/03/05</summary>\n\n- 适配浙江地区，使用微信扫码进行绑定\n- 适配上海地区，使用微信扫码进行绑定\n- 适配江苏地区，需要自行抓包\n- 适配安徽地区，需要自行抓包\n\n</details>\n\n<details>\n<summary>2023/03/01</summary>\n\n- 将代码上传至pypi，可使用`pip install TeenStudy`指令安装本插件\n- 上传基础代码\n- 适配湖北地区，无需抓包，安装即用\n- 适配江西地区，无需抓包，安装即用\n\n</details>\n',
    'author': 'ZM25XC',
    'author_email': 'xingling25@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ZM25XC/TeenStudy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
