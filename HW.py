name = input("Enter your name: ")
Club = input("Enter your Sports Club name: ")

Tenure_m = 11.75
player_no = 8
goals_scored = 14
assists = 22
active = True

print("\n\n Name: "+ name, " | Type -> ", type(name))
print("Club name: "+ Club, " | Type -> ", type(Club))
print("Tenure: ", Tenure_m, " | Type -> ", type(Tenure_m))
print("Player no. : ", player_no, " | Type -> ", type(player_no))
print("Goals Scored: ", goals_scored, " | Type -> ", type(goals_scored))
print("Assists Given: ", assists, " | Type ->", type(assists))
print("Player is active? ", active, " | Type -> ", type(active))

tenure_str = str(Tenure_m)
player_str = str(player_no)
goals_str = str(goals_scored)
assists_str = str(assists)
status_str = str(active)

first_three = name[0:3]
last = name[-1]
playercodename = first_three + last
print("First 3 letters: ", first_three)
print("Last letter: ", last)
print("Codename: ", playercodename)

reverse_clubname = Club[::-1]
print("Reversed Club Name: ",reverse_clubname)

badge_line_1 = "PLAYER: " + playercodename.upper()
badge_line_2 = "TENURE: " + tenure_str + " months" + "   |   GOALS: " + goals_str
badge_line_3 = "ASSISTS: " + assists_str + "   |   ACTIVE STATUS: " + status_str
badge_line_4 = "SECRET CLUB NAME: " + reverse_clubname.upper()

print("\n")
print("======= PLAYER PROFILE =======")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("====~~~~====")