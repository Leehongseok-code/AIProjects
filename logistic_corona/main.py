#pytorch-1.4.0
class counter():
    am=0
    eu=0
    asia=0
    ch=0
    af=0
    au=0
c=counter()
if __name__=="__main__":#이 파일을 실행시켰을 때만 import하기
    from ch import *
    from eu import *
    from am import *
    from asia import *
    from af import *
    from au import *

print("중국:",c.ch,"아시아:",c.asia,"유럽:",c.eu,"아프리카:",c.af,"미주:",c.am,"호주:",c.au)
print("count:",c.am+c.eu+c.asia+c.ch+c.af+c.au)
