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

#question 3

for num in range(37,1051):
    if num % 2 == 0:
    
     print(num)
'''     

#question4

word = ""  # start with an empty string

while True:
    letter = input("Enter a letter (or type 'done' to finish): ")

    if letter.lower() == "done":   # check if user is finished
        break
    elif len(letter) != 1:         # make sure only single letters are added
        print("Please enter only one letter at a time.")
    else:
        word += letter             # add the letter to the word

print("Your newly created word is:", word)


''''
# question 5

sum = 0

for i in range (51,517,1):
    sum += i
print(sum)
'''
