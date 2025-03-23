class Employee:
    def __init__(self, employee_name, current_ctc, increment_percent):
        self.employee_name = employee_name
        self.current_ctc = current_ctc
        self.increment_percent = increment_percent

    def calculate_increment(self):
        return self.current_ctc * (self.increment_percent / 100)

    def get_employee_detail(self):
        return f"Employee: {self.employee_name}, CTC: {self.current_ctc}, Increment(In %age): {self.increment_percent}"

    def updated_ctc(self):
        return self.current_ctc + self.calculate_increment() #return the calculated ctc.

class Updated_ctc:
    def final_ctc(self, employee):
        details = employee.get_employee_detail()
        updated_ctc_value = employee.updated_ctc() #get the calculated value.

        print("----Employee----")
        print(details)
        print(f"Updated_ctc: {updated_ctc_value}") #print the returned value.
        print('----------------')

# Corrected usage:
updated_ctc_generator = Updated_ctc()

Arsh = Employee("Arsh", 1000000, 4)
updated_ctc_generator.final_ctc(Arsh)

Arshpreet = Employee("Arshpreet", 2000000, 15)
updated_ctc_generator.final_ctc(Arshpreet)

Manik = Employee("Manik", 1500000, 3)
updated_ctc_generator.final_ctc(Manik)