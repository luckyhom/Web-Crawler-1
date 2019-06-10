输入下面命令运行splash：

    docker run -p 8050:8050 scrapinghub/splash
一个splash的基本实例：

    function main(splash, args)
        splash:go("http://www.baidu.com")
        splash:wait(0.5)
        lcoal title = splash:evaljs("document.title")
        return {title=title}
    end
将上面实例复制到 localhost:8050 的代码编辑区域，并将网址设为 http://www.baidu.com

点击Render me！返回 http://www.baidu.com 的title

我们在这里定义的方法名称为main()，这个名称是固定的，Splash会根据这个名字执行。

* 入口及返回值

该方法的返回值既可以是字典形式，也可以是字符串形式，最后都会转化为Splash HTTP Response。

* 异步处理

Splash支持异步处理，但是这里没有显式指明回调方法，其回调实在Splash内部完成的。

示例如下：

    function main(splash, args)
        local example_urls = {"www.baidu.com", "www.taobao.com", "www.zhihu.com"}
        local urls = args.urls or example_urls
        local results  = {}
        for index, url in ipairs(urls) do
            local ok, reason = splash:go("http://" .. url)
            if ok then
                splash:wait(2)
                results[url] = splash:png()
            end
        end
        return results
    end
上面实例运行结果为，三个网站的的截图。
在脚本内调用的wait()方法类似与sleep()。其参数为等待的秒数。

“..”为拼接字符串。

### Splash对象属性
* args

该属性可以获取加载时配置的参数，比如URL，

如果为GET请求，它还可以获取GET请求参数；

如果为POST请求，它可以获取表单提交的数据。

Splash也支持使用第二个参数直接作为args，例如：

    function main(spalsh, args)
        local url = args.url
    end
这里第二个参数args就相当于splash.args属性，以上代码等价于：
    function main(spalsh)
        local url = splash.args.url
    end
* js_enable

这个属性是Splash的JavaScript执行开关，可以将其配置为true或false来控制是否执行JavaScript代码，默认为true.

一般不用设置此属性，默认开启。
* resource_timeout

顾名思义，此属性设置加载的超时时间，单位为秒。如果设置为0或者nil(类似python中的None)，代表不检测超时。

此属性用于加载速度较慢的情况，避免给一直等待，超过时间无响应，直接抛出异常忽略即可。
* image_enable

顾名思义，设置图片是否加载，默认情况加载。禁用之后可以节省网络流量并提高加载速度。

注意，禁用图片加载可能会影响JavaScript渲染。因为禁用图片加载后，它的外层DOM节点的高度会发生变化，进而影响

DOM节点的位置。若JavaScript对图片节点有操作的话，其执行就会有影响。

初次之外Splash使用了缓存，一开始缓存了图片，然后禁用了图片加载。再进行加载图片还会出现，此时重启Splash即可

。
* plugins_enable

此属性控制浏览器插件（如Flash插件）是否开启。默认false，不开启。
* scroll_position

通过设置此属性来控制页面上下或左右滚动。
示例如下：

    function main(splash, args)
        assert(splash:go("https://www.taobao.com"))
        splash.scroll_position = {y=400}
        return {png = splash:png()}
    end
这样我们可以控制页面向下滚动400像素。
### Splash对象方法
* go()

该方法用来请求某个链接，也可以模拟GET和POST请求，同时支持传入请求头、表单等数据，其用法如下：

    ok, reason = splash:go{url, baseurl=nil, http_method="GET", body=nil, formdata=nil}
其参数说明如下：

1.url：请求的URL。

2.baseurl：可选参数，默认为空，表示资源加载相对路径。

3.headers：可选参数，默认为空，表示请求头。

4.http_method：可选参数，默认为GET，同时支持POST。

5.body：可选参数，默认为空，发POST请求时的表单数据，使用的Content-type为application/json。

6.formdata：可选参数，默认为空，POST请求时的表单数据，使用的Content-type为application/x-www-form-urlencoded
