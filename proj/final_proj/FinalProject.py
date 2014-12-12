# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 23:37:10 2014

@author: meinazhou
"""
import sys
from user_input_process import *
from user_exceptions import *


def main():

    age =secure_input(age_validation,'Please enter your age.', parse_func.parse_age) # parse func need to revised after finishing parse functions
    education =secure_input(education_validation,'Please enter your education.',parse_func.parse_education)
    marital_status =secure_input(marital_validation,'Please enter your marital status.', parse_func.parse_marital_status)
    ocupation =secure_input(ocupation_validation,'Please enter your ocupation.',parse_func.parse_ocupation)
    capital_gain =secure_input(capital_gain_validation,'Please enter your capital gain.', parse_func.parse_capital_gain)
    hours_per_week = secure_input(hours_per_week_validation,'Please enter your working hours per week.',parse_func.parse_hours_per_week) 
               
            
def secure_input(validation_func, input_request,parse_function):
    
    while True:
        try:
            input_string = raw_input(input_request)
           
        except (KeyboardInterrupt, EOFError):
            #exception class
            sys.exit()
        termination_orders = ['Exit', 'End', 'Quit']
        if input_string in termination_orders:
            print '-----------Terminating the program.---------'
            sys.exit()
        if validation_func(input_string): #if the validation function returns true                      
            new_input = parse_func()
            parsed_input = parse_function(new_input, input_string) # revised
            break
        else:
            # ask the user to confirm whether treat the specific feature as unknown or not

            reenter_reply =raw_input('Your input is not valid. Do you want to re-enter it? Type Y if yes. N if not and we will treat this variable as unknown.')
            reenter_reply = ''.join(reenter_reply.split())
            
            if reenter_reply =='Y':
                continue
                                    
            else:
                print 'This variable will be treated as unknown.'
                parsed_input = 'unknown'
                break
            
        
    return parsed_input 
            
            
          
            
                
    