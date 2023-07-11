import random

alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]

for _ in range(len(alphabet)):
    letter = random.choice(alphabet)
    print(letter)

    if letter in ["K", "I", "Y", "U", "N", "A"]:
        break
