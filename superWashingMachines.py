"""
https://leetcode.com/problems/super-washing-machines/

Description:
You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 ? m ? n) washing machines, 
and pass one dress of each washing machine to one of its adjacent washing machines at the same time.

Given an integer array representing the number of dresses in each washing machine from left to right on the line,
you should find the minimum number of moves to make all the washing machines have the same number of dresses.
If it is not possible to do it, return -1.

Why failed?
Do not stick on one point,
step is decided by the on requires most movement,
others are not important.

"""
class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        clothes = sum(machines)
        if clothes % len(machines) != 0:
            return -1
        final = clothes / len(machines)
        """
        cumu = 0
        Mcumu = 0
        for i in range(len(machines)):
            cumu += machines[i] - final
            Mcumu = max(abs(cumu), Mcumu)
        
        return max(Mcumu, max(machines) - final)
        """
        steps = 0
        left = 0
        res = 0
        for i in machines:
            #for each point, if we want to move "least" steps:
            right = i - left - final
            res = max(res, left, right, left+right)
            left = -right
        return res