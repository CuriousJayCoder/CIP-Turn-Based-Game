import random
# Turn Based Combat Game Final Project. Will Break down into individual milestones as needed

# Step 1: Make a Text-Based Interface for Players and Enemies : DONE

# Step 2: Implement Attack/Buff/Defend/Heal commands : DONE

# Step 3: Have an initial print-out of the player and enemy's health at the start of each person's turn. 
# : HAVE IT ON PLAYER's END via command, Not ENEMY's End but if enemy selects attack, will print out afterwards.

# Step 4: Make set multipliers for Buff/Defend and formulas for the Attack command with building in critical chances : DONE

# Step 5: Create variables for storing Buff/Defend Multipliers for the attack formula and change them depending on the action taken
# while reverting them once they've been used in the damage formula calculation for that turn. DONE

# Step 6: Make a coin-flip to decide who goes first. : DONE

# Step 7: If coin-flip occurs, print out a prompt to determine turn order and take result and compare it with a
#  random variable to determine turn order : DONE

# Step 8: Create a while loop that compares both player health and enemy health to being greater than 0 to keep the game going and if loops
# to occur based on the player input and randomization on the enemy's end for determining their action : DONE

# Step 9 : Import the random library and use a range from 0-100 for determining the probablity on extra damage since the amount of extra damage
# will already be pre-determined : DONE

# Step 10: Can break down the Attack/Buff/Defend/Heal function into their own proper functions. : DONE, figured out and works properly, used
#global to allow use even outside of functions.

# Step 11: Can work on running the process- mid coding in order to test out various commands and that the loops flow properly : DONE

# Step 12: Create an if loop comparing the player command input and if it doesn't match to re-enter the command again : DONE

# Step 13: (Optional): Maybe add additional commands to bring up the player health and enemy health at the same time or more prompts to print
# at the beginning to detail damage ranges : HP Command added for Player, Damage ranges mentioned in the beginning.

# Step 14: Comment out each function in order to test each aspect of the game before putting it all together.



# Standard variables needed for the functions to work as intended are declared here. Variable names make sense from initial glance.

PLAYER_HEALTH = 100
ENEMY_HEALTH = 100 #Two variables above track both player and enemy's HP
CRIT_CHANCE = 15 #Static variable that is used to represent the chance of getting a critical hit on both player's attack command
ENEMY_DEFEND_VALUE = 1
PLAYER_DEFEND_VALUE = 1 # Two variables that can be modified upon taking the Defend command
PLAYER_BUFF_VALUE = 1
ENEMY_BUFF_VALUE = 1 # Two variables that can be modified upon taking the Buff command
TURN_VALUE = 0 # It will be decided on that turn_value = 0 is the player's turn and = 1 is the enemy's turn. Set to 0 temporarily to define it
ENEMY_PROBABILITY = 0 # Set to 0 intially, Will be changed to utilize the random.randint command from 0 to 100

