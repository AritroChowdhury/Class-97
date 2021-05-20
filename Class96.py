#pocketMoney=int(input('Enter The Pocketmoney:'))

#if(pocketMoney>500):
    #print('You Are A Rich Kid')
#elif(pocketMoney>100):
    #print('You Have A Good Life')
#else:
    #print('I Know What You Feel')

#friendList=['Adrish','Priyanshu','Pritam']
#for friends in friendList:
    #print(friends)

#count=5
#while(count>=0):
    #print(count)
    #count=count-1
 
introString=input('Enter Your Introduction:')
charecterCount=0
wordCount=1

for i in introString:
    charecterCount=charecterCount+1
    if(i==' '):
        wordCount=wordCount+1

print(charecterCount)
print(wordCount)