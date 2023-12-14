class Solution(object):
    ASKuser = int(input("Enter a number: "))
    def isPalindrome(number):
        empty = ""
        number = str(number)
        rightpointer = 0
        leftpointer = len(number) - 1
        for i in range(0, len(number)):
            front = number[rightpointer]
            back = number[leftpointer]
            if front == back:
                rightpointer += 1
                leftpointer -= 1
            else:
                pass
        if front == back:
            print(True)
        else:
            print(False)
            
    isPalindrome(ASKuser)
