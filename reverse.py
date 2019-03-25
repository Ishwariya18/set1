def reverseWordSentence(Sentence):
words=Sentence.split("")
newWords=[word[::-1]for word in words]
newSentence="".join(newwords)
return newSentence
