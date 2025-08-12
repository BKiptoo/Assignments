# # The question asks you to create a function called FizzBuzz(num) that takes an integer num as input. This function
# should return a string containing numbers from 1 to num, separated by spaces. The core of the problem is to replace
# certain numbers with specific words:

# # Numbers divisible by 3 should be replaced with the word "Fizz".

# # Numbers divisible by 5 should be replaced with the word "Buzz".

# # Numbers divisible by both 3 and 5 should be replaced with the word "FizzBuzz".

# # For example, if the input num is 16, the function should return the string "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz
# # 13 14 FizzBuzz 16". The input number num is guaranteed to be within the range of 1 to 50.

def FizzBuzz(num):

  # code goes here
  result = []
  
  for i in range(1, num + 1):
    if i % 3 == 0 and i % 5 == 0:
      result.append("FizzBuzz")
    elif i % 3 == 0:
      result.append("Fizz")
    elif i % 5 == 0:
      result.append("Buzz")
    else:
      result.append(str(i))
  
  return " ".join(result)

# keep this function call here 
print(FizzBuzz(int(input())))
