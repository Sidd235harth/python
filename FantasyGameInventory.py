def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print(f"Total number of items: {item_total}")


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


# Example usage
if __name__ == "__main__":
    player_inventory = {
        'gold coin': 42,
        'rope': 1,
        'torch': 6,
        'dagger': 1
    }

    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    print("Before collecting loot:")
    display_inventory(player_inventory)

    player_inventory = add_to_inventory(player_inventory, dragon_loot)

    print("\nAfter collecting loot:")
    display_inventory(player_inventory)
