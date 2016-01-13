boss_hp = 51
boss_damage = 9

player_hp = 50
player_mana = 500
player_armor = 0

shield_active = False
poison_active = False
recharge_active = False

MAGIC_MISSILE_COST = 53
DRAIN_COST = 73
SHIELD_COST = 113
POISON_COST = 173
RECHARGE_COST = 229

def cast_magic_missile():
    if player_mana >= MAGIC_MISSILE_COST:
        player_mana -= MAGIC_MISSILE_COST
        boss_hp -= 4
        return True
    return False

def cast_drain():
    if player_mana >= DRAIN_COST:
        player_mana -= DRAIN_COST
        player_hp += 2
        boss_hp -= 2
        return True
    return False

def cast_shield():
    if shield_active:
        return False
    if player_mana >= SHIELD_COST:
        player_mana -= SHIELD_COST
        shield_active = True
        return True
    return False

def cast_poison():
    if poison_active:
        return False
    if player_mana >= POISON_COST:
        player_mana -= POISON_COST
        poison_active = True
        return True
    return False

def cast_recharge():
    if recharge_active:
        return False
    if player_mana >= RECHARGE_COST:
        player_mana -= RECHARGE_COST
        recharge_active = True
        return True
    return False

def receive_boss_damage():
    damage = boss_damage - player_armor
    if damage < 0:
        damage = 1
    player_hp -= damage

# optimal = using the least amount of mana
# returns the minimum amount of mana that should be
# spent by the player to win
def optimal_strategy(player_hp, player_mana, player_armor, boss_hp):
    case1 = 
