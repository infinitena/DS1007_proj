# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 23:37:10 2014

@author: meinazhou
"""
import sys
from validationFunctions import *
def main():

    age =secure_input(age_validtion(),'Please enter your age.', parse_func) # parse func need to revised after finishing parse functions
    education =secure_input(education_validation(),'Please enter your education.',parse_func)
    martial_status =secure_input(martial_validation(),'Please enter your martial status.', parse_func)
    ocupation =secure_input(ocupation_validation(),'Please enter your ocupation.',parse_func)
    capital_gain =secure_input(capital_gain_validation(),'Please enter your capital gain.', parse_func)
    hours_per_week secure_input(hours_per_week_validation(),'Please enter your working hours per week.',parse_func) 
    
            
            
def secure_input(validation_func, input_request,parse_func):
    while True:
        try:
            string = raw_input(input_request)
        except (KeyboardInterrupt, EOFError):
            #exception class
            sys.exit()
        termination_orders = ['Exit', 'End', 'Quit']
        if string in termination_orders:
            print '-----------Terminating the program.---------'
            sys.exit()
        if validation_func(string): #if the validation function returns true
            parsed_input = parse_func(string)
        else:
            # ask the user to confirm whether treat the specific feature as unknown or not

            reenter_reply =raw_input('Your input is not valid. Do you want to re-enter it? Type Y if yes. N if not and we will treat this variable as unknown.')
            reenter_reply = ''.join(reenter_reply.split())
            if reenter_reply =='Y':
                continue 
            else:
                parsed_input = 'unknown'
                
        
    return parsed_input 
            
            
          
            
                
    