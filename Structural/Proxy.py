from random import randint


class User:
    pass


class Dice:
    @staticmethod
    def roll_dice():
        return randint(1, 6)


def check_turn(fn):
    def wrapped_func(game, user):
        if game.turn == user:
            game.change_turn()
            return game.dice.roll_dice()
        return fn()

    return wrapped_func


class Game:
    def __init__(self, u1, u2):
        self.user1 = u1
        self.user2 = u2
        self.turn = u1
        self.dice = Dice()

    def change_turn(self):
        if self.turn == self.user1:
            self.turn = self.user2
        else:
            self.turn = self.user1


@check_turn
def roll():
    """
    Proxy pattern check your accessibility to an object
    without destroy struct of our obj
    (Django use it alot of in their FrameWork, and they deploy Proxy patter with "Decorator" adjective in python)
    :return:
    """
    return "It's Not Your Turn!"


if __name__ == "__main__":
    user1 = User()
    user2 = User()

    game = Game(user1, user2)

    print(roll(game, user1))
    print(roll(game, user2))
    print(roll(game, user1))
    print(roll(game, user2))
    print(roll(game, user2))
