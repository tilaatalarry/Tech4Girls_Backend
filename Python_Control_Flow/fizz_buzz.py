for i in range(1, 51):

 # if number is divisible by 3 and returns 0, print Fizz
     if (i % 3 == 0):
         print('Fizz')

 # if number is divisible by 5 and returns 0, print Buzz
     elif (i % 5 == 0):
         print('Buzz')

# if number is divisible by 3 and 5, print FizzBuzz
     elif (i % 3 == 0 and i % 5 == 0):
         print('FizzBuzz')

     else:
         print(i)