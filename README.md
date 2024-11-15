# WeCom Notification Service

#### 该代码和文档由阿里云通义千问AI自动生成

这是一个使用 Flask 框架构建的 Web 服务，能够通过 WeCom（企业微信）发送通知消息。本项目还支持通过代理发送包含图片链接的通知消息。

## 目录结构
wecom-notification-service/
├── app.py               # 主程序入口
├── requirements.txt     # 项目依赖
└── templates/           # 模板文件夹
└── index.html       # 示例主页模板

## 安装

### 1. 环境准备

确保您的系统已经安装了 Python 3.6+ 和 pip。您可以使用以下命令检查是否已安装：

```sh
python --version
pip --version
```

### 2. 克隆仓库
克隆该项目到本地：

```sh
深色版本
git clone https://github.com/ui-beam-9/autobangumi-wecom-test.git
cd autobangumi-wecom-test
```
### 3. 安装依赖
安装项目所需的依赖库：

```sh
深色版本
pip install -r requirements.txt
```

### 4. 配置
确保您有一个有效的 WeComChan 应用 Token 和 API URL。
您可以通过修改 app.py 中的代码来配置默认值，或者在发送通知时通过请求参数传递。

### 5. 运行服务
运行 Flask 应用：

```sh
python app.py
```
默认情况下，应用会在 http://127.0.0.1:5000/ 上运行。

### 6. 访问服务
打开浏览器并访问 http://127.0.0.1:5000，您将看到一个简单的主页。

### 7. 发送通知
发送普通文本通知
使用 POST 请求发送文本通知：

```sh
curl -X POST http://127.0.0.1:5000/send_notification \
-H "Content-Type: application/json" \
-d '{
  "token": "YOUR_WECOM_APP_TOKEN",
  "chat_id": "YOUR_WECOM_CHAT_ID",
  "message": "这是一条测试消息"
}'
```

发送带图片的图文通知
使用 POST 请求发送带图片的图文通知：

```sh
深色版本
curl -X POST http://127.0.0.1:5000/proxy_send_notification \
-H "Content-Type: application/json" \
-d '{
  "token": "YOUR_WECOM_APP_TOKEN",
  "chat_id": "YOUR_WECOM_CHAT_ID",
  "message": "这是一条测试消息",
  "title": "【番剧更新】",
  "picurl": "https://article.biliimg.com/bfs/article/d8bcd0408bf32594fd82f27de7d2c685829d1b2e.png"
}'
```

### 8. 日志
应用的日志将会输出到控制台。您可以通过查看控制台输出来调试和监控应用的行为。

### 9. 部署
您可以将此应用部署到任何支持 Python 的服务器上，例如 Heroku、AWS、Google Cloud 等。具体部署步骤取决于您选择的平台。

贡献
欢迎贡献！如果您有任何建议或发现任何问题，请提交 Issue 或 Pull Request。

许可证
本项目采用 MIT 许可证，详情请参见 LICENSE 文件。