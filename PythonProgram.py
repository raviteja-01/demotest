def isPalindrome(string):
  rev_string = string[::-1]
  if string== rev_string:
    return True 
  return False

user_string = input() 
if isPalindrome(user_string):
  print(user_string,"is a Palindrome")
else:
  print(user_string,"is not a Palindrome")
