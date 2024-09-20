from Osu_Id import *
import re
def getdata(html):
    User=re.findall('"username":"(.*?)"',html)
    Join=re.findall('"join_date":"(.*?)"',html)
    Coun=re.findall('"country":{"code":"(.*?)"',html)
    Leval=re.findall('level":{"current":(.*?),"progress":(.*?)},',html)
    Rank=re.findall('"pp":(.*?),"pp_exp":(.*?),"ranked_score":(.*?),"hit_accuracy":(.*?),"play_count":(.*?),"',html)
    Score=re.findall('"grade_counts":{"ss":(.*?),"ssh":(.*?),"s":(.*?),"sh":(.*?),"a":(.*?)},"country_rank":(.*?),',html)
    try:
        TJ=User
        TL=Leval[0]
        TR=Rank[0]
        TS=Score[0]
        userID,addTime,Cou=TJ,Join,Coun
        sadd ='''
---------------------------------------------
        用户名--------- %s
        注册 %s
        国家------------------ %s
        等级-------------- %s(%s%%)
        PP积分--------- %s
        Ranked总分%s
        ACC正确率------ %s
        PC游戏次数-------- %s
------------------累计成绩评级----------------
       ss:%s     ssh:%s
       s :%s     sh :%s
          a :%s
        国内排名:%s
--------------------------------------------
'''%(userID,addTime,Cou,TL[0],TL[1],TR[0],TR[2],TR[3],TR[4],TS[0],TS[1],TS[2],TS[3],TS[4],TS[5])
    except:
        sadd = '人呢，我问你人呢'

    return sadd



