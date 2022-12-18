import pygame

import random

import time



pygame.init()



field=[]

infov=[]

infoh=[]

checkv=[]

checkh=[]



def textfunc(r,x,i,o):

  if r == 0:

    a=""

  elif r == 1:

    a="1"

  elif r == 2:

    a="2"

  elif r == 3:

    a="3"

  elif r == 4:

    a="4"

  elif r == 5:

    a="5"

  elif r == 6:

    a="6"

  elif r == 7:

    a="7"

  elif r == 8:

    a="8"

  elif r == 9:

    a="9"

  text = font.render(a, True, x)

  screen.blit(text, [i,o])



  

def draw():

  for y in range(0,9):

      for x in range(0,4):

          if len(infov[y])>=(x+1):

              r=infov[y][x]

              lx=261-x*70

              ly=341+y*70

              textfunc(r,BLUE,lx,ly)

              if r == 0:

                pygame.draw.circle(screen, BLACK, [(270-70*x), (355+70*y)], 33, 3)

  for y in range(0,9):

      for x in range(0,4):

          if len(infoh[y])>=(x+1):

              r=infoh[y][x]

              lx=345+y*70

              ly=258-x*70

              textfunc(r,BLUE,lx,ly)

              if r == 0:

                pygame.draw.circle(screen, BLACK, [(355+70*y), (270-70*x)], 33, 3)



def difficulty(x):

  chance=x*20+5

  for x in range(0,9):

    row=[]

    for y in range(0,9):

      gen=random.randrange(0,100)+1

      if gen<=chance:

        row.append(1)

      else:

        row.append(0)

    if row == [1,0,1,0,1,0,1,0,1]:

      for y in range(0,9):

        row.append(random.randrange(0,2))

    if row == [1,0,1,0,1,0,1,0,1]:

      row=[1,1,1,0,1,0,1,1,0]

    field.append(row)

  return field



def tutorial():

  screen.fill(WHITE)

  tortext=titlef.render("Sex",True,RED)

  x=0

  while x == 0:

    ev = pygame.event.get()

    for event in ev:

      if event.type==pygame.MOUSEBUTTONDOWN:

        x=1

  

size = (1000, 1000)

screen = pygame.display.set_mode(size) 

pygame.display.set_caption("CrossBlock") 

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

BLUE = (0, 0, 255)

GREEN = (0, 255, 0)

RED = (255, 0, 0)

YELLOW = (255,255,51)

dif=0

mode=0

font = pygame.font.SysFont('Calibri', 38, True, False)

fontst = pygame.font.SysFont('Calibri', 140, True, False)

titlef = pygame.font.SysFont('Arial',180,True,False)



screen.fill(BLACK)

pygame.draw.rect(screen, GREEN, [72,382,856,237])

pygame.draw.rect(screen, YELLOW, [72,691,856,237])

title = titlef.render("CrossBlock", True, WHITE)

screen.blit(title,[100,126])

playtext = fontst.render("PLAY", True, BLACK)

screen.blit(playtext, [330,442])

tuttext = fontst.render("TUTORIAL", True, BLACK)

screen.blit(tuttext, [178,751])

pygame.display.flip()

while mode==0:

  for event in pygame.event.get():

    if event.type==pygame.MOUSEBUTTONDOWN:

      pos = pygame.mouse.get_pos()

      if 72<pos[0]<928:

        if 382<pos[1]<619:

          mode=1

        elif 691<pos[1]<928:

          mode=2



if mode == 2:

  tutorial()

screen.fill(BLACK)

pygame.draw.rect(screen, GREEN, [72,73,856,237])

pygame.draw.rect(screen, YELLOW, [72,382,856,237])

pygame.draw.rect(screen, RED, [72,691,856,237])

easytext = fontst.render("EASY", True, BLACK)

screen.blit(easytext, [350,132])

mediumtext = fontst.render("MEDIUM", True, BLACK)

screen.blit(mediumtext, [219,442])

hardtext = fontst.render("HARD", True, BLACK)

screen.blit(hardtext, [330,751])

pygame.display.flip()

while dif==0:

  ev = pygame.event.get()

  for event in ev:

    if event.type==pygame.MOUSEBUTTONDOWN:

      pos = pygame.mouse.get_pos()

      if 72<pos[0]<928:

        if 73<pos[1]<310:

          dif=3

        elif 382<pos[1]<619:

          dif=2

        elif 691<pos[1]<928:

          dif=1

