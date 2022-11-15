#Import section
from datetime import date                  #Import this for Data
import getpass                             #Import this for User

#Flowerbox section
#######################################################
#
#   Name: Joanna Elendu
#   Date: 09/11/2022
#   Program Description: 
#   
#   This program runs lines of code that will show 
#   employees username, current data and several lines
#   of output
#   
#   It also prints out resulting calculations as the 
#   inputs their data
#
######################################################

#Variables section
first_name = ''
last_name = ''
year_born = ''

is_this_correct = ''

all_employee_data_in_tuples_list = []

username_list = []

username_sorted_list = []

employee_data_dictionary = {}

YES_LIST = ["Yes", "YES","Y", "yes", "y"]


#Input section
while len(all_employee_data_in_tuples_list) < 5:
    first_name = input("Enter an employee first name: ")
    while len(first_name) < 2:
        first_name = input("Enter an employee first name: ")

    last_name = input("Enter an employee last name: ")
    while len(last_name) < 2:
        last_name = input("Enter an employee last name: ") 

    year_born = input("Enter an employee year of birth: ")
    while len(year_born)< 4:
        year_born = input("Enter an employee year of birth: ") 

    print("You entered " + first_name + " " + last_name +" " + year_born + "Is this correct?")
    is_this_correct = input("Yes or No ")

    if(is_this_correct in YES_LIST):
        employee_data = (first_name, last_name, year_born)
        all_employee_data_in_tuples_list.append(employee_data)
        first_name = ''
        last_name = ''
        year_born = ''
    else: 
        first_name = ''
        last_name = ''
        year_born = ''
        continue   
    #print(employee_data) 
    #print(all_employee_data_in_tuples_list)          #Prints as the list is being built

#print(all_employee_data_in_tuples_list)              #Prints whole list


#Process section
for employee in all_employee_data_in_tuples_list: 
    employee_first_name = employee[0]            #got first name from employee tuple
    employee_last_name = employee [1]
    employee_year_born = employee [2]

    first_init = employee_first_name[0].lower()
    last_name_username = employee_last_name.lower()
    last_two_digits_year_born = employee_year_born[-2:]

    username = first_init+last_name_username+last_two_digits_year_born

    if username in username_list:
        username = first_name.lower() + last_name[0:1].lower()+last_two_digits_year_born 
        username_list.append(username)
    else:
        username_list.append(username) 

    employee_data_dictionary[username] = employee 

username_sorted_list = list(username_list)           

username_sorted_list.sort()
    
#Output section
print(getpass.getuser())
print(date.today())

print(all_employee_data_in_tuples_list)
print(username_list)
print(employee_data_dictionary)
print(username_sorted_list)

for employee in all_employee_data_in_tuples_list:
    employee_data_displayed = employee[0] + " " + employee[1] + " was born in " + employee[2]
    print(employee_data_displayed) 
