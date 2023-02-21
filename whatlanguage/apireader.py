#app.py
import requests
from flask import Flask,request,jsonify
import re
google_api_key=""
#video_id=input("비디오 아이디를 입력하세요:")

app=Flask(__name__)
@app.route("/comments",methods=["POST"])

#input data->data_딕셔너리, json을 파싱해서 원하는 정보를 리턴

def isHangul(text):
    #출처:https://m.blog.naver.com/PostView.nhn?blogId=chandong83&logNo=221142971719&proxyReferer=https%3A%2F%2Fwww.google.com%2F
    encText=text
    #유니코드에서 한글이 차지하는 범위에 속하는 글자가 있는지 판정
    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))
    if hanCount>0:
        return 'Korean'
    else:
        return False

def takecomments(d_dict):
    return d_dict["snippet"]["topLevelComment"]["snippet"]["textOriginal"]

def takeids(d_dict):
    return d_dict["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]

#다른 파일에서 comments_data_list를 제공하기 위해(함수를 빠져나오면 json_data가 소멸하기 때문)
class comments_data_list():
    c_data_list=[]
    c_ids=[]
    c_comments=[]
    req_url=""
    n_page_token=" "
    vid_id=""
    def nextpage(self):
        if c.n_page_token is not "":
            comments(self.vid_id,c.n_page_token)
            return 0
        else:
            print("마지막 페이지입니다.")
            return 1

#input:video_id, output:video_comment-video id를 인풋으로 주면, comments_data_list 클래스에 각종 데이터 업데이트
#이후에 takeids나 takecomments함수로 원하는 값 추출
def comments(vid,next_page_token):
    #f-string->문자열에서 %나 +를 사용하지 않고도 편리하게 문자열 조립
    #ex)name="Sam", age=15
    # f"{name} is {age}years old"-> Sam is 15 years old
    google_api_key="AIzaSyBHdscrgCv920Tx5-TfqHoqn_cp4lRD0IQ"
    request_url=f"https://www.googleapis.com/youtube/v3/commentThreads?key={google_api_key}" \
                f"&textFormat=plainText&part=snippet&videoId={vid}&maxResults=50&pageToken={c.n_page_token}"
    c.req_url=request_url
    print(c.req_url)
    json_data=requests.get(c.req_url)
    json_data=json_data.json()
    next_page_token=json_data.setdefault("nextPageToken","")
    c.n_page_token = next_page_token
    #print(json_data)
    data_list=json_data["items"]
    c.c_data_list=json_data["items"]#c_data_list=data_list의 복사본
    #print(data_list[1]["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
    #print(data_list)
    #print(isHangul(takecomments(data_list[1])))

c=comments_data_list()
#c.nextpage()


