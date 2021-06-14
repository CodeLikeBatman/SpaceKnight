import pygame #Must have when using the pygame library.

pygame.init()  #Initialize pygame

display_width = 800
display_height = 600
#name a variable (display in this case) where
#the game will be displayed, then set width and height of the window.
#note that the tuple goes in the double brackets.
display = pygame.display.set_mode( ( display_width, display_height) )
pygame.display.update()

#health = 100
score = 0

#Give the game window a caption
pygame.display.set_caption("My First Game!")

# create a text suface object to write in.
#text = font.render('Red Knight Health: ' + str(health), True, ( 0, 255, 0 ), ( 0, 0, 0) )

# create a rectangular object for the text surface object
#textRect = text.get_rect()
 
# set the center of the rectangular object.
#textRect.center = (display_width * 3 //4, display_height //10)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
IMAGES AND SPIRITS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#load the images the game will use 
#first set a string shortcut for the names
folder= "C:/Users/shade/Desktop/PythonWork/artwork/knights/Knights/SeperateImages/BlueKnight_entity_"
bg_image = pygame.image.load("C:/Users/shade/Desktop/PythonWork/artwork/starry_background.png")
#BLUE KNIGHT SPRITES:
walk_right = [
            pygame.transform.scale(pygame.image.load(folder + "walk_right_000.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_right_001.png"), (64,78)), 
            pygame.transform.scale(pygame.image.load(folder + "walk_right_002.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_right_003.png"), (64,78)), 
            pygame.transform.scale(pygame.image.load(folder + "walk_right_004.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_right_005.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_right_006.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_right_007.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_right_008.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_right_009.png"), (64,78))]
walk_left = [
            pygame.transform.scale(pygame.image.load(folder + "walk_000.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_001.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_002.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_003.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_004.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_005.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_006.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_007.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_008.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder + "walk_009.png"), (64,78))
            ]
blue_knight_char = [ 
            pygame.transform.scale(pygame.image.load(folder + "Idle_000.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_001.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_002.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_003.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_004.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_005.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_006.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_007.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_008.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_009.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_000.png"), (64,78) )
            ]
blue_knight_char_r = [
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_000.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_001.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_002.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_003.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_004.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_005.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_006.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_007.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_008.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_009.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder + "Idle_right_000.png"), (64,78) )
]
#RED KNIGHT SPRITES:
folder_red= "C:/Users/shade/Desktop/PythonWork/artwork/knights/Knights/SeperateImages/RedKnight_entity_"

red_knight_walk_right = [       #pygame.transform.flip(image, T/F for horizontal flip, T/F for verticle flip)
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_001.png"), (64,78)), True, False), 
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_000.png"), (64,78)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_002.png"), (64,78)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_003.png"), (64,78)), True, False), 
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_004.png"), (64,78)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_005.png"), (64,78)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_006.png"), (64,78)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_007.png"), (64,78)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_008.png"), (64,78)), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "walk_009.png"), (64,78)), True, False)]


red_knight_walk_left = [
            pygame.transform.scale(pygame.image.load(folder_red + "walk_000.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder_red + "walk_001.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder_red + "walk_002.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder_red + "walk_003.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder_red + "walk_004.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder_red + "walk_005.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder_red + "walk_006.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder_red + "walk_007.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder_red + "walk_008.png"), (64,78)),
            pygame.transform.scale(pygame.image.load(folder_red + "walk_009.png"), (64,78))
            ]
red_knight_char = [ 
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_000.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_001.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_002.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_003.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_004.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_005.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_006.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_007.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_008.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_009.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "Idle_000.png"), (64,78) )
            ]
red_knight_char_r = [ 
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_000.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_001.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_002.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_003.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_004.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_005.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_006.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_007.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_008.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_009.png"), (64,78) ), True, False),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load(folder_red + "Idle_000.png"), (64,78) ), True, False)
]

