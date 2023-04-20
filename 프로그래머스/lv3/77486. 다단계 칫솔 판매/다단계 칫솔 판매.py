import math

class Member:

    parent = None
    money = 0

    def __init__(self, name):
        self.name = name

    def getParent(self):
        return self.parent

    def getMoney(self):
        return self.money

def moneyDistribution(memberDict, name, money):
    MyParent = memberDict[name].parent
    if MyParent == "-":
        if money * 0.1 < 1:
            temp = 0
        else:
            temp = math.floor(money * 0.1)
        memberDict[name].money += money - temp
    else:
        while(True):
            if money == 0:
                break
            if money * 0.1 < 1:
                temp = 0
            else:
                temp = math.floor(money * 0.1)
            memberDict[name].money += money - temp
            if MyParent == "-":
                break
            money = temp
            name = memberDict[name].parent
            MyParent = memberDict[name].parent

def solution(enroll, referral, seller, amount):
    answer = []
    member_dict = {}

    for i in range(len(enroll)):
        new_member = Member(enroll[i])          # 클래스 생성
        new_member.parent = referral[i]         # 부모 설정
        member_dict[enroll[i]] = new_member


    for i in range(len(seller)):
        moneyDistribution(member_dict, seller[i], amount[i]*100)

    for i in range(len(enroll)):
        answer.append(member_dict[enroll[i]].money)

    return answer