import datetime
from datetime import date 
import timedelta


#Get start and end date
def get_start_date():
    is_valid = False
    while not is_valid:
        user_in = input(
            "Enter 'STARTING' date (Use this format mm/dd/yy:  ")
        try:  # strptime throws an exception if the input doesn't match the pattern
            date = datetime.datetime.strptime(user_in, "%m/%d/%y")
            is_valid = True
        except:
            print("Wrong Date format. Use this format 'mm/dd/yy :(\n")
    return date


def get_end_date():
    is_valid = False
    while not is_valid:
        user_in = input(
            "Enter 'ENDING' date (Use this format mm/dd/yy:  ")
        try:  # strptime throws an exception if the input doesn't match the pattern
            date = datetime.datetime.strptime(user_in, "%m/%d/%y")
            is_valid = True
        except:
            print("Wrong Date format. Use this format 'mm/dd/yy :(\n")
    return date


def diff_dates():
    delta = get_start_date() - get_end_date()
    return (delta.days * -1)

def calc_dates():
    return diff_dates() / #<diviser comes from split data stored in dictionary of tuples in splits module


def gen_dates():
    diff = diff_dates()
    my_list = []
    for day in range(diff):
        a_date = (start_date + datetime.timedelta(days = day)).isoformat()
        my_list.append(a_date)

    print(my_list)