#Attack - Attacks your rival with a damage range of 10-15 health with a 15 percent chance of doing critical damage(1.15* normal range.))
# Defend and Buff values in the respective loops will reset upon use of the Attack command.
def Attack(): 
    global PLAYER_HEALTH, ENEMY_HEALTH, PLAYER_BUFF_VALUE, ENEMY_DEFEND_VALUE, PLAYER_DEFEND_VALUE, ENEMY_BUFF_VALUE, TURN_VALUE
    if TURN_VALUE == 0:
        if CRIT_CHANCE < random.randint(0,100): #Player chooses Attack and doesn't get the 15% chance to proc a critical hit
            DAMAGE = int((random.randint(10,20) * PLAYER_BUFF_VALUE) *ENEMY_DEFEND_VALUE)
            ENEMY_HEALTH -= DAMAGE
            print("You've attacked! The enemy's health is now "+ str(ENEMY_HEALTH)+ ". Strategize for the next turn.")
            print("")
        else: #Player chooses Attack and does get the 15% chance to proc a critical hit
            DAMAGE = int((random.randint(10,20) * PLAYER_BUFF_VALUE *1.15) *ENEMY_DEFEND_VALUE)
            ENEMY_HEALTH -= DAMAGE
            print("CRITICAL HIT! The enemy's health is now "+ str(ENEMY_HEALTH)+ ". Captialize on the lead you got just now!")
            print("")
        PLAYER_BUFF_VALUE = 1
        ENEMY_DEFEND_VALUE = 1
    elif TURN_VALUE == 1: 
        if CRIT_CHANCE < random.randint(0,100): #Enemy chooses Attack and doesn't get the 15% chance to proc a critical hit
            DAMAGE = int((random.randint(10,20) * ENEMY_BUFF_VALUE) *PLAYER_DEFEND_VALUE)
            PLAYER_HEALTH -= DAMAGE
            print("The enemy attacked! Your health is now "+ str(PLAYER_HEALTH)+ ". Strategize for the next turn and get your payback.")
            print("")
        else: #Enemy chooses Attack and does get the 15% chance to proc a critical hit
            DAMAGE = int((random.randint(10,20) * ENEMY_BUFF_VALUE * 1.15) *PLAYER_DEFEND_VALUE)
            PLAYER_HEALTH -= DAMAGE
            print("WARNING! CRITICAL DAMAGE HAS BEEN TAKEN! Your health is now "+ str(PLAYER_HEALTH)+ ". The situation is looking dire now.")
            print("")
        ENEMY_BUFF_VALUE = 1
        PLAYER_DEFEND_VALUE = 1
    TURN_VALUE = 1 - TURN_VALUE # This switches turns
    
    

# " Buff - Make it so that your next attack will do 1.2 times what you roll for your attack damage. This can't stack repeatedly."
def Buff(): 
    global PLAYER_BUFF_VALUE, ENEMY_BUFF_VALUE, TURN_VALUE
    if TURN_VALUE == 0: # Player chooses to Buff, affecting their variable in the attack formula and command.
        PLAYER_BUFF_VALUE = 1.20
        print("You focus on your rival classmate, making your next attack stronger.")
        print("")
    elif TURN_VALUE ==1: # Enemy chooses to Buff, affecting their variable in the attack formula and command.
        ENEMY_BUFF_VALUE = 1.20
        print("The enemy rival focuses on you with malicious intent, strengthening their next attack. Be aware!")
        print("")
    TURN_VALUE = 1 - TURN_VALUE # This switches turns

# " Defend - Make it so that when you take damage from your rival, it gets reduced by a flat 20%. This can't stack repeatedly."
def Defend():
    global PLAYER_DEFEND_VALUE, ENEMY_DEFEND_VALUE, TURN_VALUE
    if TURN_VALUE == 0: # Player chooses to defend, affecting the overall damage they take when the enemy attacks.
        PLAYER_DEFEND_VALUE = 0.80
        print("You brace yourself for whatever might come, getting ready to reduce the enemy's damage.")
        print("")
    elif TURN_VALUE ==1: # Enemy chooses to defend, affecting the overall damage they take when the Player attacks.
        ENEMY_DEFEND_VALUE = 0.80
        print("Your rival has bunkered down. Expect them to receive reduced damage!")
        print("")
    TURN_VALUE = 1 - TURN_VALUE # This switches turns

# " Heal - Make it so that you heal from a range from 5-15 HP back to your current total HP."
def Heal():
    global PLAYER_HEALTH, ENEMY_HEALTH, TURN_VALUE
    if TURN_VALUE == 0: # Player chooses to heal, affecting their current hp within the specified range.
        HEAL_AMOUNT = random.randint(5, 15)
        print("You look at your phone and see a notification that states that your current HP is "+str(PLAYER_HEALTH)+ "HP.")
        print("")
        PLAYER_HEALTH += HEAL_AMOUNT
        print("You take your trusty snack out that never fails you, healing you back to "+str(PLAYER_HEALTH)+ "HP.")
        print("")
    elif TURN_VALUE == 1: # Enemy chooses to heal, affecting their current hp within the specified range.
        HEAL_AMOUNT = random.randint(5, 15)
        print("The enemy laughs at you and states that their current HP is "+str(ENEMY_HEALTH)+ "HP.")
        print("")
        ENEMY_HEALTH += HEAL_AMOUNT
        print("The enemy eats a snack and states that their current HP is now "+str(ENEMY_HEALTH)+ "HP.")
        print("")
    TURN_VALUE = 1 - TURN_VALUE # This switches turns



