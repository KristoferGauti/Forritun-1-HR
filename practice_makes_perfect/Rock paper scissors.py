#rock paper scissors
import random

listi = ["rock","paper","scissors"]

score1 = 0
score2 = 0

player2 = str(input("press 1 for rock, 2 for paper or 3 for scissors "))

while player2 == "1" or player2 == "2" or player2 == "3":
    player1 = random.choice(listi)
    if (player1 == "rock" and player2 == "1") or (player1 == "paper" and player2 == "2") or (player1 == "scissors" and player2 == "3"):
        print("it is tie")
        print(player1,player2)
        score1 += 0
        score2 += 0
        print(score1,":",score2)
        
    elif player1 == "rock" and player2 == "3":
        print("Player 1 gets the point")
        print(player1,player2)
        score1 += 1
        score2 += 0
        print(score1,":",score2)
    elif player1 == "paper" and player2 == "1":
        print("player 1 gets the point")
        print(player1,player2)
        score1 += 1
        score2 += 0
        print(score1,":",score2)
    elif player1 == "scissors" and player2 == "2":
        print("player 1 gets the point")
        print(player1,player2)
        score1 += 1
        score2 += 0
        print(score1,":",score2)

    elif player1 == "rock" and player2 == "2":
        print("Player 2 gets the point")
        print(player1,player2)
        score1 += 0
        score2 += 1
        print(score1,":",score2)
    elif player1 == "paper" and player2 == "3":
        print("player 2 gets the point")
        print(player1,player2)
        score1 += 0
        score2 += 1
        print(score1,":",score2)
    elif player1 == "scissors" and player2 == "1":
        print("player 2 gets the point")
        print(player1,player2)
        score1 += 0
        score2 += 1
        print(score1,":",score2)
        
    elif player2 == "scissors" and player1 == "2":
        print("player 2 gets the point")
        print(player1,player2)
        score1 += 0
        score2 += 1
        print(score1,":",score2)
    elif player2 == "paper" and player1 == "1":
        print("player 2 gets the point")
        print(player1,player2)
        score1 += 0
        score2 += 1
        print(score1,":",score2)
    elif player2 == "rock" and player1 == "3":
        print("player 2 gets the point")
        print(player1,player2)
        score1 += 0
        score2 += 1
        print(score1,":",score2)
        
    
    player2 = str(input("press 1 for rock, 2 for paper or 3 for scissors: "))
