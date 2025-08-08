# 小码王社区举报处理系统

这是一个用于处理小码王社区举报的工具，支持自动获取Token、查看举报列表、处理举报等功能。
##开源版本README文件请往下看

## 功能特点

- 自动获取Token，无需手动复制粘贴（测试中，不推荐使用）
- 支持命令行和图形界面两种使用方式
- 可查看举报列表并进行处理
- 支持向举报人和被举报人发送站内信
- Token自动保存，下次使用无需重复获取

## 安装依赖

不需要安装依赖（当前版本）

## 使用方法

### 图形界面版本

1. 启动程序后，点击"自动获取Token"按钮
2. 程序会自动打开浏览器访问小码王社区举报页面
3. 如果您已经登录小码王账号，程序会自动获取Token
4. 获取成功后，程序会自动加载举报列表

### 命令行版本（暂不可用）

命令行版本目前暂不可用，请使用图形界面版本。

## 自动获取Token的工作原理

程序使用Selenium模拟浏览器访问小码王社区举报页面，并从网络请求中提取Token。具体流程如下：

### Token获取流程

1. 访问 https://world.xiaomawang.com/w/report 页面
2. 拦截包含 "get-unread" 的网络请求
3. 从请求头中提取 "Access-Token" 参数
4. 将Token保存到本地文件，方便下次使用


## 注意事项

- 首次运行需要安装Chrome浏览器和ChromeDriver

## 下载该程序
- 点击右侧Release选择最新版本
- 自动获取Token前，请确保您已经在浏览器中登录了小码王账号
- 如果自动获取Token失败，可以尝试手动输入
- Token有效期有限，过期后需要重新获取

# 开源文件说明
# 核心请求模块

- 仅包含小码王社区举报接口的请求构建逻辑。
- 不包含任何网络请求执行或鉴权获取逻辑。
- 需要调用方自行提供 `Access-Token` 与请求执行器。

## 目录
- `http_types.py`: 轻量级 `HttpRequest` 类型
- `executor_protocol.py`: 执行器协议定义
- `requests_core.py`: 核心请求构建函数
- `__init__.py`: 公共导出

## 使用示例（仅示意，无法直接运行）
```python
from kaiyuan import (
    HttpRequest,
    build_get_comment_list,
    build_get_report_info,
    build_verify_comment,
)

access_token = "YOUR_TOKEN"
req1: HttpRequest = build_get_comment_list(access_token, page=1, page_size=10, report_status=0)
req2: HttpRequest = build_get_report_info(access_token, report_id=123)
req3: HttpRequest = build_verify_comment(
    access_token=access_token,
    report_id=123,
    report_detail_ids=[456],
    action=1,
    remark="",
    reporter_message="",
    user_message="",
)

# 需要自行实现请求执行器，例如使用 requests 库：
# executor.execute(req1)
``` 
