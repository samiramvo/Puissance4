import pygame
import moviepy.editor

pygame.init()
video= moviepy.editor.VideoClip("C://Users//Samira//Pictures//pexels-frank-cone-3279307.mp4")
video.preview()
pygame.quit()