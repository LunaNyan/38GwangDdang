# !! 완성되지 않음 !!
raise NotImplementedError
# 완성 시 위 범위 내 코드 제거바람

# 필요한 것
# - game 클래스 내 콜 비용 변수 필요

def half(me, game): # 하프
    if (me.money / 2) <= (game.stake / 2): # 올인
        game.stake += me.money
        me.money = 0
    else: #일반 하프
        game.stake += game.stake / 2
        me.money -= game.stake / 2

def quarter(me, game): # 쿼터
    if (me.money / 4) <= (game.stake / 4): # 올인
        game.stake += me.money
        me.money = 0
    else: # 일반 쿼터
        game.stake += game.stake / 4
        me.money -= game.stake / 4

def double(me, prev, game): # 따당
    if me.money < prev.money * 2: # 올인
        game.stake += me.money
        me.money = 0
    else:
        prev.money 

def call(me, prev, game): # 콜
    if me.money < prev.money: # 올인
        game.stake += me.money
        me.money = 0
    else:
        
def small(me, game): # 삥

def check(me, game): # 체크

def die(me, game): # 다이
    me.dead = True