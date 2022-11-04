import pygame
import playsound
import os

print(os.getcwd())

pygame.mixer.init()
pygame.mixer.music.load('ori.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


playsound.playsound('ori.mp3')