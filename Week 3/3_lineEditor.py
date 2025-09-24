from ArrayList import ArrayList

# 라인 편집기용 ArrayList 생성
list = ArrayList(100)

while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, q-종료=> ")

    if command == "i":  # 삽입
        pos = int(input(" 입력행 번호: "))
        line = input(" 입력행 내용: ")
        list.insert(pos, line)

    elif command == "d":  # 삭제
        pos = int(input(" 삭제행 번호: "))
        list.delete(pos)

    elif command == "r":  # 변경
        pos = int(input(" 변경행 번호: "))
        line = input(" 새 내용: ")
        list.replace(pos, line)

    elif command == "p":  # 출력
        print("Line Editor")
        for i in range(list.size):
            print(f"[{i}] {list.getEntry(i)}")

    elif command == "q":  # 종료
        print("프로그램을 종료합니다.")
        break

    else:
        print("알 수 없는 명령입니다.")
