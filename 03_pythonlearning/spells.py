def remove_duplicates(spells):
    spell_set = set()
    unique_spells = []

    for spell in spells:
        spell_set.add(spell)

    for spell in spell_set:
        unique_spells.append(spell)

    return unique_spells
