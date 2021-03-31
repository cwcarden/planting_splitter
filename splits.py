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

    print("")
    print(planting_splits)