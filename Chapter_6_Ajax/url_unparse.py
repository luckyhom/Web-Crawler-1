from urllib.parse import parse_qs

url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json' \
      '&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis' \
      '&timestamp=1560081980216'
print(parse_qs(url))