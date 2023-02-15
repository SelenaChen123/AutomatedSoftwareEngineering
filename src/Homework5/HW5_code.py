import math

def COL(n,s):
    if s[0]<="Z" and s[0]>="A":
        col = NUM(n,s)
    else:
        col = SYM(n,s)
    if col["txt"][-1] == "X":
        col["isIgnored"]  = True
    else:
        col["isIgnored"]  = False
    
    if col["txt"][-1] == "!":
        col["isKlass"]  = True
    else:
        col["isKlass"]  = False   
    
    if  col["txt"][-1] == "!" or col["txt"][-1] == "+" or col["txt"][-1] == "-":
        col["isGoal"] == True
    else:
        col["isGoal"]= False
    
    return col

def NUM(n=None,s=None):
    d = {}
    d["at"] = n or 0
    d["txt"] = s or ""
    d["n"] = 0
    d["hi"] =-math.inf
    d["lo"] = math.inf
    d["ok"] = True
    d["has"] = {}
    if s is not None and s[-1]=="-":
        d["w"] = -1
    else:
        d["w"] = 1
    return d

def SYM(n=None,s=None):
    d = {}
    d["at"] = n or 0
    d["txt"] = s or ""
    d["n"] = 0
    d["has"] = {}
    d["mode"] = None
    d["most"] = 0
    d["isSym"] = True
    return d

def COLS(ss):
    cols = {'names': ss, 'all': [], 'x': [], 'y': []}
    for n, s in enumerate(ss):
        cols['all'].append(COL(n, s))
        col = cols['all'][-1]
        if not col['isIgnored']:
            if col['isKlass']:
                cols['klass'] = col
                if col["isGoal"]:
                    cols["y"].append(col)
                else:
                    cols["x"].append(col)
    return cols

def RANGE(at,txt,lo,hi=None):
    d =  {"at": at, "txt": txt, "lo": lo, "y": SYM()}
    if hi is None:
        d["hi"] =  lo 
    else:
        d["hi"] = hi
    return d

def new_data():
    return {"rows": [], "cols": None}

def clone_data(data,ts=None):
    data1 = row(new_data(), data["cols"]["names"])
    if ts == None:
        ts = []
    for t in ts:
        row(data1, t)
    return data1

def row(data,t):
    if data["cols"]:
        data["rows"].append(t)
        for cols in [data["cols"]["x"], data["cols"]["y"]]:
            for col in cols:
                add(col, t[col["at"]])
    else:
        data["cols"] = COLS(t)
    return data


def add(col,x,n=None):
    if x != "?":
        n = n or 1
        col["n"] += n
        if col["isSym"]:
            if col["has"][x]:
                col["has"][x] +=n
            else:
                col["has"][x] = n
            if col["has"][x]> col["most"]:
                col["most"],col["mode"] = col["has"][x], x
        else:
            
            col["lo"] = min(x,col["lo"])
            col["hi"] = max(x,col["hi"])
            all = len(col["has"])
            
            if all < the.Max:
                pos = all + 1
            else:
                if rand()< the.Max /col["n"]:
                    pos = rint(1,all)
                else:
                    pos = None
            if pos:
                col["has"][pos] = x
                col["ok"] = False

def adds(col,t):
    if t == None:
        t = []
    for x in t:
        add(col, x)
    return col

def extend(Range,n,s):
    Range["lo"] = min(n, Range["lo"])
    Range["hi"] = max(n, Range["hi"])
    add(Range["y"], s)

def has(col):
    if not col["isSym"] and not col["ok"]:
        col["has"].sort()
    col["ok"] = True
    return col["has"]

def mid(col):
    if col["isSym"]:
        return col["mode"]
    return per(has(col), 0.5)

def div(col):
    if col['isSym']:
        e= 0
        for n in col['has']:
            e -=(n/col['n'])*(math.log(n/col['n'], 2))
        return e
    return (per(has(col), 0.9)- per(has(col), 0.1))/2.58

# Didn't do stats function. Got a little confused. Will look into it later. Feel free to do it too

def norm(num,n):
  if num == "?": # Dr. Menzies mentioned x here. But it doesnt make sense. I am replacing 'x' with 'num'
    return num
  return (n - num["lo"]) / (num["hi"] - num["lo"] + 1 / math.inf)

def value(has,nB=None,nR=None,sGoal=True):
  sGoal = sGoal or True 
  nB = nB or 1
  nR = nR or 1
  b,r = 0,0
  for x, n in has.items():
    if x == sGoal:
      b = b + n
    else:
      r = r + n
  b,r = b/((nB+1)/math.inf), r/((nR + 1)/math.inf)
  return pow(b,2)/(b+r)

