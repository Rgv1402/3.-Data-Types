name = input("Enter your real name, Agent: ")
gadget = input("What's your favourite gadget, Agent? ")

agent_no = 8
height_m = 1.65
speed_rating = 27.4
is_active = True
mission_count = 138

print("Name: "+ name, "Type -> ", type(name))
print("Fav Gadget: " + gadget, "Type -> ", type(gadget))
print("Agent No. : ", agent_no, "Type -> ", type(agent_no))
print("Height: ", height_m, "Type -> ", type(height_m))
print("Speed Rating: ", speed_rating, "Type ->", type(speed_rating))
print("Mission Count: ", mission_count, "Type -> ", type(mission_count))
print("Active? ", is_active, "Type -> ", type(is_active))

agent_no_str = str(agent_no)
height_m_str = str(height_m)
speed_str = str(speed_rating)
mission_str = str(mission_count)
status_str = str(is_active)
print("\n\n After typecasting\n\n")
print("Agent No. : ", agent_no_str, "Type -> ", type(agent_no_str))
print("Height: ", height_m_str, "Type -> ", type(height_m_str))
print("Speed Rating: ", speed_str, "Type ->", type(speed_str))
print("Mission Count: ", mission_str, "Type -> ", type(mission_str))
print("Active? ", status_str, "Type -> ", type(status_str))

first_three = name[0:3]
last = name[-1]
codename = first_three + last
print("First 3 letters: ", first_three)
print("Last letter: ", last)
print("Codename", codename)

reversed_gadget = gadget[::-1]
print("Reversed Gadget Name: ", reversed_gadget)

badge_line_1 = "AGENT " + codename.upper()
badge_line_2 = "ID " + agent_no_str + "   |   MISSIONS " + mission_str
badge_line_3 = "SPEED " + speed_str + "   |   STATUS " + status_str
badge_line_4 = "HEIGHT " + height_m_str
badge_line_5 = "SECRET GADGET CODE " + reversed_gadget.upper()

print("")
print("======= SECRET AGENT BADGE =======")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print(badge_line_5)
print("===================================")