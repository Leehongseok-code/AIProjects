import pandas as pd
from apireader import *#여기서 최초로 데이터 갱신
from IPython.display import display
from predict import predict

#input값으로 원하는 언어를 입력하면, 해당 언어의 댓글들만 필터링해 저장된 리스트를 반환
def language_filtering(langu,video):
    c.vid_id=video
    ids_list=[]#사용자들의 id만 모아놓은 리스트
    comments_list=[]#사용자들의 댓글만 모아놓은 리스트
    #print(d_list)
    c_status=0
    comments(video," ")#클릭할때마다 새로운 url에 해당하는 데이터 공급
    while True:#모든 댓글을 긁어오기위해  next_page_token이 안나올때까지 탐색
        d_list = c.c_data_list  # 원본 json데이터를 가공하기 전 자료
        c_status=c.nextpage()
        print(c_status)
        for i in range(0,len(d_list)):
            if predict(takecomments(d_list[i]))==langu:
                ids_list.append(takeids(d_list[i]))
                comments_list.append(takecomments(d_list[i]))
                #comments_list.append(takecomments(d_list[i]).replace("!@#$%^&*()_+",""))
        if c_status==1:
            break
    #객체에 정보를 업데이트
    c.c_ids=ids_list
    c.c_comments=comments_list
    pd_data_all={"ID":ids_list,"Comment":comments_list}
    pd_data_ids={"ID":ids_list}
    pd_data_comments={"Comment":comments_list}
    youtube_pd=pd.DataFrame(pd_data_all)
    display(youtube_pd)
    youtube_pd.to_csv("comments.csv",encoding="utf-8-sig")

#language_filtering("Korean")