# indexing = accessing elements of seuence using indexing operator
# [start : end : step]   a 1

credit_number = "2345-6789-0054-2732"
print(credit_number[0]) #single element is extracted from given position
print(credit_number[0:4]) #range specified start to end
print(credit_number[:4]) #even if range not specified taken as end
print(credit_number[5:9]) #range 
print(credit_number[5:])  #start point specified print all after it
print(credit_number[-2]) #selects from reverse like from behind
print(credit_number[-1])
print(credit_number[::2]) #steps after leaving every one digit
print(credit_number[::3]) #steps after leaving every two digits
last_digit = (credit_number[-4:])  #starts from reverse of 4
print(f"XXXX-XXXX-XXXX-{last_digit}") #this is how credit card numbers are printed 
credit_number = credit_number[::-1]
print(credit_number) #printed in backward