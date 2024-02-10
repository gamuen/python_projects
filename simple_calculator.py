import math
# 제곱과 제곱근을 구하는 걸 만들어볼게요. 일단 입력할 정수 값을 받을 함수가 필요합니다. java 는 switch 와 scanner 이지만 파이썬은?

def calculator():
    print("---1. 밑은 원하는 양의 실수이고, 지수도 원하는 실수인 실수 값을 출력합니다.---")
    print("---2. 파이 값과 자연 상수 값을 출력합니다.---")
    print("---3. 밑이 1 이상, 진수는 1 이상으로 갖는 로그 함수의 치역 값을 출력합니다.---")
    print("---4. 삼각함수의 치역 값을 출력합니다.---")
    print("---5. 역삼각함수의 치역 값을 출력합니다.---")
    print("---6. 최고 3000차까지, 다항함수의 정적분 값을 출력합니다.---")
    print("---7. 최고 3000차까지, 다항함수의 미분 값을 출력합니다.---")

    x=int(input("위 7개의 메뉴 중에서 사용하기를 원하는 메뉴 값을 선택하세요."))

    if x==1:
        x1=float(input("계산하고 싶은 밑을 양의 실수로써 하나 기입하세요."))
        x2=float(input("밑 %s 에 대한 지수를 한 실수로써 하나 기입하세요."%(x1)))
        print(x1**x2)

    elif x==2:
        def fac(n):
            c=1
            for i in range(1,n+1):
                c*=i
            print(c)
        e=1
        for i in range(1,100):
            e+=1/fac(i)
        print("e:"+e)
    
    elif x==3:
            x1=float(input("로그 함수에 대입할 밑 값을 1 이상의 양의 실수로써 기입하세요."))
            x2=float(input("로그 함수의 %s 에 대해 대입할 진수 값을 1 이상의 양의 실수로써 기입하세요."%(x1)))
            print(math.log(x1,x2))


    elif x==4:
        x1=float(input("sin 함수에 대입할 정의역 값을 실수로써 기입하세요."))
        print(math.sin(x1))
        x2=float(input("cos 함수에 대입할 정의역 값을 실수로써 기입하세요."))
        print(math.cos(x2))
 
    
    elif x==5:
        x1=float(input("sin 함수의 역함수에 대입할 정의역 값을 -1 이상, 1 이하의 실수로써 기입하세요."))
        if x1>1 or x1<-1:
            print("기입한 실수 값은 sin 함수의 역함수에는 기입할 수 없습니다.")
        else:
            print(math.arcsin(x1))

        x2=float(input("cos 함수의 역함수에 대입할 정의역 값을 -1 이상, 1 이하의 실수로써 기입하세요."))
        if x2>1 or x2<-1:
            print("기입한 실수 값은 cos 함수의 역함수에는 기입할 수 없습니다.")
        else:
            print(math.arccos(x2))

    
    elif x==6:
        n=int(input("정적분하고 싶은 다항함수의 최고차 항의 지수 값을 입력하세요:"))
        if 1<=n<3001:
            x0=float(input(" 다항 함수에 대입할 정의역의 값을 입력하세요 : "))

            a=[]
            for i in range(0,n+1):
                c=float(input("%s 번째 다항의 계수를 입력하세요."%(i)))
                a.append(c)

            i1=0
            for i in range(0,n+1):
                i1+=(a[i]/(i+1))*(x0**(i+1))
            print(i1)

        else:
            print("3000보다 큰 최고차수 값을 가진 다항함수는 이 프로그램에서 계산하지 않습니다.")
    
    elif x==7:
        n=int(input("미분하고 싶은 다항함수의 최고차 항의 지수 값을 입력하세요:"))
        if 1<=n<3001:
            x0=float(input(" 다항 함수에 대입할 정의역의 값을 입력하세요 : "))

            a=[]
            for i in range(0,n+1):
                c=float(input("%s 번째 다항의 계수를 입력하세요."%(i)))
                a.append(c)

            i1=0
            for i in range(0,n+1):
                i1+=(a[i]/(i+1))*(x0**(i+1))
            print(i1)

        else:
            print("3000보다 큰 최고차수 값을 가진 다항함수는 이 프로그램에서 계산하지 않습니다.")

calculator()



