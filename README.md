# zhenxun_xxqg_helper

学xi什么的，交给真寻就好了

# 前言

本项目是基于TechXueXi衍生的真寻机器人插件

（按理说nonebot的机器人应该都可以使用，暂未实验）



### 传送门：

-----

- [TechXueXi](https://github.com/TechXueXi/TechXueXi)
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [zhenxun_bot](https://github.com/HibiKier/zhenxun_bot)



### 环境

-----

- python3
- go-cqhttp
- zhenxun_bot(nonebot或许也可以)
- chrome/chromium
- chromedriver



### 使用方法

-----

默认为go-cqhttp、zhenxun_bot、python3、chrome/chromium、chromedriver已经装好的情况下

1. 将文件解压到真寻的插件目录下（也可以手动创建插件目录后在bot.py内注册）

2. 使用一下目录安装依赖库

   ```shell
    pip3 install -r requirements.txt
   ```

   

3. 修改path.py中的目录为你的目录地址

   **一定要填写绝对目录**

   如

   ```python
   # 插件绝对路径,__init__.py的路径
   plugin_path = "/zhenxun/lugins/xxqg_helper/"
   
   # chrome或chromium的绝对路径
   chrome_path = "/usr/bin/google-chrome"
   
   # chromedriver的绝对路径
   chromedriver_path = "/usr/bin/chromedriver"
   ```

4. 重启真寻

5. 对真寻发送**学xi强国**(自己替换文字，dddd)

6. 真寻会给你发送登陆二维码，扫码登陆就可以让真寻自己刷啦

**有些题目查询不到答案，遇到这种题目会提前结束，稳定性并不算太好**

~~奈何本人水平有限，暂时不打算解决~~



### 其它

-----

等我想起来再写





------

**不接受任何形式的捐赠。**
