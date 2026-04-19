class Solution:
    def isPalindrome(self, s: str) -> bool:
        i , j = 0 , len(s)-1
        while(i<j):
          if not (s[i].isalpha() or s[i].isdigit()):
            print(s[i])
            i+=1
            continue
          if not (s[j].isalpha() or s[j].isdigit()):
            print(s[j])
            j-=1  
            continue
          if (s[i].lower()!=s[j].lower()):
            print(s[i],"ddd",s[j])
            return False
          i+=1
          j-=1
        return True      

        