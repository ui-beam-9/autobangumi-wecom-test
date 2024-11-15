from flask import Flask, request, jsonify, render_template
import logging
import requests
from flask_cors import CORS

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class WecomNotification:
    """使用 WeComChan 推送消息"""

    def __init__(self, api_url, token):
        self.api_url = api_url
        self.token = token

    @staticmethod
    def gen_message(message) -> str:
        return message.strip()

    def post_msg(self, message) -> bool:
        title = "【番剧更新】"
        msg = self.gen_message(message)
        
        data = {
            "key": self.token,
            "msgtype": "text",
            "text": {
                "content": msg
            }
        }
        
        try:
            logger.debug(f"Sending data to {self.api_url}: {data}")  # 添加日志以调试请求体内容
            resp = requests.post(self.api_url, json=data)
            if resp is None:
                logger.error(f"WeCom notification failed: Response is None")
                return False
            logger.debug(f"WeCom notification response: {resp.status_code}, {resp.text}")
            return resp.status_code == 200
        except requests.RequestException as e:
            logger.error(f"Failed to send notification: {str(e)}")
            return False

app = Flask(__name__)
CORS(app)  # 允许所有来源的请求

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_notification', methods=['POST'])
def send_notification():
    try:
        data = request.json
        logger.debug(f"Received data: {data}")  # 添加日志以调试请求体内容
        
        token = data.get('token')
        api_url = data.get('chat_id')
        message = data.get('message')
        
        if not token or not api_url or not message:
            return jsonify({"error": "Missing token, chat_id, or message"}), 400
        
        wecom_notification = WecomNotification(api_url, token)
        success = wecom_notification.post_msg(message)
        
        if success:
            return jsonify({"message": "Notification sent successfully"}), 200
        else:
            return jsonify({"message": "Failed to send notification"}), 500
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/proxy_send_notification', methods=['POST'])
def proxy_send_notification():
    try:
        data = request.json
        logger.debug(f"Proxy received data: {data}")  # 添加日志以调试请求体内容
        
        token = data.get('token')
        api_url = data.get('chat_id')
        message = data.get('message')
        title = data.get('title') or "【番剧更新】"
        picurl = data.get('picurl') or ""
        
        if not token or not api_url or not message:
            return jsonify({"error": "Missing token, chat_id, or message"}), 400
        
        data_to_send = {
            "key": token,
            "type": "news",
            "title": title,
            "msg": message,
            "picurl": picurl
        }
        
        logger.debug(f"Forwarding data to {api_url}: {data_to_send}")
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        logger.debug(f"Headers: {headers}")
        
        resp = requests.post(api_url, data=data_to_send, headers=headers)
        
        if resp.status_code == 200:
            return jsonify({"message": "Notification sent successfully", "response": resp.json()}), 200
        else:
            return jsonify({"message": "Failed to send notification", "response": resp.json(), "status_code": resp.status_code}), resp.status_code
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)






