x = int(input("원하는 크리스마스 트리의 높이를 설정하세요!: "))

for i in range(1, x+1):
    for j in range(x+1-i):
        print(" " ,end = "")
    for j in range(2*i-1):
        print("*", end = "")
        # end를 사용하여 한줄에 여러 개의 값을 출력한다.
    print()
