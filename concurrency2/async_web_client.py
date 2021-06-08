import time, asyncio
import urllib.parse

urls = ['https://www.sch.ac.kr', 'https://www.google.co.kr', 'https://www.daum.net', 
        'https://www.naver.com']

async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(url.hostname, 443, ssl=True) 
    else:
        reader, writer = await asyncio.open_connection(url.hostname, 80) 
        
    http_req = f'HEAD / HTTP/1.1\r\nHost: {url.hostname}\r\n\r\n'
    
    writer.write(http_req.encode()) 
    await writer.drain()
    while True:
        resp = await reader.readline()
        if not resp:
            break
        
        resp = resp.decode().rstrip() 
        print(url.hostname, 'HTTP header>', resp)
    
    writer.close()

async def main():
    # 테스크 리스트를 만듬
    tasks = []

    for url in urls: 
        # url 각각에 대해서 http헤더를 출력하는 함수를 이용해 테스크를 만들어 리스트에 추가함
        tasks.append(asyncio.create_task(print_http_headers(url)))

    # 리스트로 gather 하려면 * 붙이기 
    await asyncio.gather(*tasks)

asyncio.run(main())