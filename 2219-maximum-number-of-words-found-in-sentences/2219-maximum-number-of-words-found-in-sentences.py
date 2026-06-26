class Solution(object):
    def mostWordsFound(self, sentences):
            max_word=0
            max_sen=""
            for i in sentences:
                count=len(i.split())
                if count>max_word:
                    max_word=count
                    max_sen=i
            return max_word