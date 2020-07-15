# Programmer: Christine Doan
# Prompt: Create a driver's license exam with 20 multiple choice.

# Starting screen

# function stores the answers in a file
def storeAnswers(file, answers):
    writtenAnswerf = open(file, 'w')
    allQs = len(answers)

    for CurrentIndex in range (allQs):
        writeAnswer = input('What is your answer for question ' + str((CurrentIndex + 1)) + '? ')
        writtenAnswerf.write(writeAnswer + '\n')

    writtenAnswerf.close()

def readAnswers(file):
    writtenAnswerList = []
    writtenAnswerf = open(file, 'r')

    for writtenAnswer in writtenAnswerf:
        writtenAnswerList.append(writtenAnswer)

    return writtenAnswerList
# function will check for correct answers
def checkAnswers (correctAnswersList, studentCorrAnswersList):
    correctAnswers = 0
    allQs = len(correctAnswersList)

    for CurrentIndex in range(allQs):
        if studentCorrAnswersList[CurrentIndex] == correctAnswersList[CurrentIndex]:
            correctAnswers += 1
            return correctAnswers
        
def checkIncorrectAnswer(numbersofCorrect, numbersofQuestion):
    numbersofIncorrect = numbersofQuestion - numbersofCorrect
    return numbersofIncorrect

def getIncorrectNumbers(correctAnswersList, studentCorrAnswersList):
    incorrectNumbersList = []
    numberQuestions = len(correctAnswersList)

    for CurrentIndex in range (numberQuestions):
        if studentCorrAnswersList[CurrentIndex] != correctAnswersList[CurrentIndex]:
            incorrectNumbersList.append(CurrentIndex + 1)
    return incorrectNumbersList

def passExam(passing, studentCorrAnswersList):
    if len(studentCorrAnswersList) >= passing:
        return True
    else:
        return False

def printValues(anylist):
    for currentValueIndex in range (len(anylist)):
        print(anylist[currentValueIndex])

def results(numbersCorrect, numbersIncorrect, incorrectNumbersList):
    print('You got' + str(numbersCorrect), '\n', 'And you got wrong' + str(numbersIncorrect))


def main():
    correctAnswersList = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 
    'A', 'C', 'B', 'A', 'D', 'C', 
    'A', 'D', 'C', 'B', 'B', 'D', 'A']

    numberQs = len(correctAnswersList)
    filename = 'answers.txt'
    passreq = 15

    storeAnswers(filename, correctAnswersList)
    studentAnswersList = readAnswers(filename)

    correctAnswers = checkAnswers(correctAnswersList, studentAnswersList)

    # incorrectAnswers = checkIncorrectAnswer(correctAnswers, numberQs)
    #       type error with int and nonetype. 

   # incorrectList = getIncorrectNumbers(correctAnswersList, studentAnswersList)

   # results(correctAnswers, incorrectAnswers, incorrectList)

    if passExam(passreq, studentAnswersList):
        print('You have passed the exam. Check answers.txt for you list of answers.')
    else:
        print('You have not passed. Try again.')

main()