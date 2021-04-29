#Write your code below this line 👇

def prime_checker(number):
  if number == 2:
    print("PRIME")
    return
  if number % 2 == 0 and number !=2:
    print("NOT PRIME")
    return
  divider = n - 1
  while divider != 2:
    if number % divider == 0:
      print("NOT PRIME")
      break
    elif number % divider != 0:
      divider -= 1
      continue
  if divider == 2:
    print("PRIME")







#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))


prime_checker(number=n)



