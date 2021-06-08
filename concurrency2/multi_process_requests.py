# 2개의 사이트를 번갈아 가면서 총 160번 웹 페이지 요청/응답 수신
# 멀티 프로세싱

import requests, time
import multiprocessing

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name 
        print(f"{name}:Read {len(response.content)} \
            from {url}")

def download_all_sites(sites):
    # 프로세스 5개 만듬
    with multiprocessing.Pool(processes=5, initializer=set_global_session) as pool:
        pool.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://homepage.sch.ac.kr",
        "https://www.google.co.kr", 
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")