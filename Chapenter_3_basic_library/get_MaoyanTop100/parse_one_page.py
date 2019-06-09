import re


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime'
        '.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S
    )
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip(),
        }


def main():
    html = '''<dd>
                            <i class="board-index board-index-1">1</i>
        <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
          <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
          <img data-src="https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
        </a>
        <div class="board-item-main">
          <div class="board-item-content">
                  <div class="movie-item-info">
            <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
            <p class="star">
                    主演：张国荣,张丰毅,巩俐
            </p>
    <p class="releasetime">上映时间：1993-01-01</p>    </div>
        <div class="movie-item-number score-num">
    <p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
        </div>

          </div>
        </div>

                    </dd>
                    <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/1297" title="肖申克的救赎" class="image-link" data-act="boarditem-click" data-val="{movieId:1297}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@160w_220h_1e_1c" alt="肖申克的救赎" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a></p>
        <p class="star">
                主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
        </p>
<p class="releasetime">上映时间：1994-09-10(加拿大)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                    '''
    dic = parse_one_page(html)
    print(type(dic))
    for item in dic:
        print(item)
        print(type(item))


main()
