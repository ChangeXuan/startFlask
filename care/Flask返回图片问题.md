##图片文件放置问题

- 在"templates"同级目录下创建一个名字为"static"的文件夹
- 把需要使用的图片放入"static"文件夹中(假如有一个"112211.jpg")
- 在路由控制的"view.py"中,<br>

@main.route("/<imgName>")
def image(imgName):
  return Response(imgName,mimetype="image/jpeg")

