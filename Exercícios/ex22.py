#22. Faça um programa em python que abra e reproduza o audio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()