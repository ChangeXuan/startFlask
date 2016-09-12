##如果你的windows账户是中文名，那当你/*pip install flask*/的时候，可能会出现编码错误<br>
###解决方法
- python目录 Python27\Lib\site-packages 建一个文件sitecustomize.py 
- 写入：

>import sys <br>
>sys.setdefaultencoding('gb2312') 


