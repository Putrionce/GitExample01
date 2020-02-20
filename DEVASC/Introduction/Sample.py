playerhealth = 10


class Player:
    health = 10
    revives = 3

    def revive(self):
        if self.health > 0:
            print("Player has HP no need to revive")
            return
        elif self.revives < 0:
            print("Player has no revives left")
            return

        self.revives = self.revives - 1
        self.health = 10


#D.R.Y
while playerhealth > 0:
    print("Choose an action to perform - ")
    action = input()

    if action == "fight":
        print ("fighting...")

    elif action == "explore":
        print ("exploring...")

    elif action == "quit":
         print ("quitting...")

    else:
        print ("Action not regonized!")