red_knight_fall_f = [
            pygame.transform.scale(pygame.image.load(folder_red + "dead_front_000.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "dead_front_001.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "dead_front_002.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "dead_front_003.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "dead_front_004.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "dead_front_005.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "dead_front_006.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "dead_front_007.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "dead_front_008.png"), (64,78) )

]

red_knight_fall_b = [
            pygame.transform.scale(pygame.image.load(folder_red + "die_back_000.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "die_back_001.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "die_back_002.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "die_back_003.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "die_back_004.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "die_back_005.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "die_back_006.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "die_back_007.png"), (64,78) ),
            pygame.transform.scale(pygame.image.load(folder_red + "die_back_008.png"), (64,78) )
]

#Set the clock in the game and use this to set the Frams Per Second of the game inside the main game loop
clock = pygame.time.Clock()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
GAME SOUNDS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
soundFolder = "C:/Users/shade/Desktop/PythonWork/sounds/"

#Pass the sound files over into variables using the pygame.mixer.Sound("filename.wav")  sounds must be .wav format
shootSound = pygame.mixer.Sound(soundFolder + "shoot1.wav")
hitSound = pygame.mixer.Sound(soundFolder + "bullet_crack.wav")
deathSound = pygame.mixer.Sound(soundFolder + "death.wav")
collisionSound = pygame.mixer.Sound(soundFolder + "collision.wav")
#to play the sound use shootSound.play()

#Pass background music file over using the pygame.mixer.load("filename")   music can be in .wav or .mp3 format
music = pygame.mixer.music.load(soundFolder + "spaceMusic.wav")
#to play the music continuously (by entering -1 it will keep looping.)
pygame.mixer.music.play(-1)
#adjust the volume:
pygame.mixer.music.set_volume(0.2)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
CREATE CLASSES AND METHODS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Create a class for player so that we can optimize the program as well as clean up the code.
class player(object):   #create a class with name player, object is passed for future stuff but not needed at the moment
    def __init__(self, x, y, player_width, player_height):      #initialize attributes using "self"
        #Our charachter will need some attributes: 
        # x-position, y-position, height, width, velocity
        self.x = x                                #50
        self.y = y                                #500
        self.player_width = player_width          #64
        self.player_height = player_height        #78
        self.velocity = 5                         #velocity                 
        #need to set some variable so we know which direction, if we're walking
        # and how many steps we have taken thus far to set the proper picture etc
        self.facing_left = False
        self.facing_right = False
        self.standing_still = True
        self.is_jump = False
        self.walk_count = 0
        self.stay_still_count = 0
        self.jump_count = 10
        #the hitbox is a rectangle around the spirit where collision can occur
        #adjusting the numbers will refine the collision to get rid of empty space.
        self.hitbox = (self.x + 0, self.y + 0, self.player_width + 0, self.player_height + 0)
        

    #Create a method for the player so that it can draw itself when called
    def draw(self, display):
        if self.walk_count + 1 >= 30:  #the number 30 comes from having 10 index in our knight image (images 000-009) and we will display each for 3 frames, so 3 x 10 = 30
            self.walk_count = 0
        if self.stay_still_count + 1 >= 33: #got 11 images in the indes so 3x11
            self.stay_still_count = 0

        if self.standing_still == False:
            if (self.facing_left == True):
                display.blit(walk_left[self.walk_count//3], ( self.x, self.y) )
                self.walk_count +=1
                self.stay_still_count = 0
            elif (self.facing_right == True):
                #then display our character in the facing left format
                display.blit(walk_right[self.walk_count//3], ( self.x, self.y) )
                self.walk_count +=1
                self.stay_still_count = 0
            
        else:
            #if self.standing_still == False:
            if self.facing_right:
                display.blit(blue_knight_char_r[self.stay_still_count//3], ( self.x, self.y) )
                self.walk_count = 0
                self.stay_still_count += 1
                
            else:
                display.blit(blue_knight_char[self.stay_still_count//3], ( self.x, self.y) )
                self.walk_count = 0
                self.stay_still_count += 1
        self.hitbox = (self.x + 0, self.y + 0, self.player_width + 0, self.player_height + 0)
        #pygame.draw.rect(display, (0,0,255), self.hitbox, 2)   #temporary code to adjust hitbox
    
    def hit(self):
        #pop up a display that says something when player is hit
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("-5", 1, ( 255, 0, 0))          #to say player lost 5 points
        display.blit(text, ( 400 , 300))
        pygame.display.update()                             #display to screen
        #build a timer into blit display so player has time to see it.
        i = 0
        while i < 2:
            pygame.time.delay(10)
            i += 1
            #Make sure that the player can quit the game while its in the loop if they press the X button to close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i =3
                    pygame.quit()



#Create another class for things to throw or lightning bolts etc
class projectile(object):
    def __init__( self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius  #testing out a circle so using radius rather than width and height to try something different.
        self.color = color 
        self.facing = facing    #which way was character facing so know which directly it flow etc -1 is left, 1 is right
        self.velocity = 7 * facing

    #giving the projectile a method to get displayed.
    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius) #after self.radius I can add a 1 if I only want the outline of the circle and not have it filled in.



class villain(object):   #create a class with name player, object is passed for future stuff but not needed at the moment
    def __init__(self, x, y, villain_width, villain_height, end):      #initialize attributes using "self"
        #Our charachter will need some attributes: 
        # x-position, y-position, height, width, velocity
        self.x = x                                #50
        self.y = y                                #500
        self.villain_width = villain_width          #64
        self.villain_height = villain_height        #78
        self.end = end 
        self.path = [self.x, self.end]
        self.hitbox = (self.x, self.y + 0, self.villain_width + 0, self.villain_height + 0)

        self.velocity = 5                         #velocity                 
        self.facing_left = False
        self.facing_right = False
        self.standing_still = True
        self.is_jump = False
        self.walk_count = 0
        self.stay_still_count = 0
        self.jump_count = 10
        self.health = 100
        self.visible = True

    def draw(self, display):
        self.move(display)
        if self.visible == True: #Only draw the villain if health is greater than 0
            if self.walk_count + 1 >= 30:
                self.walk_count = 0
            
            if self.velocity > 0:
                display.blit(red_knight_walk_right[self.walk_count //3], ( self.x, self.y) )
                self.walk_count += 1
            else:
                display.blit(red_knight_walk_left[self.walk_count //3], ( self.x, self.y) )
                self.walk_count += 1
            #want to display 2 rectangels above each other to represent health of the villain.
            #paramaters(x_postion, y-position plus a little above of villain, width of bar, height of bar, optional thickness of rectangle 0 is filled in- 1 thin line -2 thicker etc)
            pygame.draw.rect( display, ( 255, 0, 0), (self.x + 0, self.y -30, 60, 15), 1)
            pygame.draw.rect( display, ( 0, 255, 0), (self.x + 0, self.y -30, 60 - ((3/5)*(100 - self.health)), 15) )
            self.hitbox = (self.x + 0, self.y + 0, self.villain_width + 0, self.villain_height + 0) #move the hitbox with the villain
            #pygame.draw.rect(display, (255,0,255), self.hitbox, 1)   #temporary code to adjust hitbox and draw the hitbox
        else:
            #self.walk_count = 0
            #if self.walk_count + 1 >= 27:
            #    self.walk_count = 0
            if self.velocity > 0:
                if self.walk_count < 27:
                    display.blit(red_knight_fall_f[self.walk_count //3], (self.x, self.y))
                    self.walk_count +=1
                else:
                    pass
            else:
                if self.walk_count < 27:
                    display.blit(red_knight_fall_b[self.walk_count//3], (self.x, self.y))
                    self.walk_count += 1
                else:
                    pass


    def move(self, display):
        if self.velocity > 0: #if moving to the right
            if self.x + self.velocity < self.path[1]: #if position + amount to be moved is less than the endpoint then proceed.
                self.x += self.velocity
            else: #else meaning about to hit endpoint then we need to flip direction of movement
                self.velocity = self.velocity * -1
                self.walk_count = 0 #reset the walk count so the spirit starts fresh
        else: #if moving to the left
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walk_count = 0
        pass
    
    def hit(self):
        print("hit")
        print(self.health)
        if self.health > 0:
            self.health -= 5
        else:
            deathSound.play()
            self.visible = False



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
THINGS THAT NEED TO GET DRAWN IN
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def redraw_game_window():
    #Should be able to get rid of these global variables now that we created the player class.
    #global walk_count
    #global stay_still_count

    #Need to fill the screen before we draw a new rectangle or the old position will remain
    # display.fill((0,0,0)) #This would fill the screen with a solid color
    # to fill the background with an image, set the variable name of image and the starting point of the top left pixel:
    display.blit(bg_image, (0,0))


    text = font.render("Score: " + str(score), 1, ( 255, 0, 0))
    # copying the text surface object to the display surface object
    display.blit(text, (display_width * 1//2, display_height //10))
   


    #Draw a rectangle that will represent our charachter.
    #Here using a rectangle for rectangle, circle , polygons etc are allowed look up documentation for the inputs needed for those.
    #in rect(the window variable we set at the begining where this will be displayed, 
    # color in RGB, rectangle coordinates (x, y, width, height) )
    #pygame.draw.rect(display,( 255, 0, 0), ( x, y, player_width, player_height) ) #replacing out rectangle now with the knight image
    
    #Call our character witht the created player class
    blue_knight.draw(display)

    #Draw the bullets with the created projectile class, since there are list of bullets will use a loop
    for bullet in bullets:    
        bullet.draw(display)

    #Call the red knight villain
    red_knight.draw(display)
    #now we need to refresh the display to see the charachter
    pygame.display.update() 
    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
MAIN GAME LOOP
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#paprameters(fontName, fontSize, Bold, Italic)
font = pygame.font.SysFont("Comic Sans MS", 32, True, True )
#All pygames need a main loop. In the loop it will check for
#Collision, mouse events, if you hit something etc..

#Set up an instance of my player class
# (x_start_position, y_start_position, player_width, player_height)
blue_knight = player( 50, 500, 64, 78)
#create an instance of the villain(red_knight)
red_knight = villain (364, 500, 64, 78, 736 )
shoot_cooldown = 0
bullets = []
run = True
while run:
    #Set a time delay to work as a clock so things dont occur super fast.
    #the number is in milliseconds.
    #pygame.time.delay(33) 
    #Using the clock variable we created near the top will now set the FPS in the loop
    clock.tick(30) #chose 30 FPS
    
    #Check to make sure the villain is still playing. Otherwise points will keep getting hit with the hitbox. If False nothing happens which is when the villain is killed.
    if red_knight.visible ==True:
        #first see if there is a collision, between blue_knights hitbox and villain hitbox
        #first check to see if they are on the same y coordinates
        if blue_knight.hitbox[1] < red_knight.hitbox[1] + red_knight.hitbox[3] and blue_knight.hitbox[1] + blue_knight.hitbox[3] > red_knight.hitbox[1]:
            #check to see if they are in the same x coordinates
            if blue_knight.hitbox[0] + blue_knight.hitbox[2] > red_knight.hitbox[0] and blue_knight.hitbox[0] < red_knight.hitbox[0] +red_knight.hitbox[2]:
                #register the hit between player and villain
                blue_knight.hit()
                score -= 5
                #make a collision sound
                collisionSound.play()  
    else:
        pass     #I could send the player to and end game screen and scroreboard in the future.             

    #create a timer for the shooting cooldown so that it doesn't shoot everything at the same time
    if shoot_cooldown > 0:
        shoot_cooldown += 1
    if shoot_cooldown > 3:
        shoot_cooldown = 0
    


    #Now we are going to start watching for events
    #An event is anything done by the user such as move mouse etc
    #Next line is the syntax used to get events in pygame
    for event in pygame.event.get():
        #First checking to see if they clicked the big X in the top corner
        if event.type == pygame.QUIT:
            #Kills the loop the game is played in.
            run = False

    #for each projectile that is fired
    for bullet in bullets:
        #first see if there is a collision, if the bullet is within the red_knights hitbox then its a collision
        #first check to see if they are on the same y coordinates
        if bullet.y + bullet.radius < red_knight.hitbox[1] + red_knight.hitbox[3] and bullet.y + bullet.radius > red_knight.hitbox[1]:
            #check to see if they are in the same x coordinates
            if bullet.x + bullet.radius > red_knight.hitbox[0] and bullet.x - bullet.radius < red_knight.hitbox[0] +red_knight.hitbox[2]:
                #register the hit to the villain
                red_knight.hit()
                #make a hitSound
                hitSound.play()
                #Score some points
                score += 10
                #make the bullet leave the game
                bullets.pop(bullets.index(bullet))


        #if the bullet is within the screen:
        if bullet.x < display_width and bullet.x > 0:
            bullet.x += bullet.velocity 
        #if the bullet has gone of the screen want to delete it from the list bullets
        else:
            bullets.pop(bullets.index(bullet))
    
    
    #get info from keys that are getting pressed/held down
    keys = pygame.key.get_pressed()

    #create bullets as projectile class when the space bar get hit and takes into account the cooldown timer
    if keys[pygame.K_SPACE] and shoot_cooldown == 0:
        #make shooting sound
        shootSound.play()
        #pygame.time.delay(100) #This works to slow down the bullet firings but slows donw the game as well which is bad.
        if blue_knight.facing_left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5: #limit the number of bullets that can be shot
            bullets.append(projectile(round(blue_knight.x + blue_knight.player_width//2), 
                                      round(blue_knight.y + blue_knight.player_height//2), 
                                      6, (255,255,255), facing))
        shoot_cooldown = 1

    #Now we can check if individual keys were pressed:
    #left arrow key and position of charachter is not goint to move of the screen
    if keys[pygame.K_LEFT] and blue_knight.x > blue_knight.velocity: 
        #move to the left
        blue_knight.x -= blue_knight.velocity
        blue_knight.facing_left = True
        blue_knight.facing_right = False
        blue_knight.standing_still = False
    elif keys[pygame.K_RIGHT] and blue_knight.x < display_width - blue_knight.player_width - blue_knight.velocity:
        blue_knight.x += blue_knight.velocity
        blue_knight.facing_right = True
        blue_knight.facing_left = False
        blue_knight.standing_still = False
    else: #if not moving left or right
        blue_knight.standing_still = True
        blue_knight.walk_count = 0

    #restrict movement in the y direction if jumping.
    if blue_knight.is_jump == False:
        if keys[pygame.K_UP]:
            blue_knight.is_jump = True
            blue_knight.walk_count = 0
            #blue_knight.stay_still_count = 0
    #What happens when jumping:
    else:
        if blue_knight.jump_count >= -10:
            neg = 1
            if blue_knight.jump_count < 0:
                neg = -1
            #the 0.5 is to shrink the movement to the size of the screen
            #neg is to represent changing direction due to gravity at the top of the curve it changes.
            blue_knight.y -= (blue_knight.jump_count **2) * 0.5 * neg 
            blue_knight.jump_count -= 1
        #else exit the jump loop when jump_count reaches -10 and reset is_jump and jump_count
        else:
            blue_knight.is_jump = False
            blue_knight.jump_count = 10
    
    redraw_game_window()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
QUIT GAME AND DUMP MEMORY
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Quit the game and close the browser.
pygame.quit()
#Delete any memory that the game was using.
quit()