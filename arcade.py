"""Weber State University - CS 1400 (Adamic): Programming I -- Final Project
Python arcade cabinet.

Main Entrypoint for the Arcade Cabinet.
Handles the main menu and selection of games to play.

===============================================================================
INSTRUCTIONS:
===============================================================================
You should implement the game logic for other games in the folder:
    games/<game_name>/<game_name>.py

Ie: games/pong/pong.py
    games/snake/snake.py

(You may add more games if you wish, but you must implement at least two games.)
Each game should have a class with the same name as the game file.
Each game class should have a run method that starts the game loop.
Ie: the class Pony in games/pong/pong.py has a run method that starts the game loop.

ALL OTHER IMPLEMENTATION DETAILS ARE UP TO YOU. BE CREATIVE AND HAVE FUN!
Feel free to use any of the code from the midterm project as a starting point.

You may also use built-in pygame functions and classes to help you implement your games.
Specifically, pygame.Rect has a lot of useful methods for collision detection and movement.
https://www.pygame.org/docs/ref/rect.html#pygame.Rect

===============================================================================

DO NOT MODIFY ANYTHING IN THIS FILE EXCEPT THE NAME OF THE ARCADE.
"""
import importlib
import os
import pygame


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
COLOR_LIGHT_BLUE = (173, 216, 230)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_BLACK = (0, 0, 0)


class Arcade():
    """A class to handle the main menu and selection of games to play.
    DO NOT MODIFY ANYTHING IN THIS CLASS."""
    def __init__(self, title="Arcade"):
        # A list to store all the game classes we find in the games directory.
        self.title = title
        self._games = []
        self._current_game_index = 0

    def detect_games(self):
        """Detect all games in the games directory and dynamically import them.
        DO NOT MODIFY ANYTHING IN THIS FUNCTION."""
        # Loop through the games directory and import each game module.
        for game_dir in os.listdir("games"):
            game_file = f"games.{game_dir}.{game_dir}"
            try:
                game_module = importlib.import_module(game_file)
                # Get the class from the file and add it to the list of games.
                game_class = getattr(game_module, game_dir.title())
                self._games.append(game_class)
            except ModuleNotFoundError:
                pass

    def main_menu(self):
        """Create main menu and handle user input.
        DO NOT MODIFY ANYTHING IN THIS FUNCTION."""
        pygame.init()
        pygame.display.set_caption(self.title)
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        clock = pygame.time.Clock()

        # Main menu loop
        while True:
            window.fill(COLOR_BLACK)
            font = pygame.font.Font(None, 74)
            title = font.render(self.title, True, COLOR_LIGHT_BLUE)
            window.blit(title, (WINDOW_WIDTH / 2 - title.get_width() / 2, 50))

            # Draw the list of games to the window in gray.
            for index, game in enumerate(self._games):
                game_title = font.render(game.__name__, True, COLOR_GRAY)
                window.blit(
                    game_title,
                    (WINDOW_WIDTH/8, WINDOW_HEIGHT/3 + (index * 100))
                )

            # Highlight the selected game in white.
            # (This simply draws it again so it appears highlighted.)
            selected_game_title = font.render(
                self._games[self._current_game_index].__name__,
                True,
                COLOR_WHITE
            )
            window.blit(
                selected_game_title,
                (WINDOW_WIDTH/8, WINDOW_HEIGHT/3 + (self._current_game_index * 100))
            )

            # Flip the display (update the screen) and advance the clock.
            pygame.display.flip()
            clock.tick(30)

            # Get user input
            for event in pygame.event.get():
                # If the user closes the window or presses esc, quit the game.
                if (event.type == pygame.QUIT or
                    (event.type == pygame.KEYDOWN and
                     event.key == pygame.K_ESCAPE)
                ):
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    # Change the selected game with the up and down arrow keys.
                    if event.key == pygame.K_UP:
                        self._current_game_index = (
                            (self._current_game_index - 1) % len(self._games)
                        )
                    elif event.key == pygame.K_DOWN:
                        self._current_game_index = (
                            (self._current_game_index + 1) % len(self._games)
                        )

                    # If the user presses enter, start the selected game.
                    elif event.key == pygame.K_RETURN:
                        contine_running = self.play_game()
                        # If the game returns False, quit the arcade.
                        if not contine_running:
                            return

    def play_game(self):
        """Create an instance of the current game and run it.
        DO NOT MODIFY ANYTHING IN THIS FUNCTION."""
        # Get the current game from the list of games, and Instantiate it.
        game = self._games[self._current_game_index]()
        return game.run()

    def run(self):
        """Detect games and start the main menu.
        DO NOT MODIFY ANYTHING IN THIS FUNCTION."""
        self.detect_games()
        self.main_menu()


if __name__ == "__main__":
    arcade = Arcade("____'s Arcade")
    arcade.run()
