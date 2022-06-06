import json
import pickle
from turtle import update

class Employee:

    # This function adds the employees to the file
    
    def add_employee(self, departament):
        
        self.name= input("Please type the first name: ")
        self.last_name = input("Please type the last name: ").title()
        self.age = input("Please type the age: ")
        self.job = input("Please type the job: ").title()
        self.salary= float(input("Please type the salary: "))
        self.bonus=float(input("Please type the bonus: "))
        self.new_employee = {
            

            self.name:{
    
                "First name": self.name.title(),
                "Last name": self.last_name,
                "Age": self.age,
                "Job": self.job,
                "Salary":self.salary,
                "Bonus": self.bonus,
                "Total salary": self.bonus + self.salary
                }
            }
        
        #Opening the file for writing

        try:

            with open(rf"employees_{departament}", "r") as file:
                    
                data = json.load(file)
                    
        except FileNotFoundError:

            with open(rf"employees_{departament}", "w") as file:
                json.dump(self.new_employee, file, indent = 4 )

        else:
            data.update(self.new_employee)

            with open(rf"employees_{departament}", "w") as file:
                json.dump(data, file, indent = 4 )

        file.close()
        
#Searches for the employee and adds the bonus

    def apply_bonus(self, departament, name):
    

        with open(rf"employees_{departament}", "r+") as file:
            self.bonus=  float(input("Please type the new bonus: "))
            data = json.load(file)
            if name in data:
                old_bonus= float(data[name]["Bonus"])
                new_bonus = self.bonus+old_bonus
                self.updateed_employee={
                    name:{
                        "First name": name,
                        "Last name": data[name]["Last name"],
                        "Age": data[name]["Age"],
                        "Job": data[name]["Job"],
                        "Salary": data[name]["Salary"],
                        "Bonus": new_bonus,
                        "Total salary":float(data[name]["Salary"])+ new_bonus

                    }
                }
                data.update(self.updateed_employee)
                with open(rf"employees_{departament}", "w") as file:
                    json.dump(data, file, indent = 4 )
                    file.close()
            else:
                print("That name does not exit in the database")
            
#Displays the employees of that epartament
            
    def display_employees(self,departament):     
        with open(rf"employees_{departament}", "r+") as file:
            data= json.load(file)
            print("The employees of this departament are: '\n")
            for name in data:
                if data[name]["First name"] !="":
                    print(data[name]["First name"], data[name]["Last name"])
        file.close()                   

# Removes an employee from the database

    def remove(self,departament,rname):
        with open(rf"employees_{departament}", "r+") as file:
            data= json.load(file)
            if rname in data:
                del(data[rname] )
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent = 4 )
            else:
                print("That name does not exit in the database")
        file.close()

#this function  gives everyone in the departament a bonus

    def bonus_all(self, departament):
        with open(rf"employees_{departament}", "r+") as file:
            self.bonus=  float(input("Please type the new bonus: "))
            data = json.load(file)
            for name in data:

                old_bonus= float(data[name]["Bonus"])
                new_bonus = self.bonus+old_bonus
                self.updateed_employee={
                    name:{
                        "First name": name,
                        "Last name": data[name]["Last name"],
                        "Age": data[name]["Age"],
                        "Job": data[name]["Job"],
                        "Salary": data[name]["Salary"],
                        "Bonus": new_bonus,
                        "Total salary":float(data[name]["Salary"])+ new_bonus

                    }
                }
                data.update(self.updateed_employee)
                with open(rf"employees_{departament}", "w") as file:
                    json.dump(data, file, indent = 4 )
                    file.close()


        
    def display_departaments(self):
        print("Our departaments are Managering and Software")