difficulty(dif)

for x in range(0,9):

  c=0

  irow=[]

  for y in range(0,10):

    if y==9:

      if c>0:

        irow.append(c)

    else:

      if field[x][y] == 1:

        c+=1

      else:

        if c>0:

          irow.append(c)

          c=0

  xrow = irow[::-1]

  while len(xrow)<5:

    xrow.append(0)

  infov.append(xrow)

for x in range(0,9):

  c=0

  irow=[]

  for y in range(0,10):

    if y==9:

      if c>0:

        irow.append(c)

    else:

      if field[y][x] == 1:

        c+=1

      else:

        if c>0:

          irow.append(c)

          c=0

  xrow = irow[::-1]

  while len(xrow)<5:

    xrow.append(0)

  infoh.append(xrow)

player=[]

for o in range(0,9):

    f=[]

    for i in range(0,9):

        f.append(0)

    player.append(f)

acheck=[]

done = False

clock = pygame.time.Clock()

screen.fill(BLACK)

pygame.draw.rect(screen, RED, [30,30,220,110])

pygame.draw.rect(screen, BLUE, [320,320,630,630])

resettext = font.render("RESET", True, WHITE)

screen.blit(resettext, [95,68])

pygame.draw.circle(screen, BLACK, [(60+70*x), (355+70*y)], 33, 3)

game=0

for x in range(0,9):

   for y in range(0,9):

       pygame.draw.rect(screen, BLACK, [(322+x*70),(322+y*70),66,66])

for i in range(355,916,70):

    pygame.draw.circle(screen, BLUE, [60, i], 33, 3)

    pygame.draw.circle(screen, BLUE, [130, i], 33, 3)

    pygame.draw.circle(screen, BLUE, [200, i], 33, 3)

    pygame.draw.circle(screen, BLUE, [270, i], 33, 3)

for p in range(355,916,70):

    pygame.draw.circle(screen, BLUE, [p, 60], 33, 3)

    pygame.draw.circle(screen, BLUE, [p, 130], 33, 3)

    pygame.draw.circle(screen, BLUE, [p, 200], 33, 3)

    pygame.draw.circle(screen, BLUE, [p, 270], 33, 3)

draw()

acheck=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

