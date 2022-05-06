# Python 虚拟环境管理工具 PDM

[PDM官网文档](https://pdm.fming.dev/)
[PDM插件](https://github.com/pdm-project/awesome-pdm)

## Windows 系统安装PDM
```bat
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py -UseBasicParsing).Content | python -
```
打开pdm.exe 文件位置： 按win+r键 在运行窗口中输入 %APPDATA%\Python\Scripts 回车即可跳转到pdm.exe 文件存放位置
如果想全局使用需要把此路径添加到Windows系统的，系统属性环境变量中，然后重启电脑即可生效


## Linux 系统安装PDM

```bash
curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
```
打开pdm 执行文件存放位置： `cd $HOME/.local/bin` 


## 全局启动 PEP582
> 为了使 Python 解释器了解 PEP 582 包，需要将 添加pdm/pep582/sitecustomize.py 到 Python 库搜索路径。
### Windows 用户
> 只需执行pdm --pep582，然后环境变量将自动更改。不要忘记重启终端会话才能生效。
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
  
