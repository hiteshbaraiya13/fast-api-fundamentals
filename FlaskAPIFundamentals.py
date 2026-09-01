from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    
    return{
        "message": "Welcome to Super30 Flask API"
    }

@app.get("/student")
def student():
    
    return{
        "Name": "John Doe",
        "Age": 20,
        "Grade": "A",
        "School": "Super30"
    }

@app.get("/course")
def courseAPI():
    
    return{
        "Course-Name": "Python Programming",
        "Duration": "12 weeks",
        "Mentor": "John Smith",
        "Topics" : ["Variables", "Data Types", "Control Flow", "Functions", "Modules", "File Handling", "Object-Oriented Programming"]
    }

@app.get("/skills")
def skillsAPI():
    
    return{
        "Skills": ["Python", "Flask", "FastAPI", "Django", "Data Analysis", "Machine Learning"]
    }

@app.get("/addition")
def addition(a: int, b: int):
    result = a + b
    return {
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/multipy")
def multiply(a: int, b: int):
    result = a * b
    return {
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/square")
def square(n: int):
    result = n ** 2
    return {
        "n": n,
        "result": result
    }

@app.get("/check_even_odd")
def check_even_odd(n: int):
    if n % 2 == 0:
        return {
            "n": n,
            "result": "Even"
        }
    else:
        return {
            "n": n,
            "result": "Odd"
        }

@app.get("/table")
def table(n: int):
    table_data = []
    for i in range(1, 11):
        table_data.append({
            "multiplier": i,
            "result": n * i
        })
    return {
        "number": n,
        "table": table_data
    }

@app.get("/profile/{name}/{age}")
def profile(name: str, age: int):
    return {
        "name": name,
        "age": age,
    }

@app.get("/number/{num}")
def number(num: int):
    if num % 2 == 0:
        return {
            "n": num,
            "result": "Even"
                }
    else:
        return {
                "number": num,
                "square": num ** 2,
                "cube": num ** 3,
                "result": "Odd"}
    
