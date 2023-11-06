# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 19540607 (IIT No: 20220701)
# Date: 12/12/2022
# Part 1 program allowing multiple outcomes and histogram


progress_count = 0  # counts for histogram
trailer_count = 0
retriever_count = 0
excluded_count = 0


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

    passs = validation('passed', 'passs')
    defer = validation('deferred', 'defer')
    fail = validation('failed', 'fail')

    if(passs + defer + fail) != 120:
        print('Total incorrect')
       
    elif passs == 120:
        print('Progress')
        progress_count += 1
       
    elif passs == 100:
        print('Progress (module trailer)')
        trailer_count += 1
        
    elif fail == 80 or fail == 100 or fail == 120:
        print('Exclude')
        excluded_count += 1
       
    else:
        print('Module retriever')
        retriever_count += 1
        
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


def loop():  # loops for multiple inputs and output results(histogram)

    while True:
        print('Would you like to enter another set of data?')
        next_run = input("Enter 'y' if yes or enter 'q' to stop and view results: ")

        if next_run.lower() == "q":
            call_histogram()
            print('.' * 80)
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
            print('.' * 80)            
            break
        elif mode == 2:
            progression_outcome()
            loop()
            break

    except ValueError:
        print('Invalid option, Pls re-enter')
        continue

