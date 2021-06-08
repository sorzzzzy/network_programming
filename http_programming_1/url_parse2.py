'''
urllib.parse.urlsplit(url[, ...]) 함수
- url을 분해하여 5개의 요소를 갖는 SplitResult 객체를 반환
    − SplitResult는 튜플의 서브클래스인 namedtuple 객체임
'''

from urllib import parse 

url = 'https://homepage.sch.ac.kr/sch/06/06050000.jsp?mode=view&article_no=20200528202911520374&pager.offset=0&board_no=20200302132057325672'

parsed_url = parse.urlsplit(url)
print(parsed_url)
print('scheme :', parsed_url.scheme)    #https 
print('netloc :', parsed_url.netloc)    #homepage.sch.ac.kr
print('path :', parsed_url.path)        #/sch/06/06050000.jsp 
print('query :', parsed_url.query)      #mode=view&article_no=20200528202911520374&pager.offset=0&board_no=20200302132057325672
print('fragment:', parsed_url.fragment)