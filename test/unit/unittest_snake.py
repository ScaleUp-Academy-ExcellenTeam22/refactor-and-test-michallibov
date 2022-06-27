import unittest
from snake_game import snake_game


class TestSnake(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        This is like a constructor of the tests class. It creates an instance of the game
        class so we won't need to create an instance of the object we test in each test function.
        """
        cls.snake_instance = snake_game.SnakeGame()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        This is like a destructor. We are using the default destructor.
        """
        pass

    def test_first_position(self) -> None:
        """
        This function tests if the first position of the snake is really in the middle of the
        screen.
        """
        current_snake_position = self.snake_instance.get_snake_position()
        middle_of_screen = snake_game.get_middle_screen_position()
        self.assertEqual(current_snake_position, middle_of_screen)

    def test_snake_length(self) -> None:
        """
        This function tests if the initial length of the snake is really the score + 1.
        """
        self.assertEqual(self.snake_instance.get_score() + 1, self.snake_instance.get_snake_length())

    def test_initial_score(self) -> None:
        """
        This function tests if the initial score is really 0.
        """
        self.assertEqual(self.snake_instance.score, 0)


if __name__ == '__main__':
    unittest.main()
