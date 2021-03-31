import csv

#Returns hybrid name for csv naming
def get_hybrid_code():
    hybrid_code = input("Enter Fantasy Code or Hybrid name: ").upper()
    return hybrid_code


#Get female or male first
def is_male_first():
    male_first = input("Male or Female first? (Enter M or F):  ").upper()
    if male_first == "M":
        return True
    else:
        return False


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