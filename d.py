import requests

def remove_first_word(src, word):
      pos = src.find(word) + len(word)
      src = src[pos:]
      return src

headers = {'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


for q in range(1, 7, 1):
      url = 'https://comic.naver.com/webtoon/detail?titleId=807314&no={0}'.format(q)
      site = requests.get(url, headers=headers)
      source_data = site.text

      source_data = remove_first_word(source_data, 'title" content="')
      #pos1 = source_data.find('title" content="')+ len('title" content="')
      #source_data = source_data[pos1:]

      pos2 = source_data.find('">')
      a_data = source_data[: pos2].strip()

