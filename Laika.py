# Brooke Barlow and Alexis Warren (bcb2tc and alw6ec)
"""We are making a game where the player is a husky named Laika who is trying to recruit as many cats as possible while
trying not to fall ill by other obstacles. The game ends once the health bar is empty (4 obstacle hit). For the optional
pieces we are going to implement animation, enemies, collectibles, and a health bar."""

import gamebox
import pygame
import random

camera = gamebox.Camera(800, 600)

game_on = False
end_game = False
score = 0
health = 100
dog_speed = 5
cat_speed = 7
screenWidth = 800
screenHeight = 600
x = 400
y = 500
width_dog = 20
height_dog = 20
# colors = ['brown', 'black', 'gray', 'orange']
ticks = 4000
# dog sprites
# dog = gamebox.from_color(400, 300, "white", 20, 20)
# dog = gamebox.from_image(400, 300, "http://www.pngmart.com/files/8/Husky-PNG-Transparent-Image.png")
sprite_sheet = gamebox.load_sprite_sheet("https://opengameart.org/sites/default/files/Dog_1.png", 6, 6)
dog = gamebox.from_image(600, 500, sprite_sheet[0])
sprite_sheet_wolf = gamebox.load_sprite_sheet("http://orig13.deviantart.net/5545/f/2013/318/f/5/smile_dog___rpg_sprites_by_lagoon_sadnes-d5vz65h.png", 4, 4)
wolf = gamebox.from_image(200, 400, sprite_sheet_wolf[10])
frame = 0
wolf.scale_by(3)
# cats
"""cat = [
  gamebox.from_color((random.randrange(100, 800)), random.randrange(100, 600), "brown", 20, 20),
  gamebox.from_color((random.randrange(100, 800)), random.randrange(100, 600), "black", 20, 20),
  gamebox.from_color((random.randrange(100, 800)), random.randrange(100, 600), "gray", 20, 20),
  gamebox.from_color((random.randrange(100, 800)), random.randrange(100, 600), "orange", 20, 20)
]"""

a = gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600), "Cat-Small-Cute-PNG.png")
b = gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600), "brown-white-cat-png-4.png")
c = gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600), "580b57fbd9996e24bc43bb8a.png")
# d = gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600), "http://www.pngonly.com/wp-content/uploads/2017/06/Cat-Sweet-PNG-File.png")
a.scale_by(.20)
b.scale_by(.15)
c.scale_by(.15)
# d.scale_by(.03)
cat = [
    # gamebox.from_image((random.randrange(100,800)), random.randrange(100, 600), a),
    # gamebox.from_image((random.randrange(100,800)), random.randrange(100, 600), b),
    # gamebox.from_image((random.randrange(100,800)), random.randrange(100, 600), c),
    # gamebox.from_image((random.randrange(100, 800)), random.randrange(100,600), d)
    a, b, c]

cats = ["https://www.pngonly.com/wp-content/uploads/2017/06/Cat-Small-Cute-PNG.png", "https://www.freeiconspng.com/uploads/brown-white-cat-png-4.png",
       "http://assets.stickpng.com/thumbs/580b57fbd9996e24bc43bb8a.png"]
# "http://www.pngonly.com/wp-content/uploads/2017/06/Cat-Sweet-PNG-File.png"]

# obstacles
d = gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600), "http://www.clipartbest.com/cliparts/4i9/ogA/4i9ogAqGT.png")
d.scale_by(.01)
obstacle = [d]

# background image
background = gamebox.from_image(400, 300, 'alley.jpg')

# I will make the health bar here
health_bar = [gamebox.from_color(75, 60, "dark green", 30, 10), gamebox.from_color(75, 60, "green", 30, 10),
             gamebox.from_color(75, 60, "yellow", 30, 10), gamebox.from_color(75, 60, "red", 30, 10), ]

walls = [
  gamebox.from_color(400, 600, "black", 1000, 20),
  gamebox.from_color(400, 0, "black", 1000, 20),
  gamebox.from_color(0, 400, "black", 20, 1000),
  gamebox.from_color(800, 400, "black", 20, 1000)]


def dog_movements(keys):
   """in here we need to code the dog to move and we could also code what should happen when the dog touches an
   obstacle or a cat and update score and health in this function then in tick function we need to call this moving the
    dog sprite without leaving the screen"""

   # for dog in dogs:
   if pygame.K_DOWN in keys and y < screenWidth - height_dog - dog_speed:
       dog.speedy = +5
       dog.image = sprite_sheet[16]
   if pygame.K_UP in keys and y > dog_speed:
       dog.speedy = -5
       dog.image = sprite_sheet[15]
   if pygame.K_LEFT in keys:
       dog.speedx = -5
       dog.image = sprite_sheet[12]
   if pygame.K_RIGHT in keys:
       dog.speedx = +5
       dog.image = sprite_sheet[14]
   dog.move_speed()


