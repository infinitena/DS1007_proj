# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 02:45:16 2014

@author: meinazhou

This file contains validation functions for each input of the features.
"""

def age_validation(age_input):
    '''This function validates the input of age. The function raises exceptions when th input is invalid.
    We assume the age range is [18,70]''' 
    try:
        age_input =int(age_input)
    except:
        raise invalid_age_exception
        
    if (age_input < 18) or (age_input>70):
        raise out_of_range_age_exception
    else:
        return True
    
 
def education_validation(education_input):
    '''This function validates the input of education. The function raises exception when the input is invalid.'''      
    education_input = ''.join(education_input.split())
    
    if education_input in ['Doctorate', 'Masters', 'Bachelors', 'Assoc-acdm', 'Assoc-voc', 'Some-college', 'Prof-school', '10th', '11th', '12th', '1st-4th', '5th-6th', '7th-8th','9th','Preschool', 'HS-grad']:
        return True 
    else:
        return False

def martial_validation(martial_input):
    '''This function validates the input of martial status.'''
    martial_input = ''.join(martial_input.split())
    if martial_input in ['Married-AF-spouse', 'Married-civ-spouse', 'Married-spouse-absent', 'Separated', 'Divorced', 'Never-married', 'Widowed']:
        return True
    else:
        return False 

def ocupation_validation(ocupation_input):
    '''This function validates the input of ocupation.'''
    ocupation_input = ''.join(ocupation_input.split())
    if ocupation_input in ['Adm-clerical', 'Armed-Forces', 'Craft-repair', 'Exec-managerial', 'Farming-fishing', 'Handlers-cleaners', 'Machine-op-inspct','Other-service', 'Priv-house-serv', 'Prof-specialty', 'Protective-serv','Sales', 'Tech-support', 'Transport-moving']:
        return True
    else:
        return False
 
def capital_gain_validation(capital_gain_input):
    '''
    This function validates the input of capital gain. This function raises exception when the input of capital gain is out of range.
    We assume the range is [0,100000]    
    '''
    try:
        capital_gain_input =int(capital_gain_input)
    except:
        raise invalid_capital_gain_exception
    
    if (capital_gain_input < 0) or (capital_gain_input > 100000):
        raise out_of_range_capital_gain_exception
    else:
        return True

def hours_per_week_validation(hours_per_week_input):
    '''
    This function validates the input of hours per week. This function raises exception when the input of hours per week is out of range.
    We assume the range is [0,100]    
    '''
    try:
        hours_per_week_input =int(hours_per_week_input)
    except:
        raise invalid_hours_per_week_exception
    
    if (hours_per_week_input < 0) or (hours_per_week_input > 100):
        raise out_of_range_capital_gain_exception
    else:
        return True
    
        
class invalid_age_exception(Exception):
    '''Raise exception when the input of age is not a valid integer.'''
    def __str__(self):
        return 'The input of age is not a valid integer.' 

class out_of_range_age_exception(Exception):
    '''Raise exception when the input of age is out of the range [18,70].'''
    def __str__(self):
        return 'The input of age is out of the range [18,70].'

class invalid_capital_gain_exception(Exception):
    '''Raise exception when the input of capital gain is not a valid integer.'''
    def __str__(self):
        return 'The input of capital gain is not a valid integer.'
        
class out_of_range_capital_gain_exception(Exception):
    '''Raise exception when the input of capital gain is out of the range [0,100000].'''
    def __str__(self):
        return 'The input of capital gain is out of the range [0,100000].'

class invalid_hours_per_week_exception(Exception):
    '''Raise exception when the input of hours per week is not a valid integer.'''
    def __str__(self):
        return 'The input of hours per week is not a valid integer.'
        
class out_of_range_hours_per_week_exception(Exception):
    '''Raise exception when the input of capital gain is out of the range [0,100].'''
    def __str__(self):
        return 'The input of capital gain is out of the range [0,100].'
