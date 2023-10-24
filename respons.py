import requests
import json

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

transcribe_id = config_data.get('trs_id', '')  
jwt_token = config_data.get('jwt_token', '')  

url = f'https://openapi.vito.ai/v1/transcribe/{transcribe_id}'
headers = {
    'Authorization': f'Bearer {jwt_token}',
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    results = data.get('results', {})
    utterances = results.get('utterances', [])
    
    # 'utterances' 리스트에서 'msg' 데이터 추출
    msg_data = []
    for utterance in utterances:
        msg = utterance.get('msg', '')
        if msg:
            msg_data.append(msg)

    if msg_data:
        # 'msg' 데이터를 파일로 추가.
        with open('transcribe_msg.txt', 'a', encoding='utf-8') as file:
            for msg in msg_data:
                file.write(msg + '\n')

        print(f"Message data appended to 'transcribe_msg.txt'")
    else:
        print("No 'msg' data in the API response.")
else:
    print(f"Request failed with status code: {response.status_code}")
