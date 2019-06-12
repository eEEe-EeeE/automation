# 自动化测试项目

*版本：v0.0.1 by xx*

#### 文档内容

  * 环境简介
  * 软件功能
  * 项目结构
  * 接口说明
  * 文档维护
  * 环境配置

#### 相关链接
  * [selenium](https://www.seleniumhq.org/docs/)
  * [unittest](https://docs.python.org/3.6/library/unittest.html#module-unittest)

## 软件环境

*操作系统，解释器，驱动，浏览器和软件包等*

### 操作系统

- Windows 10

### 解释器

- Python3.6.8

### 浏览器驱动

- geckodriver 0.24.0
- chromedriver 74.0.3729.169

### 浏览器

+ Firefox 67.0
+ Chrome 74.0

### 软件包

- selenium2.0 = selenium 1.0 + WebDriver ： web测试
- unittest ： 单元测试
- xlrd ： 读取xlsx文件
- html-testRunner ： 生成测试报告
- pyautogui ： windows gui自动化工具包
- pyperclip ： windows 剪贴板工具包
- pywinauto ： win32 自动化工具包

## 软件功能

*界面测试，功能测试*

### 界面测试

- 测试用户界面的功能模块的布局是否合理、整体风格是否一致、各个控件的放置位置是否符合客户使用习惯，此外还要测试界面操作便捷性、导航简单易懂性，页面元素的可用性，界面中文字是否正确，命名是否统一，页面是否美观，文字、图片组合是否完美等。

### 功能测试

- 功能测试就是对产品的各功能进行验证，根据功能测试用例，逐项测试，检查产品是否达到用户要求的功能。
- 例如测试增加一条记录或者查询一条记录的功能，用户需要向xlsx文件按一定的格式写入

## 项目结构

- 参考结构

```struct
\---automatedtesting
    |   dir_tree.txt
    |   README.md
    |   run_nbp_test.py
    |   
    +---driver
    |       chromedriver.exe
    |       geckodriver.exe
    |       selenium-server-standalone-3.141.59.jar
    |       
    +---nbp
    |   |   __init__.py
    |   |   
    |   +---data
    |   +---report
    |   |   |   2019-05-24 14_22_59result.htm
    |   |   |   
    |   |   \---image
    |   |           baidu.png
    |   |           start.png
    |   |           
    |   \---test_case
    |       |   login_sta.py
    |       |   om_sta.py
    |       |   __init__.py
    |       |   
    |       +---models
    |       |       driver.py
    |       |       function.py
    |       |       myunit.py
    |       |       __init__.py
    |       |       
    |       \---page_obj
    |               base_page.py
    |               login_page.py
    |               om_config_page.py
    |               om_device_page.py
    |               om_patrol_page.py
    |               __init__.py
    |               
    +---package
    |       README.md
    |       
    +---reports
    \---scripts
            generate_dir_tree.bat
            startup.bat
```

- [具体结构](./dir_tree.txt)

- 目录摘要

  - driver目录 : 存放webdriver程序和RC-jar包，以及相关软件驱动
  
  - nbp目录 : 存放所有与测试用例相关的模块
  
    - date目录 : 存放输入数据
    
    - report目录 : 存放unittest测试报告

      - image目录 : 存放测试截图
      
    - test_case目录 : 存放测试实例
    
      - models目录 : 存放所有公用函数和配置函数
      
      - page_obj目录 : 存放页面所有对象
    
    
  - package目录 : 存放项目用到的软件包
    
  - scripts目录 : 存放项目的配置脚本
    
## 接口说明

- run_nbp_test.py

```
项目总控制函数，调用各个测试用例组
```

- *_sta.py

```
一个测试用例，从setUp开始，执行所有test_*函数，以tearDown结束
```
    
## 文档维护

- 本项目文档使用MarkDown编写，之后也需要使用MarkDown维护

- [MarkDown基础教程](http://www.markdown.cn/)
    
## 环境部署

1. 安装./package下的python3.6.8(64bit或32bit)，确保安装目录下的Scripts目录在环境变量PATH中
2. 打开CMD，切换至项目目录automatedtesting下，并执行 : 

    pip install --user -r requirements.txt
3. 将./driver目录加入环境变量PATH