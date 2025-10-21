
input_value = input()
print("the value i wrote in my terminal is:", input_value)

ui_ux_design = []
front_end_development = []
backend_development = []

print("welcome to unielcity.")
name = input("what is your name?: ")
course = input(
    f"what is the course you are planning to take?\n1. UI/UX Design.\n2. Front-End design.\n3. Back-End development"
    )
if course == "1":
    ui_ux_design.append(name)
elif course =="2":
    front_end_development.append(name)
elif course =="3":
    backend_development.append(name)
else:
    print("you chose the wrong option. you are to choose between 1,2 and 3.")

    print("ui/ux Design:", ui_ux_design)
    print("Front-End Development:", front_end_development)
    print("Backend Development:", backend_development)


