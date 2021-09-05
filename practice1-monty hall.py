import random

#Write a function that is a door not having a prize (the host knows) and is not the player choice so it will be opened
def open_non_prize_door(host, player_choice, num_doors):
    i = 0
    while i == host or i == player_choice:
        i = (i+1)%num_doors
    return i

#Write a function what happens if the player switch door: the door will not be the one with prize and not the one chosen in the first place by player
def switch_door(shown_door, player_choice, num_doors):
    i = 0
    while i == shown_door or i == player_choice:
        i = (i+1)%num_doors
    return i    
    
def monty_hall_sim(switch, num_tests):
    #For every scenarios, we count number of wins and losses
    doors = [0, 1 ,2]
    num_doors = len(doors)
    original_player_choice = random.randint(0, num_doors-1)
    host = random.randint(0, num_doors-1)
    door_shown = open_non_prize_door(host, original_player_choice, num_doors)

    #Initialize number of losses and wins
    win_with_switch = 0
    win_wo_switch = 0
    loss_with_switch = 0
    loss_wo_switch = 0

    #If player decides to switch
    player_choice = switch_door(door_shown, original_player_choice, num_doors)
    for i in range(num_tests):
        if switch == "TRUE" and host == player_choice:
            print("You win by switching to door ", player_choice, "Your original choice is ", original_player_choice, "The door shown is ", door_shown)
            win_with_switch += 1
        elif switch == "TRUE" and host == original_player_choice:
            print("You lose by switching to door ", player_choice, "Your original choice is ", original_player_choice, "The door shown is ", door_shown)
            loss_with_switch += 1 
        elif switch == "FALSE" and host == original_player_choice:
            print("You win by staying with this door ", original_player_choice, "The door shown is ", door_shown)
            win_wo_switch += 1 
        elif switch == "FALSE" and host != original_player_choice:
            print("You lose by staying with this door ", original_player_choice, "The door shown is ", door_shown)
            loss_wo_switch += 1
        else:
            print("There is something wrong")
    return num_tests, win_with_switch, loss_with_switch, win_wo_switch, loss_wo_switch

def calc_percentage(switch, num_tests):
    sim = monty_hall_sim(switch, num_tests)
    perc_win_switch = sim[1]/sim[0]
    perc_loss_switch = sim[2]/sim[0]
    perc_win_no_switch = sim[3]/sim[0]
    perc_loss_no_switch = sim[4]/sim[0]
    return perc_win_switch, perc_loss_switch, perc_win_no_switch, perc_loss_no_switch

#Play the game
sim1 = monty_hall_sim("TRUE", 20)