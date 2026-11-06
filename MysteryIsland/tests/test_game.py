import unittest
from game import new_game, move_player, collect_item, is_win, is_lost

class TestMysteryIsland(unittest.TestCase):

    def test_game_starts_with_five_energy(self):
        game = new_game("Ada")
        self.assertEqual(game["energy"], 5)

    def test_new_game_starts_at_beach(self):
        game = new_game("Ada")
        self.assertEqual(game["location"], "Beach")

    def test_new_game_starts_with_empty_inventory(self):
        game = new_game("Ada")
        self.assertEqual(game["inventory"], [])

    def test_player_can_move_to_jungle(self):
        game = new_game("Ada")

        result = move_player(game, "Jungle")

        self.assertTrue(result)
        self.assertEqual(game["location"], "Jungle")
        self.assertEqual(game["energy"], 4)

    def test_invalid_movement_does_not_change_state(self):
        game = new_game("Ada")

        result = move_player(game, "Mountain")

        self.assertFalse(result)
        self.assertEqual(game["location"], "Beach")
        self.assertEqual(game["energy"], 5)

    def test_cannot_cross_bridge_without_rope(self):
        game = new_game("Ada")
        game["location"] = "Jungle"

        result = move_player(game, "Old Bridge")

        self.assertFalse(result)
        self.assertEqual(game["location"], "Jungle")
        self.assertEqual(game["energy"], 5)

    def test_player_collects_rope_in_jungle(self):
        game = new_game("Ada")
        game["location"] = "Jungle"

        result = collect_item(game)

        self.assertEqual(result, "Rope")
        self.assertIn("Rope", game["inventory"])

    def test_player_collects_lantern_in_cave(self):
        game = new_game("Ada")
        game["location"] = "Cave"

        result = collect_item(game)

        self.assertEqual(result, "Lantern")
        self.assertIn("Lantern", game["inventory"])

    def test_player_cannot_collect_rope_twice(self):
        game = new_game("Ada")
        game["location"] = "Jungle"

        collect_item(game)
        result = collect_item(game)

        self.assertIsNone(result)
        self.assertEqual(game["inventory"], ["Rope"])

    def test_player_cannot_collect_lantern_twice(self):
        game = new_game("Ada")
        game["location"] = "Cave"

        collect_item(game)
        result = collect_item(game)

        self.assertIsNone(result)
        self.assertEqual(game["inventory"], ["Lantern"])

    def test_cannot_enter_lighthouse_without_lantern(self):
        game = new_game("Ada")
        game["location"] = "Old Bridge"

        result = move_player(game, "Lighthouse")

        self.assertFalse(result)
        self.assertEqual(game["location"], "Old Bridge")
        self.assertEqual(game["energy"], 5)

    def test_player_wins_at_lighthouse_with_lantern(self):
        game = new_game("Ada")
        game["location"] = "Lighthouse"
        game["inventory"].append("Lantern")

        self.assertTrue(is_win(game))

    def test_player_loses_when_energy_reaches_zero(self):
        game = new_game("Ada")
        game["energy"] = 0

        self.assertTrue(is_lost(game))

    def test_player_cannot_move_with_zero_energy(self):
        game = new_game("Ada")
        game["energy"] = 0

        result = move_player(game, "Jungle")

        self.assertFalse(result)
        self.assertEqual(game["location"], "Beach")
        self.assertEqual(game["energy"], 0)

    def test_last_energy_point_allows_move(self):
        game = new_game("Ada")
        game["energy"] = 1

        result = move_player(game, "Jungle")

        self.assertTrue(result)
        self.assertEqual(game["location"], "Jungle")
        self.assertEqual(game["energy"], 0)
        self.assertTrue(is_lost(game))

    def test_player_does_not_win_without_lantern(self):
        game = new_game("Ada")
        game["location"] = "Lighthouse"

        self.assertFalse(is_win(game))


if __name__ == "__main__":
    unittest.main()