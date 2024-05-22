def count_enemies(enemy_names):
    tally = {}

    for enemy_name in enemy_names:
        if enemy_name in tally:
            tally[enemy_name] += 1
        else:
            tally[enemy_name] = 1

    return tally
