# 维多利亚3：AI梦境

## 项目简介

这是一个基于维多利亚3的AI梦境项目，旨在通过AI技术模拟和分析外交关系。

## 作者

quanfa

## 环境设置

项目使用Conda环境，定义在`environment.yml`文件中。请按照以下步骤设置环境：

```bash
conda env create -f environment.yml
conda activate your_env_name
```

## 项目结构

项目的目录结构如下：

```
# 项目根目录
.  
# 脚本目录
./myscripts  

# 具体脚本
## AI梦境-外交历史评论家
./myscripts/s1_diplomacy_relation_agent_prompt.py 

# Git忽略文件
./.gitignore  

# 项目说明文件
./readme.md  

# 环境依赖文件
./requirements.txt  

# 主程序文件
./main.py  
```

## 使用说明

1. 克隆项目到本地：
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. 设置Conda环境：
    ```bash
    conda env create -f environment.yml
    conda activate your_env_name
    ```

3. 运行主程序：
    ```bash
    python main.py
    ```
