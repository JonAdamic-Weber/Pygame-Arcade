"""Weber State University - CS 1400 (Adamic): Programming I -- Midterm Project
Python implementation of the classic game Pong.

This is a template for the implementation of the game Pong. You should
implement the game logic in this file.
"""
# TODO: Remove unused imports and delete this comment before submitting.
import math
import random
import pygame


# Global constants
# TODO: (You may move these to be class attributes if you desire). TODO: Delete this comment before submitting.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
USER1_UP = pygame.K_w       # W key
USER1_DOWN = pygame.K_s     # S key
USER2_UP = pygame.K_UP      # Up arrow key
USER2_DOWN = pygame.K_DOWN  # Down arrow key
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)


# TODO: Implement the Player Class.


# TODO: Implement the Ball Class. (Below is a template to get you started.)
#class Ball():
#    def __init__(self):
#        self.radius = 20
#        self.rect = pygame.Rect(
#            WINDOW_WIDTH / 2 - self.radius / 2,
#            WINDOW_HEIGHT / 2 - self.radius / 2,
#            self.radius, self.radius
#        )
#
# TODO: IMPLEMENT THE REST OF THE BALL CLASS.

class Pong():
    """A class to handle the game logic and state of Pong."""
    def __init__(self):
        """Initialize the game state.

        TODO: IMPLEMENT THIS FUNCTION. You may want to reference the commented
        out code below to help you get started, but you may implement this
        function however you like, as long as the 
        """
        pass # TODO: Remove this line when you start implementing this function.
        # TODO: You may want to add parameters for starting positions for the players and balls, and other initialization values.
        # self.player1 = Player()
        # self.player2 = Player()
        # self.balls = [Ball()]

    def update(self):
        """Update the game objects based on their current state.

        TODO: IMPLEMENT THIS FUNCTION. You may want to reference the commented
        out code below to help you get started, but you may implement this
        function however you like, as long as it updates the objects in the game.
        """
        pass # TODO: Remove this line when you start implementing this function.
        # TODO: You may want to call individual update functions on the players and balls here.
        # TODO: (Again this is just a suggestion, you may implement this function however you like.)
        # self.player1.update()
        # self.player2.update()

        # for ball in self.balls:
            # ball.update([self.player1, self.player2])

    def render(self):
        """Draw the game objects to the window based on their current position.

        TODO: You may need to make slight modifications to this function to
        render your players and balls correctly. See the comments in the code for
        more information.
        """
        # pylint: disable=unsubscriptable-object
        self.window.fill(COLOR_BLACK)

        # Draw a line down the middle of the window.
        pygame.draw.line(
            self.window,
            COLOR_WHITE,
            (WINDOW_WIDTH/2, 0),
            (WINDOW_WIDTH/2, WINDOW_HEIGHT),
            4
        )

        # Draw the balls
        # TODO: You may need to modify this to draw your ball.
        # I assume you will have a list of balls, each with a .rect attribute that is a pygame.Rect
        for ball in self.balls:
            pygame.draw.rect(self.window, COLOR_WHITE, ball.rect)

        # Draw the paddles
        # TODO: You may need to modify this to draw your players' paddles.
        # I assume you will have two players, each with a .paddle attribute that is a pygame.Rect
        pygame.draw.rect(self.window, COLOR_WHITE, self.player1.paddle)
        pygame.draw.rect(self.window, COLOR_WHITE, self.player2.paddle)

        # Draw the scores for each player.
        # TODO: You may need to modify this to draw your players' scores.
        # I assume you will have two players, each with a .score attribute that is an integer
        font = pygame.font.Font(None, 74)
        score1 = font.render(str(self.player1.score), True, COLOR_WHITE)
        score2 = font.render(str(self.player2.score), True, COLOR_WHITE)
        score1_pos = (WINDOW_WIDTH / 4 - score1.get_width() / 2, 30)
        score2_pos = (3 * WINDOW_WIDTH / 4 - score2.get_width() / 2, 30)
        self.window.blit(score1, score1_pos)
        self.window.blit(score2, score2_pos)

        # Flip the display (update the screen)
        pygame.display.flip()

    def run(self):
        """Start the game loop.

        - Calls functions to update the game state and render the game.

        DO NOT MODIFY ANYTHING IN THIS FUNCTION.
        """
        pygame.init()
        pygame.display.set_caption("Pong")
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                # If the user closes the window, quit the game completely.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.KEYDOWN:
                    # If the user presses the escape key, return to the main menu.
                    if event.key == pygame.K_ESCAPE:
                        return True

            # Update and render the game
            self.update()
            self.render()

            # Limit the game to update consistently 60 times per second
            self.clock.tick(60)


if __name__ == "__main__":
    # DO NOT MODIFY ANYTHING IN THIS BLOCK.
    pong = Pong()
    pong.run()
