def choose_ability(df,player):
    power_type = player.attributes['power']
    power_amt = player.attributes['power_amount']
    df = df.sort_values(by='damage',ascending=False)
    df = df[df['current_cd'] <= 0]
    if df.shape[0] == 0:
        return("CD")
    df = df[df['cost'] < power_amt]
    if df.shape[0] == 0:
        return("OOM")

    # find the ability that is highest damage that can be cast
    # TODO: this logic requires much more beef
    ability = df.iloc[[0]].index[0]

    return(ability)

def calc_ability_damage(df,ability,player):

    # determine the base damage of the attack
    damage = df.loc[[(ability)]]['damage'][0]
    damage_spread = 10

    damage = damage + (damage_spread * (.5-random.random()))

    # TODO: Inherit these from player eventually
    crit_multiplier = 2
    crit_perc = .3


    # % of attacks that will be glancing
    glancing_bounds = .05

    # % of attacks that will be dodged
    # TODO: this should be function of expertise
    dodged_bounds = .05
    dodged_bounds += glancing_bounds
    # % of attacks that will be parried
    # TODO: this should be function of expertise
    parried_bounds = .05
    parried_bounds += dodged_bounds

     # % of attacks that will be parried
    crit_bounds = crit_perc
    crit_bounds += parried_bounds

    attack_outcome = random.random()
    if attack_outcome < glancing_bounds:
        damage_done = damage*.5
        damage_type = "glancing"
    elif attack_outcome < dodged_bounds:
        damage_done = 0
        damage_type = "dodge"
    elif attack_outcome < parried_bounds:
        damage_done = 0
        damage_type = "parry"
    elif attack_outcome < crit_bounds:
        damage_done = damage*crit_multiplier
        damage_type = "critical"
    else:
        damage_done = damage
        damage_type = "normal"

    return(damage_done,damage_type)



def use_ability(df,ability,player):
    # determine the cost of the ability
    power_cost = df.loc[[(ability)]]['cost'][0]

    # set ability on cd
    df.at[ability,'current_cd'] = df.at[ability,'cooldown']

    #calc damage and type
    damage_done, damage_type = calc_ability_damage(df,ability,player)

    #print(ability,damage_done,damage_type,power_cost)
    return(df,damage_done,damage_type,power_cost)
