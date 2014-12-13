import sys
import numpy as np
from data_clean import *
from user_input_process import *
from user_exceptions import *
from prediction_model import *

def main():

    #take and parse user input to prepare data for prediction
    age = secure_input(age_validation,'Please enter your age: ', parse_func.parse_age) 
    education = secure_input(education_validation,'Please enter your education (choose the best one that represents you: Doctorate, Masters, Bachelors, Associate, Prof-school, Below 12th): ',parse_func.parse_education)
    marital_status = secure_input(marital_validation,'Please enter your marital status (choose the best one that represents you: Married, Married-spouse-absent, Separated, Divorced, Never-married, Widowed): ', parse_func.parse_marital_status)
    ocupation = secure_input(ocupation_validation,'Please enter your ocupation (choose the best one that represents you: Adm-clerical, Armed-Forces, Craft-repair, Exec-managerial, Farming-fishing, Handlers-cleaners, Machine-op-inspct, Other-service, Priv-house-serv, Prof-specialty, Protective-serv, Sales, Tech-support, Transport-moving): ',parse_func.parse_ocupation)
    capital_gain = secure_input(capital_gain_validation,'Please enter your capital gain (between 0 and 100000): ', parse_func.parse_capital_gain)
    hours_per_week = secure_input(hours_per_week_validation,'Please enter your working hours per week (between 0 and 100): ',parse_func.parse_hours_per_week) 
    
    #if a user inputs unknown for a variable above, we take the mean of the variable in our model data
    cleaned_data = clean_data_for_prediction('adult_data.txt')
    dictionary_map = {'age': age, 'education': education, 'martial-status': marital_status, 'ocupation': ocupation, 'capital-gain': capital_gain, 'hours-per-week': hours_per_week}
    #iterate through the dictionary, find which variables are assigned to 100 (unknown), and reassign them to the mean in model data
    for name, value in dictionary_map.items():
        if value == 100:
            value = np.mean(cleaned_data[name])
             
    #read data into panda series 
    data_to_predict = pd.Series(dictionary_map, index = None)
    #put the serie of data into our random forest model to predict whether a person makes over 50k per year
    output = randomForest(data_to_predict)
    if output:
        print '\nAccording to our model prediction, you make over 50 thousand dollars per year.'
    else:
        print '\nAccording to our model prediction, you make less than 50 thousand dollars per year.'
    
    return
    
    
def secure_input(validation_func, input_request,parse_function):
    '''
    this function takes validation functions, parse functions, and input request as arguments to output parsed user input.
    '''
    while True:
        try:
            input_string = raw_input(input_request)
        except (KeyboardInterrupt, EOFError):
            raise invalid_input_exception()
            sys.exit()
            
        termination_orders = ['Exit', 'End', 'Quit']
        if input_string in termination_orders:
            print '-----------Terminating the program.---------'
            sys.exit()
        
        #if user input is validated, then use the parse class functions to parse the input
        if validation_func(input_string):                     
            new_input = parse_func()
            parsed_input = parse_function(new_input, input_string) 
            break
        else:
            # ask the user to confirm whether treat the specific feature as unknown or not
            reenter_reply =raw_input('Your input is not valid. Do you want to re-enter it? Type Y if yes. N if not and we will treat this variable as unknown.')
            reenter_reply = ''.join(reenter_reply.split())
            
            if reenter_reply =='Y':
                continue
            else:
                print '\nThis variable value will be taken from the mean of our sample data.'
                #assign the unknown variable to an integer type (default 100 here)
                parsed_input = 100
                break
            
    return parsed_input 
            
            
          
            
                
    