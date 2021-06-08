import requests

API_URL = 'https://dapi.kakao.com/v2/translation/translate'
REST_API_KEY = '19b7f33aa4a1fe01be2fa8975ab3e85f'

# GET 요청
def translate_get(text):
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    # 쿼리 스트링 만들기
    data = {'src_lang': 'kr', 'target_lang': 'en', 'query': text} 
    # 데이를 쿼리로 만들기 위해서, get에서는 params를 사용함
    rsp = requests.get(API_URL, headers=headers, params=data) 
    return rsp.json()

# POST 요청
def translate_post(text): 
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'src_lang': 'kr', 'target_lang': 'fr', 'query': text} 
    # post에서는 그냥 data(url_encoded 방식)
    rsp = requests.post(API_URL, headers=headers, data=data) 
    return rsp.json()

if __name__ == "__main__":
    while True:
        # 무한루프를 돌며 번역할 문장을 입력받기
        text = input('Enter the sentence to translate: ') 
        # q를 누르면 종료
        if text != 'q':
            # get으로 번역하기
            translated_text = translate_get(text) 
            print(translated_text)
            print('[GET]', translated_text['translated_text'][0][0]) 

            # post로 번역하기
            translated_text = translate_post(text) 
            print(translated_text)
            print('[POST]', translated_text['translated_text'][0][0])
        else: 
            break