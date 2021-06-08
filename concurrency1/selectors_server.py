import selectors
import socket

# 이벤트 처리기(셀렉터) 모듈 생성
sel=selectors.DefaultSelector()

# 새로운 클라이언트로부터 연결을 처리하는 함수
# mask는 거의 쓰지 않음
def accept(sock,mask):
    conn, addr = sock.accept()
    print('connected from', addr)
    # 클라이언트 소켓을 이벤트 처리기에 등록 (이 소켓 또한 감시해야 하므로)
    sel.register(conn, selectors.EVENT_READ, read)  

# 기존 클라이언트로부터 수신한 데이터를 처리하는 함수
def read(conn, mask):
    data = conn.rectv(1024)
    if not data:
        # 소켓 연결 종료 시, 이벤트 처리기에서 등록 해제
        sel.unregister(conn)
        conn.close()
        return
    # 정상 상황일 때 
    print('received data:', data.decode())
    conn.send(data)

# --------여기서부터 시작----------
# 소켓 만들기(기본으로 만들면 TCP)
sock = socket.socket()
sock.bind(('', 2500))
sock.listen(5)

# 서버 소켓(신규 클라이언트 연결을 처리하는 소켓)을 이벤트 처리기에 등록
# 인자 : 위에서 만든 소켓(sock), read만 하기 위함, 실행할 함수(accept())
sel.register(sock, selectors.EVENT_READ, accept)
while True:
    # 등록된 객체에 대한 이벤트 감시 시작(블로킹되어있음)
    events = sel.select()  
    # 발생한 이벤트를 모두 검사(이벤트는 여러 개가 될 수 있기 때문에 for루프를 사용)
    # key가 중요함
    for key, mask in events:
        # key.data : 이벤트 처리기에 등록한 callback 함수
        callback = key.data
        # callback 함수 호출 ()
        callback(key.fileobj, mask)
