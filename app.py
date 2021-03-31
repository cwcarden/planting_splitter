import csv
import datetime
from datetime import date 
import timedelta


#Get female or male first
def is_male_first():
    male_first = input("Male or Female first? (Enter M or F):  ").upper()
    if male_first == "M":
        return True
    else:
        return False


#Returns hybrid name for csv naming
def get_hybrid_code():
    hybrid_code = input("Enter Fantasy Code or Hybrid name: ").upper()
    return hybrid_code


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
    return int(diff_dates() / 6)    # <- calculated and dependent on planting splits


#gets user input data for planting splits returns dictionary of tuples
def get_splits():
    female_split_doc = input("Are there days of change in the female? Y or N ").upper()
    if female_split_doc == "Y":
        female_split = int(input("Enter female split ('EX' X would equal 0) "))
        female_split_2 = int(input("Enter female days of change: "))
        female = (female_split, female_split_2)
    else:
        female_split = int(input("Enter female split ('EX' X would equal 0) "))
        female = (female_split,)

    first_male_split_doc = input("Are there days of change on first male? Y or N ").upper()
    if first_male_split_doc == "Y":
        first_male_split = int(input("Enter 'FIRST' male split ('EX' X would equal 0) "))
        first_male_split_2 = int(input("Enter 'FIRST male days of change: "))
        first_male = (first_male_split, first_male_split_2)
    else:
        first_male_split = int(input("Enter 'FIRST' male split ('EX' X would equal 0) "))
        first_male = (first_male_split,)
    
    second_male_split_doc = input("Any days of change on second male? Y or N ").upper()
    if second_male_split_doc == "Y":
        second_male_split = int(input("Enter 'SECOND' male split ('EX' X would equal 0) "))
        second_male_split_2 = int(input("Enter 'SECOND' male days of change: "))
        second_male = (second_male_split, second_male_split_2)
    else:
        second_male_split = int(input("Enter 'SECOND' male split ('EX' X would equal 0) "))
        second_male = (second_male_split,)

    third_male_split_doc = input("Any days of change on third male? Y or N ").upper()
    if third_male_split_doc == "Y":
        third_male_split = int(input("Enter 'THIRD' male split ('EX' X would equal 0) "))
        third_male_split_2 = int(input("Enter 'THIRD' male days of change: "))
        third_male = (third_male_split, third_male_split_2)
    else:
        third_male_split = int(input("Enter 'THIRD' male split ('EX' X would equal 0) "))
        third_male = (third_male_split,)

    planting_splits = {
        "female": female,
        "1M": first_male,
        "2M": second_male,
        "3M": third_male
        } 

    return planting_splits


#Create CSV with headers based on Male or Female Named after get_hybrid_code() input
def create_csv():
    
    split_name = get_hybrid_code()
    with open(f'{split_name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        if is_male_first() == True:
            writer.writerow(["First 1/3 Male", "Second 1/3 Male", "Last 1/3 Male", "Female"])
            file.close()
        else:
            writer.writerow(["Female", "First 1/3 Male", "Second 1/3 Male", "Last 1/3 Male"])
            file.close()

def gen_dates():
    date1 = get_start_date()
    date2 = get_end_date()
    diff = diff_dates()
    my_list = []
    for day in range(diff):
        a_date = (date1 + datetime.timedelta(days = day)).isoformat()
        my_list.append(a_date)

    print(my_list)
