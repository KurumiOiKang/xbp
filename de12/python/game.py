import random
import time

mark = ["spead","heart","diamond","club"]


print("ブラックジャックへようこそ")


print("ゲームの説明を聞く"）
if players=YES
print("【遊び方】")
print("21点を超えずに合計点が21に近い人が勝ちです。同じ点数の場合は引き分けです。")
print("ヒット＝カードを追加する")
print("スタンド＝カードを追加しない")
print("自分のターンが終わったら次の人に変わりましょう")

else:
   print("さあ、ゲーム会場に移りましょう")　
   
class Deck:
    def__init__(self):
       self.cards = [
           [i,j]
           for i in range(1,14)
           for j in mark
           ]
      random.shuffle(self.cards)
    def emission(self):
        emission_card = self.cards.pop()
        return emission_card

 # deck = Deck()
 # print(len(desk.cards))
 # print(deck.cards)     

 def str_point(card):
     if card[0] > 10:
        return 10
     elif card[0] == 1:
        return 11
     else:
        return card[0]

def count_card(cards):
    point = [str_point(i) for i in cards]
    cnt = point.count(11)
    card=sum = sum(point)
    for i in range(cnt):
        if card_sum > 21:
           card_sum -= 10
    return card_sum   


class player():
    def __init__(self):
        global deck

        self.cards = []
        card1 = deck.emission()
        self.cards.append(card1)
        card2 = desk.emission()
        self.cards.append(card2)

    def card_open(self):
        print("PL:self.cards")

    def point_open(self):
        print("PL:",count_card(self.cards))

    def draw(self):
        card = deck.emission()
        self.cards.append(card)

class Deerer(Player):
    def card_open(self):
            print("DR:",self.cards)

    def point_open(self):
        print("DR:",count_card(self.cards))

    def card_close(self):
        print("DL:",self.cards[0],"[*,*]")

    def point_close(self):
        print("DL:",str_point(self.cards[0]))

def game(desk):

   player = Player()
   player.card_open()
   player.point_open()

   deerer = Deerer()
   deerer.card_close()
   deerer.point_close()

   select = 0
  
   while count_card(player.cards) <= 21:
       time.sleep(1)

       if count_card(player.cards) == 21:
           print("BJ")
         　 return 1

       select = input("ヒットするYES:1...")

       if select == 1:
          player.draw()
          player.card_open()
          player.point_open() 
       else:
           break
   else:
       print("BERST")
       return 0

   time.sleep(1)
   deerer.card_open()
   time.sleep(1)
   deerer.point_open()

   while count_card(deerer.cards) < 16:
       time.sleep(1)
       deerer.draw()

       time.sleep(1)
       deerer.card_open()

       time.sleep(1)
       deerer.point_open()

       if count_card(deerer.cards) > 21:
           print("BJ")
           return 1
   time.sleep(1)

   if count_card(deerer.cards) < count_card(player.cards)
       return 1 
   elif count_card(player.cards) < count_card(deerer.cards):
       return 0
   else:
       return -1
                
start = 1
win_lose=[0,0]

deck = Deck()

while len(deck.cards) > 10:
    start = input("ゲームを始めましょう！YES1...")
    if start != 1:
       print("終了しました")
       break
    print("ゲームを始めます")

    rslt = game(deck)
    if rslt== 1:
      win_lose[0] += 1
      print("winner")
      print(win_lose[0],"勝",win_lose[1],"敗")
    elif rslt ==0: 
         win_lose[1] +=1
         print("YOU　LOSE")
         print(win_lose[0]"勝",win_lose[1],"敗")
    else:
       print("DRAW")
       print(win_lose[0],"勝",win_lose[1],"敗")
else:
     print("カードが無くなりました")

   



          
            
                    
                  

          








    








