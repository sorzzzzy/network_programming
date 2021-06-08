from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse


class http_handler(BaseHTTPRequestHandler):
    # 경로에 따라 다르게 라우팅
    def do_GET(self):
        self.route()

    def do_POST(self):
        self.route()

    def route(self):
        # urlpalse하기 
        parsed_path = parse.urlparse(self.path) 
        # ex) http://localhost:8080/button?status=on
        # path : /button?status=on
        real_path = parsed_path.path
        if real_path == '/':
            self.send_html()

        # proc_query : 쿼리를 처리하는 함수
        elif real_path == '/button':
            self.proc_query()
        elif real_path == '/form_get':
            self.proc_query()
        elif real_path == '/form_post':
            self.proc_form_post()
        else:
            self.response(404, '<h1>Not Found</h1>')

    def send_html(self): 
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # 사용자 웹페이지를 바꾸고 싶을 때, 아래 해당되는 html 파일 외의 다른 것을 주석 처리하면 됨
        with open('index_button.html', 'r', encoding='utf-8') as f:
        # with open('index_get.html', 'r', encoding='utf-8') as f: 
        # with open('index_post.html', 'r', encoding='utf-8') as f:
            msg = f.read()
            self.wfile.write(msg.encode())

    # get 요청 처리
    def proc_query(self):
        parsed_path = parse.urlparse(self.path)
        # 쿼리 = '?'뒤에 오는 모든것
        # 따라서 예시에서는 'status=on'
        query = parsed_path.query
        print(query)
        # 쿼리 status=on을 {'status': ['on']}으로 파싱
        parsed_query = parse.parse_qs(query)
        print(parsed_query)
        # 리스트이기 때문에, status의 [0]을 가져옴
        status = parsed_query['status'][0]
        if status == 'on':
            message = '<h2>LED in IoT Device is now turned on</h1>'
        elif status == 'off':
            message = '<h2>LED in IoT Device is now turned off</h1>'
        else:
            message = '<h2>Wrong Status</h2>'

        self.response(200, message)

    def proc_form_post(self):
        content_length = int(self.headers['Content-Length'])
        # rfile.read : 바디부분을 읽기 위함 (길이만큼만 읽고 문자열로 바꿈)
        body = self.rfile.read(content_length).decode()
        print(body)
        # body 내용은 쿼리 status=on(또는 off)
        parsed_body = body.split('=')
        print(parsed_body)
        # parsed_body = ['status', 'on']
        status = parsed_body[1]
        if status == 'on':
            message = '<h2>LED in IoT Device is now turned on</h1>'
        elif status == 'off':
            message = '<h2>LED in IoT Device is now turned off</h1>'
        else:
            message = '<h2>Wrong Status</h2>'
        self.response(200, message)
        
    # 응답 메시지 전송 함수
    def response(self, status_code, body):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(body.encode())


httpd = HTTPServer(('localhost', 8080), http_handler)
print('Serving HTTP localhost on 8080')
httpd.serve_forever()