import datetime
import time

   
# Function to display timer
def displayTimer(seconds):
    minutes, seconds = divmod(seconds, 10)
    timeFormat = "{:02d}:{:02d}".format(minutes, seconds)
    print("Time elapsed: ", timeFormat)

# Function to print and validate user choice
def correctChoice(choices):
    for choice in choices:
        print(choice)
    userChoice = input("Enter your choice (a/b/c/d): ")
    while userChoice not in ['a', 'b', 'c', 'd']:
        print("Invalid choice!")
        userChoice = input("Enter your choice (a/b/c/d): ")
    return userChoice

def correctChoice1(choices):
    print(choices)
    userChoice = input("Enter your choice (a/b/c/d): ")
    while userChoice not in ['a', 'b', 'c', 'd']:
        print("Invalid choice!")
        userChoice = input("Enter your choice (a/b/c/d): ")
    return userChoice


# Define easy level questions and answers
def easyLevel():
   print("\nEasy Level\n")
   questions = [
      "1. What is the output of the following code?\nprint(3+2*2)",    
      "2. What is the output of the following code?\nprint('Hello World'[0:5])",
      "3. What is the output of the following code?\nprint(type(3.14))",
      "4. What is the output of the following code?\nprint('Python'.find('o'))",
      "5. What is the output of the following code?\nprint(len([1,2,3]))",
      "6. What is the output of the following code?\nprint('Python'.upper())",
      "7. What is the output of the following code?\nprint(2**3**2)",
      "8. What is the output of the following code?\nprint('Hello ' + 'World')",
      "9. What is the output of the following code?\nprint(list(range(2, 11, 2)))",
      "10. What is the output of the following code?\nprint(1 != 2)"]

   choices = [
      ['A. 7', 'B. 8', 'C. 10', 'D. 12'],
      ['A. Hello', 'B. World', 'C. Hello ', 'D. Hello W'],
      ['A. int', 'B. float', 'C. str', 'D. None'],
      ['A. 3', 'B. 4', 'C. 5', 'D. -1'],
      ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
      ['A. PYTHON', 'B. Python', 'C. PyThOn', 'D. PYTHon'],
      ['A. 64', 'B. 512', 'C. 9', 'D. 81'],
      ['A. Hello World', 'B. HelloWorld', 'C. Hello World ', 'D. Hello World!'],
      ['A. [2, 4, 6, 8, 10]', 'B. [2, 4, 6, 8]', 'C. [1, 3, 5, 7, 9]', 'D. [1, 2, 3, 4, 5]'],
      ['A. True', 'B. False', 'C. None', 'D. Error']]

   answers = ['C', 'C', 'B', 'B', 'D', 'B', 'B', 'D', 'A', 'A']

   calculateResult = 0
   startTime = time.time()

   for i in range(len(questions)):
      print("\n" + questions[i])
      userChoice = correctChoice(choices[i])
      if userChoice == answers[i]:
         calculateResult += 1
      endTime = time.time()
      timeElapsed = endTime - startTime

      print(f"\nYou scored {calculateResult} out of {len(questions)}")
      print(f"Time elapsed: {int(timeElapsed)} seconds")   
   return calculateResult;




# Define average level questions and answers
def averageLevel():
   print("\nAverage Level\n")
   questions = {
      1: "1. What is the output of the following code?\nprint('Python'.replace('o', 'a'))",
      2: "2. What is the output of the following code?\nprint(' '.join(['Python', 'is', 'awesome']))",
      3: "3. What is the output of the following code?\nprint(any([True, False, False]))",
      4: "4. What is the output of the following code?\nprint(list(range(1, 10, 2))))",
      5: "5. What is the output of the following code?\na = [1, 2, 3]\nb = a\nc = b\nprint(a is c)",
      6: "6. What is the output of the following code?\nprint(len([0, 1, 2] * 3))",
      7: "7. What is the output of the following code?\nprint('hello'.capitalize() + 'world'.upper())",
      8: "8. What is the output of the following code?\nprint(5 + 6 + '7')",
      9: "9. What is the output of the following code?\nprint('hello'.replace('l', 'L', 1))",
      10: "10. What is the output of the following code?\nprint(1 and 0)" }

   choices = {
      1: "a) Pythan, b) Python, c) Pythaa, d) None of the above", 
      2: "a) Python is awesome, b) Python isawesome, c) Pythonisawesome, d) None of the above",
      3: "a) True, b) False, c) Syntax Error, d) None of the above",
      4: "a) [1, 3, 5, 7, 9], b) [1, 2, 3, 4, 5], c) [0, 2, 4, 6, 8], d) Syntax Error",
      5: "a) True, b) False, c) Syntax Error, d) None of the above",
      6: "a) 6, b) 9, c) 3, d) None of the above",
      7: "a) HELLOWORLD, b) HelloWorld, c) Hello World, d) None of the above",
      8: "a) 567, b) 18, c) TypeError, d) None of the above",
      9: "a) heLLo, b) heLlo, c) hLLo, d) None of the above",
      10: "a) 0, b) 1, c) True, d) False"
        }

   answers = {1: "b", 2: "a", 3: "a", 4: "a", 5: "a", 6: "b", 7: "b", 8: "c", 9: "a", 10: "b"}

   calculateResult1 = 0
   startTime = time.time()

   for x in questions:
      print("\n" +questions[x])
      userChoice = correctChoice1(choices[x])
      if userChoice == answers[x]:
         calculateResult1 += 1
      endTime = time.time()
      timeElapsed = endTime - startTime

      print(f"\nYou scored {calculateResult1} out of {len(questions)}")
      print(f"Time elapsed: {int(timeElapsed)} seconds")

   return calculateResult1;

