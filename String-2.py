"""
Solutions to String-2
"""
"""double_char 

Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""

def double_char(str):
  a = ""
  for char in str:
    a += char*2
  return a

"""count_hi

Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""

def count_hi(str):
  count = 0
  for i in range(len(str)):
    if str[i:i+2]== "hi":
      count += 1
  return count

"""cat_dog

Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""

def cat_dog(str):
  count_cat = 0
  count_dog = 0
  for i in range(len(str)):
    if str[i:i+3] == "cat":
      count_cat += 1
  for j in range(len(str)):
    if str[j:j+3] == "dog":
      count_dog += 1
  return count_cat == count_dog

"""count_code

Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""

def count_code(str):
  count = 0
  for i in range(len(str)):
    if str[i:i+2] == "co" and str[i+3:i+4] == "e":
        count += 1
  return count

"""end_other

Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""

def end_other(a, b):
  for i in range(len(b)):
    if a.lower() == b.lower()[len(b)-len(a):]:
      return True
  for j in range(len(a)):
    if b.lower() == a.lower()[len(a)-len(b):]:
      return True
  return False

#or

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return b.endswith(a) or a.endswith(b)

"""xyz_there

Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""

def xyz_there(str):
  for i in range(len(str)):
    if str[i:i+3] == "xyz":
      if str[i-1] != ".":
        return True
  return False