while game==0:

    ev = pygame.event.get()

    for event in ev:

         if event.type==pygame.MOUSEBUTTONUP:

             pos = pygame.mouse.get_pos()

             if 30<pos[0]<250:

               if 30<pos[1]<140:

                 draw()

                 for x in range(0,9):

                   for y in range(0,9):

                     pygame.draw.rect(screen, BLACK, [(322+x*70),(322+y*70),66,66])

                     player[x][y]=0

                     acheck[x][y]=0                   

             if 322<pos[0]<388:

                 xcl=0

             elif 392<pos[0]<458:

                 xcl=1

             elif 462<pos[0]<528:

                 xcl=2

             elif 532<pos[0]<598:

                 xcl=3

             elif 602<pos[0]<668:

                 xcl=4

             elif 672<pos[0]<738:

                 xcl=5

             elif 742<pos[0]<808:

                 xcl=6

             elif 812<pos[0]<878:

                 xcl=7

             elif 882<pos[0]<948:

                 xcl=8

             else:

                 break

             if 322<pos[1]<388:

                 ycl=0

             elif 392<pos[1]<458:

                 ycl=1

             elif 462<pos[1]<528:

                 ycl=2

             elif 532<pos[1]<598:

                 ycl=3

             elif 602<pos[1]<668:

                 ycl=4

             elif 672<pos[1]<738:

                 ycl=5

             elif 742<pos[1]<808:

                 ycl=6

             elif 812<pos[1]<878:

                 ycl=7

             elif 882<pos[1]<948:

                 ycl=8

             else:

                 break

             if player[ycl][xcl]==0:

                 if event.button == 1 or event.button == 2:

                   pygame.draw.rect(screen, WHITE, [(322+xcl*70),(322+ycl*70),66,66])

                   player[ycl][xcl]=1

                   acheck[ycl][xcl]=1

                 else:

                   pygame.draw.rect(screen, BLACK, [(322+xcl*70),(322+ycl*70),66,66])

                   pygame.draw.line(screen, RED, [(326+xcl*70),(326+ycl*70)],[(384+xcl*70),(384+ycl*70)],5)

                   player[ycl][xcl]=2

                   acheck[ycl][xcl]=0

             elif player[ycl][xcl]==1:

                 if event.button == 1 or event.button == 2:

                    pygame.draw.rect(screen, BLACK, [(322+xcl*70),(322+ycl*70),66,66])

                    player[ycl][xcl]=0

                    acheck[ycl][xcl]=0

                 else:

                    pygame.draw.rect(screen, BLACK, [(322+xcl*70),(322+ycl*70),66,66])

                    pygame.draw.line(screen, RED, [(326+xcl*70),(326+ycl*70)],[(384+xcl*70),(384+ycl*70)],5)

                    player[ycl][xcl]=2

                    acheck[ycl][xcl]=0

             elif player[ycl][xcl]==2:

                 pygame.draw.rect(screen, BLACK, [(322+xcl*70),(322+ycl*70),66,66])

                 player[ycl][xcl]=0

             checkv=[]

             checkh=[]

             for x in range(0,9):

                c=0

                irow=[]

                for y in range(0,10):

                  if y==9:

                    if c>0:

                      irow.append(c)

                  else:

                    if acheck[x][y] == 1:

                      c+=1

                    else:

                      if c>0:

                        irow.append(c)

                        c=0

                xrow = irow[::-1]

                while len(xrow)<5:

                  xrow.append(0)

                checkv.append(xrow)

             for x in range(0,9):

                c=0

                irow=[]

                for y in range(0,10):

                  if y==9:

                    if c>0:

                      irow.append(c)

                  else:

                    if acheck[y][x] == 1:

                      c+=1

                    else:

                      if c>0:

                        irow.append(c)

                        c=0

                xrow = irow[::-1]

                while len(xrow)<5:

                  xrow.append(0)

                checkh.append(xrow)

             for i in range(0,9):

                if checkv[i][0]==infov[i][0] and checkv[i][1]==infov[i][1] and checkv[i][2]==infov[i][2] and checkv[i][3]==infov[i][3]:

                  for q in range(0,4):

                    r=infov[i][q]

                    lx=261-70*q

                    ly=341+i*70

                    textfunc(r,GREEN,lx,ly)

                else:

                  for q in range(0,4):

                    r=infov[i][q]

                    if r != 0:

                      pygame.draw.circle(screen, BLACK, [(270-70*q), (355+70*i)], 34)

                      pygame.draw.circle(screen, BLUE, [(270-70*q), (355+70*i)], 33, 3)

                    lx=261-70*q

                    ly=341+i*70

                    textfunc(r,BLUE,lx,ly)

             for i in range(0,9):

                if checkh[i][0]==infoh[i][0] and checkh[i][1]==infoh[i][1] and checkh[i][2]==infoh[i][2] and checkh[i][3]==infoh[i][3]:

                  for q in range(0,4):

                    r=infoh[i][q]

                    lx=345+i*70

                    ly=258-q*70

                    textfunc(r,GREEN,lx,ly)

                else:

                  for q in range(0,4):

                    r=infoh[i][q]

                    if r!=0:

                      pygame.draw.circle(screen, BLACK, [(355+70*i), (270-70*q)], 34)

                      pygame.draw.circle(screen, BLUE, [(355+70*i), (270-70*q)], 33, 3)

                    lx=345+i*70

                    ly=258-q*70

                    textfunc(r,BLUE,lx,ly)

    if checkv == infov and checkh == infoh:

      game=1

    pygame.display.flip()

    clock.tick(45)

fontw = pygame.font.SysFont('Calibri', 176, True, False)

fontw2 = pygame.font.SysFont('Calibri', 180, True, False)

wintext = fontw.render("YOU WON!", True, WHITE)

wintext2 = fontw2.render("YOU WON!", True, GREEN)

screen.blit(wintext2, [80,400])

screen.blit(wintext, [90,400])

pygame.display.flip()

print ("YOU WON!")

print (field)

finish=0

while finish == 0:

  ev = pygame.event.get()

  for event in ev:

    if event.type==pygame.MOUSEBUTTONDOWN:

      finish=1

pygame.quit()

