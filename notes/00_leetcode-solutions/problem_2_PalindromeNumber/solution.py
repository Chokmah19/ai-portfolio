class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 負數直接不是回文
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0

        while x > rev:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        # 若數字長度為奇數，rev 多一位，要去掉中間那位比較
        return x == rev or x == rev // 10
