#v telegrame 30-01-25 19:15

def A(n): #uslovie delimosti dlya A
    return n % 11

def is_prime(n): # proverka prostoti ot 2 do kornya iz n
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def B(n): #uslovie dlya B
    if is_prime(n):
        return 1
    return -2

def C(n): #uslovie dlya C
    if n % 5 == 0:
        return 1
    return 0

def D(n): #uslovie dlya D
    if n // 100 > 0 and n // 1000 == 0:
        return 1
    return 0

def a(n): #uslovie dlya a
    if D(n) == 1 and C(n) == 0:
        return 2
    return 3

#primechanie: v 3 zadanii gogvoritsa, chto mi mozhem viigrat' maximalnoe kolichestvo monet
# hotya bi pri odnom znachenii x iz otrezka [1, 300]. Polzuemsya)))))))
#esli bi nelzya bilo, to oni bi ne sprashivali, tak kak 2 vopros podrazumevaet
# nahozhdeniye minimalnogo x.


minimal_x = 9999
coins_in_jackpot = 0
jackpot_amount = 0
for x in range(1, 301):
    curr_win = ((a(x) - B(x) + C(x)) * A(x))
    if coins_in_jackpot < curr_win: #formula iz nachala zadaniya
        coins_in_jackpot = curr_win

print("Question 1:", coins_in_jackpot)

for x in range(1, 301):
    curr_win = ((a(x) - B(x) + C(x)) * A(x))
    if curr_win == coins_in_jackpot:
        minimal_x = x
        break

print("Question 2:", minimal_x)

for x in range(1, 301):
    curr_win = ((a(x) - B(x) + C(x)) * A(x))
    if curr_win == coins_in_jackpot:
        jackpot_amount += 1

print("Question 3:", jackpot_amount/300, "what is equivalent to", (jackpot_amount/300)*100, "%")


print("& remember 2 things, kiddo:")
print()
print("1) U can only cash out yo winnings when u leave da table")
print("2) Casino always wins))")