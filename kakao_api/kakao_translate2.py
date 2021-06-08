import requests

# detect 하는 url과 번역하는 url 서로 다름 주의
API_URL_1 = 'https://dapi.kakao.com/v2/translation/translate' 
API_URL_2 = 'https://dapi.kakao.com/v3/translation/language/detect' 
REST_API_KEY = '19b7f33aa4a1fe01be2fa8975ab3e85f'

def detect_language_get(text):
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'query': text }
    rsp = requests.get(API_URL_2, headers=headers, params=data) 
    return rsp.json()

def translate_post(text, src_lang):
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    # 요청 온 언어를 프랑스어로 번역
    data = {'src_lang': src_lang, 'target_lang': 'fr', 'query': text} 
    rsp = requests.post(API_URL_1, headers=headers, data=data)
    return rsp.json()

if __name__ == "__main__":
    while True:
        text = input('Enter the sentence to translate: ') 
        if text != 'q':
            # get으로 detect
            detect_output = detect_language_get(text) 
            print(detect_output)
            detect_lang = detect_output['language_info'][0]['code'] 

            # 감지한 언어만 빼내서 번역하기 위해 사용
            translated_text = translate_post(text, detect_lang) 
            print(translated_text)
            print('[POST]', translated_text['translated_text'][0][0])
        else: 
            break