# 가위 바위 보 게임 미니 프로젝트

print("=" * 30)
print("가위바위보 게임")
print("=" * 30)

import random

# 가위, 바위, 보 (1. 가위, 2. 바위, 3. 보)
choices = {1: "가위", 2: "바위", 3: "보"}

# 점수 초기화
my_score = 0
computer_score = 0

while True:
    print("1. 가위", "2. 바위", "3. 보")
    try:
        user_input = int(input("번호를 선택하세요. : "))
        if user_input not in choices:
            print("1, 2, 3 중에서 선택하세요.\n")
            continue
    except ValueError:
        print("숫자를 입력하세요.\n")
        continue

    # 내거랑 컴퓨터의 가위 바위 보 선택
    me = choices[user_input]
    computer = choices[random.randint(1, 3)]

    # 승패 판정
    if me == computer:
        result = "비김"
    elif (
        (me == "가위" and computer == "보")
        or (me == "바위" and computer == "가위")
        or (me == "보" and computer == "바위")
    ):
        result = "승리"
        my_score += 1
    else:
        result = "패배"
        computer_score += 1

    # 결과 출력
    print("\n[게임 결과]")
    print(f"나: {me} vs 컴퓨터: {computer}")
    print(f" => 승리 / 패배 / 비김 -> {result}")
    print(f"\n현재 스코어 나 {my_score} : {computer_score} 컴퓨터\n")

    # 다시 도전
    retry = input("다시 도전 (yes/no) : ").strip().lower()
    print() 

    if retry != "y":
        print("게임을 다시 시작 합니다")

    if retry == "n":
        print("게임을 종료합니다.")
        break