# webm



一款精简的本地媒体...

CPU占用率和占用内存非常低

![uTools_1678799164674](https://suiluo.top/upload/2023/03/uTools_1678799164674.png)


## 使用教程

把文件下载下来，然后解压出来，进入文件夹中拉到最下面找到`package.json`这个文件，内容如下

```json
{
  "name": "webm",
  "version": "1.0.0",
  "author": "umrchemg",
  "github": "https://github.com/umrcheng/webm",
  "mailbox": "umrcheng@163.com",
  "dependencies": {
  },
  "path": [],
  "address": "0.0.0.0",
  "port": 80
}
```



> `port`：打开的监听端口，不清楚就不修改

> `address`：监听的地址，可以设置成你设备的IP地址，不清楚就不修改

> `path`：填写本地的文件夹路径，可以填写多个，支持`smb`网络地址，重要！



假如你要添加D盘的media文件夹路径为`D:\media`，F盘的download文件夹路径为`F:\download`，就这么写

```json
"path": [
    "D:\\media",
    "F:\\download"
],
```



然后直接运行`webm.exe`



## 测试

打开浏览器输入`127.0.0.1`，如果`address`里填写的改了，那么输入你改的.

如果你的`port`也改了那么要在输入的后面加上例如：改成了8888 `127.0.0.1:8888`


看到这个界面就表示成功了


![uTools_1678801113712](https://suiluo.top/upload/2023/03/uTools_1678801113712.png)


## 其他设备访问

运行成功之后可以任何设备都可以通过浏览器访问，iPad，手机，笔记本电脑，其他电脑，智能手表等。



首先两台设备连接到同一个网络，然后找到你设备的IP地址，不知道的可以搜一下

这里以手机为例

![Screenshot_2023-03-14-22-48-09-041_com.android.br.jpg](https://suiluo.top/upload/2023/03/Screenshot_2023-03-14-22-48-09-041_com.android.br.jpg)

![20230314224509](https://suiluo.top/upload/2023/03/20230314224509.jpg)



## 可以通过内网穿透远程访问

...







## 如果你会搭建vpn之类的也可以远程访问



...
