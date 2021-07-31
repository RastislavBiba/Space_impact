import pygame
import random
import sys

meteor_img = pygame.image.load("acces/Meteor1.png")
bonus_img = pygame.image.load("acces/bonus.jpg")
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def generate_meteor(meteor_img):
    return{
        "mask": pygame.mask.from_surface(meteor_img),
        "x": random.choice(range(10, 440, 60)),
        "y": random.choice(range(-10, -500, -60)),
    }
def generate_bonus(bonus_img):
    return{
        "mask": pygame.mask.from_surface(bonus_img),
        "x": random.choice(range(10, 440, 50)),
        "y": random.choice(range(-10, -500, -50)),
    }
def kolizia(mask1, mask2, mask1_coords, mask2_coords):
    x_off = mask2_coords[0] - mask1_coords[0]
    y_off = mask2_coords[1] - mask1_coords[1]
    if mask1.overlap(mask2, (x_off, y_off)):
        return True
    else:
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    meteors= []
    meteor_speed = 0
    pocet = 5
    bg = pygame.image.load("acces/background.jpg")
    lod = pygame.image.load("acces/ship.png")

    window = pygame.display.set_mode((500, 800))

    game_font = pygame.font.SysFont("Arial", 20)
    ship_x=(250)
    ship_y = (720)

    meteor_x= (250)
    meteor_y=(0)
    score = 0
    lod_mask = pygame.mask.from_surface(lod)
    bonus_mask = pygame.mask.from_surface(bonus_img)
    live = 1
    while True:
        score_text = game_font.render(f"Score: {score}", True, (255,255,255))
        live_text = game_font.render(f"Live: {live}", True, (255,255,255))
        if len(meteors) == 0:
            for i in range(pocet):
                if random.randint(1,7) == 5:
                    meteors.append(generate_bonus(bonus_img))
                meteors.append(generate_meteor(meteor_img))
            meteor_speed += 1
            pocet += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if ship_x > 0:
                ship_x -= 5
        if keys[pygame.K_RIGHT]:
            if ship_x < 430:
                ship_x += 5
        window.blit(bg, (0, 0))
        if live > 0:
            for meteor in meteors[:]:
                window.blit(meteor_img, (meteor["x"], meteor["y"]))
                meteor["y"] += meteor_speed
                if meteor["y"] > 800:
                    score += 1
                    meteors.remove(meteor)

                if kolizia(lod_mask, meteor['mask'], (meteor["x"], meteor["y"]),(ship_x, ship_y)):
                    live -= 1
                else:
                    live = 1
        if live == 0:
            koniec_text = game_font.render(f"GAME OVER", True, (255,255,255))
            window.blit(koniec_text, (155, 400))

        window.blit(score_text, (350,20))
        window.blit(live_text, (20, 20))
        window.blit(lod, (ship_x,ship_y))

        pygame.display.update()
        clock.tick(60)

