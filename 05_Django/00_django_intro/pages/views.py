from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
# view 함수 -> 중간 관리자
# 사용자가 접속해서 볼 페이지를 작성한다. 즉, 하나하나의 페이지를 'view'라고 부른다.
# 'view' 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다.

def index(request): # 첫번째 인자 반드시 request!
    return render(request, 'index.html')    # 첫 번째 인자를 반드시 request!

def introduce(request):
    name = '감자'
    
    # render 메서드의 세번째 인자로 변수를 딕셔너리 형태로 넘길 수 있다.
    return render(request, 'introduce.html', {'name': name})

def dinner(request):
    menu = ['진라면','신라면','너구리','짜파게티']
    pick = random.choice(menu)
    context = {
        'pick': pick
    }

    return render(request, 'dinner.html', context)

# Lorem Picsum 사용해서 랜덤 이미지 보여주는 페이지 만들기!
# 추가 실습 : 크기도 동적으로 받기
def image(request, weight, height):
    number = random.randint(1,1000)
    context = {
        'weight': weight,
        'height': height,
        'number': number
    }
    return render(request, 'image.html', context)

# 동적 라우팅
def hello(request, name):
    menu = ['진라면','신라면','너구리','짜파게티']
    pick = random.choice(menu)
    context = {
        'name': name,
        'pick': pick
    }
    return render(request, 'hello.html', context)

# 실습1 : 템플릿 변수를 2개 이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해보자.
def introduce2(request):
    name = '감자'
    age = '26'
    interest = '축구보기'
    speciality = '공부'
    context = {
        'name': name,
        'age': age,
        'interest': interest,
        'speciality': speciality
    }
    return render(request, 'introduce2.html', context)

# 실습 2 : 숫자 2개를 동적 라우팅으로 전달 받아서, 두 개의 숫자를 곱해주는 페이지를 만들자!
def times(request, number1, number2):
    mul = number1*number2
    context = {
        'number1': number1,
        'number2': number2,
        'mul': mul
    }
    return render(request, 'times.html', context)

# 실습 3 : 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자!
def area(request, radius):
    circle = radius*radius*3.141592
    context = {
        'radius': radius,
        'circle': circle
    }
    return render(request, 'area.html', context)

def template_language(request):
    menus = ['진라면','신라면','너구리','짜파게티']
    my_sentence = 'Life is short, you need python'
    messages = ['감자','고구마','호박','꽃']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow
    }
    return render(request, 'template_language.html', context)

# [실습1] ISIT YOUT BIRTH?
# 오늘 날짜와 본인 실제 생일 비교해서, 맞으면 예! 아니면 아이오!
def isbirth(request, month, day):
    today = datetime.now()
    todaymonth = today.month
    todayday = today.day
    context = {
        'today': today,
        'month': month,
        'day': day,
        'todaymonth': todaymonth,
        'todayday': todayday
    }
    return render(request, 'isbirth.html', context)

# [실습2] 회문 판별 (팰린드롬)
# ex) 오디오
def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False

    context = {
        'word': word,
        'result': result
    }
    return render(request, 'ispal.html', context)

# [실습3] 로또 번호 추첨
# 임의로 출력한 로또 번호와 가장 최근에 추첨한 로또 번호 비교해서 당첨 여부 확인
def lotto(request, n1, n2, n3, n4, n5, n6, n7):
    lotto = random.sample(range(1,46),6)
    lotto = sorted(lotto)
    # lotto.append(1)
    # lotto.append(6)
    # lotto.append(8)
    # lotto.append(25)
    # lotto.append(26)
    # lotto.append(35)
    mynum = []
    mynum2 = []
    mynum.append(n1)
    mynum.append(n2)
    mynum.append(n3)
    mynum.append(n4)
    mynum.append(n5)
    mynum.append(n6)
    mynum.append(n7)
    mynum2 = sorted(mynum)

    cnt = 0

    for i in range(0,7):
        for j in range(0,6):
            if mynum[i] == lotto[j]:
                cnt = cnt+1

    if cnt < 3:
        result = '꽝'
    elif cnt == 3:
        result = '5등 당첨'
    elif cnt == 4:
        result = '4등 당첨'
    elif cnt == 5:
        result = '3등 당첨'
    elif cnt == 6:
        if mynum[7] in lotto:
            result = '2등 당첨'
        else:
            result = '1등 당첨'

    context = {
        'lotto': lotto,
        'mynum2': mynum2,
        'cnt': cnt,
        'result': result
    }

    return render(request, 'lotto.html', context)
