from functions import Employee

if __name__ == '__main__':
    print("Welcome to the managering program\n") 
    while True:
    
        departament = input("""In which departsament do you want to go?\n Our departaments are Managering and Software Developers' type 'M' or 'S' :\n
Or you cand type 'q' to exit \n""").lower()
        if departament== "q"or departament=="s" or departament =="m":

            command= input("""What do you want to do in this departament?\n
Type 'a' if you want to add an employee\n
Type 'de' if you want to see all the  employees from this departament\n
Type 'b' if you want to add a bonus to  an individual'\n 
Type'd' to see all the departaments again \n
Type'r' to remove an employee '\n
Type ba if you want to add a bonus to all of the employees of a departament\n""")
            employee = Employee()
            if command.lower()=="a":
                employee.add_employee(departament)
            elif command.lower()=='b':
                last_name= input("State the name of the employee: ")
                employee.apply_bonus(departament, last_name.title())
            elif command.lower()=='de':
                employee.display_employees(departament)
            elif command.lower()=='d':
                employee.display_departaments()
            elif command.lower()=="r":
                rem_name= input("Please state the name of the employee that you want to remove '\n'")
                employee.remove(departament,rem_name.title())
            elif command.lower()=="ba":
                employee.bonus_all(departament)
            elif command.lower()=="ad":
                employee.add_departament()
            elif command.lower() == "q":
                break
            else:
                print("Command invalid. Please repeat")
            
        else:
            pass