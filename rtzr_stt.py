import json
import requests

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

jwt_token = config_data.get('jwt_token', '')  # 'jwt_token'는 JSON 파일에서의 jwt_token 키

config = {
  "use_diarization": True,
  "diarization": {
    "spk_count": 2
  },
  "use_multi_channel": False,
  "use_itn": False,
  "use_disfluency_filter": False,
  "use_profanity_filter": False,
  "use_paragraph_splitter": True,
  "paragraph_splitter": {
    "max": 50
  }
}

resp = requests.post(
    'https://openapi.vito.ai/v1/transcribe',
    headers={'Authorization': f'Bearer {jwt_token}'},
    data={'config': json.dumps(config)},
    files={'file': open('sample.m4a', 'rb')}
)
resp.raise_for_status()
print(resp.json())
