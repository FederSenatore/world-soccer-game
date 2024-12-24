import random
import time

Europe = ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bulgaria', 'Bosnia-Herzegovina',
          'Croatia', 'Cyprus', 'Denmark', 'England', 'Estonia', 'Faer Oer', 'Finland', 'France', 'Georgia', 'Germany',
          'Gibraltar', 'Greece', 'Hungary', 'Kazakhstan', 'Kosovo', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia',
          'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands',
          'North Ireland', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino',
          'Scotland', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine',
          'Vatican City', 'Wales']

players_of_albania = ['Enzo', 'Jurgen', 'Paolone']
players_of_armenia = ['Hayk']
players_of_austria = ['Dominik']
players_of_azerbaijan = ['Xalid']
players_of_belarus = ['Vitaliy']
players_of_belgium = ['Christoph']
players_of_bulgaria = ['Daliya']

players_of_croatia = ['Sanel', 'Terezija']
players_of_cyprus = ['Fidias']

players_of_france = ['Ambroise', 'Claire', 'Olivier']

players_of_germany = ['Moritz']

players_of_greece = ['Evanghelos', 'Konstantina', 'Niko']
players_of_hungary = ['Zoltan']
players_of_kazakhstan = ['Saltanat', 'Symbat']
players_of_kosovo = ['Verina']

players_of_israel = ['Mikhal', 'Rachel']
players_of_italy = ['Alessio', 'Federico', 'Gianluca']

players_of_poland = ['Katarzyna', 'Piotr']
players_of_portugal = ['Carolina']
players_of_romania = ['Adelina', 'Bianca', 'Leonard']
players_of_russia = ['Andreij', 'Daria']

players_of_serbia = ['Emilija']
players_of_slovakia = ['Davidko', 'Martin']

players_of_spain = ['Hector', 'Laura Beatriz']

players_of_switzerland = ['Amir']
players_of_turkey = ['Ozlem']
players_of_ukraine = ['Anton', 'Barabash', 'Bohdia', 'Igor', 'Lyubo']

round = 0

# Randomize the given list
def create_group(list):
    random.shuffle(list)
    return list

# Split the randomized list
def split_list(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]
# NB. This function's output needs to be turnt into a list by doing list()

# Create group stage
def create_group_stage(continent):
    global splitted_list
    splitted_list = list(split_list(create_group(continent), 4))
    if continent == Europe:
        first_group = splitted_list[0]
        print(first_group)
        second_group = splitted_list[1]
        print(second_group)
        third_group = splitted_list[2]
        print(third_group)
        fourth_group = splitted_list[3]
        print(fourth_group)
        fifth_group = splitted_list[4]
        print(fifth_group)
        sixth_group = splitted_list[5]
        print(sixth_group)
        seventh_group = splitted_list[6]
        print(seventh_group)
        eighth_group = splitted_list[7]
        print(eighth_group)
        time.sleep(5)
        return first_group, second_group, third_group, fourth_group, fifth_group, sixth_group, seventh_group, eighth_group
    else:
        return []

# Manage group stage.
def manage_group_stage(group, group_number):
    global round
    global results_table
    global group_0, group_1, group_2, group_3
    global result_0, result_1, result_2, result_3
    group_0 = group[0]
    group_1 = group[1]
    group_2 = group[2]
    group_3 = group[3]
    if round == 0:
        result = play_match()
        result_0 = result[0]
        result_1 = result[1]
        result = play_match()
        result_2 = result[0]
        result_3 = result[1]
        results_table = {group_0: result_0, group_1: result_1, group_2: result_2, group_3: result_3}
        print(f'GROUP {group_number+1}')
        print(f'ROUND {round+1}')
        print(f'{group_0} {result_0} - {result_1} {group_1}')

        # TODO: TRASFORMA QUANTO SEGUE IN UNA FUNZIONE
        if result_0 > result_1:
            print(f'{group_0} wins!')
        elif result_0 == result_1:
            print(f'No winner!')
        else:
            print(f'{group_1} wins!')
        print(f'{group_2} {result_2} - {result_3} {group_3}')
        if result_2 > result_3:
            print(f'{group_2} wins!')
        elif result_2 == result_3:
            print(f'No winner!')
        else:
            print(f'{group_3} wins!')
        print(results_table)
        time.sleep(5)
        round += 1

    elif round == 1:
        result = play_match()
        result0 = result[0]
        result3 = result[1]
        result = play_match()
        result1 = result[0]
        result2 = result[1]
        print(f'GROUP {group_number}')
        print(f'ROUND {round}')
        print(f'{group_3} {result3} - {result0} {group_0}')
        print(f'{group_1} {result1} - {result2} {group_2}')
        result_0 += result0
        result_3 += result3
        result_1 += result1
        result_2 += result2
        results_table = {group_0: result_0, group_3: result_3, group_1: result_1, group_2: result_2}
        print(results_table)
        time.sleep(5)
        round += 1

    else:
        result = play_match()
        result0 = result[0]
        result2 = result[1]
        result = play_match()
        result1 = result[0]
        result3 = result[1]
        print(f'GROUP {group_number}')
        print(f'ROUND {round}')
        print(f'{group_0} {result0} - {result2} {group_2}')
        print(f'{group_1} {result1} - {result3} {group_3}')
        result_0 += result0
        result_3 += result3
        result_1 += result1
        result_2 += result2
        results_table = {group_0: result_0, group_2: result_2, group_1: result_1, group_3: result_3}
        print(results_table)
        time.sleep(5)
        print(f'END OF GROUP {group_number}')
        time.sleep(10)
        round = 0

    return results_table

# Give random goals
def give_goals():
    goal = random.randint(0,9)
    if goal >= 4:
        goal += random.randint(1,4)
    return goal

# Give result
def give_result(goal1, goal2):
    if goal1 == goal2:
        return [1, 1]
    elif goal1 > goal2:
        return [3, 0]
    else:
        return [0, 3]

# Play a match
def play_match():
    points = give_result(give_goals(), give_goals())
    return points