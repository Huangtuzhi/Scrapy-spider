# Scrapy-spider
A scrapy spider.

## 安装

Windows 上安装坑略多，详见 [Scrapy 安装](https://my.oschina.net/lvyi/blog/779541) 博客

## 配置代理

连接公司的 WIFI 也需要用代理，配置方法

settings.py 中加入

```
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'tutorial.middlewares.ProxyMiddleware': 100,
}
```

和 settings 同级目录新建 middlewares.py，加入以下代码

```
class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = "http://web-proxy.oa.com:8080"
```

## 输出结果

`scrapy crawl oscspider -o items.json`

以 json 的格式序列化后输出抓取的网页内容，json 格式与 items.py 中定义的字典有关，在 spider.py 中重写的 parse 方法指定在字典中存储用 xpath 选择器选择的数据。items.py 其实就是和 Django 一样使用的 ORM 对象的方式存储数据。
