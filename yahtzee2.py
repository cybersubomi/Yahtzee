def make_roll() -> tuple:
    """
    Returns a tuple of five random values between 1 and 6.
    """
    import random
    dice_roll = (random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6))  #roll dice
    
    return dice_roll
def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    Example: sum_of_given_number((2,6,2,6,1), 6) = 12
    """
    sum_of_given_number = 0
    for digit in roll:
        if number == digit:
            sum_of_given_number += digit       #sum of all occurences of number in the dice_roll
        else:
            sum_of_given_number += 0
            
    return sum_of_given_number

def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    """
    dice_numbers = [1,2,3,4,5,6]
    sum_list = []
    for number in dice_numbers:
        sum_list.append(sum_of_given_number(roll,number))       #update sum list with all occurences of numbers between 1-6 in tuple
    
    return sum_list

def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    
    for i in range(len(names)):                 #loop through names list and print corresponding upper_section_scores list
        print(f"{names[i]}: {upper_section_scores[i]}")

def num_of_a_kind(roll: tuple, number: int) -> int:
    '''
    If a roll has EXACTLY `number` dice of the same face value,
    returns the sum of all five values in the roll.
    Otherwise, returns 0.
    '''
    from collections import Counter
    sum_value = 0
    face_count = Counter(roll)
    for key,value in face_count.items():      #sort key-value tuple pair into key value variable
        if value == number:
            for i in roll:                 #sum all values in tuple
                sum_value += i
    return sum_value



def yahtzee(roll: tuple) -> int:
    """
    Returns 50 if the roll is a Yahtzee (all dice in the roll have the same
    face value). Otherwise, returns 0.
    """
    from collections import Counter
    sum_value = 0
    face_count = Counter(roll)
    for key,value in face_count.items():      #sort key-value tuple pair into key value variable
        if value == 5:
                sum_value = 50
    return sum_value

    
def main():
    """
    Main function.
    """
    dice_roll = make_roll()                 #Roll the dice
    upper_section_score = fill_upper_section(dice_roll) #Fill the upper section
    
    print(f"Rolling the dice... {dice_roll}")
    print("Upper section:") # Display the upper section
    display_upper_section(upper_section_score)
    print("Lower section:")
    print(f"Three of a kind: {num_of_a_kind(dice_roll,3)}")     # Calculate and display "3 of a kind" for the given roll
    print(f"Four of a kind: {num_of_a_kind(dice_roll,4)}")      # Calculate and display "4 of a kind" for the given roll
    print(f"Yahtzee: {yahtzee(dice_roll)}")                     # Calculate and display "Yahtzee" for the given roll
    
   
if __name__ == "__main__":
    main()

        
  