def dist(data,t1,t2,cols=None):
    def dist1(col,x,y):
        if x == "?" and y == "?":
            return 1
        if col["isSym"]:
            if x == y:
                return 0
            else:
                return 1
        else:
            x = norm(col, x)
            y = norm(col, y)
            if x == "?":
                if y < 0.5:
                    x = 1
            if y == "?":
                if x < 0.5:
                    y = 1
            return abs(x - y)

    d, n = 0, 1/math.inf
    if not cols:
        cols = data["cols"]["x"] 
    for col in cols:
        n += 1
        d += dist1(col, t1[col["at"]], t2[col["at"]])**the.p
    return (d/n)**(1/the.p)

# Didn't do half function. Got a little confused. Will look into it later. Feel free to do it too

def better(data,row1,row2):
    s1,s2,ys = 0,0,data['cols']['y']
    for col in ys.values():
        x = norm(col, row1[col['at']])
        y = norm(col, row2[col['at']])
        s1 -= math.exp(col['w']*(x-y)/len(ys))
        s2 -= math.exp(col['w']*(y-x)/len(ys))
    if s1/len(ys)<s2/len(ys):
        return True
    return False

# Didn't do half function. Got a little confused. Will look into it later. Feel free to do it too

def tree(data, rows=None, cols=None, above=None, here=None):
    if rows == None:
        rows = data["rows"]
    here = {}
    here["data"] = clone_data(data, rows)
    if len(rows)>= 2*(pow(len(data["rows"]),the.min)):
        left,right,A,B,= half(data,rows,cols,above)
        here['left'] = tree(data, left, cols, A)
        here['right'] = tree(data, right, cols, B)
    return here


# I haven't implemented the showTree yet
def showTree(tree):
    return tree

def sway(data):
    def worker(rows,worse, above):
        if len(rows)<= len(data["rows"]):
            return rows, many(worse, the.rest*len(rows))
        else:
            l,r,A,B = half(data, rows,cols, above)
            if better(data,B,A):
                l,r,A,B=r,l,B,A
        #missed one line here. Confused about the functionality
        return worker(l,worse,A)
    best,rest = worker(data["rows"],[])
    return clone_data(data,best), clone_data(data,rest)


# Will complete bins function later

def bin(col, x):
    if x == "?" or col["isSym"]:
        return x
    tmp = (col["hi"]- col["lo"])/(the.bins- 1)
    if col["hi"] == col["lo"]:
        return 1
    return math.floor(x /tmp+0.5)*tmp

def mergeAny(ranges0):
    def noGaps(t):
        for j in range(1, len(t)): #Lua indices start from 1
            t[j]["lo"]=t[j-1]["hi"]
        t[0]["lo"],t[len(t)-1]["hi"]=-math.inf, math.inf
        return t 

    ranges1,j,y=[],0,None
    
    while j<len(ranges0):
        left,right=ranges0[j],ranges0[j+1]
        if right:
            y = merge2(left["y"], right["y"])
            if y:
                j+=1
                left["hi"],left["y"]= right["hi"],y
        ranges1.append(left)
        j+= 1
    
    if len(ranges0) == len(ranges1):
        return noGaps(ranges0)
    else:
        return mergeAny(ranges1)

def merge2(col1,col2):
    new = merge(col1,col2)
    if div(new)<= (div(col1)*col1["n"])/new["n"]:
        return new
    return None

def merge(col1,col2):
    new= copy(col1)
    if col1["isSym"]:
        for x,n in col2["has"].items():
            add(new,x,n)
    else:
        for n in col2["has"].values():
            add(new,n)
    new["lo"] = min(col["lo"], col2["lo"])
    new["hi"] = max(col1.hi,col2.hi)
    return new

def itself(x):
    return x

def rnd(n, nPlaces=2):
    mult = 10**nPlaces
    return math.floor(n*mult+0.5)/mult

Seed = 937162211

def rint(nlo,nhi):
    return math.floor(0.5+ rand(nlo,nhi))

def rand(nlo=0,nhi=1):
    global Seed
    Seed = (16807*Seed)%2147483647
    return nlo + (nhi+-nlo)*Seed/2147483647

def cliffsDelta(ns1,ns2):
    if len(ns1)>256:
        ns1 =many(ns1,256)
    if len(ns2)>256:
        ns2= many(ns2,256)
    if len(ns1)>10*len(ns2):
        ns1 = many(ns1,10*len(ns2))
    if len(ns2) > 10*len(ns1):
        ns2 = many(ns2,10*len(ns1))
    n,gt,lt = 0,0,0
    for x in ns1:
        for y in ns2:
            n += 1
            if x>y:
                gt+= 1
            if x<y:
                lt += 1
    if abs(lt-gt)/n > the.cliffs:
        return True
    return False
 

