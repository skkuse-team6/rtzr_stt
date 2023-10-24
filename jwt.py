import requests
import json

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

client_id = config_data.get('client_id', '')  # 'client_id'는 JSON 파일에서의 client_id 키
client_secret = config_data.get('client_secret', '')  # 'client_secret'은 JSON 파일에서의 client_secret 키

resp = requests.post(
    'https://openapi.vito.ai/v1/authenticate',
    data={'client_id': client_id, 'client_secret': client_secret}
)
resp.raise_for_status()
print(resp.json())
