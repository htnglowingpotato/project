import sys, pygame
from brick import Brick
from brick import Player

#screen constants
WIDTH = 640
HEIGHT = 480

#brick info
BRICK_WIDTH = 80
BRICK_HEIGHT = 40

#colors
BRICK_COLOR = (204,0,0)
PLAYER_COLOR = (200,100,0)
BLACK = (0,0,0)

#ball
speed = [6, -6]


#game setup
pygame.init()
screen = pygame.display.set_mode((640,480),pygame.RESIZABLE)

#make 2D list of bricks
bricks = []
for i in range(3):
	bricks.append([])

for i in range(3):
	for j in range(7):
		bricks[i].append(Brick(10*j+10+j*BRICK_WIDTH,10*i+10+i*BRICK_HEIGHT,False))	

#make player
player = Player(260, 440, 5)
pygame.draw.rect(screen, PLAYER_COLOR, (player.x, player.y, 120, 20), 0)

#make ball
ball = pygame.image.load("trump.png")
ballrect = ball.get_rect()
ballrect.x = 300
ballrect.y = 400

lives = 3
reStart = False

#***********************#
#   BEGIN RENDER LOOP   #
#***********************#
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(BLACK)
	if reStart == False:
		ballrect.x = 300
		ballrect.y = 390
		player.x = 260
		player.y = 440
	#key controls
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and (player.x>=10):
		player.x-=5
	if keys[pygame.K_RIGHT] and (player.x<=WIDTH-10-120):
		player.x+=5
	if keys[pygame.K_SPACE]:
		reStart = True
	pygame.draw.rect(screen, PLAYER_COLOR, (player.x, player.y, 120, 20), 0)

	#add ball
	if reStart == True:
		ballrect = ballrect.move(speed)
		#ballrect = pygame.transform.rotate(ballrect, 60)
	if ballrect.left < 0 or ballrect.right > WIDTH:
		speed[0] = -speed[0]
	if ballrect.top < 0:
		speed[1] = -speed[1]	

	screen.blit(ball, ballrect)	


	#add bricks
	for i in range(3):
		for j in range(7):
			if bricks[i][j].isHit == False:
				pygame.draw.rect(screen, BRICK_COLOR, (bricks[i][j].x,bricks[i][j].y,BRICK_WIDTH,BRICK_HEIGHT), 0)
	
	#intersection testing
	for i in range(3):
		for j in range(7):
			if pygame.Rect(bricks[i][j].x,bricks[i][j].y,BRICK_WIDTH,BRICK_HEIGHT).colliderect(ballrect):
				bricks[i][j].isHit = True

	#see if any cubes are left
	
	count = len(list(filter(lambda x: not x.isHit, bricks[0])))+len(list(filter(lambda x: not x.isHit, bricks[1])))+len(list(filter(lambda x: not x.isHit, bricks[2])))

	if count == 0:
		sys.exit()


	#player hit testing
	if ballrect.colliderect(pygame.Rect(player.x, player.y, 120, 5)):
		speed[1]= -speed[1]
	if ballrect.bottom > 480 and reStart == True:
		lives -= 1
		reStart = False
	if lives == 0:
		sys.exit()
	
	pygame.display.flip()
	pygame.display.update()
	
