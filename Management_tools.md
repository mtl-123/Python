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
  
```
