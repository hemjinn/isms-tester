from data import data, questions, choice
import random

print('''
+-----------------------------------------------------------+
|        isms 통제항목 자동 출제 프로그램 입니다.           |
|                                                           |
|        문제를 보고 항목 번호와 명칭을 입력하면 됩니다.    |
|        ex) "항목 번호를 입력하세요: 1.1.1"                |
|            "항목 명을 입력하세요: 경영진의참여"           |
|                                                           |
|        주의) 띄어쓰기 사용금지                            |
|        종료는 exit 또는 ctrl+c를 눌러주세요.              |
|                                                           |
|                                                           |
|*작성자: 박현진, 고혜원                                    |
+-----------------------------------------------------------+

''')

i=1

while True:
    questionNum = random.choice(choice) # 랜덤으로 항목 번호 뽑기
    question = random.choice(questions[questionNum]) # 랜덤으로 문제 뽑기
    questionName = data[questionNum]


    print("================================================================================================================")
    print(f"{i}. {question}")
    print("================================================================================================================")
    guessNum = input("항목 번호를 입력하세요: ")
    if (guessNum == "exit"):
        break
    guessName = input("항목 명을 입력하세요: ")

    if (guessName == "exit"):
        break
    else:
        if (guessNum == questionNum and guessName == questionName):
            print("\n정답입니다~ :)\n")
        else: 
            print("\n삐빅- 오답입니다~ XD")
            print(f"정답은 {questionNum} {questionName}\n")
    i+=1
