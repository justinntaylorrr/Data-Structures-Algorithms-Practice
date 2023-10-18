#Calculates final score based on weekly score updates, returns the highest score reached and the week where this occured.

def score_calc():
    current_score = 1500
    highest_score_value = 1500
    current_week = 0
    highest_score_week = 0
    

    updates = [42,500,-654,-973,908,444,781,-700]
    num_weeks = len(updates)

    for i in updates:
        current_score += i
        current_week += 1
        
        if current_score > highest_score_value:
            highest_score_value = current_score
            highest_score_week = current_week
      
    final_score = current_score
    
    print(f"You started with a score of '1500'. After {num_weeks} weeks, your updated score is '{final_score}'!")
    print(f"The highest score you reached was '{highest_score_value}' and this was in week {highest_score_week}.\n")
    
    return highest_score_value, final_score, highest_score_week

    
 
print(score_calc())
