# Constant for the number of scores
NUM_SCORES = 4

def get_grade(score):
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 50:
        return "P"
    else:
        return "F"

def main():
    scores = []
    
    # Loop for the number of scores (using constant NUM_SCORES)
    for i in range(1, NUM_SCORES + 1):
        score = float(input(f"Score {i}: "))
        
        # Error checking for scores between 0 and 100
        while score < 0 or score > 100:
            print("Invalid score, please enter a value between 0 and 100.")
            score = float(input(f"Score {i}: "))
        
        scores.append(score)
    
    # Calculate the total and average of the scores
    total = sum(scores)
    average = total / len(scores)

    # Display grades for each score
    for i, score in enumerate(scores):
        grade = get_grade(score)
        print(f"Score {i+1} was {score}, which is {grade}")
    
    # Display the average score
    print(f"The average score was {average:.3f}")
    
    # Trend detection: Check if the last score is higher than the average
    if scores[-1] > average:
        print("The trend is positive")
    else:
        print("The trend is not positive")

if __name__ == "__main__":
    main()
