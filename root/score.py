def lose_points(current_score):
    new_score = current_score - 10
    if current_score <= 0:
        new_score = 0
    return new_score

def score_rate(current_score):
    if current_score in range(80, 101):
        return "Excellent"
    elif current_score in range (50,80):
        return "Good"
    else:
        return "Keep Practicing"

if __name__ == "__main__":
    score = 100
    score = lose_points(score)
    print(f"Score after one incorrect answer: {score}")
    print(f"score: {score_rate(score)}")
    score = 60
    score = lose_points(score)
    print(f"score after 5 incorrect answers: {score}")
    print(f"score: {score_rate(score)}")