# Intial lines are printed out explaining the scenario, explaining the 4 commands and asking for an intitial input to decide turn order.
# start_value generated in the main command,  decided on that if the variable matches the random.randint command, you guessed correctly.
# Otherwise, it will be the enemy's turn.
def main():
    global TURN_VALUE, PLAYER_HEALTH, ENEMY_HEALTH, ENEMY_PROBABILITY
    print(" Hello fellow Code in Place user! Time for a friendly battle with your classmates to kill time until the next lecture occurs!")
    print(" The purpose of the game is to deplete your enemy's health to 0 before you reach 0 using the 4 commands that will be specified below.")
    print(" Attack - Attacks your rival with a damage range of 10-15 health with a 15 percent chance of doing critical damage(1.15* normal range.)")
    print(" Defend - Make it so that when you take damage from your rival, it gets reduced by a flat 20%. This can't stack repeatedly.")
    print(" Buff - Make it so that your next attack will do 1.2 times what you roll for your attack damage. This can't stack repeatedly.")
    print(" Heal - Make it so that you heal from a range from 5-15 HP back to your current total HP.")
    print(" Now that you know all the general commands, please choose heads(0) or tails(1) to decide who goes first. ")
    print("")
    start_value = int(input("Please type 0(heads) or 1(tails). "))
    if start_value == random.randint(0,1):
        print("Luck is in your favor fellow Code in Place user! You get to go first.")
        print("")
        TURN_VALUE = 0
    else:
        print("Darn! Unlucky this time. The computer will get to go first. Don't worry, just a minor setback.")
        print("")
        TURN_VALUE = 1
    # While loop is used to compare both player and enemy health to 0 to keep the game going.
    # If loops are utilized based on TURN_VALUE's value to go through the necessary code based on the sequence of events and who's turn it is.
    # For the player's turn, SELECTION variable is utilized to determine from the player's input what command to use and has a failsafe.
    # Once one of the 4 commands is taken, TURN_VALUE goes to 1 to execute the next set of code for the enemy which will randomly take 1 of 4 actions.

    while PLAYER_HEALTH > 0 and ENEMY_HEALTH > 0:
        if TURN_VALUE == 0:
            print("It is your turn! Please select one of the 4 commands stated above: Attack, Defend, Buff or Heal. Typing HP states both sides' hp for your convenience. ")
            print("")
            SELECTION = input("Type in your command! ")
            if SELECTION == "Attack":
                Attack()
            elif SELECTION == "Buff":
                Buff()
            elif SELECTION == "Defend":
                Defend()
            elif SELECTION == "Heal":
                Heal()
            elif SELECTION == "HP":
                print ("Your current HP is "+str(PLAYER_HEALTH)+". "+" The enemy's current HP is "+str(ENEMY_HEALTH)+".")
                print("")
            else:
                print("That command isn't recognized. Please try again.")
                print("")
        elif TURN_VALUE == 1:
            print("It is the enemy's turn! They are deliberating over their next course of action.")
            print("")
            ENEMY_PROBABILITY = random.randint(0,100)
            if ENEMY_PROBABILITY >= 0 and ENEMY_PROBABILITY <=25:
                Attack()
            elif ENEMY_PROBABILITY >= 26 and ENEMY_PROBABILITY <=50:
                Buff()
            elif ENEMY_PROBABILITY >=51 and ENEMY_PROBABILITY <=75:
                Defend()
            elif ENEMY_PROBABILITY >=76 and ENEMY_PROBABILITY <=100:
                Heal()

    if PLAYER_HEALTH <= 0:
        print("Your health is at or below 0, signaling that you have lost this battle. Better luck next time!")
        print("")
    elif ENEMY_HEALTH >=0:
        print("The enemy's health is at or below 0, signaling that you have won. Congratulations!")
        print("")
            






if __name__ == "__main__":
    main()