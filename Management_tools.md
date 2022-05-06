# Python 虚拟环境管理工具 PDM
[PDM官网文档](https://pdm.fming.dev/)

## Windows 系统安装PDM
```bat
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py -UseBasicParsing).Content | python -
```
打开pdm.exe 文件位置 按win+r键 在运行窗口中输入 %APPDATA%\Python\Scripts 回车即可跳转到pdm.exe 文件存放位置
如果想全局使用需要把此路径添加到Windows系统的，系统属性环境变量中，然后重启电脑即可生效

