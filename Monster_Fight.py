class Monster():
    def __init__(self, name, hp=20):
        self.exp = 0
        self.name = name
        self.type = 'Normal'
        self.max_hp = hp
        self.current_hp = self.max_hp
        self.attacks = {'wait': 0}
        self.possible_attacks = {'sneak_attack': 1,
                                'slash': 2,
                                'ice_storm': 3,
                                'fire_storm': 3,
                                'whirlwind': 3,
                                'earthquake': 2,
                                'double_hit': 4,
                                'tornado': 4,
                                'wait': 0}
                                
    def add_attack(self, attack_name):
        if attack_name not in self.possible_attacks:
           return False
       
    #   if more there are already 4 attacks take weakest one away when adding new one
        if len(self.attacks)== 4:
            dmg=100
            # finds weakest attack in dictionary
            for attack in self.attacks:
                if self.attacks[attack]< dmg:
                   dmg = self.attacks[attack]
                   move = attack
                elif self.attacks[attack] == dmg:
                    move = min(attack,move)
            self.remove_attack(move)
            # applies new attack
        self.attacks[attack_name] = self.possible_attacks[attack_name]
        return True
    def remove_attack(self, attack_name):
        try:
          del self.attacks[attack_name]
          if len(self.attacks) == 0:
              self.attacks['wait'] = 0
          return True
        except:
          return False
    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp
    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp
  
def monster_fight(monster1, monster2):
    m1= sorted(sorted(monster1.attacks.items(),key= lambda x:x[0])[::-1], key= lambda x:x[-1])[::-1]
    m2= sorted(sorted(monster2.attacks.items(),key= lambda x:x[0])[::-1], key= lambda x:x[-1])[::-1]
    m1_attack_index = 0
    m2_attack_index = 0
    round_number = 0
    m1_attacks=[]
    m2_attacks=[]
    if m1== [('wait',0)] and m2== [('wait',0)]:
        return(-1,None,None)
    while True:
        round_number += 1
        monster2.current_hp -= m1[m1_attack_index][-1]
        m1_attacks.append(m1[m1_attack_index][0])
        if monster2.current_hp <= 0:
            print(f'{monster1.name} wins!')
            monster1.win_fight()
            monster2.lose_fight()
            winner = monster1
            winning_attacks = m1_attacks
            break
        monster1.current_hp -= m2[m2_attack_index][-1]
        m2_attacks.append(m2[m2_attack_index][0])
        if monster1.current_hp <= 0:
            print(f'{monster2.name} wins!')
            monster2.win_fight()
            monster1.lose_fight()
            winner = monster2
            winning_attacks = m2_attacks
            break
        m1_attack_index += 1
        m2_attack_index += 1
        if m1_attack_index == len(m1):
            m1_attack_index = 0
        if m2_attack_index == len(m2):
            m2_attack_index = 0
    return(round_number,winner,winning_attacks)
    
dragon = Monster('dragon', 30)
dragon.add_attack('whirlwind')
shark = Monster('shark', 30)
shark.add_attack('slash')
print(monster_fight(dragon,shark))


