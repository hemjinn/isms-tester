from data import data, questions, choice
import random

print('''
+---------------------------------------------------------+
isms 통제항목 자동 출제 프로그램 입니다.

문제를 보고 항목 번호와 명칭을 입력하면 됩니다.
ex) "항목 번호를 입력하세요: 1.1.1"
    "항목 명을 입력하세요: 경영진의 참여"
      
종료는 exit 또는 ctrl+c를 눌러주세요.
+---------------------------------------------------------+    

''')

while True:
    questionNum = random.choice(choice) # 랜덤으로 항목 번호 뽑기
    question = random.choice(questions[questionNum]) # 랜덤으로 문제 뽑기
    questionName = data[questionNum]

    print("================================================================================================================")
    print(question)
    print("================================================================================================================")
    guessNum = input("항목 번호를 입력하세요: ")
    if (guessNum == "exit"):
        break
    guessName = input("항목 명을 입력하세요: ")

    if (guessName == "exit"):
        break
    else:
        if (guessNum == questionNum and guessName == questionName):
            print("정답입니다~ 😊")
        else: 
            print("삐빅- 오답입니다~ 🤣")
            print(f"정답은 {questionNum} {questionName}")
