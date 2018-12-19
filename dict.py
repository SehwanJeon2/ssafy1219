"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
score = 0
count = 0
for i in iu_score:
    score = score + iu_score[i]
    count = count+1

score=score/count
print(score)


#Teacher Answer
#iu_score라고 하는 dic 변수에서 value 값만 뽑아내보자.
total_score=0
count=0
#뽑아낸 값들의 총 합을 구한다
for score in iu_score:
    print(iu_score[score])
    total_score = total_score + iu_score[score]
    count=count+1
print(total_score/count)

#scores = list(iu_score.values())
#print(sum(scores)/len(scores)) 이용하는 방법도 있다.


#------------------------------------------------------------------------------
# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")

val=0
count=0
for key in score:
  print(key)
  for sub in score[key]:
    print(sub)
    val=val+score[key][sub]
    count=count+1

val=val/count
print(val)

#Teacher Answer
# 각 반을 순회하는 반복문을 작성한다
for cl in score:
    print(score[cl])
# 한 번 순회를 할 때 1번에서 작성한 코드를 활용한다.
    tmp = list(score[cl].values)
# 출력한다.
    print("{}: {}".format(cl, sum(tmp)/len(tmp)))


#------------------------------------------------------------------------------
# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")

totaltemp=0
count=0
for name in city:
  for tem in city[name]:
    totaltemp=totaltemp+tem
    count=count+1
  print(name,":", totaltemp/count)
  totaltemp=0
  count=0


#Teacher Answer
# 각 도시를 순회하는 반복문을 작성한다.
for ci in city:
    print(city[ci])
    temp = city[ci]
# 순회할 때마다 평균 값을 출력한다.
    print("{}의 평균기온: {}".format(city, round(sum(temp)/len(temp), 1)))
    print("{}의 평균기온: {:.1}".format(city, sum(temp)/len(temp)))
# python get round value (소수가 너무 길어서 반올림 찾아보자)
# 일단 2가지 찾았다. 


#------------------------------------------------------------------------------
# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")

for name in city:
  city[name].sort()
print(city)
coldcity=""
mintemp=300
for name in city:
  if(mintemp>city[name][0]):
    mintemp=city[name][0]
    coldcity=name
print("coldest city: ",coldcity)


for name in city:
  city[name].reverse()
print(city)
hotcity=""
maxtemp=-255
for name in city:
  if(maxtemp<city[name][0]):
    maxtemp=city[name][0]
    hotcity=name
print("hottest city: ",hotcity)


#Teacher Answer
# 최저기온, 최고기온을 저장할 수 있는 변수를 선언한다. (반복문 밖에서 선언한다)
minimum = ["도시명", 1000]
maximum = ["도시명", -1000]
#
# 각 도시를 순회하는 반복문을 만든다.
for ci in city:
# 각 도시의 기온 정보를 순회하는 반보문을 만든다.
    for temp in city[ci]:
# 순회하다가 최저기온의 경우에는 현재 저장된 값보다 작은값이,
# 최고 기온의 경우에는 현재 저장된 값보다 큰 값이 있는 경우
# 현재 저장되어 있는 값을 바꾼다.
    #최저기온에 해당하는 조건문
        if(maximum[1] < temp):
            maximum[0] = city
            maximum[1] = temp
    #최고기온에 해당하는 조건문
        if(minimum[1] > temp):
            minimum[0] = city
            minimum[1] = temp
print("최고 기온은 {}의 {}도이며, 최저 기온은 {}의 {}도 입니다.".format(maximum[0], maximum[1], minimum[0], minimum[1]))




#------------------------------------------------------------------------------
# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")

seoultemp = False
for tem in city['서울']:
  if(city['서울']==2):
    seoultemp = True
if(seoultemp):
  print("Yes Seoul had 2'C")
else:
  print("No Seould hadn't 2'C")


#Finish