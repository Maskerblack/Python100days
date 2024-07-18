# 100天精通Python（基础篇）——第20天：pip命令大全

## 

## **一、pip介绍**

### **1、pip是什么？**

> 嘿！你知道吗？`pip` 就像是 Python 的“快递小哥”，它负责帮你**安装**和**管理**那些不属于 Python 标准库的软件包。它就像是一个方便的工具，让你可以轻松地获取你需要的软件包，就像是在网上购物一样简单！只需一行命令，`pip` 就会帮你把软件包送到你的电脑上，让你的 Python 程序变得更加强大和灵活。所以，不要犹豫，让 `pip` 成为你的 Python 之旅中的得力助手吧！

### **2、怎么操作pip？**

**1）如果你是 Windows 用户，可以按下**`win键+ R`**，然后在弹出的窗口中输入：**`cmd`

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/klS3icnSibsdabY9h32YRrp2FQnlWcuH4WT9d5Y0WwqgN7wpD7J7otz4fdibACvaibSJs9qTIFHYFDu9StUicXDKEAw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**2）输入对应的pip命令**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/klS3icnSibsdabY9h32YRrp2FQnlWcuH4WOgfj0kvsaNOgiacGwhHicWYPvFZS9J3reBUpLn1jYj8ia2gSppstKenbA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## **二、pip常用命令**

### **查看pip所在路径**

```python
where pip
```

### **查看pip版本**

```python
pip -V
pip --version
```

### **pip升级命令**

```python
python -m pip install --upgrade pip
```

如果pip 默认源的网络连接较差，临时使用本镜像站来升级：

```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```

### **安装包**

**第一种**：

```python
pip install package_name  #这里的package_name是要安装的第三方库名
```

**第二种**（推荐使用，下载更快）：使用国内镜像源

```python
pip install package_name -i http://mirrors.aliyun.com/pypi/simple/
```

**国内镜像源**

- 阿里云：http://mirrors.aliyun.com/pypi/simple/ （推荐使用）
- 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple
- 豆瓣：http://pypi.douban.com/simple/

**第三种**（指定包版本号）：

```python
pip install package_name=版本号
```

**第四种**（本地文件安装）：

- 下载包：https://pypi.org/
- 搜索包名

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/klS3icnSibsdabY9h32YRrp2FQnlWcuH4WnAiboFzBG2tql7nEuJJatiau4voc0h0xuSeYicJibxkT6puZ28iaqpVX16w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- 找到对应版本

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/klS3icnSibsdabY9h32YRrp2FQnlWcuH4WvNsJET58rswAVmedAkp9icXXibO3QXWC8iayZA4Qic5lIiaBF4icEmBpBNBQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- 点击下载

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/klS3icnSibsdabY9h32YRrp2FQnlWcuH4Wia9SETOQ168yERRK4kuSfU0pwic5OK1x4ERVyU4OjTkJSL9ArhicAud7A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- 下载对应whl文件（我python版本是3.8，电脑window64位）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/klS3icnSibsdabY9h32YRrp2FQnlWcuH4WIdvpWTAGjrOIlNr1Eg14nbbttRMkansntCrA7TE9YiaiaYe8M0mqxBhg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- 执行安装命令

    ```python
    pip install C:\Users\Administrator\Downloads\pymssql-2.2.2-cp38-cp38-win_amd64.whl # 后面是包所在路径和包名
    ```
    
- 安装成功：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/klS3icnSibsdabY9h32YRrp2FQnlWcuH4WLc0ORTzuKc0RUGvEWz5HDsU2OTBAShJStc7Qicb0Oib3wQZYickSoltsg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

### **全局设置镜像源地址**

> 每次安装软件时都手动添加国内镜像地址确实有点麻烦。不过，你可以通过设置一个固定的配置来简化这个过程。在Python中，你可以使用`pip`命令来安装软件包。你可以创建一个名为`pip.ini`的文件，并将以下内容添加到文件中：
>
> ```python
> [global]index-url = 国内镜像地址
>```
> 
> 将"国内镜像地址"替换为你想要使用的国内镜像地址，例如：`https://pypi.tuna.tsinghua.edu.cn/simple`。然后将`pip.ini`文件保存在你的用户主目录下（Windows系统为`C:\Users\你的用户名`，Mac和Linux系统为`/Users/你的用户名`）。
> 
>这样，每次使用`pip`命令安装软件包时，它都会自动使用你设置的国内镜像地址，而无需手动添加。这样可以节省你的时间和精力，让你更专注于编写代码。希望这个方法对你有帮助！

```python
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### **卸载包**

```python
pip uninstall package_name #这里的package_name是要卸载的第三方库名
```

### **搜索包**

```python
pip search package_name
```

### **查看所有安装的包**

```python
pip list
```

### **查看安装包的详细信息**

```python
pip show package_name
```

### **更新指定的包**

```python
pip install --upgrade package_name
```

### **查看需要更新的包**

```python
pip list --outdated
```

### **查看帮助**

```python
pip -h
pip --help
Usage:
    pip<command>[options]
    
Commands:
    install                    安装包.
    uninstall                  卸载包.
    freeze                     按着一定格式输出已安装包列表
    list                       列出已安装包.
    show                       显示包详细信息.
    search                     搜索包，类似yum里的search.
    wheel                      Buildwheelsfromyourrequirements.
    zip                        不推荐.Zipindividualpackages.
    unzip                      不推荐.Unzipindividualpackages.
    bundle                     不推荐.Createpybundles.
    help                       当前帮助.
    
GeneralOptions:
    -h,--help                 显示帮助.
    -v,--verbose              更多的输出，最多可以使用3次
    -V,--version              现实版本信息然后退出.
    -q,--quiet                最少的输出.
    --log-file<path>          覆盖的方式记录verbose错误日志，默认文件：/root/.pip/pip.log
    --log<path>               不覆盖记录verbose输出的日志.
    --proxy<proxy>            Specifyaproxyintheform[user:passwd@]proxy.server:port.
    --timeout<sec>            连接超时时间(默认15秒).
    --exists-action<action>   Defaultactionwhenapathalreadyexists:(s)witch,(i)gnore,(w)ipe,(b)ackup.
    --cert<path>              证书.
```

## **三、安装报错问题**

权限问题报错

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/klS3icnSibsdabY9h32YRrp2FQnlWcuH4WW5eQnpgZiao9Yb5iaMjMz93lKOQicbRjMtOll0WhRZQMRibsgHlrBgOXtg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

加上 `--trusted-host mirrors.aliyun.com`后缀

```python
pip install pymssql -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/klS3icnSibsdabY9h32YRrp2FQnlWcuH4WeODCuSUaewmKqoN9wkHNNg6coGmKXs8vqNfsicyCQd4Zwtp7gx7iclPg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

