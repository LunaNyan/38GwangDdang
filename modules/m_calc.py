import random

def make_deck():
    # 섯다를 플레이할 수 있는 모든 화투 20개를 만들어 셔플한 후, 리스트로 산출합니다.
    # 각 패는 [월수, 끗수]로 이루어져 있습니다.
    # 끗수 설명
    # - 0 : 기타
    # - 1 : 광
    # - 2 : 열끗
    # 주의사항 : 11월(똥), 12월, 조커는 섯다에서 사용할 수 없으므로, 생성되지 않습니다.
    deck = []
    m = 0
    while m < 4:
        n = 0
        while n < 10:
            if (n == 0 or n == 2 or n == 7) and m == 0:
                deck.append([n+1, 1])
            elif m == 3:
                if n == 0 or n == 2:
                    deck.append([n+1, 0])
                else:
                    deck.append([n+1, 2])
            else:
                deck.append([n+1, 0])
            n += 1
        m += 1
    random.shuffle(deck)
    return deck

def select_deck(deck):
    # 주어진 패 목록에서 랜덤한 패 2장을 뽑고 리스트에서 삭제합니다.
    decka_ind = random.randint(0, len(deck)-1)
    decka_val = deck[decka_ind]
    del deck[decka_ind]
    deckb_ind = random.randint(0, len(deck)-1)
    deckb_val = deck[deckb_ind]
    del deck[deckb_ind]
    return [decka_val, deckb_val]

def judge(a, b):
    # [월수, 끗수]로 된 두 패를 받아 조합 결과를 산출합니다.
    # 끗수 설명
    # - 0 : 기타
    # - 1 : 광
    # - 2 : 열끗
    if ((a[0] == 3 and b[0] == 8) or (a[0] == 8 and b[0] == 3)) and a[1] == 1 and b[1] == 1: #광땡
        sd_power_text = "3 - 8 광땡!"
        sd_power = 28
    elif ((a[0] == 1 and b[0] == 8) or (a[0] == 8 and b[0] == 1)) and a[1] == 1 and b[1] == 1:
        sd_power_text = "1 - 8 광땡!"
        sd_power = 27
    elif ((a[0] == 1 and b[0] == 3) or (a[0] == 3 and b[0] == 1)) and a[1] == 1 and b[1] == 1:
        sd_power_text = "1 - 3 광땡!"
        sd_power = 26
    elif (a[0] == 9 and b[0] == 4) or (a[0] == 4 and b[0] == 9): #특수족보
        if a[1] == 2 and b[1] == 2:
            sd_power_text = "멍텅구리구사"
            sd_power = -1
        else:
            sd_power_text = "구사"
            sd_power = -2
    elif (a[0] == 7 and b[0] == 4) or (a[0] == 4 and b[0] == 7) and a[1] == 2 and b[1] == 2:
        sd_power_text = "7 - 4 암행어사"
        sd_power = -3
    elif (a[0] == 7 and b[0] == 3 and a[1] == 2 and b[1] == 1) or (a[0] == 3 and b[0] == 7 and a[1] == 1 and b[1] == 2):
        sd_power_text = "7 - 3 땡잡이"
        sd_power = -4
    elif a[0] == b[0]: #땡
        if a[0] == 10:
            sd_power_text = "장땡"
        elif a[0] == 9:
            sd_power_text = "구땡"
        elif a[0] == 8:
            sd_power_text = "팔땡"
        elif a[0] == 7:
            sd_power_text = "칠땡"
        elif a[0] == 6:
            sd_power_text = "육땡"
        elif a[0] == 5:
            sd_power_text = "오땡"
        elif a[0] == 4:
            sd_power_text = "사땡"
        elif a[0] == 3:
            sd_power_text = "삼땡"
        elif a[0] == 2:
            sd_power_text = "이땡"
        elif a[0] == 1:
            sd_power_text = "일땡"
        sd_power = 15 + a[0]
    elif (a[0] == 1 and b[0] == 2) or (a[0] == 2 and b[0] == 1): #삥
        sd_power_text = "알리"
        sd_power = 15
    elif (a[0] == 1 and b[0] == 4) or (a[0] == 4 and b[0] == 1):
        sd_power_text = "독사"
        sd_power = 14
    elif (a[0] == 1 and b[0] == 9) or (a[0] == 9 and b[0] == 1):
        sd_power_text = "구삥"
        sd_power = 13
    elif (a[0] == 1 and b[0] == 10) or (a[0] == 10 and b[0] == 1):
        sd_power_text = "장삥"
        sd_power = 12
    elif (a[0] == 4 and b[0] == 10) or (a[0] == 10 and b[0] == 4):
        sd_power_text = "장사"
        sd_power = 11
    elif (a[0] == 4 and b[0] == 6) or (a[0] == 6 and b[0] == 4):
        sd_power_text = "세륙"
        sd_power = 10
    else: #끗
        xcuta = str(a[0] + b[0])[-1]
        xcut = int(xcuta)
        # 주의사항
        # - 두 패의 월 조합이 10인 경우, 끗수가 0이므로 망통으로 처리됩니다.
        if xcut == 9:
            sd_power_text = "갑오"
        elif xcut == 8:
            sd_power_text = "여덟끗"
        elif xcut == 7:
            sd_power_text = "일곱끗"
        elif xcut == 6:
            sd_power_text = "여섯끗"
        elif xcut == 5:
            sd_power_text = "다섯끗"
        elif xcut == 4:
            sd_power_text = "네끗"
        elif xcut == 3:
            sd_power_text = "세끗"
        elif xcut == 2:
            sd_power_text = "두끗"
        elif xcut == 1:
            sd_power_text = "한끗"
        elif xcut == 0:
            sd_power_text = "망통"
        sd_power = xcut
    return [sd_power, sd_power_text]

def interpret_card(card):
    if card[1] == 0:
        card_type = ""
    elif card[1] == 1:
        card_type = " 광"
    elif card[1] == 2:
        card_type = " 열끗"
    return str(card[0]) + "월" + card_type

