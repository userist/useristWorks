# -*- encoding: utf-8 -*-   
import os,string,codecs
import sys,time

def readfile():
    wordlist=[]
    base=open('base.txt','r')
    baseinfo=base.readlines()
    tagf=open('tag.txt','r')
    tagfinfo=tagf.readlines()
    for i in tagfinfo:
        tags=i.split(' ')
    for i in baseinfo:
        words=i.split(' ')
        for word in words:
            if word != '\t'and word != '\n' and word!=' ' and word != '' and word>=2:
               word=word.replace('\t','')
               word=word.replace('\n','')
               word=word.replace(' ','')
               word=word.replace('.\n','')
               if word!='':
                   wordlist.append(word)
##        tags=['.','"',',','!','?','(',')']
        for x in range(len(tags)):
            tag=tags[x]
            for k in range(len(wordlist)):
                if tag in wordlist[k]: #用符号分割
                    words=wordlist[k].split(tag)
                    del wordlist[k]
                    for  j in range(len(words)): #去掉判断后的空字符
                        if words[j]!='':
                            wordlist.append(words[j])


    
    base.close()
    tagf.close()
    return wordlist



def getstr(word,count,allwordnum):
    countstr=word+'--------'+str(count)+'--------'+str(allwordnum)
    return countstr

if __name__=="__main__":
   wordcnt={} 
   wordlist=readfile()
   wordlistall=wordlist
   allwordnum=len(wordlistall)
   outdata=open('count.txt','w')
   print '******************************************'
   print(u'提示：')
   print(u'     1、要统计的文章放置于本程序路径下的base.txt中') 
   print(u'     2、单词分割符存放在本程序路径下的tag.txt中,以空格为分隔符，默认已对换码符，换行符，空格，句号（英文）处理')
   print(u'     3、统计的结果保存在本程序路径下的count.txt中')
   print '******************************************'
   print(u"开始统计咯......")
   
   print'------------------------------------------------------------------------'
   for i in wordlistall:
       if i in wordcnt:
          wordcnt[i]+=1
       else:
          wordcnt[i]=1
   for word,cnt in wordcnt.iteritems():
       print word+'--------'+str(cnt)+'--------'+str(allwordnum)
       outdata.write(getstr(word,cnt,allwordnum)+'\n')
   
   print'------------------------------------------------------------------------'
   print(u"完成")
   print(u'按任意键退出')
   outdata.close()
   os.system("pause")
