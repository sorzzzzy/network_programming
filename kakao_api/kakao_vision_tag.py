import argparse
import requests
from PIL import Image, ImageDraw, ImageFont 
from io import BytesIO
 
API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate' 
REST_API_KEY = '19b7f33aa4a1fe01be2fa8975ab3e85f'

def generate_tag(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = { 'image_url' : image_url }
    # string 형태이므로 파일이 아닌, 데이터로 보냄
    resp = requests.post(API_URL, headers=headers, data=data) 
    # 응답을 json으로 바꾸고, 
    result = resp.json()['result']
    if len(result['label_kr']) > 0:
        # 리스트 형태로 오기 때문
        print("이미지를 대표하는 태그는 \"{}\"입니다.".format(','.join(result['label_kr']))) 
    else:
        print("이미지로부터 태그를 생성하지 못했습니다.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Classify Tags') 
    parser.add_argument('image_url', type=str, nargs='?',
        default="https://p.kakaocdn.net/th/talkp/wmbOXVOIV9/aKtMoWYi4P4NrK5nrCodk0/s2rwz0_640x640_s.jpg", 
        help='image url to classify')
    args = parser.parse_args()
    
    generate_tag(args.image_url)