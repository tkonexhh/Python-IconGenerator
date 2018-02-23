# -*- coding:utf-8 -*-
# coding=UTF-8

import sys
from PIL import Image 
import os

#读取尺寸列表
def load_sizes():
	result=[]
	try:
		size_file=open("size_list.txt")
		for file_line in size_file.readlines():
			content=file_line.strip('\n').split(',')
			line=(int(content[0]),int(content[1]))
			print(line)
			result.append(line)
			
	finally:
		size_file.close()
		
	return result

sizes=load_sizes()
	
#512 尺寸自动生成 各种尺寸
def IconGenerator(coner):
	iconPath=os.getcwd()+"\icon.png"
	conerPath=os.getcwd()+"\coner"+str(coner)+".png"
	
	
	if os.path.exists(iconPath):
		icon=Image.open(iconPath)
		
		if coner!=0:
			conerIcon=Image.open(conerPath)
		
		try:
			for size in sizes:
				icon.thumbnail(size)
				
				
				#如果需要添加角标
				if coner!=0:
					conerIcon.thumbnail(size)
					icon=Image.composite(conerIcon,icon,conerIcon)
					icon.save("icon_"+str(size[0])+"X"+str(size[1])+"_coner"+str(coner)+".png")
				else:
					icon.save("icon_"+str(size[0])+"X"+str(size[1])+".png")
				
		finally:
			icon.close()
	else:
		print("no image")
	
		
IconGenerator(0)
IconGenerator(1)
