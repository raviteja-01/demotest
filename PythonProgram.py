def isPalindrome(s):
  rev_s = s[::-1]
  if s== rev_s:
    return True 
  return False

s = input() 
if isPalindrome(s):
  print(s,"is a Palindrome")
else:
  print(s,"is not a Palindrome")
