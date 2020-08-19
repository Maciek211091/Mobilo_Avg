def Selecting (options):
    for i in range(len(options)):
        print(f"{i+1}: {options[i]}")

    choice = input("Select your choice: ")

    return choice


options = ['load data', 'export data', 'analyze & predict']

choice = 'x'

while choice:

    choice = Selecting(options)

    if choice:
        try:
            choice_num = int(choice)-1

            if choice_num>=0 and choice_num<len(options):
                print(options[choice_num])

            else:
                print("Choice not valid")

        except:
            print("You need to select number")

    else:
        print('----END----')