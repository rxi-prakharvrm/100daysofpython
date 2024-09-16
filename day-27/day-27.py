'''
Create a program capable of displaying questions to the user like KBC.
Use List data type to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game.
'''

# data
questions = [
    {
        "qno": 1,
        "question": "Which of the following data types is immutable in Python?",
        "a": "int",
        "b": "bool",
        "c": "list",
        "d": "tuple",
        "correct": "d"
    },
    {
        "qno": 2,
        "question": "Which function is used to get the length of a list in Python?",
        "a": "length()",
        "b": "len()",
        "c": "size()",
        "d": "count()",
        "correct": "b"
    },
    {
        "qno": 3,
        "question": "Which of the following is not a valid keyword in Python?",
        "a": "try",
        "b": "finally",
        "c": "catch",
        "d": "except",
        "correct": "c"
    },
    {
        "qno": 4,
        "question": "How do you create a variable with the floating-point value 5.5 in Python?",
        "a": "float num = 5.5",
        "b": "num = float(5.5)",
        "c": "num = 5.5",
        "d": "float num = '5.5'",
        "correct": "c"
    },
    {
        "qno": 5,
        "question": "Which of the following loops in Python is known as an entry-controlled loop?",
        "a": "while loop",
        "b": "do-while loop",
        "c": "for loop",
        "d": "foreach loop",
        "correct": "a"
    },
    {
        "qno": 6,
        "question": "Which of the following functions is used to convert a string into a list of characters in Python?",
        "a": "list()",
        "b": "str()",
        "c": "split()",
        "d": "join()",
        "correct": "a"
    },
    {
        "qno": 7,
        "question": "Which operator is used to check if two values are not equal in Python?",
        "a": "!=",
        "b": "==",
        "c": "!==",
        "d": "<>",
        "correct": "a"
    },
    {
        "qno": 8,
        "question": "Which of the following is the correct way to declare a function in Python?",
        "a": "def functionName():",
        "b": "function functionName():",
        "c": "void functionName():",
        "d": "functionName function():",
        "correct": "a"
    },
    {
        "qno": 9,
        "question": "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
        "a": "strip()",
        "b": "trim()",
        "c": "remove()",
        "d": "clean()",
        "correct": "a"
    },
    {
        "qno": 10,
        "question": "Which of the following methods is used to add an element to the end of a list in Python?",
        "a": "insert()",
        "b": "append()",
        "c": "add()",
        "d": "extend()",
        "correct": "b"
    },
    {
        "qno": 11,
        "question": "Which of the following is not a valid data type in Python?",
        "a": "str",
        "b": "int",
        "c": "float",
        "d": "real",
        "correct": "d"
    },
    {
        "qno": 12,
        "question": "Which built-in function returns the largest item in an iterable in Python?",
        "a": "max()",
        "b": "largest()",
        "c": "top()",
        "d": "high()",
        "correct": "a"
    },
    {
        "qno": 13,
        "question": "How do you start a comment in Python?",
        "a": "//",
        "b": "/*",
        "c": "#",
        "d": "<!--",
        "correct": "c"
    },
    {
        "qno": 14,
        "question": "Which of the following modules in Python is used for regular expressions?",
        "a": "regex",
        "b": "re",
        "c": "regexp",
        "d": "match",
        "correct": "b"
    },
    {
        "qno": 15,
        "question": "What is the output of the following code: print(2 ** 3)?",
        "a": "6",
        "b": "8",
        "c": "9",
        "d": "5",
        "correct": "b"
    },
    {
        "qno": 16,
        "question": "Which of the following functions can be used to read a line from the standard input in Python?",
        "a": "input()",
        "b": "get()",
        "c": "scan()",
        "d": "read()",
        "correct": "a"
    },
    {
        "qno": 17,
        "question": "Which of the following is a mutable data type in Python?",
        "a": "tuple",
        "b": "str",
        "c": "list",
        "d": "int",
        "correct": "c"
    },
    {
        "qno": 18,
        "question": "Which of the following methods can be used to convert a string to lowercase in Python?",
        "a": "lower()",
        "b": "toLowerCase()",
        "c": "strtolower()",
        "d": "lowercase()",
        "correct": "a"
    },
    {
        "qno": 19,
        "question": "Which of the following will raise an error in Python?",
        "a": "10 / 2",
        "b": "10 // 2",
        "c": "10 / 0",
        "d": "10 * 2",
        "correct": "c"
    },
    {
        "qno": 20,
        "question": "What does the 'len()' function do in Python?",
        "a": "Returns the size of a file",
        "b": "Returns the length of an iterable",
        "c": "Returns the maximum value in a list",
        "d": "Returns the number of arguments passed",
        "correct": "b"
    }
]

levels = {
    "1": 1000,
    "2": 2000,
    "3": 5000,
    "4": 10000,
    "5": 20000,
    "6": 40000,
    "7": 80000,
    "8": 160000,
    "9": 320000,
    "10": 640000,
    "11": 1250000,
    "12": 2500000,
    "13": 5000000,
    "14": 10000000,
    "15": 70000000,
}

users = [
    {
        "mobile": 9356845256,
        "fname": "Prakhar",
        "lname": "Verma",
        "age": 23,
        "currLevel": 1,
        "winningPrice": 0
    },
    {
        "mobile": 1254632589,
        "fname": "Harry",
        "lname": "Jain",
        "age": 34,
        "currLevel": 1,
        "winningPrice": 0
    }
]

# program
from random import choice

currPlayer = choice(users)

for question in questions:

    qno = question["qno"]

    if qno > 5:
        break

    print(qno, ". ", question["question"])
    for key in ['a', 'b', 'c', 'd']:
        print(f"{key}. {question[key]}")
    print()

    ans = input("Select your ans (a, b, c, d): ")

    if ans == question["correct"]:
        print("Congratulations! You won: ", levels[str(qno)])
        currPlayer["currLevel"] += 1
        currPlayer["winningPrice"] = levels[str(qno)]
    else:
        print("Better luck next time! Your winning price is: ", currPlayer["winningPrice"])
        break