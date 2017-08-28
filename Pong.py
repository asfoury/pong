import pygame

pygame.init()
w = 500
h = 500
screen = pygame.display.set_mode([w,h])
play  = True
white = 255,255,255
clock = pygame.time.Clock()


ball_speed_x = 2
ball_speed_y = 0







speed =[2,1]
counter = 0



class Paddle(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("paddle.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_paddle(self):
        screen.blit(self.image,self.rect)

    def move_paddle(self,key1,key2,stick_speed):
        keys = pygame.key.get_pressed()
        if keys[key1]:
            if self.rect.y > 0:
                self.rect = self.rect.move(0,-stick_speed)
        if keys[key2]:
            if self.rect.y < h - 65:
                self.rect = self.rect.move(0,stick_speed)

    def get_vector_paddle(self):
        ball_vect = pygame.math.Vector2((self.rect.x,self.rect.y))
        print("("+str(ball_vect.x)+", "+str(ball_vect.y)+")")

    

        
class Ball(pygame.sprite.Sprite):
    
    




    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

    def draw_ball(self):
        screen.blit(self.image,self.rect)

    def move_ball(self):
        
        self.rect = self.rect.move(speed)

        if self.rect.top < 0 or self.rect.bottom > h:
            speed[1] = -speed[1]

        if self.rect.right > w or self.rect.left < 0:
            speed[0] = -speed[0]
##            pygame.quit()
##            quit()

    
    def get_vector_ball(self):
        ball_vect = pygame.math.Vector2((self.rect.x,self.rect.y))
        print("("+str(ball_vect.x)+", "+str(ball_vect.y)+")")
   
            

    
            
        

p1 = Paddle(0,(h/2)-30)
p2 = Paddle(w - 6,(h/2) - 30)
b = Ball(w/2,h/2)


def collison(item1,item2):
    if pygame.sprite.collide_rect(item1,item2):
        print("collision")
        speed[0] = -speed[0]
        
    











while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            pygame.quit()
            quit()

    screen.fill(white)

    ball_vect = pygame.math.Vector2((b.rect.x,b.rect.y))
    paddle1_vect = pygame.math.Vector2((p1.rect.x,p1.rect.y))




    p1.draw_paddle()
    p1.move_paddle(pygame.K_w,pygame.K_s,2)

    p2.draw_paddle()
    p2.move_paddle(pygame.K_UP,pygame.K_DOWN,2)
    

    b.draw_ball()
    b.move_ball()
    print(ball_vect.angle_to(paddle1_vect))
    

    

    collison(p1,b)
    collison(p2,b)

 






    pygame.display.flip()
    clock.tick(60)
    






        
        
        
        
    
