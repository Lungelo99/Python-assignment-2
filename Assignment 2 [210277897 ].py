#problem 1

def list_check(listz):
    """
        Seaching through a list for sequence 023
    """
    isValid = False
    x = 0
    position = ''

    #checking if characters contains 023 and extracting them 

    while (x < len(listz)):
        if(listz.__contains__(0)):
            position = position + str(listz[listz.index(0)])
            if(listz.__contains__(2)):
                position = position + str(listz[listz.index(2)])
                if(listz.__contains__(3)):
                    position = position + str(listz[listz.index(3)])
                    x = len(listz) + 1

#making sure its the requered sequence

        if(position == '023'):
            isValid = True
        x = x + 1
    return isValid


myBool = list_check([1,0,2,3,1])
print(myBool)


# Problem 2

def  string_bits(myStr):
    """
     A function that return every other string
    """

    other = myStr[::2] 
           
    return other

everyOther = string_bits('Hello') 

print()
print(everyOther)


# problem 3

def end_other(s_1, s_2):
  """
   Comparing strings using slice
   method

  """
  str_1 = s_1[-3:]
  str_2 = s_2[-3:]

  if(str_1.lower() == s_2.lower()):
    
    isValid = True
  elif(str_2.lower() == s_1.lower()):
    isValid = True
  else:
    isValid = False
  return isValid

print()
print(end_other('Hiabc','abc'))


# Problem 4




def  double_char(s):
    """
     Doubling every character in a string 
    """
    x = 0
    doubler = ''
    while(x < len(s)):
        doubler = doubler  + (s[x] * 2)
        x = x + 1
     
           
    return doubler

doubled = double_char('Hello') 

print()
print(doubled)


# Problem 5

def fix_teen(n):
  """
    Checks if a vaule is a teen or not

  """
  x = 0

  while(x < len(n)):
    if(n[x] in(13, 14, 17,18,19)):
      n[x] = 0
    x = x + 1
  
  return n


def no_teen_sum(a,b,c):

  """
    Summing all non-teen values

  """
  list = []
  list.append(a)
  list.append(b)
  list.append(c)

  myTeen = fix_teen(list)
  sum = 0
  x = 0

  for x in myTeen:
    sum = sum + x

  return sum

mySum = no_teen_sum(2,3,13)

print()
print(mySum)


# Problem 6

def count_events(n):
  """
    counts even numbers in a list

  """
  count = 0
  x = 0

  while(x < len(n)):

    if(n[x] % 2 == 0):

      count = count + 1
    x = x + 1 
  return count
myCount = count_events([2,1,2,3,4])
display = 'number of even numbers: {}'.format(myCount) 
print()
print(display)
print()