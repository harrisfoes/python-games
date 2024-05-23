def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    max_enemy_so_far = None
    
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            max_so_far = enemies_dict[enemy]
            max_enemy_so_far = enemy

    return max_enemy_so_far

