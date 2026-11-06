# The island map
ISLAND_MAP = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave", "Old Bridge"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Jungle", "Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}


def new_game(player_name):
    return {
        "name": player_name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "jungle_decision_made": False,
        "cave_decision_made": False,
        "game_over": False,
        "won": False
    }


def move_player(game, destination):
    if game["energy"] <= 0:
        return False

    current_location = game["location"]

    if destination not in ISLAND_MAP[current_location]:
        return False

    if destination == "Old Bridge" and "Rope" not in game["inventory"]:
        return False

    if destination == "Lighthouse" and "Lantern" not in game["inventory"]:
        return False

    game["location"] = destination
    game["energy"] -= 1

    return True


def collect_item(game):
    item = None

    if game["location"] == "Jungle":
        item = "Rope"

    elif game["location"] == "Cave":
        item = "Lantern"

    if item is not None and item not in game["inventory"]:
        game["inventory"].append(item)
        return item

    return None


def is_win(game):
    return (
        game["location"] == "Lighthouse"
        and "Lantern" in game["inventory"]
    )


def is_lost(game):
    return game["energy"] <= 0