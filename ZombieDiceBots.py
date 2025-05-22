import random

print("Siddarth \n USN:1AY24AI106 \n SEC:O")

DICE_POOL = {
    'green': ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'],
    'yellow': ['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'],
    'red': ['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun']
}

ALL_DICE = ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3

class ZombieBot:
    def __init__(self, name):
        self.name = name
        self.total_brains = 0

    def roll_die(self, color):
        return random.choice(DICE_POOL[color])

    def draw_dice(self, dice_pool, n):
        return [dice_pool.pop(random.randint(0, len(dice_pool)-1)) for _ in range(min(n, len(dice_pool)))]

    def take_turn(self):
        dice_pool = ALL_DICE.copy()
        random.shuffle(dice_pool)

        brains = 0
        shotguns = 0
        footprints = []

        print(f"\n{self.name}'s turn begins!")

        while True:
            needed = 3 - len(footprints)
            drawn_dice = footprints + self.draw_dice(dice_pool, needed)
            footprints = []

            print(f"\nRolling: {drawn_dice}")
            results = [self.roll_die(color) for color in drawn_dice]

            for color, result in zip(drawn_dice, results):
                print(f"Rolled a {color} die: {result}")
                if result == 'brain':
                    brains += 1
                elif result == 'shotgun':
                    shotguns += 1
                else:
                    footprints.append(color)

            print(f"Current: {brains} brains, {shotguns} shotguns")

            if shotguns >= 3:
                print(f"{self.name} got blasted! No brains earned this turn.")
                return 0

            if self.should_stop(brains, shotguns):
                print(f"{self.name} stops and banks {brains} brains.")
                return brains

    def should_stop(self, brains, shotguns):
        # Default bot strategy: stop if 2 brains or 2 shotguns
        return brains >= 2 or shotguns >= 2


class GreedyBot(ZombieBot):
    def should_stop(self, brains, shotguns):
        return shotguns >= 2


class CautiousBot(ZombieBot):
    def should_stop(self, brains, shotguns):
        return brains >= 1 or shotguns >= 1


def simulate_game():
    bots = [ZombieBot("Bot A"), GreedyBot("GreedyBot"), CautiousBot("CautiousBot")]
    scores = {bot.name: 0 for bot in bots}
    turn = 0

    while max(scores.values()) < 13:
        current_bot = bots[turn % len(bots)]
        gained = current_bot.take_turn()
        scores[current_bot.name] += gained
        print(f"{current_bot.name}'s total score: {scores[current_bot.name]}")
        turn += 1

    winner = max(scores, key=scores.get)
    print(f"\n🏆 {winner} wins with {scores[winner]} brains!")


if __name__ == "__main__":
    simulate_game()
