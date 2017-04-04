
#One end BFS, O(N*L), TLE
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        #:type beginWord: str
        #:type endWord: str
        #:type wordList: List[str]
        #:rtype: int
        if len(wordList)==0: return False
        toVisit=[]
        self.addNextWord(beginWord,wordList,toVisit)
        dist=2
        while len(toVisit)>0:
            num=len(toVisit)
            for i in range(num):
                word=toVisit.pop(0)
                if word==endWord: 
                    return dist
                self.addNextWord(word,wordList,toVisit)
            dist+=1
        return 0
        
        
    def addNextWord(self, word, wordList, toVisit):
        if len(wordList)>0 and word in wordList:  #notice this line
            wordList.remove(word)
        for i in range(len(word)):
            for j in range(26):
                replaced=word[:i]+chr(ord('a')+j)+word[i+1:]
                if len(wordList)>0 and replaced in wordList:
                    toVisit.append(replaced)
                    wordList.remove(replaced)
                    


#One end BFS, O(N*L)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        #:type beginWord: str
        #:type endWord: str
        #:type wordList: List[str]
        #:rtype: int
        wordList=set(wordList)
        if len(wordList)==0: return 0
        toVisit=set()
        toVisit.add(beginWord)
        dist=1
        while len(toVisit)>0:
            temp=set()
            for word in toVisit:
                if word==endWord: 
                    return dist
                for i in range(len(word)):
                    for j in range(26):
                        replaced=word[:i]+chr(ord('a')+j)+word[i+1:]
                        if len(wordList)>0 and replaced in wordList:
                            temp.add(replaced)
                            wordList.remove(replaced)
            toVisit=temp
            dist+=1
        return 0


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        #:type beginWord: str
        #:type endWord: str
        #:type wordList: List[str]
        #:rtype: int
        wordList=set(wordList)
        if len(wordList)==0: return 0
        if endWord not in wordList: return 0
        toVisitBegin=set()
        toVisitEnd=set()
        toVisitBegin.add(beginWord)
        toVisitEnd.add(endWord)
        wordList.remove(endWord)
        dist=2
        while len(toVisitBegin)>0 and len(toVisitEnd)>0:
            if len(toVisitBegin)>len(toVisitEnd):
                swap=toVisitBegin
                toVisitBegin=toVisitEnd
                toVisitEnd=swap
            temp=set()
            for word in toVisitBegin:
                for i in range(len(word)):
                    for j in range(26):
                        replaced=word[:i]+chr(ord('a')+j)+word[i+1:]
                        if replaced in toVisitEnd:
                            return dist
                        if len(wordList)>0 and replaced in wordList:
                            temp.add(replaced)
                            wordList.remove(replaced)
            toVisitBegin=temp
            dist+=1
        return 0
           
        
        

            
            
            
        
        
        
        