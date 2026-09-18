#!/usr/bin/env python3
ROWS=[("16:30:00",29.1),("16:42:00",27.6),("16:55:00",25.8),("17:07:00",24.1),("18:25:00",10.7),("19:41:00",-0.5),("20:41:00",-1.5),("21:41:00",-18.0),("22:41:00",-28.5),("00:11:00",-37.7),("00:19:00",-37.8)]
def sec(t):
 h,m,s=map(int,t.split(":"));x=h*3600+m*60+s
 return x if h>=16 else x+86400
def correction(t):
 x=sec(t)
 for (a,fa),(b,fb) in zip(ROWS,ROWS[1:]):
  xa,xb=sec(a),sec(b)
  if xa<=x<=xb:return fa+(fb-fa)*(x-xa)/(xb-xa)
 raise ValueError("outside primary table")
if __name__=="__main__":
 for t in ("19:41:03","20:41:05","21:41:27","22:41:22","00:11:00"):
  print(t,correction(t))
