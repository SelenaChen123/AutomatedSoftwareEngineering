import math

def COL(n, s):
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

def NUM(n=None, s=None):
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

# Create a `SYM` to summarize a stream of symbols.
def SYM(n=None, s=None):
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

def RANGE(at, txt, lo, hi=None):
    d =  {"at": at, "txt": txt, "lo": lo, "y": SYM()}
    if hi is None:
        d["hi"] =  lo 
    else:
        d["hi"] = hi
    return d

def DATA_new():
    return {"rows": [], "cols": None}

def DATA_read(sfile):
    data = DATA_new()
    # csv(sfile, lambda t: row(data, t))
    return data

def DATA_clone(data, ts=None):
    data1 = row(DATA_new(), data["cols"]["names"])
    if ts == None:
        ts = []
    for t in ts:
        row(data1, t)
    return data1

def row(data, t):
    if data["cols"]:
        data["rows"].append(t)
        for cols in [data["cols"]["x"], data["cols"]["y"]]:
            for col in cols:
                add(col, t[col["at"]])
    else:
        data["cols"] = COLS(t)
    return data


def add(col, x, n=None):
    if x != "?":
        n = n or 1
        col["n"] += n
        if col["isSym"]:
            if col["has"][x]:
                col["has"][x] += n
            else:
                col["has"][x] = n
            if col["has"][x] > col["most"]:
                col["most"], col["mode"] = col["has"][x], x
        else:
            
            col["lo"] = min(x, col["lo"])
            col["hi"] = max(x, col["hi"])
            all = len(col["has"])
            
            if all < the.Max:
                pos = all + 1
            else:
                if rand() < the.Max / col["n"]:
                    pos = rint(1, all)
                else:
                    pos = None
            if pos:
                col["has"][pos] = x
                col["ok"] = False

def adds(col, t):
    if t == None:
        t = []
    for x in t:
        add(col, x)
    return col

def extend(Range, n, s):
    Range["lo"] = min(n, Range["lo"])
    Range["hi"] = max(n, Range["hi"])
    add(Range["y"], s)

