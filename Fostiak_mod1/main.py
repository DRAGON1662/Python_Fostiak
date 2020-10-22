from validation import Validation as v, ERR_VALUE

class E_Date:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year
    
    def getDay(self):
        return self.__day
    
    def getMonth(self):
        return self.__month
    
    def getYear(self):
        return self.__year
    
    def __repr__(self):
        return f"{self.__day}/{self.__month}/{self.__year}"
    
    def __str__(self):
        return f"{self.__day}/{self.__month}/{self.__year}"
        
        
class Work_Calendar:
    def __init__(self):
        self.__calendar = {}
    
    def add_to_calendar(self, employee, date):
        year_key = date.getYear
        if year_key not in self.calendar:
            self.__calendar[year_key] = {i: [] for i in range(1, 13)}
            self.__calendar[year_key][date.getMonth()].append(employee)
        else:
            self.__calendar[year_key][date.getMonth()].append(employee)
    
    def getCalendar(self):
        return self.__calendar
        
class Employee:
    def __init__(self, name, salary, FirstWorkingDate, LastWorkingDate):
        self.__name = v.validateName(name, 'Name')
        self.__salary = v.validateFloat(salary, 'Salary')
        self.__FirstWorkingDate = FirstWorkingDate
        self.__LastWorkingDate = LastWorkingDate
    
    def getName(self):
        return self.__name
        
    def getSalary(self):
        return self.__salary

    def getFirstWorkingDate(self):
        return self.__FirstWorkingDate

    def getLastWorkingDate(self):
        return self.__LastWorkingDate
    
    def __repr__(self):
        return f"Name: {self.__name}\n\tSalary: {self.__salary}\n\tStart work: {self.__FirstWorkingDate}\n\tStop work: {self.__LastWorkingDate}"
    
    def __str__(self):
        return f"Name: {self.__name}\n\tSalary: {self.__salary}\n\tStart work: {self.__FirstWorkingDate}\n\tStop work: {self.__LastWorkingDate}"
    
class Factory:
    def __init__(self):
        self.amountOfEmployees = 0
        self.cdar = Work_Calendar()
        self.__hired_employees = []
        self.__fired_employees = []
        
    def hire_employee(self, employee):
        if self.check_20():
            self.__hired_employees.append(employee)
            self.amountOfEmployees += 1
            self.cdar.add_to_calendar(employee, employee.getFirstWorkingDate())
        
    def fire_employee(self, employee):
        if self.check_20():
            self.__hired_employees.remove(employee)
            self.__fired_employees.append(employee)
            self.amountOfEmployees -= 1
            self.cdar.add_to_calendar(employee, employee.getLastWorkingDate())
        
    def check_20(self):
        cald = self.cdar.getCalendar()
        for year in cald:
            for month in cald[year]:
                if len(cald[year][month])/self.amountOfEmployees > 0.2:
                    return False
        return True
    
    def show_info(self):
        for emp in self.__hired_employees:
            print(emp)
    
    def read_array(self):
        pass
        
    def write_to_file(self, filename):
        pass