import zombiedice

class RandomBot(zombiedice.Bot):
    def __init__(self, name):
        super().__init__(name)

    def turn(self, game_state):
        dice_roll_results = self.roll()
        while dice_roll_results is not None:
            dice_roll_results = self.roll()


class CautiousBot(zombiedice.Bot):
    def __init__(self, name):
        super().__init__(name)

    def turn(self, game_state):
        brains = 0
        shotguns = 0

        dice_roll_results = self.roll()
        while dice_roll_results is not None:
            for die in dice_roll_results:
                if die['color'] and die['value']:
                    if die['value'] == 'brain':
                        brains += 1
                    elif die['value'] == 'shotgun':
                        shotguns += 1

            if shotguns >= 2:
                break
            if brains >= 2:
                break
            dice_roll_results = self.roll()


class GreedyBot(zombiedice.Bot):
    def __init__(self, name):
        super().__init__(name)

    def turn(self, game_state):
        brains = 0
        shotguns = 0

        dice_roll_results = self.roll()
        while dice_roll_results is not None:
            for die in dice_roll_results:
                if die['value'] == 'brain':
                    brains += 1
                elif die['value'] == 'shotgun':
                    shotguns += 1
            if shotguns >= 2:
                break
            dice_roll_results = self.roll()


if __name__ == "__main__":
    zombiedice.runWebGui(
        # Replace or add more bots here
        bots=[
            RandomBot("RandomBot"),
            CautiousBot("CautiousBot"),
            GreedyBot("GreedyBot"),
        ],
        numGames=1000
    )
