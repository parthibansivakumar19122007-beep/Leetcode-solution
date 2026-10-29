class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        c=0
        for i in range(1,len(salary)-1):
            c+=salary[i]
        return c/(len(salary)-2)