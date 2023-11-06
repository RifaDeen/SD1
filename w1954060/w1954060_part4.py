# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 19540607 
# Date: 12/12/2022
# Seperate program for part 4 (dictionary)

progression = {}  # open dictionary 


def stu_id():   # to get student id and check if it already exists in the dictionary
    global student_id
    student_id = input('Enter the student ID: ')
    while (student_id in progression.keys()):
         print('The student ID was entered already, please enter a valid ID.')
         student_id = input('Enter the student ID: ')
         
    return student_id


def validation(msg, credit):  # to validate inputs

    while True:
        try:
            credit = int(input('Enter the number of credits ' + str(msg) + ' : ', ))
            if credit % 20 != 0 or credit > 120 or credit < 0:
                print('Value entered is out of range')
                continue
        except ValueError:
            print('Integer required')
            continue
        return credit


def progression_outcome():  # to get the progression outcomes

    stu_id()

    passs = validation('passed', 'passs')
    defer = validation('deferred', 'defer')
    fail = validation('failed', 'fail')

    if(passs + defer + fail) != 120:
        print('Total incorrect')
           
    elif passs == 120:
        print('Progress')
        progression[student_id]=(f'Progress - {passs}, {defer}, {fail}')  # to add keys and values to the dictionary
        
    elif passs == 100:
        print('Progress (module trailer)')
        progression[student_id]=(f'Progress (module trailer) - {passs}, {defer}, {fail}')
        
    elif fail == 80 or fail == 100 or fail == 120:
        print('Exclude')
        progression[student_id]=(f'Exclude - {passs}, {defer}, {fail}')
        
    else:
        print('Module retriever')
        progression[student_id]=(f'Module retriever - {passs}, {defer}, {fail}')
        
    print('.' * 80)
    


def loop():  # loops for multiple inputs and output results

    while True:
        print('Would you like to enter another set of data?')
        next_run = input("Enter 'y' if yes or enter 'q' to stop and view results: ")

        if next_run.lower() == "q":
            print('.' * 80)
            print('Part 4:')
            for key,value in progression.items():         # to print the input progression data from the dictionary
                print(key, ':', value)    
            break
        elif next_run=='y':
            print('.' * 80)
            progression_outcome()
            continue
        else:
            print('.' * 80)
            print('Invalid option, Pls re-enter')
            continue

progression_outcome()
loop()