# Define hard level questions and answers
def hardLevel():
  print("\nHard Level\n")
  questions = {1: "1. What is the output of the following code?\nprint('Hello, World!'.split(','))",
        2: "2. What is the output of the following code?\nprint('Hello, World!'.find('o'))",
        3: "3. What is the output of the following code?\nprint('Hello, World!'.replace('l', 'L', 1))",
        4: "4. What is the output of the following code?\nprint('Hello, World!'.upper().replace('O', 'X'))",
        5: "5. What is the output of the following code?\nprint([x*2 for x in range(5) if x%2==0])",
        6: "6. What is the output of the following code?\nprint(any([True, False, False]))",
        7: "7. What is the output of the following code?\nprint(list(range(1, 10, 2)))",
        8: "8. What is the output of the following code?\nprint('Hello, World!'[::-1])",
        9: "9. What is the output of the following code?\nprint(10//3)",
        10: "10. What is the output of the following code?\nprint(not True and False)"}

  choices = {
        1: "a) ['Hello', ' World!'], b) ['Hello,', ' World!'], c) 'Hello, World!', d) None of the above",
        2: "a) 4, b) 7, c) -1, d) None of the above",
        3: "a) 'HeLlo, World!', b) 'HeLLo, World!', c) 'Hello, World!', d) None of the above",
        4: "a) 'HELLX, WXRLD!', b) 'HELLO, WORLD!', c) 'HELLO, WXRLD!', d) None of the above",
        5: "a) [0, 4, 8], b) [0, 2, 4, 6, 8], c) [2, 4, 6, 8, 10], d) None of the above",
        6: "a) True, b) False, c) Syntax Error, d) None of the above",
        7: "a) [1, 3, 5, 7, 9], b) [1, 2, 3, 4, 5], c) [0, 2, 4, 6, 8], d) Syntax Error",
        8: "a) '!dlroW ,olleH', b) 'dlroW ,olleH', c) 'Hello, World!', d) None of the above",
        9: "a) 3, b) 3.0, c) 3.3333, d) None of the above",
        10: "a) True, b) False, c) Syntax Error, d) None of the above"}

  answers = {1: "b", 2: "b", 3: "b", 4: "a", 5: "a", 6: "a", 7: "a", 8: "d", 9: "c", 10: "c"}

  calculateResult2 = 0
  startTime = time.time()

  for x in questions:
     print("\n" + questions[x])
     userChoice = correctChoice1(choices[x])
     if userChoice == answers[x]:
        calculateResult2 += 1
     endTime = time.time()
     timeElapsed = endTime - startTime

     print(f"\nYou scored {calculateResult2} out of {len(questions)}")
     print(f"Time elapsed: {int(timeElapsed)} seconds")        
  return calculateResult2;


def main():
    quizDate = datetime.datetime.now()
    print("\nDate and Time: ",quizDate, "\n")
    # Quiz description
    print('''        Welcome to Python Quiz Application!
        This application will test your knowledge of Python programming.
        You will be asked a series of multiple choice questions at three different levels:
        Easy, Average, and Hard.
        Your task is to choose the correct answer from the options provided.
        There is no negative marking for wrong answers.
        good Luck! ''')

    # Ask player name
    playerName = input("\nPlease enter your name: ").upper()

    print("=========================")
    print(f"Player Name:{playerName}")
    print("=========================")


    # Ask for level choice and call corresponding function
    
    calculateResult = 0
    calculateResult1 = 0 
    calculateResult2 = 0   
    play = True
    while play:
        levelChoice = input("Choose your level: Easy (E), Average (A), or Hard (H): ").upper()

        if levelChoice == 'E':
            calculateResult += easyLevel()

        if levelChoice == 'A':
            calculateResult1 += averageLevel()

        if levelChoice == 'H':
            calculateResult2 += hardLevel()

            
            
        while True:   
            again = input("\nDo you want to play again, type Y or any other letter to: ").upper()
            if again == "Y":
                break
                
            if again != "Y":
                print(f"calculateResult Easy Level: {calculateResult}")
                print(f"calculateResult Average Level: {calculateResult1}")
                print(f"calculateResult Hard Level: {calculateResult2}")
                print("***GoodBye***")
                play = False

                return
     
main()
