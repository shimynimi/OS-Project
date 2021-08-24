from random import randint
import random
import threading
import time


N = int(input("number of countries: "))

NameList = [
    'lenin', 'Ra', 'Fulton', 'Victory', 'Olympic', 'Santa marina', 'Long',
    'Lighter', 'raft', 'Gondola', 'Cutter', 'Frigate', 'Carval', 'Brig',
    'Bark', 'Junk', 'Paru', 'Sloop', 'Galleon', 'Dory', 'Mast', 'Sail',
    'Castle', 'U_Ship'
]

ships = [NameList[i] for i in range(N)]
ThreadList = [] 
ship_attack = {}  #aval hame true hame mitunan b ham hamle konn , age tir bokhore false mishe dige kari nemitoone bokone
print("ships in war ==> {}".format(ships)) #vaghti toye yek string mikhaym yek seri dade biarim

print('START WAR')

target = '' #keshti k mikhaimhamle konim bhsh globale

for i in range(len(ships)):
    ship_attack['{}'.format(ships[i])] = True



#kelase asli k nakha ro tush dorost mikonim

class theThread(threading.Thread):
    #constructor
    # self hamun this hast 
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name



    def run(self):
        if ship_attack[f'{self.name}'] == True:
#sanie random midim
            x = randint(1, 3)

            print(f'ship {self.name} takes {x} seconds to prepare')
            time.sleep(x)
            # print(ships)
            while True:
                target = ships[random.randint(0, len(ships) - 1)]
                if self.name != target:
                    break
#ham kasi k gharare hamle besh ham kasi k hamle mikone 
        if ship_attack[target] == True and ship_attack[f'{self.name}'] == True:
            print(f'{self.name} fired the target {target}')
            ship_attack[target] = False
#ship hayee k mordan ro hazf mikonim
            if len(ships) != 1:
                ships.remove(target)
            else:
                quit()
                #az run miad birun


            #error midad
            if len(ships) == 1:
                print('*******************************END WAR*********************************')
                print(f'*****************************winner is {ships[0]}*******************************')
                input()
                quit()
            
            next_shot = theThread(f"{self.name}")
            # ThreadList.append(next_shot)
            next_shot.start()


def CreateThread(n):
    for i in range(n):
        new_ship = theThread(f"{ships[i]}")
        ThreadList.append(new_ship)
        ThreadList[i].start()
        
    # for i in range(len(ThreadList)):
    #     ThreadList[i].start()


CreateThread(N)
