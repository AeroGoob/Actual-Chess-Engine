#main file
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512 
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
  pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
  for piece in pieces:
    IMAGES[piece] = p.image.load("images/" + piece + ".png")
