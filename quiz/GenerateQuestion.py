import random

def generate_questions():
    questions = [
        {"question": "What is the formula for calculating the area of a triangle?",
         "options": ["A) 1/2 * base * height", "B) base * height", "C) 1/3 * base * height", "D) base + height"],
         "answer": "A", "difficulty": "Easy", "category": "IF CALC"},

        {"question": "What is the unit of measurement for angles?", 
         "options": ["A) Meters", "B) Degrees", "C) Liters", "D) Grams"], 
         "answer": "B", "difficulty": "Easy", "category": "IF IDENTIFICATION"},
        
        {"question": "What does GPS stand for?", 
         "options": ["A) Global Positioning System", "B) Geographical Positioning System", "C) Global Positioning Service", "D) Geographical Positioning Service"], 
         "answer": "A", "difficulty": "Easy", "category": "IF IDENTIFICATION"},
        
        {"question": "What is the main purpose of leveling in surveying?", 
         "options": ["A) To measure distances", "B) To determine elevation", "C) To calculate angles", "D) To find coordinates"], 
         "answer": "B", "difficulty": "Medium", "category": "IF CALC"},
        
        {"question": "Which of the following is a type of survey?", 
         "options": ["A) Topographic", "B) Geological", "C) Environmental", "D) All of the above"], 
         "answer": "D", "difficulty": "Medium", "category": "IF IDENTIFICATION"},
        
        {"question": "What is the formula for calculating the volume of a cylinder?", 
         "options": ["A) πr^2h", "B) 2πrh", "C) πr^2", "D) 2πr^2h"], 
         "answer": "A", "difficulty": "Medium", "category": "IF CALC"},
        
        {"question": "What is the purpose of a theodolite?", 
         "options": ["A) To measure temperature", "B) To measure angles", "C) To measure pressure", "D) To measure distance"], 
         "answer": "B", "difficulty": "Hard", "category": "IF IDENTIFICATION"},
        
        {"question": "What is the principle of triangulation?", 
         "options": ["A) Measuring angles to determine distances", "B) Measuring distances to determine angles", "C) Measuring heights", "D) None of the above"], 
         "answer": "A", "difficulty": "Hard", "category": "IF CALC"},
        
        {"question": "What is the significance of the datum in surveying?", 
         "options": ["A) It is a reference point", "B) It is a measurement unit", "C) It is a type of survey", "D) It is a tool"], 
         "answer": "A", "difficulty": "Hard", "category": "IF IDENTIFICATION"},
        
        {"question": "What is the formula for calculating the circumference of a circle?", 
         "options": ["A) 2πr", "B) πr^2", "C) πd", "D) 2r"], 
         "answer": "A", "difficulty": "Hard", "category": "IF CALC"}
    ]
    return random.sample(questions, 10)