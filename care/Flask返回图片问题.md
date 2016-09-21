##图片文件放置问题

- 在"templates"同级目录下创建一个名字为"static"的文件夹
- 把需要使用的图片放入"static"文件夹中
- 在路由控制的"view.py"中,<br>

```Python
from flask import Response

@main.route("/<imgName>")
def image(imgName):
    return Response(imgName, mimetype="image/jpeg")
```
- 如果在"static"中有一个"112211.jpg"的图片，那访问的地址为:http://localhost:8080/static/112211.jpg
- 如果在"static"中有一个"images"的文件夹,"images"文件夹中有一个"112211.jpg"的图片，那访问的地址为:http://localhost:8080/static/images/112211.jpg
