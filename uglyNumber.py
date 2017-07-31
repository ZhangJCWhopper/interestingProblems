"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
"""
class Solution(object):
	def nthUglyNumber(self, n):
		ugly = [1]
		cursor = [0]*3
		for iteration in range(n-1):
			neo = [ugly[cursor[0]] *2, ugly[cursor[1]] *3, ugly[cursor[2]] *5]
			for i in range(3):
				#use if instead of if ... elif: there may be some equal values, get rid of duplication
				if neo[i] == min(neo):
					cursor[i] += 1
			ugly.append(min(neo))
		return ugly[-1]

S = Solution()
print S.nthUglyNumber(1690)
