game = {
    "hp": 50,
    "mana": 500,
    "armor": 0,
    "spend": 0,
    "shield": 0,
    "poison": 0,
    "recharge": 0,
    "boss_hp": 51,
    "boss_damage": 9
}

def apply_effects(game):
    if game["shield"] > 0:
        game["armor"] = 7
        game["shield"] -= 1
    else:
        game["armor"] = 0

    if game["poison"] > 0:
        game["boss_hp"] -= 3
        game["poison"] -= 1

    if game["recharge"] > 0:
        game["mana"] += 101
        game["recharge"] -= 1

def cast(game, cost):
    new = dict(game)
    new["mana"] -= cost
    new["spend"] += cost
    return new

best = 10 ** 6

def your_move(game):
    global best

    game["hp"] -= 1
    if game["hp"] <= 0:
        return

    apply_effects(game)
    mana = game["mana"]

    if game["spend"] >= best:
        return

    if mana >= 53:
        new = cast(game, 53)
        new["boss_hp"] -= 4
        boss_move(new)

    if mana >= 73:
        new = cast(game, 73)
        new["hp"] += 2
        new["boss_hp"] -= 2
        boss_move(new)

    if mana >= 113 and game["shield"] == 0:
        new = cast(game, 113)
        new["shield"] = 6
        boss_move(new)

    if mana >= 173 and game["poison"] == 0:
        new = cast(game, 173)
        new["poison"] = 6
        boss_move(new)

    if mana >= 229 and game["recharge"] == 0:
        new = cast(game, 229)
        new["recharge"] = 5
        boss_move(new)

def boss_move(game):
    global best

    apply_effects(game)
    if game["boss_hp"] <= 0:
        best = min(best, game["spend"])
        return

    game["hp"] -= max(1, game["boss_damage"] - game["armor"])
    if game["hp"] <= 0:
        return

    your_move(game)

your_move(game)

print(best)