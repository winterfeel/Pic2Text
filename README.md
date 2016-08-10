# pic2text 图片转文字
A script to transform picture to text, supporting Chinese</br>
一个将图片转换成文字图的脚本，支持中文</br>
刚学Python不久，代码不是特别简洁，因为要计算出灰度范围，导致循环了两次</br>
为了支持中文，必须要使用中文字体</br>
代码基本每一行都注释了</br>
效果图：
![image](preview.jpg)
# Dependencies 环境依赖
Python 2.7</br>
PIL

# How to use 如何使用
copy a font file to your directory and edit line 27:</br>
拷贝一个字体文件到目录，然后修改代码27行中的字体名称：
```python
  ft = ImageFont.truetype("msyhbd.ttf",fontSize)
```
edit last several lines of codes:</br>
编辑最后几行代码：
```python
    textList = ['撒','啊','呵','王','一']
    pic2Text('test.jpg',textList)
```
sort characters by Density</br>
按照字母笔画密集程度排列

# About 关于作者
不灭的小灯灯</br>
Love programming,love designing</br>
Mail:winterfeel@qq.com</br>
Blog:www.winterfeel.com
