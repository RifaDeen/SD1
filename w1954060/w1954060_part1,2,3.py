# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 19540607 
# Date: 12/12/2022
# Extension of part 1 program for part 2(lists) and part 3(file)


progress_count = 0  # counts for histogram
trailer_count = 0
retriever_count = 0
excluded_count = 0
prog_list = []  # lists to store inputs
trail_list = []
ret_list = []
excl_list = []
file = open('progression_outcomes.txt', 'w')
file.write('Part 3: \n')  # open and write into a file


def validation(msg, credit):  # to validate inputs

    while True:
        try:
            credit = int(input('Enter the number of credits ' + str(msg) + ' : ', ))
            if credit % 20 != 0 or credit > 120 or credit < 0:
                print('value entered is out of range')
                continue
        except ValueError:
            print('Integer required')
            continue
        return credit


def progression_outcome():  # to get the progression outcomes

    global progress_count, trailer_count, retriever_count, excluded_count
    global prog_list, trail_list, ret_list, excl_list
    
    passs = validation('passed', 'passs')
    defer = validation('deferred', 'defer')
    fail = validation('failed', 'fail')

    if(passs + defer + fail) != 120:
        print('Total incorrect')   

    elif passs == 120:
        print('Progress')
        progress_count += 1
        prog_list.extend((passs, defer, fail))
        file.write(f'Progress - {passs}, {defer}, {fail}\n')
               
    elif passs == 100:
        print('Progress (module trailer)')
        trailer_count += 1
        trail_list.extend((passs, defer, fail))
        file.write(f'Progress (module trailer) - {passs}, {defer}, {fail}\n')
        
    elif fail == 80 or fail == 100 or fail == 120:
        print('Exclude')
        excluded_count += 1
        excl_list.extend((passs, defer, fail))
        file.write(f'Exclude - {passs}, {defer}, {fail}\n')

    else:
        print('Module retriever')
        retriever_count += 1
        ret_list.extend((passs, defer, fail))
        file.write(f'Module retriever - {passs}, {defer}, {fail}\n')
        
    print('.' * 80)


def histogram(message, variable):  # to print histogram according to outcomes
    print(message, variable, ':', '*' * variable)


def call_histogram():
    total = progress_count + trailer_count + retriever_count + excluded_count
    print('.' * 80)
    print('Histogram')
    histogram('Progress', progress_count)  # function call for histogram
    histogram('Trailer', trailer_count)
    histogram('Retriever', retriever_count)
    histogram('Excluded', excluded_count)
    print(total, 'outcomes in total')


def lists(list_name, message):  # to store values in respective progression lists
    for i in range(0, len(list_name), 3):
        print(message, list_name[i], ',', list_name[i + 1], ',', list_name[i + 2])


def call_lists():
    print('Part 2:')
    lists(prog_list, 'Progress -')  # function call for lists
    lists(trail_list, 'Progress(module trailer) - ')
    lists(ret_list, 'Module retriever - ')
    lists(excl_list, 'Exclude - ')
    print('.' * 80)


def loop():  # loops for multiple inputs and output results

    while True:
        print('Would you like to enter another set of data?')
        next_run = input("Enter 'y' if yes or enter 'q' to stop and view results: ")

        if next_run.lower() == "q":
            call_histogram()
            print('.' * 80)
            call_lists()
            break
        elif next_run=='y':
            print('.' * 80)
            progression_outcome()
            continue
        else:
            print('.' * 80)
            print('Invalid option, Pls re-enter')
            continue
       

#to select mode, whether student or staff
while True:
    try:
        print('Greetings!')
        mode = int(input("Enter 1 if you are a student \nEnter 2 if you are a staff member : "))
        print('.' * 80)
        if mode == 1:
            progression_outcome()
            break
        elif mode == 2:
            progression_outcome()
            loop()
            file = open('progression_outcomes.txt', 'r')  # read and print outcomes from file
            content = file.read()
            print(content)
            file.close()
            break

    except ValueError:
        print('Invalid option, Pls re-enter')
        continue


    
