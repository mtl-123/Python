# Python 虚拟环境管理工具 PDM

[PDM官网文档](https://pdm.fming.dev/)
[PDM插件](https://github.com/pdm-project/awesome-pdm)

## Windows 系统安装PDM
第一种安装方法，需要科学上网
```bat
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py -UseBasicParsing).Content | python -
```
第二种安装方法
`pip install --user pdm`
- 注：PDM只支持python3.7 以上版本一般系统没有安装高于3.7的版本和pip 安装方法如下：
```bash
# 增加 ppa 仓库，并更新源数据
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
# 如果提示找不到 add-apt-repository 命令，执行如下命令安装
sudo apt install software-properties-common
# 更新完成源数据之后，就可以安装 ppa 仓库中的包了，这个仓库中不止是包含 python3.8，还包含其他版本的 python 包，详细情况可查看链接：
https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
# 执行以下命令安装 python3.8 相关的包：
sudo apt install python3.8 python3.8-dev python3.8-distutils python3.8-venv -y
# 安装完成后，当需要使用 3.8 版本的 python 时，执行：
python3.8 --version
# 安装 pip
# 当需要使用 pip 时，由于系统源里的 pip 是 python3.5 对应的，所以针对 python3.8 并不能正常工作，比如使用 virtualenv 创建 python3.8 的虚拟环境时就会报错，可以执行如下命令查看 pip 是对应哪个 python 版本的：
pip3 --version （可能的输出如下，注意最后括号里的内容）

pip 8.1.1 from /usr/lib/python3/dist-packages (python 3.5)
# 前面新增的 ppa 仓库中，只有 python 的包，没有 pip 的，所以需要额外的安装方法，参考 pip 官方安装教程：https://pip.pypa.io/en/stable/installation/，使用如下方法安装 python3.8 对应的 pip：
wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py
python3.8 /tmp/get-pip.py
# 下载的pip3.8 程序路径位于 cd ./home/m/.local/bin/
sudo cp /home/m/.local/bin/pip3.8 /usr/local/bin/
# 上面的两个命令是，下载 pip 官方安装脚本，然后使用 python3.8 执行安装脚本，执行完成后就安装好了 python3.8 对应的 pip，执行如下命令检验：
pip --version
pip3 --verison
pip3.8 --version
```
打开pdm.exe 文件位置： 按win+r键 在运行窗口中输入 %APPDATA%\Python\Scripts 回车即可跳转到pdm.exe 文件存放位置
如果想全局使用需要把此路径添加到Windows系统的，系统属性环境变量中，执行下面命令即可生效

```bat
win+r打开cmd输入命令
taskkill /f /im explorer.exe  && explorer.exe
```


## Linux 系统安装PDM

```bash
curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
```
打开pdm 执行文件存放位置： `cd $HOME/.local/bin` 


## 全局启动 PEP582
> 为了使 Python 解释器了解 PEP 582 包，需要将 添加pdm/pep582/sitecustomize.py 到 Python 库搜索路径。
### Windows 用户
> 只需执行pdm --pep582，然后环境变量将自动更改。
> 不要忘记重启终端会话才能生效。

### Linux 用户
> 更改环境变量的命令可以打印出来pdm --pep582 [<SHELL>]。如果<SHELL> 没有给出，PDM 将根据一些猜测选择一个。你可以运行eval "$(pdm --pep582)"来执行命令。
> 您可能希望在您的.bash_profile（或类似的配置文件）中写一行以使其在登录时生效。例如，在 bash 中您可以这样做：
```bash
pdm --pep582 >> ~/.bash_profile
```
再一次，不要忘记重新启动终端会话才能生效。

### 配置PDM命令自动补全
  
> PDM 支持为 Bash、Zsh、Fish 或 Powershell 生成完成脚本。以下是每个 shell 的一些常见位置：
  
Linux 用户配置
`pdm completion bash > /etc/bash_completion.d/pdm.bash-completion`
Windows用户配置
```bat
# Create a directory to store completion scripts
mkdir $PROFILE\..\Completions
echo @'
Get-ChildItem "$PROFILE\..\Completions\" | ForEach-Object {
    . $_.FullName
}
'@ | Out-File -Append -Encoding utf8 $PROFILE
# Generate script
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
pdm completion powershell | Out-File -Encoding utf8 $PROFILE\..\Completions\pdm_completion.ps1
```
### PDM 常用命令

```bash
- pdm info
- pdm add flask
- pdm list
- pdm list --graph
- pdm config feature.install_cache on
- pdm sync --reinstall
- pdm config -d feature.insatll.cache
- pdm plugin add pdm-venv
- pdm venv list
- pdm venv remove <version>
- pdm use <version>
- pdm run python
- pdm install 
- pdm plugin remove pdm-venv
- pdm add -dG format black
- pdm update # 更新全部
- pdm update requests # 更新指定
- pdm update --update-eager requests # 更新指定及其依赖
- pdm update --unconstrained requests # 突破版本限制升级
- pdm update --outdated  # 查看可更新的包

  # 从其他包管理器迁移
- pdm import <filename>
- 支持多种文件：
  - Pipfile(pipenv)
  - pyproject.tom(Poetry)
  - pyproject.tom(flit)
  - requirements.txt(pip)
- 自动探测文件类型
- 导出requirements.txt: pdm export -o requirements.txt
 
- 虚拟环境支持： pdm -venv
- 添加发布到Pypi命令： pdm -publish
- 打包成可移动的zip应用：pdm -packer
- 更多：https://github.com/pdm-project/awesome-pdm

# PDM的使用
## 创建一个虚拟环境
- 基于3.8解释器创建一个virtualenv
`pdm venv create 3.8`
- 分配一个不同于版本字符串的名称
`pdm venv create --name for-test 3.8`
- 使用venv作为后端进行创建，支持3个后端:virtualenv(默认)，venv, conda
`pdm venv create --with venv 3.9`
- 激活虚拟环境
`pdm venv activate for-test`
- 查看创建的虚拟环境
`pdm venv list`

## 删除虚拟环境
`pdm venv remove for-test`

  
```
