print("*" * 59)
print("*" * 9, " Давай сыграем в игру крестики нолики ", "*" * 10)
print("*" * 59)

board = list(range(1,10))

def draw_board(board):  #Создаем тело игрового поля
   print("█" * 22, "-" * 13, "█" * 22) # █ данный символ реализован через сочетание alt+219
   for i in range(3):
      print("█" * 22, "|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|", "█" * 22)
      print("█" * 22, "-" * 13, "█" * 22)

def take_input(player_token): #создаем ввод для игроков и проверку ввода
   valid = False
   while not valid:
      player_answer = input("Куда поставим  " + player_token)
      try:
         player_answer = int(player_answer)
      except:
         print("Введен неверный символ")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Здесь есть значение")
      else:
        print("Неверный символ. Введите число от 1 до 9.")

def check_win(board): #проверка на выигрышь
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board): #запуск функций
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "УРА, Вы выиграли!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Давай сыграем еще разок!")