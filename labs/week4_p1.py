#Mark Munetsi

larger_num = int(input("enter the larger number: "))
smaller_num = int(input("enter the smaller number"))

num = 0 

while larger_num > smaller_num:
    larger_num /= 2
    num += 1

print(f"number of times halved: {num}")    

