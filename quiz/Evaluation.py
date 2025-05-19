def evaluate_score(score):
    percentage = (score / 10) * 100
    if percentage >= 70:
        return "Excellent! You are ready for the exam."
    elif percentage >= 50:
        return "Good, but you should review some topics."
    else:
        return "Keep practicing! Consider reviewing the fundamentals."