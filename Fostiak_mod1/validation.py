import re

ERR_VALUE = -9999

def validationDecorator(func):
    def inner (*args, **kwargs):
        try:
            returnVal = func(*args, **kwargs)
        except ValueError as ve:
            print('ERROR: ' + str(ve) + ' (' + str(args[0]) + ')')
            returnVal = ERR_VALUE
        return returnVal

    return inner

class Validation:
    def __init__(self): 
        pass

# Validation for Salary
    @staticmethod
    @validationDecorator
    def validateFloat(val, _str):
        try:
            val = round(float(val), 2)
        except ValueError: 
            raise ValueError(_str + ' must have a float value with two digits')
        
        return val      
# End Validation for Salary
# Validation for name

    @staticmethod
    @validationDecorator
    def validateStr(val, _str):
        if not isinstance(val, str):
            raise ValueError(_str + ' must have a string value')

        return val

    @staticmethod
    @validationDecorator
    def validateName(val, _str):
        if re.search(r'[^A-Za-z ]+', val) is not None: 
            raise ValueError(_str + ' must contain only letters')
        
        return val     

# End Validation for name
# Validate Employee

    @staticmethod
    def validateEmployee(val, _str='Employee'):
        Validation.validateName(val.getName(), 'Name')  # change getter
        Validation.validateFloat(val.getSalary(), 'Salary')  # change getter
        

        return val