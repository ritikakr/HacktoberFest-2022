nterms = int(input("Enter the range of terms in the fibinocci series : "))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence of range",nterms,"terms :", end=" ")
   while count < nterms:
       print(n1, end =" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
