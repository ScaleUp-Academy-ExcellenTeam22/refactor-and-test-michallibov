import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 10
# The speed of the snake
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def message() -> None:
    """
    This function prints to the screen the message when the user loses.
    """
    msg = font_style.render("You Lost! Press C-Play Again or Q-Quit", True, red)
    dis.blit(msg, [dis_width / 6, dis_height / 3])


def our_snake(snake_block, snake_list) -> None:
    """
    This function draws the snake.
    :param snake_block: the square that represents one unit of length of the snake.
    :param snake_list: the list of the snake (that is built from snake_blocks)
    """
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def get_middle_screen_position() -> tuple:
    """
    This function returns the position of the middle of the screen of the game (the point where the snake
    starts)
    :return: a tuple of x and y of the middle of the screen of the game.
    """
    return dis_width / 2, dis_height / 2


class SnakeGame(object):
    """
    This class represents an instance of the game. I chose to do it like that so we can test each functionality
    easily with a logic.
    """
    def __init__(self):
        """
        The constructor of the game. It initializes the members of the game.
        """
        self.game_close = False
        self.game_over = False
        self.snake_list = []
        self.length_of_snake = 1
        self.x_dir = 0
        self.y_dir = 0
        self.current_x = dis_width / 2
        self.current_y = dis_height / 2
        self.food_x = 0
        self.food_y = 0
        self.score = 0

    def get_snake_length(self) -> int:
        """
        This function returns the current length of the snake.
        :return: the length of the snake.
        """
        return self.length_of_snake

    def get_key(self) -> None:
        """
        This function reads from the user a key when the user is lost- 'q' for quitting and 'c' to
        continue the game. The function will update the members if needed.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_over = True
                    self.game_close = False

                if event.key == pygame.K_c:
                    self.set_game()

    def get_score(self) -> int:
        """
        This function returns the current score of the player.
        :return: the score.
        """
        return self.score

    def get_food_position(self) -> tuple:
        """
        This function returns the current position of the food.
        :return: a tuple of x and y of the position of the food.
        """
        return self.food_x, self.food_y

    def print_score(self) -> None:
        """
        This function prints the score to the screen of the game.
        """
        value = score_font.render("Your Score: " + str(self.score), True, yellow)
        dis.blit(value, [0, 0])

    def set_dir(self):
        """
        This function sets the direction of the snake at the beginning of the game.
        """
        self.y_dir = 0
        self.x_dir = 0

    def get_snake_position(self) -> tuple:
        """
        This function returns the current position of the snake.
        :return: a tuple of x and y of the current position of the snake.
        """
        return self.current_x, self.current_y

    def change_dir(self) -> tuple:
        """
        This function changes the direction of the snake based on the key the user pressed.
        :return: The new direction of the snake.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_dir = -snake_block
                    self.y_dir = 0
                elif event.key == pygame.K_RIGHT:
                    self.x_dir = snake_block
                    self.y_dir = 0
                elif event.key == pygame.K_UP:
                    self.y_dir = -snake_block
                    self.x_dir = 0
                elif event.key == pygame.K_DOWN:
                    self.y_dir = snake_block
                    self.x_dir = 0
        self.check_position()
        self.current_x += self.x_dir
        self.current_y += self.y_dir
        return self.x_dir, self.y_dir

    def set_game(self) -> None:
        """
        This function sets the game when it starts. It will initialize all the needed elements in the game.
        :return:
        """
        self.game_over = False
        self.game_close = False

        self.current_x = dis_width / 2
        self.current_y = dis_height / 2

        self.x_dir = 0
        self.y_dir = 0

        self.snake_list = []
        self.length_of_snake = 1
        self.randomize_food_location()

    def check_position(self) -> None:
        """
        This function checks if the position of the snake is good. If not, the game will be over.
        """
        if self.current_x >= dis_width or self.current_x < 0 or self.current_y >= dis_height or self.current_y < 0:
            self.game_close = True

    def randomize_food_location(self) -> None:
        """
        This function randomizes the food's position after each time the snake ate it.
        """
        self.food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    def update_snake(self) -> None:
        """
        This function updates the snake (increases it's size) every time the snake eats the food. It also
        updates the score.
        """
        snake_head = list()
        snake_head.append(self.current_x)
        snake_head.append(self.current_y)
        self.snake_list.append(snake_head)
        if len(self.snake_list) > self.length_of_snake:
            del self.snake_list[0]

        for x in self.snake_list[:-1]:
            if x == snake_head:
                self.game_close = True
        our_snake(snake_block, self.snake_list)
        self.print_score()

    def game_loop(self) -> None:
        """
        This function controls the game. It runs the game and calls all other functions.
        """
        self.randomize_food_location()
        while not self.game_over:

            while self.game_close:
                dis.fill(blue)
                message()
                self.set_dir()
                self.print_score()
                self.get_key()
                pygame.display.update()

            self.change_dir()

            dis.fill(blue)
            pygame.draw.rect(dis, green, [self.food_x, self.food_y, snake_block, snake_block])
            self.update_snake()
            pygame.display.update()

            if self.current_x == self.food_x and self.current_y == self.food_y:
                self.randomize_food_location()
                self.length_of_snake += 1
                self.score += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.game_loop()
