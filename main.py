import groups

splitted_list = []
results_table = {}

print("WELCOME!")
game = input("Enter OLD for playing with the OLD groups.\nEnter NEW for playing with NEW groups.")

if game == "OLD":
    print("You have selected OLD")
elif game == "NEW":
    print("You have selected NEW")

    group_stage = groups.create_group_stage(groups.Europe)

    for group in group_stage:
        group_number = group_stage.index(group)
        turn = 0
        while (turn <= 2):
            results_table = groups.manage_group_stage(group, group_number)
            turn += 1
        # Order by points
        print(sorted(results_table.items(), key=lambda item: item[1]))
else:
    print("Not valid")
