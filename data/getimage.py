#encoding: utf-8
import os
import pygame

chinese_dir = 'character images'
chinese_txt = 'result.txt'
if not os.path.exists(chinese_dir):
	os.mkdir(chinese_dir)
pygame.init()

with open(chinese_txt, 'r') as f:
	for line in f.readlines():
	    cur_line = line.strip() # 把末尾的'\n'删掉
	    print(cur_line)
	    for word in cur_line:
	    	font = pygame.font.Font("msyh.ttf", 64)
	    	rtext = font.render(word, True, (0, 0, 0), (255, 255, 255))
	    	pygame.image.save(rtext, os.path.join(chinese_dir, word + ".png"))
