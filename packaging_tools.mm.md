# Python 打包工具
> 将Python代码转成exe的程序

- 优缺点：
- nuitka真香！
  - 同一个项目，生成的exe只有7M！
  - 打包超级快（1min以内），启动超级快。
- pyinstaller体验很差！
  - 一个深度学习的项目最后转成的exe竟然有近3个G的大小（pyinstaller是将整个运行环境进行打包），对，你没听错，一个EXE有3个G！
  - 打包超级慢，启动超级慢。

--- 

[原博主博客](https://www.lixiaofei2yy.website/python%E7%9A%84%E6%89%93%E5%8C%85%E7%A5%9E%E5%99%A8nuitka)
# Nuitka
- 安装nuitka
`pip install Nuitka`
- 下载vs2019（MSVS）或者MinGw64，反正都是C++的编译器
- windows 系统
`nuitka --standalone --show-memory --show-progress --nofollow-imports --plugin-enable=qt-plugins --follow-import-to=utils,src --output-dir=out --windows-icon-from-ico=./logo.ico demo.py`

参数详解：
- `--standalone：`方便移植到其他机器，不用再安装python
- `--show-memory --show-progress：`展示整个安装的进度过程
- `--nofollow-imports：`不编译代码中所有的import，比如keras，numpy之类的。
- `--plugin-enable=qt-plugins：`我这里用到pyqt5来做界面的，这里nuitka有其对应的插件。
- `--follow-import-to=utils,src：`需要编译成C++代码的指定的2个包含源码的文件夹，这里用,来进行分隔。
- `--output-dir=out：`指定输出的结果路径为out。
- `--windows-icon-from-ico=./logo.ico：`指定生成的exe的图标为logo.ico这个图标，这里推荐一个将图片转成ico格式文件的网站（比特虫）。
- `--windows-disable-console：`运行exe取消弹框。这里没有放上去是因为我们还需要调试，可能哪里还有问题之类的。
- 当然这里你会发现真正运行exe的时候，会报错：no module named torch,cv2,tensorflow等等这些没有转成C++的第三方包。
- 这里需要找到这些包（我的是在software\python3.7\Lib\site-packages下）复制（比如numpy,cv2这个文件夹）到demo.dist路径下。
- 至此，exe能完美运行啦！
# pyinstaller
