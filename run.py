import pygame
import os
import time
import random
pygame.font.init()

#.................................Initialize a window or screen for display 
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invaders")  

#.................................Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "red_alien_ship.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "green_alien_ship.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets","blue_alien_ship.png"))

#...............................The user's character image (player)
WAR_SPACE_SHIP = pygame.image.load(os.path.join("assets","raider_raptor.png"))

#...............................Laser images
RED_LASER = pygame.image.load(os.path.join("assets", "laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "laser_yellow.png"))

#..............................Background image
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "outer_space_bg.png")), (WIDTH, HEIGHT))

#.........................Class for shooting lasers, collision, movement, and exceed screen height  
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img) 
        
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        
    def movement(self, speed):
        self.y += speed
        
    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)
        
    def collision(self, obj):
        return collide(self, obj)

#..................................Ships attributes
class Ship: 
    COOLDOWN = 30
    
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.player_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0
        
    #..........................Method that draws size of player on the window (temporary design *rectangle*)
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y,))
        for laser in self.lasers:
            laser.draw(window)
    
    #..........................................method for different scenarios upon firing lasers          
    def move_lasers(self, speed, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.movement(speed)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
    
    #..................................Timer that allows user to fire lasers again    
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    
    #...................................allows the succession of when lasers can be fired   
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
     
    #........................................returns value of ship width    
    def get_width(self):
        return self.ship_img.get_width()
    
    #........................................returns value of ship height 
    def get_height(self):
        return self.ship_img.get_height()
        
#.........................................attributes for player ship 
class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = WAR_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        
    def move_lasers(self, speed, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.movement(speed)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
    
    #...........................draw health_life
    def draw(self, window):
        super().draw(window)
        self.health_life(window)
    
    
    #....................................................Player's health bar                    
    def health_life(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health), 10))
        

#........................................Enemy ship class and their attributes         
class Enemy(Ship):
    ENEMY_COLORS = {
                   "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
                   "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                   "red": (RED_SPACE_SHIP, RED_LASER)
                    } #.......................................Dictionary for colors of enemy ships 
     
    def __init__(self, x, y, color, health = 100):
        super().__init__(x, y, health)  
        self.ship_img, self.laser_img = self.ENEMY_COLORS[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
     
    #..................................................................Enemy movement     
    def movement(self, speed):
        self.y += speed
        
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
       
#............a collision function for overlapping of two masks based on the offset of their top left coordinates
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

#............................Function that runs game while window remains open
#............................Fucntion that determines player lives and levels
def main():
    run = True
    FPS = 60
    level = 0       
    lives = 5
    main_font = pygame.font.SysFont("showcardgothic", 40)
    loser_font = pygame.font.SysFont("showcardgothic", 40)
    
    enemies = []
    wave_length = 5
    enemy_speed = 2
    
    player_speed = 5
    laser_speed = 6
    
#.............................calling the class player, inputs for players location on the window    
    player = Player(350, 620)
    
    clock = pygame.time.Clock()
    
    lost = False
    lost_count = 0
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        #Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (128, 255, 0))
        level_label = main_font.render(f"Level: {level}", 1, (128, 255, 0))
        
        WIN.blit(lives_label, (20, 20))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 20, 20))
        
        #...................................Draw each enemy on the screen
        for enemy in enemies:
            enemy.draw(WIN)
        
        #...........................Draw window for the appearance of the player     
        player.draw(WIN)
        
        #..................................Displays message when you die in game 
        if lost:
            lost_label = loser_font.render("You Died", 1, (255, 51, 51))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
        
        pygame.display.update()
    #..............................while loop that runs game at 60fps (all devices) and checks for events
    while run:
        clock.tick(FPS)
        redraw_window()
        
        #.........................player dies when he runs out of lives
        if lives <= 0:
            lost = True
            lost_count += 1
        
        #..............................if player loses all health, 1 life is lost and health is reset      
        if player.health == 0:
            lives -= 1
            player.health = 100
            
        #...................................................Timer that quits game after losing    
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        
        #............................. Zero enemies triggers the next level with 2 more enemies added
        if len(enemies) == 0:
            level += 1
            wave_length += 3
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1300, -100), random.choice(["blue", "green", "red"]))
                enemies.append(enemy)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        #..................................Key input for user movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_speed > -10: #.........................Left
            player.x -= player_speed
        if keys[pygame.K_d] and player.x + player_speed + player.get_width() -10 < WIDTH: #......................Right
            player.x += player_speed
        if keys[pygame.K_s] and player.y + player_speed + player.get_height() + 10 < HEIGHT: #.........................Down
            player.y += player_speed
        if keys[pygame.K_w] and player.y - player_speed > 0: #.........................Up
            player.y -= player_speed
        if keys[pygame.K_SPACE]:
            player.shoot()
        
        #.....................................Speed in which the enemies and lasers move on the screen    
        for enemy in enemies[:]:
            enemy.movement(enemy_speed)
            enemy.move_lasers(laser_speed, player)
            
            if random.randrange(0, 2*60) == 1:
                enemy.shoot()
                
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy) 
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
                      
        player.move_lasers(-laser_speed, enemies) # checks if lasers have collided with enemies

#.................fucntion for main-menu that begins with a mouse click 
def main_menu():
    title_font = pygame.font.SysFont("showcardgothic", 40)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Click 'MOUSE' to begin!", 1, (51, 255, 51))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()           
    pygame.quit()                                             
        
main_menu()