from abc import abstractmethod, ABC
from random import choice


class PlayerBase(ABC):
    choices = ['r', 's', 'p']

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(PlayerBase):
    def move(self):
        m = input('Enter your next move: ')
        if m in self.choices:
            return m
        return self.move()


class SystemPlayer(PlayerBase):
    def move(self):
        return choice(self.choices)


class Game:
    """
    Actually there is complicated for creating object we handled that
    that's we need to restraint alot of if and else for creating
    in our play_ground
    after that we should make if in future we have new feature we have interfaced app to
    develop agile

    """
    def start_game(self):
        game_type = input('Enter game type ("s" for single-player "m" for multiple): ')
        if game_type == 's':
            p1 = HumanPlayer()
            p2 = SystemPlayer()
        elif game_type == 'm':
            p1 = HumanPlayer()
            p2 = HumanPlayer()
        else:
            print('Invalid input')
            return self.start_game()

        return p1, p2


game = Game()
player1, player2 = game.start_game()
for player in [player1, player2]:
    print(player.move())
