l=["a","e","i","o","u","A","E","I","O","U"]
a=input()
if a.isalpha():
  if a in l:
    print ("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
