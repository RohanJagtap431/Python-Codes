
while True:
      num1 = int(input("Enter your fist number:  "))
      op = input("choice opratars +/-/×/÷:  ")
      num2 = int(input("Enter your second number:  "))

      if op == '+':
         print(num1 + num2)
    
      elif op == '-':
          print(num1 -  num2)
    
      elif op == '×':
            print(num1 * num2)
    
      elif op == '÷':
          if num2 == 0 :
              print("Cannot divide by zero")
          
          elif num1 / num2:
               print(num1/num2)