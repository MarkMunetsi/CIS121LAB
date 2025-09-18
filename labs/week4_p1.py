#Mark Munetsi
'''
larger_num = int(input("enter the larger number: "))
smaller_num = int(input("enter the smaller number"))

num = 0 

while larger_num > smaller_num:
    larger_num /= 2
    num += 1

print(f"number of times halved: {num}")    


#question 2

word = input("enter a word: ")
result = ""

for i in range (1, len(word)-1,2):
    result += word[i]

print(f"output = {result}")    
'''
#question 3

for num in range(37,1051):
    if num % 2 == 0:
    
     print(num)

