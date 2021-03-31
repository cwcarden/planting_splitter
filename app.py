import csv
import datetime
from datetime import date 


#Create CSV with headers based on Male or Female
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

#Get female or male first
def is_male_first():
    male_first = input("Male or Female first? (Enter M or F):  ").upper()
    if male_first == "M":
        return True
    else:
        return False

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
    return (delta * -1) / 6

def get_male_split():
    first_male_split = int(input("Enter 'FIRST' male split ('EX' X would equal 0) "))
    second_male_split = int(input("Enter 'SECOND' male split ('EX' X would equal 0) "))
    third_male_split = int(input("Enter 'THIRD' male split "))
    print(f"Male split is: (1M-{first_male_split}, 2M-{second_male_split}, 3M-{third_male_split})")
    male_split =(first_male_split, second_male_split, third_male_split)
    return (male_split)