def tick(keys):
   global score, ticks
   global health, dog_speed, x, y, width_dog, height_dog, screenWidth, game_on, frame, end_game
   if game_on is False:
       camera.clear('black')
       camera.draw(gamebox.from_text(camera.x, camera.y - 100, "Laika's Secret Mission ", 100, "red"))
       camera.draw(dog)
       camera.draw(wolf)
       camera.draw(gamebox.from_text(camera.x - 200, camera.y + 25, "You'll pay Laika!!", 25, "white"))
       camera.draw(gamebox.from_text(camera.x - 200, camera.y + 50, "Tonight, in the back alley", 25, "white"))
       camera.draw(gamebox.from_text(camera.x - 50, camera.y + 250, "Press space to continue", 30, "white"))
       if pygame.K_SPACE in keys:
           camera.clear('black')
           camera.draw(dog)
           camera.draw(gamebox.from_text(camera.x + 175, camera.y + 125, "I'm going to need to recruit backup...", 25, "white"))
           camera.draw(gamebox.from_text(camera.x + 175, camera.y + 150, "Who though? All of the other dogs are on his side.", 25, "white"))
           camera.draw(gamebox.from_text(camera.x-350, camera.y - 100, "Meooow....", 25, "white"))
           camera.draw(gamebox.from_text(camera.x - 50, camera.y + 250, "Press space to begin", 30, "white"))
           camera.draw(gamebox.from_text(camera.x, camera.y -100, "Collect the cats while avoiding the cacti", 30, "green"))
           camera.draw(gamebox.from_text(camera.x, camera.y - 125, "Move using the arrow keys", 30, "green"))
           camera.display()
   if pygame.K_SPACE in keys:
       camera.clear("white")
       game_on = True
   ticks -= 1
   score_box = gamebox.from_text(75, 30, "Score: " + str(score), 24, "white")
   timer_box = gamebox.from_text(75, 10, "Time left: " + str(ticks), 24, "white")
   if game_on is True and end_game is False:
       camera.draw(background)
       frame += 1
       if frame > 35:
           frame = 0
       # dog = gamebox.from_image(camera.x, camera.y, dogs[frame])
       camera.draw(dog)
       dog_movements(keys)
       for wall in walls:
           camera.draw(wall)
       for c in cat:
           camera.draw(c)
           c.x -= random.randrange(1, 3)
           if c.right < camera.left:
               c.x += random.randrange(100, 800)
               c.y = random.randrange(100, 600)
           if dog.touches(c, -25):
               cat.remove(c)
               score += 1
           if len(cat) < 4:
               for i in range(4):
                   x = random.randint(0, len(cats) - 1)
                   random_cat = cats[x]
                   p = gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600), random_cat)
                   p.scale_by(0.2)
                   cat.append(p)

                   """cat.append(
                       gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600), random_cat)
                   )
                   print(cat)"""

                   # gamebox.from_image(random.randrange(100, 800), random.randrange(100, 600), random_cat))

       for o in obstacle:
           camera.draw(o)
           o.x -= 1
           if o.right < camera.left:
               o.x += random.randrange(100, 800)
               o.y = random.randrange(100, 600)
           if dog.touches(o, -25):
               obstacle.remove(o)
               health -= 33
           if len(obstacle) < 2:
               for i in range(2):
                   # x = random.randint(0, len(colors2) - 1)
                   p = gamebox.from_image((random.randrange(100,800)), random.randrange(100, 600), "http://www.clipartbest.com/cliparts/4i9/ogA/4i9ogAqGT.png")
                   p.scale_by(0.01)
                   obstacle.append(p)
                   # gamebox.from_color(random.randrange(100, 800), random.randrange(100, 600), "green", 20, 15))
       camera.draw(score_box)
       camera.draw(timer_box)
       camera.display()

       if dog.touches(walls[0]):
           dog.yspeed = -dog_speed
           dog.xspeed = -dog_speed
       if dog.touches(walls[1]):
           dog.yspeed = dog_speed
           dog.xspeed = dog_speed
       if dog.touches(walls[2]):
           dog.yspeed = dog_speed
           dog.xspeed = dog_speed
       if dog.touches(walls[3]):
           dog.yspeed = -dog_speed
           dog.xspeed = -dog_speed

       if 67 < health <= 100:
           camera.draw(health_bar[0])
       elif 34 < health <= 67:
           camera.draw(health_bar[1])
       elif 1 < health <= 34:
           camera.draw(health_bar[2])
       elif 0 < health <= 1:
           camera.draw(health_bar[3])
       elif health < 1 and score > 20:
           end_game = True
           camera.clear('black')
           camera.draw(gamebox.from_text(camera.x, camera.y - 100, "You Won!", 100, "red"))
           camera.draw(gamebox.from_text(camera.x, camera.y + 20, "You collected " + str(score) + " cats", 35, "white"))
           camera.draw(gamebox.from_text(camera.x, camera.y + 50, "Which were enough cats to win in the fight", 35, "white"))
           camera.draw(gamebox.from_text(camera.x, camera.y + 80, "Press q to leave", 35, "white"))
           camera.display()
       elif health < 1 and score <= 20:
           end_game = True
           camera.clear('black')
           camera.draw(wolf)
           camera.draw(gamebox.from_text(camera.x, camera.y - 100, "Game Over", 100, "red"))
           camera.draw(gamebox.from_text(camera.x, camera.y + 80, "Your score is: " + str(score), 35, "white"))
           camera.draw(gamebox.from_text(camera.x, camera.y + 50, "Press q to leave", 35, "white"))
           camera.draw(gamebox.from_text(camera.x, camera.y + 300, "ticks: " + str(ticks) + "score:" + str(score), 35, "white"))
           camera.display()

       if ticks == 3000:
           if len(obstacle) < 6:
               p = gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600), "http://www.clipartbest.com/cliparts/4i9/ogA/4i9ogAqGT.png")
               p.scale_by(0.01)
               obstacle.append(p)

       if ticks == 2000:
           if len(obstacle) < 7:
               p = gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600), "http://www.clipartbest.com/cliparts/4i9/ogA/4i9ogAqGT.png")
               p.scale_by(0.01)
               obstacle.append(p)

       if ticks == 1000:
           if len(obstacle) < 8:
               p = gamebox.from_image((random.randrange(100, 800)), random.randrange(100, 600),"http://www.clipartbest.com/cliparts/4i9/ogA/4i9ogAqGT.png")
               p.scale_by(0.01)
               obstacle.append(p)

   if pygame.K_q in keys:
       gamebox.stop_loop()

   camera.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
