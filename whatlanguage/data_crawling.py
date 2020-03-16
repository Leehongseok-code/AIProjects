import pandas as pd
from apireader import *
from IPython.display import display

c.vid_id="rS9i2RmNrec"
ids_list=[]#사용자들의 id만 모아놓은 리스트
comments_list=[]#사용자들의 댓글만 모아놓은 리스트
#print(d_list)
c_status=0
while True:

    d_list = c.c_data_list  # 원본 json데이터를 가공하기 전 자료
    c_status=c.nextpage()
    print(c_status)
    for i in range(0,len(d_list)):
        ids_list.append(takeids(d_list[i]))
        comments_list.append(takecomments(d_list[i]))
    if c_status==1:
        break

pd_data_all={"ID":ids_list,"Comment":comments_list}
pd_data_ids={"ID":ids_list}
pd_data_comments={"Comment":comments_list}
youtube_pd=pd.DataFrame(pd_data_all)
display(youtube_pd)
youtube_pd.to_csv("comments.csv",encoding="utf-8-sig")