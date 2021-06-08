from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse, request
import json
import requests

REST_API_KEY = '19b7f33aa4a1fe01be2fa8975ab3e85f'


class http_handler(BaseHTTPRequestHandler):
    # 경로에 따라 다르게 처리
    def do_GET(self):
        self.route()

    def route(self):
        parsed_path = parse.urlparse(self.path)
        real_path = parsed_path.path

        # 기본 경로로 들어오면
        if real_path == '/':
            self.send_html()
        # 리다이렉트로 올라오면, 인증기능을 수행하는 함수 수행
        elif real_path == '/oauth':
            self.process_oauth()
        else:
            self.response(404, 'Not Found')

    def send_html(self):
        self.send_response(200)
        self.end_headers()
        with open('index_kakao.html', 'r', encoding='utf-8') as f:
            msg = f.read()
            self.wfile.write(msg.encode())

    def process_oauth(self):
        # 인증 코드 얻기
        parsed_path = parse.urlparse(self.path)
        query = parsed_path.query

        parsed_query = parse.parse_qs(query)
        authorize_code = parsed_query['code']
        print(authorize_code)
        self.response(200, 'Kakao authentication is successful.')

        # access token과 refresh token 얻기
        token_api_url = "https://kauth.kakao.com/oauth/token"
        data = {'grant_type': 'authorization_code',
                'client_id': REST_API_KEY,
                'redirect_uri': "http://localhost:8888/oauth",
                'code': authorize_code}

        rsp = requests.post(token_api_url, data=data)
        rsp_json = json.loads(rsp.text)
        access_token = rsp_json['access_token']
        refresh_token = rsp_json['refresh_token']
        print('access_token:', access_token)
        print('refresh_token:', refresh_token)

        # 카카오톡 프로필 가져오기
        profile_url ="https://kapi.kakao.com/v1/api/talk/profile"
        # 딕셔너리로 만들기
        header = {'Authorization': 'Bearer ' + access_token}
        rsp = requests.get(profile_url, headers=header)
        # json을 딕셔너리로 반환
        json_profile = rsp.json()
        print(json_profile)

        # URL의 이미지를 파일로 저장, 프로필 사진을 다운받고 싶음
        # 이 url에 있는 데이터를 쉽게 이름을 정해서 저장할 수 있음
        image_path = 'profile.jpg'
        request.urlretrieve(json_profile['profileImageURL'], image_path)
    
        print('나한테 카톡 보내기')
        # 나한테 카톡 보내기
        talk_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        # access token 만들기
        header = {'Authorization': 'Bearer ' + access_token}
        template_object = {
                            "object_type": "text",
                            "text": "카카오 API 정말 쉽구나!",
                            # 콘텐츠 클릭 시 이동할 링크 정보
                            "link":
                                    {
                                        "web_url": "https://labs.sch.ac.kr/department/iot/m/",
                                        "mobile_web_url": "https://labs.sch.ac.kr/department/iot/m/"
                                    }
                            }
        # 딕셔너리를 json 포맷으로 바꿔서 보내야 함
        template_object_json = json.dumps(template_object)
        # json 형식으로 만든 것을 데이터에 담아 쿼리 형태로 저장
        data = {'template_object': template_object_json}
        # 데이터와 헤더도 같이 전송
        rsp = requests.post(talk_url, headers=header, data=data)

    def response(self, status_code, body):  # 응답 메시지 전송 함수
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(body.encode())


httpd = HTTPServer(('localhost', 8888), http_handler)
print('Serving HTTP on {}:{}'.format('localhost', 8888))
httpd.serve_forever()