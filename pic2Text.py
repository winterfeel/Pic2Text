#-*- coding:utf-8 -*-
from PIL import Image,ImageDraw,ImageFont

def pic2Text(_file,_text):
	img = Image.open(_file).convert("RGBA")
	w = 100 #宽度固定
	h = int((float(img.size[1])/float(img.size[0]))*w) #高度按比例得出
	fontSize = 20 #输出字体大小
	img.thumbnail((w,h)) #获取缩略图
	src = img.convert('L') #转换成灰度图
	minGrey = 255 #最小灰度
	maxGrey = 0 #最大灰度
	greyMap =  [[0 for col in range(h)] for row in range(w)] #灰度图 注意 w h
	#此处循环求得灰度表以及最大最小灰度值
	for i in range(w):
		for j in range(h):
			greyMap[i][j] = src.getpixel((i,j)) #获取每一个点的灰度值
			if greyMap[i][j] > maxGrey: #获取最大灰度
				maxGrey = greyMap[i][j]
			if greyMap[i][j] < minGrey: #获取最小灰度
				minGrey = greyMap[i][j]
	#计算灰度间隔
	greyStep = (maxGrey - minGrey)/len(_text)
	#此处生成文字图片,注意输出的时候 w 和 h
	output = Image.new('RGBA',(w*fontSize,h*fontSize),(255,255,255))
	draw = ImageDraw.Draw(output)
	ft = ImageFont.truetype("msyhbd.ttf",fontSize) #注意字体支持中文
	for j in range(h):
		for i in range(w):
			index = int((greyMap[i][j] - minGrey)//greyStep) #计算出改点使用哪个字符
			if index >= len(_text):
				index = len(_text) - 1  #注意结尾最大灰度值，防止越界
			draw.text((i*fontSize,j*fontSize),unicode(_text[index],'UTF-8'), fill=img.getpixel((i,j)), font=ft) #汉字编码
	output.save(_file.split('.')[0] + '_text.jpg','JPEG')

if __name__ == '__main__':
	textList = ['骤','撒','啊','哈','王','一']
	pic2Text('test.jpg',textList)