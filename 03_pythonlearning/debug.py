def take_magic_damage(health, resist, amp, spell_power):
   max_damage = spell_power * amp 
   actual_damage = max_damage - resist
   return health - actual_damage
