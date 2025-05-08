import random

def generate_flips(num_flips=100):
    return [random.choice(['H', 'T']) for _ in range(num_flips)]

def count_streaks(flips, streak_length=6):
    streaks = 0
    current_streak = 1

    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
            if current_streak == streak_length:
                streaks += 1
        else:
            current_streak = 1

    return streaks

def run_simulations(simulations=10000, flip_count=100, streak_len=6):
    streak_occurrences = 0

    for _ in range(simulations):
        flips = generate_flips(flip_count)
        if count_streaks(flips, streak_len) > 0:
            streak_occurrences += 1

    print(f"Chance of a streak of {streak_len} heads or tails in {flip_count} flips: {streak_occurrences / simulations * 100:.2f}%")

if __name__ == "__main__":
    run_simulations()
