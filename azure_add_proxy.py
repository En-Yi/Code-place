import requests
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# 替换为您的订阅密钥和终结点
subscription_key = "your_subscription_key"
endpoint = "your_endpoint"

# 设置代理
proxies = {
    "http": "http://your_proxy_address:proxy_port",
    "https": "http://your_proxy_address:proxy_port"
}

# 创建 ComputerVisionClient
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# 设置 session 以便使用代理
session = requests.Session()
session.proxies.update(proxies)
client.config.session = session

# 分析图像 URL
image_url = "https://example.com/image.jpg"
analysis = client.analyze_image(image_url, visual_features=["Categories", "Description", "Color"])

# 打印结果
print(analysis)
