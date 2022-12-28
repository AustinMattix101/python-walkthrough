# # Sequential Steps
# x = 1
# print(x)
# y = x + 1
# print(y)
# x = x + 5
# print(x)
# if x << 10 : print("Smaller than 10") # greater than
# if x >> 10 : print("Bigger than 10") # lesser than
# elif x != 5 : print("Neither equal 5") # neither
# print("Finish")
# # Repeated Steps
# n = 3
# while n > 0 :
#     print(n)
#     n = n - 1
# print("Blast off")

# while y > 0 :
#     print(y)
#     y = y + 1
# print("Never stop!")

# x = 0
# y = x + 0
# while y >= 0 :
#     print(y)
#     y = y + 1
# print("Never stop!")

# x = 999999
# y = x + 1
# while y > 0 :
#     print(y)
#     y -= 1
# print("Reached from 1 Million")


    # 5.1 - Loops and Iteration
# while True :
#     line = input('Say Something or Type exit() to Exit>')
#     if line == 'exit()' :
#         break
#     print('Did you just say:', line)
# print('Done, exited!')

# while True :
#     line = input('Say-Something>')
#     if line[0] == '&' :
#         pass
#     if line[0] == '#' :
#         continue
#     if line == 'done' :
#         break
#     print('Did you just say:', line)
# print('Done!')

        # 5.2 - Definite Loops
# for i in [1, 2, 3, 4, 5] :
#     print(i)
# print("Blastoff")
friends = ['Connor', 'RethMano', 'Austin', 'Mattix', 'ShenZe']
for friend in friends :
    print('Happy New Year,', friend + '!')
print("I Love You!")