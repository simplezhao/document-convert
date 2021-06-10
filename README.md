# document-convert
通过flask API上传文件，然后通过[unoconv](https://github.com/unoconv/unoconv)将文件转为化支持的格式，并返回文件内容



## 使用方法

推荐使用docker的方式运行服务，目前已经编译并上传的docker有两种：

1. [base镜像](https://hub.docker.com/r/simplezhao/document-convert)，安装了转换所需的依赖包，以下是已经安装在镜像的清单
   1. 中文字体
   2. [unoconv](https://github.com/unoconv/unoconv)
   3. libreoffice
   4. [qpdf](https://github.com/qpdf/qpdf)
   5. requirements-prod.txt 依赖包
2. [包含代码镜像](https://hub.docker.com/r/simplezhao/document-convert)，具体生成流程参考Dockerfile

启动镜像：

```bash
docker pull simplezhao/document-convert

docker run -d -p 5000:5000 --rm  simplezhao/document-convert
```

发送请求：

```bash
curl -X "POST" "http://127.0.0.1:5000/convertApi/v1/convert" \
     -H 'Content-Type: multipart/form-data; charset=utf-8; 
     -F "file={content}" \
     -F "convertType=pdf"
```



### 使用的环境变量

如果你使用[sentry](https://docs.sentry.io/platforms/python/guides/flask/performance/) 来监控程序运行，可以将如下变量加入到docker 环境变量中

```bash
SENTRY_DSN=xxx
SENTRY_ENVIRONMENT=dev
SENTRY_TRACES_RATE=1.0
```



### 版本历史

【2021-06-10】实现上传一个文件，并返回pdf文件