# csdn_reading_upup

这是一个刷csdn阅读量的脚本

这里是提取的csdn中的rrs订阅的链接

我们先通过rrs订阅的链接中，拿到最近的20篇文章的地址

然后在通过地址一个个的去访问，不过是要加一下代理的，用同一个ip一直访问只会加一个阅读量

## github地址：
https://github.com/jixn-hu/csdn_reading_upup

## 使用说明
你可以直接修改`config.yaml` 配置文件

csdnRRS 是csdn的rrs连接

proxy是代理，随机更换的

### 如何找csdn的rrs链接

你可以先打开你的个人主页

在主页中，可以轻易找到

![](https://hqx.oss-cn-beijing.aliyuncs.com/image/picgo_img20230825104241.png?x-oss-process=style/jixn)

### 运行

直接跑`mian.py`文件即可

```cmd
python main.py
```