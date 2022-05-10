from j.k import Character
from random import randint,choice

def l():
    print("You can go away")
    l=input("Are you sure, you want to escape?")
    if l=="yes":
        print("The end of fight")
        #break


class Player(Character):
    def __init__(s) -> None:
        super().__init__()
        s.name=input("Enter your name: ")

    def goAway(s):
        if s.movementSpeech>=10:
            print
           



    #def mediumAtack(s):
        
            
        
            
class Tank(Player(Character)):
    def __init__(s) -> None:
        super().__init__()
        s.name=s.name + " Tank"
        s.atack=5
        s.hp=50
        s.bulletDamage=20
        def movementSpeech(s):
            o=choice([9,0,9,8,4,3,2,1,4,6,7,9,0,9,0,0,0,0,0,0,0,0,0,0,0,0])
            if o==1:
                s.movementSpeech=10
            elif o==0:
                s.movementSpeech=2
            else:
                s.movementSpeech=0    


        



    
    