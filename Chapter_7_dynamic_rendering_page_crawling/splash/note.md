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

1. url：请求的URL。

2. baseurl：可选参数，默认为空，表示资源加载相对路径。

3. headers：可选参数，默认为空，表示请求头。

4. http_method：可选参数，默认为GET，同时支持POST。

5. body：可选参数，默认为空，发POST请求时的表单数据，使用的Content-type为application/json。

6. formdata：可选参数，默认为空，POST请求时的表单数据，使用的Content-type为application/x-www-form-urlencoded

该方法的返回结果是结果ok和原因reason的组合，如果ok为空，代表网页加载出现了错误，此时reason变量包含了错误的原因，否则证明页面加载成功。

示例如下：

    function main(splash, args)
        local ok, reason = splash:go{"http://httpbin.org/post", http_method="POST", body="name=Germy"}
        if ok then
            return splash:html()
        end
    end
* wait()

此方法可以控制页面等待时间使用方法如下：
ok, reason = splash:wait(time, cancel_on_redirect=false, cancel_on_error=true)

参数说明如下：

1. time：等待的秒数。
2. cancel_on_redirect：可选参数默认为false，表示如果发生重定向就停止等待，并返回重定向的结果。
3. cancel_on_error：可选参数，默认为false，表示如果发生了加载错误，就停止等待。

返回结果也是ok和reason的组合。

* jsfunc()

此方法可以直接调用JavaScript定义的方法，但是所调用的方法需要用双中括号包围，这相当于实现了JavaScript方法到Lua脚本的转换。

* evaljs()

此方法可以执行JavaScript代码并返回最后一条JavaScript语句的返回结果，使用方法如下：

    result = splash:evaljs(js)

* runjs()

此方法可以执行JavaScript代码，它与evaljs()的功能类似，但是更偏向于执行某些动作或声明某些方法。

* autoload()

此方法可以设置每个页面访问时自动加载的对象，使用发放如下：

    ok, reason = splash:autoload{source_or_url, source=nil, url=nil}
参数说明如下：

1. source_or_url：JavaScript代码或者JavaScript库链接。
2. source：JavaScript代码
3. url：JavaScript库链接

此方法只负责加载JavaScript代码或库，不执行任何操作。执行操作的话，需要调用evaljs()或runjs()方法。

* call_later()

此方法可以通过设置定时任务和延迟时间来实现任务延时执行，并且可以在执行前通过cancel()方法重新执行定时任务。

示例如下：

    function main(splash, args)
        local snapshots = {}
        local timer = splash:call_later(function()
            snapshots["a"] = splash:png()
            splash:wait(1.0)
            snapshots["b"] = splash:png()
        end, 0.2)
        splash:go("https://www.taobao.com")
        splash:wait(3.0)
        return snapshots
    end

* http_get()

此方法可以模拟发送HTTP的GET请求，使用方法如下：

    response = splash:http_get{url, headers=nil, follow_redirects=true}
参数说明如下：

1. url：请求URL
2. headers：可选参数，默认为空，请求头。
3. follow_redirects：可选参数，表示是启动自动重定向，默认为true。

* http_post()

此方法用来模拟发送POST请求，使用方法如下：

     response = splash:http_post{url, headers=nil, follow_redirects=true, body=nil}
参数说明如下：

1. url：请求URL。
2. headers：可选参数，默认为空，请求头。
3. follow_redrects：可选参数，表示是否启动自动重定向，默认为true
4. body：可选参数，即表单数据，默认为空

* set_content()

此方法用来设置页面的内容，示例如下：

    function main(splash, args)
        assert(splash:set_content("<html><body><h1>hello</h1></body></html>"))
        return splash:png()
    end

* html()

此方法用来获得网页的源代码

* png()

此方法用来获取PNG格式的网页截图。

* jpeg()

此方法用来获取JPEG格式的网页截图。

* har()

此方法用来获得页面加载过程描述

* url()

此方法可以获取当前正在访问的URL

* get_cookies()

此方法可以获取当前页面的Cookies。

* add_cookies()

此方法可以为当前页面添加Cookies。

* clear_cookies()

此方法可以清除所有的Cookies。

* get_viewport_size()

此方法可以获取当前浏览器页面的大小。

* set_viewport_size()

此方法可以设置当前浏览器页面的大小

* set_viewport_full()

此方法可以设置浏览器全屏显示

* set_uer_agent()

此方法可以设置浏览器的User-Agent。

* set_custom_headers()

此方法可以设置请求头

* select()

该方法可以选中符合条件的第一个节点，如果有多个节点符合条件，则只会返回一个，其参数时CSS选择器。

* select_all()

此方法可以选中所有符合条件的节点，其参数是CSS选择器。

* mouse_click()

此方法可以模拟鼠标点击操作，传入的参数为坐标值的x 和y。此外，也可以直接选中某个节点，然后调用此方法。

### Splash API调用
与python结合调用。

* render.html
此接口用于获取JavaScript渲染的页面的HTML代码，接口地址就是Splash的运行地址加此接口名称，
例如 :

    http://localhost:8050/render.html?url=https://www.baidu.com

我们给此接口传递了一个url参数来指定渲染的URL，返回结果即页面渲染后的源代码。

* render.png

此接口可以获取网页截图，通过width和heigh来控制宽高，返回PNG格式的图片二进制数据。示例如下：

    curl http://localhost:8050/rnder.png?url=https://www.taobao.com&wait=5&width=1000&height=700

* render.jpeg

此接口接口返回jpeg格式的网页截图。参数quality用来设置图片质量。

* render.har

此接口用于获取页面加载的HAR数据，示例如下：

    curl http://localhost:8050/render.har?url=https://www.jd.com&wait=5

* render.json

此接口包含了前面接口的所有功能，返回结果是JSON格式。

* execute

此接口是最为强大的接口，实现了与Lua脚本的对接。

### Splash负载均衡设置

负载均衡的目的就是为了多个服务器分担压力。
假设四台服务器哦IP地址为：

* 127.0.0.1
* 127.0.0.2
* 127.0.0.3
* 127.0.0.4

四台服务器的Splash均通过dockers的splash镜像在端口：8050开启服务。
选择任意一台带有公网IP的主机来配置负载均衡。

首先在服务器安装Nginx。

修改Nginx的配置文件nginx.conf，添加如下内容：

    http {
        upstream splash {  # 服务器集群名为splash
            least_conn;  
            # 代表最少链接负载均衡，去掉此行将使用默认的轮询策略实现负载均衡
            # 若使用ip_hash，此方法确保同一服务器响应请求，此方法适合有状态的服务。
            # Splash不需要应用此设置。
            server 127.0.0.1:8050;
            # 还可以添加weight参数设置权值，权值越高分配到的请求越多。
            server 127.0.0.2:8050;
            server 127.0.0.3:8050;
            server 127.0.0.4:8050;
        }
        server {
            listen 8050;
            location / {
                proxy_pass http://splash;
                # 设置下面两行来进行用户认真。
                auth_basic "Restricted";
                auth_baseic_user_file /etc/nginx/conf.d/.htpasswd;
            }
        }
    }

上面用户认证的用户名和密码配置放置在 /etc/nginx/conf.d 目录下，我们需要使用htpasswd命令创建。

例如，创建一个用户名为admin的文件，相关命令如下：

    htpasswd -c .htpasswd admin
之后输入两次密码即可。

配置完成后需要重启Nginx服务。

测试文件在

    ./test_load_balance.py
