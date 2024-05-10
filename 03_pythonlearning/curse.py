def curse(weapon_damage):
    lesser_curse = weapon_damage * 0.5
    greater_curse = weapon_damage * 0.25
    return lesser_curse, greater_curse


def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("==========================")

def main():
    test(100)
    test(500)
    test(1000)


main()
