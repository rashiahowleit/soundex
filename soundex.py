#Soundex
#Rashia Howleit
#Turns a single name into a 4 character sequence starting with the
#first letter of the name followed by a 3 digit number sequence

numbers = {
  "A" : 0,
  "a" : 0,
  "E" : 0,
  "e" : 0,
  "I" : 0,
  "i" : 0,
  "O" : 0,
  "o" : 0,
  "U" : 0,
  "u" : 0,
  "H" : 0,
  "h" : 0,
  "W" : 0 ,
  "w" : 0,
  "Y" : 0 ,
  "y" : 0,
  "B" : 1,
  "b" : 1,
  "F" : 1,
  "f" : 1,
  "P" : 1,
  "p" : 1,
  "V" : 1,
  "v" : 1,
  "C" : 2,
  "c" : 2,
  "G" : 2,
  "g" : 2,
  "J" : 2,
  "j" : 2,
  "K" : 2,
  "k" : 2,
  "Q" : 2,
  "q" : 2,
  "S" : 2,
  "s" : 2,
  "X" : 2,
  "x" : 2,
  "Z" : 2,
  "z" : 2,
  "D" : 3,
  "d" : 3,
  "T" : 3,
  "t" : 3,
  "L" : 4,
  "l" : 4,
  "M" : 5,
  "m" : 5,
  "N" : 5,
  "n" : 5,
  "R" : 6,
  "r" : 6,
}
print("** Welcome to the Soundex app **\n")

surname = input("\nEnter a surname (x to quit):")
while surname != "x": #when. the surname is not equal to x, which is what stops the loop, run the rest to code
  result = ""
  clean_surname = ""
  for letter in surname:
    if letter.isalpha(): 
      clean_surname += letter #for every letter that is an alphabet, add in clean surname string
  print("\nStep 1: Cleaned up surname:", clean_surname)
  if clean_surname == "":
    print("Invalid surname, cannot be encoded. Please try again.") #if clean surname is blank it is invalid
  else:
    for letter in clean_surname:
      result = result + str(numbers[letter]) #makes a string that turns letters into numbers for encoded surname
    print("Step 2: Encoded surname:", result)
    
    new_str = ""
    prev = ""
    for c in result:
      if prev != c: #compares previous character to current character to check if theyre not equal
        new_str += c #adds character thats not equal to previous character to a new 
        prev = c
    print("Step 3: Coalesced encoding:", new_str)
    
    new_name = clean_surname[0] + new_str[1:] #first index of clean surname + every index second including and after the second in new string
    print("Step 4: First digit replaced:", new_name.upper())
    
    no_zero = ""
    for i in new_name:
      if i != "0":
        no_zero += i #if each letter doesnt equal 0 add it to the string no zero
    print("Step 5: All zeros removed:", no_zero.upper())
    
    soundex_code = ""
    if len(no_zero) >= 4:
      soundex_code = no_zero[:4]
    if len(no_zero) == 3:
      soundex_code = no_zero + "0"
    if len(no_zero) == 2:
      soundex_code = no_zero + "0" + "0"
    if len(no_zero) == 1:
      soundex_code = no_zero + "0" + "0" + "0"
    if len(no_zero) == 0 :
      soundex_code = no_zero + "0" + "0" + "0" + "0"
    print("Step 6: Soundex code is:", soundex_code.upper()) #add zeros to the length until the length equals 4

  surname = input("\nEnter a surname (x to quit):") 
print("\nAll done.")




