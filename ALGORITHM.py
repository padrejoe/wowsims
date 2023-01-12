# Big updated algo with the data and such


import pandas as pd
import random


from classes import paladin

from ability import choose_ability,use_ability,calc_ability_damage



new_player = paladin()
ability_df = pd.DataFrame(new_player.abilities).T
ability_df['current_cd'] = 0

total_damage = 0
total_time = 100

for t in range(total_time):
    power_amount = new_player.attributes['power_amount']
    power_type = new_player.attributes['power']


    # Mana Regen
    if power_amount < 3900:
        power_amount += 100
    else:
        power_amount = 4000

    ability_df['current_cd'] -= 1
    print("Time Step: "+str(t))
    print(str(power_type)+ ": "+ str(power_amount))

    ability = choose_ability(ability_df,new_player)
    #ability_df = pd.DataFrame(new_player.abilities).T
    if (ability in pd.DataFrame(new_player.abilities).T.index):
        ability_df,damage_done,damage_type,power_cost = use_ability(ability_df,ability,new_player)
        new_player.attributes['power_amount'] = power - power_cost
        print(str(damage_type) + "! " + str(ability) + " hits for " + str(damage_done))
        total_damage += damage_done
    else:
        print(ability)

    # update player object with new power amount
    new_player.attributes['power_amount'] = power_amount


print("Total Damage:" + str(total_damage))
print("DPS:" + str(total_damage/total_time))
