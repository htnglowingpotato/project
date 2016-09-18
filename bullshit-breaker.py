<<<<<<< HEAD
import sys, pygame, requests, json, random
=======
import sys, pygame, requests, json, random
>>>>>>> 5b59797be79ea781615951b1d6480cc4c848ba14
from brick import Brick
from brick import Player

#***********************#
#   	Constants		#
#***********************#

#screen 
WIDTH = 640
HEIGHT = 480

#brick info
BRICK_WIDTH = 80
BRICK_HEIGHT = 40

#colors
BRICK_COLOR = (204,0,0)
PLAYER_COLOR = (200,100,0)
BLACK = (0,0,0)
FONT_COLOR = (255,255,0)

#ball
speed = [7, -7]

#player
PLAYER_WIDTH = 120
PLAYER_HEIGHT = 20

#***********************#
#   	 Setup   		#
#***********************#

#game setup
pygame.init()
screen = pygame.display.set_mode((640,480),pygame.RESIZABLE)

#make 4x7 2D list of bricks 
bricks = []
for i in range(4):
	bricks.append([])

for i in range(4):
	for j in range(7):
		bricks[i].append(Brick(10+j*(BRICK_WIDTH+10), 10+i*(BRICK_HEIGHT+10), False))	

#make player
player = Player(260, 440, 5)
pygame.draw.rect(screen, PLAYER_COLOR, (player.x, player.y, PLAYER_WIDTH, PLAYER_HEIGHT), 0)

#make ball
ball = pygame.image.load("trump.png")
ballrect = ball.get_rect()
ballrect.x = 300
ballrect.y = 400


#string to text

test_string1 = "Never met but never liked dopey Robert Gates. Look at the mess the U.S. is in. Always speaks badly of his many bosses, including Obama."

def get_tweet:
	url = 'https://hackthenorth-b9b85.firebaseio.com/negtweets.json?auth=k8oUcZFSAcbBZpHcQkyTPeepFj8ckSG4zQcp1tme&print=pretty'
	response = requests.get(url)
	return json.loads(response.text)[random.choice(json.loads(response.text).keys())]['message']

#string to text
block_words = []
def split_string(text):
	words = text.split()
	for word in words:
		block_words.append(word)

split_string(test_string1)

for i in range(4):
	for j in range(7):
		if(len(block_words)>(7*i+j)):
			bricks[i][j].text = block_words[7*i+j]


lives = 3
hasStarted = False


#***********************#
#   BEGIN RENDER LOOP   #
#***********************#
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(BLACK)

	#set the innitial location of the ball and player, code also used to reset when player loses a life
	if hasStarted == False:
		ballrect.x = 300
		ballrect.y = 390
		player.x = 260
		player.y = 440
	
	#key controls
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and (player.x>=10):
		player.x-=5
	if keys[pygame.K_RIGHT] and (player.x<=WIDTH-10-PLAYER_WIDTH):
		player.x+=5
	if keys[pygame.K_SPACE]:
		hasStarted = True #start game
	pygame.draw.rect(screen, PLAYER_COLOR, (player.x, player.y, PLAYER_WIDTH, PLAYER_HEIGHT), 0)

	#add ball
	if hasStarted == True:
		ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > WIDTH:
		speed[0] = -speed[0]
	if ballrect.top < 0:
		speed[1] = -speed[1]	

	screen.blit(ball, ballrect)	


	#add bricks
	for i in range(4):
		for j in range(7):
			if bricks[i][j].isHit == False:
				pygame.draw.rect(screen, BRICK_COLOR, (bricks[i][j].x,bricks[i][j].y,BRICK_WIDTH,BRICK_HEIGHT), 0)
	
	#font
	myfont = pygame.font.SysFont("monospace", 16)
	for i in range(4):
		for j in range(7):
			label = myfont.render(bricks[i][j].text, 1, FONT_COLOR)
			screen.blit(label, (bricks[i][j].x,bricks[i][j].y))

	#intersection testing
	for i in range(4):
		for j in range(7):
			if pygame.Rect(bricks[i][j].x,bricks[i][j].y,BRICK_WIDTH,BRICK_HEIGHT).colliderect(ballrect):
				bricks[i][j].isHit = True
				bricks[i][j].text = ""

	#see if any cubes are left
	
	count = len(list(filter(lambda x: not x.isHit, bricks[0])))+len(list(filter(lambda x: not x.isHit, bricks[1])))+len(list(filter(lambda x: not x.isHit, bricks[2])))+len(list(filter(lambda x: not x.isHit, bricks[3])))

	if count == 0:
		sys.exit()

	#player hit testing
	if ballrect.colliderect(pygame.Rect(player.x, player.y, PLAYER_WIDTH, PLAYER_HEIGHT)):
		speed[1]= -speed[1]
	if ballrect.bottom > 480 and hasStarted == True:
		lives -= 1
		hasStarted = False
	if lives == 0:
		sys.exit()
	
	pygame.display.flip()
	pygame.display.update()
	
