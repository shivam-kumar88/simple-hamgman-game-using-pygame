import pygame
import os
import math
import random

#display setup
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('hang him')

#button veriables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + (GAP * 2) + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + (i // 13) * (RADIUS * 2 + GAP)
    letters.append([x, y, chr(A + i), True])

#fonts

LETTERS_FONTS = pygame.font.SysFont('comicsans', 35) #here (name of font style, size of font)
WORD_FONT = pygame.font.SysFont('Helvetica', 40)
MSG_FONT = pygame.font.SysFont('Helvetica', 60)
TITLE_FONT = pygame.font.SysFont('Helvetica', 20)

#greafical image setup
images = []
for i in range(7):
    Image = pygame.image.load("hangman"+str(i)+".png")
    images.append(Image)

#variables of the project
hangman_status = 0
f = open("hangman words.txt", 'r')
words = f.readlines() #ADDED the text file using file handeling
word = random.choice(words)
print(word)
guessed = []

#COLOURS GRADING
WHITE = (255, 255, 255) #here the values are for RGB respectevely SO 255 IS MAX value and 0 is MIN value.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#game loop setup
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)
    text = TITLE_FONT.render("HangHim Game \n\n By Shivam Kumar", 1, BLUE)
    win.blit(text, (100, 20))

    #draw word
    display_word = " "
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '
        else:
            display_word += '_ '
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))


    #draw button
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS,2)  # here (where, color, cordinates, radius, pxlelwidth of circle)
            text = LETTERS_FONTS.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))   # text.get_hight()/2 is basic math


    win.blit(images[hangman_status], (100, 100))
    pygame.display.update()

def gameresult_message(message):
    if message == "you won":
        COLOUR = GREEN
        text = MSG_FONT.render("you WON!", 1, BLACK)

    else:
        COLOUR = RED
        text = MSG_FONT.render("you LOSE!", 1, BLACK)
    win.fill(COLOUR)
    win.blit(text, (0, 0))
    pygame.display.update()
    pygame.time.delay(3000)

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)  # pythagoras theorem -- it lets know what button we pressed
                    if dis < RADIUS:
                        letter[3] = False
                        print(ltr)
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
       gameresult_message("you won")
       break

    if hangman_status == 6:
        gameresult_message("you lose")
        break


pygame.quit()





# and to re open the game after the  result we just have to put  the while loop in the in diffent functuion
# and use global vareable for  stuff like the "hangman " status



# although the game is ready