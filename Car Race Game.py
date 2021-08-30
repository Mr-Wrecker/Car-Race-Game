# Library Importing
import pygame
import time
import random

# Start Pygame Engine
pygame.init()

# Frime Rate
FPS = pygame.time.Clock()

# Create Window Display For Game
window_width = 800
window_height = 600
display = pygame.display.set_mode((window_width, window_height))

# Set Window Display Caption
pygame.display.set_caption("Car Race")

# Main BackGround For Window Display
Background = pygame.image.load('ref//BackGround.jpg')

# Load Score Icon
Score_image = pygame.image.load('ref//Score.png')

# Cars Load
Race_Car = pygame.image.load("ref//Cars//Car.png")
Race_Car_width, Race_Car_height = Race_Car.get_size()
Car1 = pygame.image.load("ref//Cars//Car-1.png")
Car2 = pygame.image.load("ref//Cars//Car-2.png")
Car3 = pygame.image.load("ref//Cars//Car-3.png")
Car4 = pygame.image.load("ref//Cars//Car-4.png")
Car5 = pygame.image.load("ref//Cars//Car-5.png")
Car6 = pygame.image.load("ref//Cars//Car-6.png")
Car_List = [Car1, Car2, Car3, Car4, Car5, Car6]

Road_line = pygame.image.load('ref//Road line.png')


# Colors
White_Color = (255, 255, 255)
Black_Color = (0, 0, 0)

# --------------------------------- Defintion ---------------------------------


def wellcom():  # First Page When Game Run
    # pygame.key.name(event.key)
    # Load First Page Image
    Home_Page = pygame.image.load('ref//home.jpg')

    while True:
        for event in pygame.event.get():    # Get Any Event From Game Display
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    main()

        display.blit(Home_Page, (0, 0))
        Print_Message("Press Enter To Start", White_Color, 410, 500, 20)
        pygame.display.update()
        FPS.tick(25)


def Print_Score(score):
    display.blit(Score_image, (30, 10))
    Print_Message('Score : ' + str(score), White_Color, 90, 40, 15)


def text_object(text, font, color):
        textsurface = font.render(text, True, color)
        return textsurface, textsurface.get_rect()


def Print_Message(text, color, x_pos, y_pos, font_size):
    print_font = pygame.font.Font('freesansbold.ttf', font_size)
    textsurf, textrect = text_object(text, print_font, color)
    textrect.center = (x_pos, y_pos)
    display.blit(textsurf, textrect)


def draw_road(R_y):
    display.blit(Road_line, (175, R_y))
    display.blit(Road_line, (325, R_y))
    display.blit(Road_line, (475, R_y))
    display.blit(Road_line, (625, R_y))


def draw_car(C_y, Car, Location):
    display.blit(Car, (Location, C_y))


def draw_race_car(x, y):
    display.blit(Race_Car, (x, y))


def crash(action, score):
    Crash_image = pygame.image.load('ref//car-accident-top.jpg')

    with open('Score.txt', 'a') as file:
        file.write(str(score) + '\n')
# 
    time.sleep(0.5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    main()
# 
        display.fill(White_Color)
        display.blit(Crash_image, (100, 0))
        Print_Message("Y O U - C R A S H E D", Black_Color, 425, 425, 60)
        Crash_Guard = "You have an accident with the  Guard"
        Crash_Cars = "You have an accident with the  Cars"
# 
        if action == 'Guard':
            Print_Message(Crash_Guard, Black_Color, 425, 485, 15)
        else:
            Print_Message(Crash_Cars, Black_Color, 425, 485, 15)
        Print_Message("FOR PLAY AGANE PRESS ENTER", Black_Color, 425, 500, 10)
# 
        pygame.display.update()
        FPS.tick(30)


def main():

    car_loc = [75, 225, 375, 525, 675]

    Car = random.choice(Car_List)
    Car_width, Car_height = Car.get_size()
    Car_location = random.choice(car_loc)

    Race_Car_x = 375
    Race_Car_y = window_height * 0.7

    RoadLine_y = -50
    CarLine_y = -600
    speed = 7

    Race_Car_x_Change = 0
    Race_Car_y_Change = 0

    scores = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Race_Car_y_Change = -5

                if event.key == pygame.K_DOWN:
                    Race_Car_y_Change = 4

                if event.key == pygame.K_LEFT:
                    Race_Car_x_Change = -(speed)

                if event.key == pygame.K_RIGHT:
                    Race_Car_x_Change = speed

            if event.type == pygame.KEYUP:
                Race_Car_x_Change = 0
                Race_Car_y_Change = 0

        Race_Car_x += Race_Car_x_Change  # Move Car To UP and Down
        Race_Car_y += Race_Car_y_Change  # Move Car To LEFT and RIGHT
        if Race_Car_y < 40:
            Race_Car_y = 40
        if Race_Car_y > 450:
            Race_Car_y = 450

        display.blit(Background, (0, 0))  # Set BackGround Road Image

        Print_Score(scores)  # Show Scores in Main Window Display

        draw_road(RoadLine_y)  # Draw Line Road
        RoadLine_y += speed
        if RoadLine_y + 600 > window_height:  # Repeat Drawing Line Road
            RoadLine_y = -50
            draw_road(RoadLine_y)

        draw_race_car(Race_Car_x, Race_Car_y)  # Draw Race Car
        draw_car(CarLine_y, Car, Car_location)  # Draw Cars
        CarLine_y += speed
        if CarLine_y > window_height:  # Repeat Cars
            CarLine_y = -200
            Car = random.choice(Car_List)
            Car_location = random.choice(car_loc)
            draw_car(CarLine_y, Car, Car_location)
            scores += 1
            if scores % 2 == 0:
                speed += 1

        # Accident with the wall
        if Race_Car_x < 20 or Race_Car_x > window_width-(Race_Car_width):
            crash('Guard', scores)
        # Accident with Cars
        # -------------------------------------------------------------------------------------------------------------
        if (CarLine_y - Race_Car_height < Race_Car_y and
        Race_Car_y < CarLine_y + Race_Car_height):
            if (Race_Car_x > Car_location and
            Race_Car_x < Car_location + Car_width):
                crash(None, scores)
            elif (Race_Car_x + Race_Car_width > Car_location and
            Race_Car_x < Car_location + Car_width):
                crash(None, scores)

        # -----------------------------------------------------------------------------------------------------------------
        pygame.display.update()
        FPS.tick(60)


if __name__ == "__main__":
    wellcom()
