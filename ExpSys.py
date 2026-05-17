

# 1. Information Management (like a study notes finder)

def info_system(topic):
    notes = {
        "python": "Python basics: variables, loops, functions.",
        "java": "Java basics: classes, objects, inheritance.",
        "sql": "SQL basics: SELECT, INSERT, UPDATE."
    }
    return notes.get(topic.lower(), "No information available.")

print(info_system("python"))





# 2. Hospitals and Medical Facilities (symptom checker)
def medical_system(symptoms):
    if "fever" in symptoms and "cough" in symptoms:
        return "Possible flu. Consult a doctor."
    elif "headache" in symptoms:
        return "Possible migraine. Take rest."
    else:
        return "No diagnosis available."

print(medical_system(["fever", "cough"]))




# 3. Help Desk Management (FAQ bot)
def helpdesk(query):
    if "password" in query.lower():
        return "To reset password: Go to settings then Reset."
    elif "wifi" in query.lower():
        return "Check router and reconnect."
    else:
        return "Contact IT support."

print(helpdesk("How to reset password"))



# 4. Employee Performance Evaluation
def performance_system(score):
    if score >= 80:
        return "Excellent Performance"
    elif score >= 50:
        return "Average Performance"
    else:
        return "Needs Improvement"

print(performance_system(75))




# 5. Stock Market Trading (basic advisor)
def stock_system(trend):
    if trend == "up":
        return "Buy the stock."
    elif trend == "down":
        return "Sell the stock."
    else:
        return "Hold the stock."

print(stock_system("up"))



# 6. Airline Scheduling and Cargo
def airline_system(weight):
    if weight < 100:
        return "Assign to small plane."
    else:
        return "Assign to cargo plane."

print(airline_system(120))
