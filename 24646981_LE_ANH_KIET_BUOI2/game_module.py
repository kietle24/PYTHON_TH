# game_module.py
import random

def play_game():
    secret = random.randint(1, 10)
    print("Bạn có 3 lượt đoán số từ 1 đến 10.")
    for i in range(3):
        try:
            guess = int(input(f"Lần đoán {i+1}: "))
            if guess == secret:
                print("Bạn đoán đúng!")
                return "Thắng"
        except ValueError:
            print("Nhập sai định dạng! Hãy nhập số nguyên.")
    print(f"Bạn đã thua. Số đúng là {secret}.")
    return "Thua"
