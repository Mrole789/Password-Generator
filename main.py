import random

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","U","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums = ["0","1","2","3","4","5","6","7","8","9"]
syms = ["!","#","$","%","&","(",")","*","+"]

print("""
 ____                                     _    
|  _ \ __ _ ___ _____      _____  _ __ __| |   
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |   
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |   
|_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|   
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
""")
cl = int(input("How many letters do you want in your password?\n"))
cn = int(input("How many numbers do you want in your password?\n"))
cs = int(input("How many symbols do you want in your password?\n"))

p = []
for x in range(1, (cl + 1)):
    a = random.choice(letters)
    p.append(a)

for y in range(1, (cn + 1)):
    b = random.choice(nums)
    p.append(b)

for z in range(1, (cs + 1)):
    c = random.choice(syms)
    p.append(c)

fp = " "
for a in range(1, (len(p) + 1)):
    b = random.choice(p)
    fp += b
    p.remove(b)

print(fp)