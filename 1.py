import requests

headers = {'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


def print_result(result ,*a_data):
    '''
    이름들을 전부 가져오는 목적
    '''
    for q in range(result):
        print(a_data[q])
    

for i in range(1, 9, 1):
    url = 'https://comic.naver.com/webtoon/detail?titleId=807314&no={0}'.format(i)
    site = requests.get(url, headers=headers)
    source_data = site.text

    pos1 = source_data.find('title" content="')+ len('title" content="')
    source_data = source_data[pos1:]

    pos2 = source_data.find('">')
    a_data = source_data[: pos2].strip()
    
    print_result(1, a_data)
    #print(a_data)
