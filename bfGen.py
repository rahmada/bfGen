class bfGen:
	charAlfaSmall=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	charAlfaBig=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	charNum=['0','1','2','3','4','5','6','7','8','9']

	def __init__(self,start,stop):
		if start==0 :
			start=1
		self.startDigit=start
		self.stopDigit=stop
		self.nowString=""
		self.tryCharList=[]
		self.tryCharList.extend(bfGen.charAlfaSmall)
		self.tryCharList.extend(bfGen.charAlfaBig)
		self.tryCharList.extend(bfGen.charNum)
		self.nowArray=[]
		self.done=False
		for i in range(0,self.startDigit):
			self.nowArray.append(0)
		self.genString()
	
	def nextString(self):
		loopFlag=True
		cur=len(self.nowArray)-1
		while loopFlag:
			self.nowArray[cur]=self.nowArray[cur]+1
			if self.nowArray[cur]>=len(self.tryCharList)-1:
				self.nowArray[cur]=0
				cur=cur-1
				if cur<0:
					for f in self.nowArray:
						self.nowArray[f]=0
					self.nowArray.append(0)
					if len(self.nowArray)>self.stopDigit:
						self.done=True
					else:
						loopFlag=False
			else:
				loopFlag=False
		self.genString()
		

	def genString(self):
		self.nowString=""
		for i in range (0,len(self.nowArray)):
			self.nowString=self.nowString+self.tryCharList[self.nowArray[i]]

#inital use example
#baru = bruteForcer(4,4)
#while baru.done==False:
#        print baru.nowString
#        baru.nextString()

