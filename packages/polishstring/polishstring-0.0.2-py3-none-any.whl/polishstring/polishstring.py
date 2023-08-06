from stringtokenizer import *
def __preposttoin__(s,f):
    if f!='>' and f!='<':
        raise Exception('Invalid Attribute')
    try:
        l=list(s if f=='>' else s[::-1])
        i=0
        while i<len(l)-1:
            ch=l[i+2]
            if ch in '+-*/^':
                k1=l[i+1]
                k2=l[i]
                l[i]='('+((k2+ch+k1) if f=='>' else (k1+ch+k2))+')'
                del l[i+2]
                del l[i+1]
                i=0
            else:
                i+=1
        return l[0]
    except:
        return 'Invalid'
def __bracket__(s,p):
    f=l=-1
    s=s.strip()+' '
    for i in range(len(s)):
        ch=s[i]
        if ch=='(':
            f=i
        elif ch==')':
            l=i
            break
    if f==-1 and l==-1:
        return s
    elif f!=-1 and l!=-1:
        k=__plusminus__(s[f+1:l],p)
        s=s[:f]+__alter__(k,True)+s[l+1:]
    else:
        raise Exception
    return __bracket__(s,p)
def __plusminus__(s,p):
    if len(s)==1:
        if s in '+-*/^':
            raise Exception
        return s
    elif '+' not in s and '-' not in s:
        return __muldiv__(s,p)
    t1=StringTokenizer(s,'+-',True)
    s1=s2=s3=''
    while t1.hasMoreTokens():
        if len(s1)==0:
            s1=t1.nextToken()
            s1=__muldiv__(s1,p)
        s2=t1.nextToken()
        s3=t1.nextToken()
        s3=__muldiv__(s3,p)
        if p:
            s1=s2+s1+s3
        else:
            s1=s1+s3+s2
    return s1
def __muldiv__(s,p):
    if len(s)==1:
        if s in '+-*/^':
            raise Exception
        return s
    elif '*' not in s and '/' not in s and '^' not in s:
        return s
    t1=StringTokenizer(s,'*/^',True)
    s1=s2=s3=''
    while t1.hasMoreTokens():
        if len(s1)==0:
            s1=t1.nextToken()
        s2=t1.nextToken()
        s3=t1.nextToken()
        if p:
            s1=s2+s1+s3
        else:
            s1=s1+s3+s2
    return s1
def __check__(s):
    if len(s)==0:
        return
    prv=s[0]
    for ch in s[1:]:
        if prv=='(' or prv==')' or ch=='(' or ch==')' or prv in '+-*/^' or ch in '+-*/^':
            prv=ch
        else:
            raise Exception
def __alter__(s,k):
    o1='+-*/^'
    o2=chr(156)+chr(157)+chr(158)+chr(159)+chr(160)
    t=''
    for i in s:
        ch=i
        if k:
            if ch in o1:
                ch=o2[o1.index(ch)]
        else:
            if ch in o2:
                ch=o1[o2.index(ch)]
        t+=ch
    return t
def __intoprepost__(s,p):
    try:
        __check__(s)
        s='('+s+')'
        s=__bracket__(s,p)
        s=__alter__(s,False)
        return s
    except Exception:
        return 'Invalid'
def inf_prf(st):
    return __intoprepost__(st,True).strip()
def inf_pof(st):
    return __intoprepost__(st,False).strip()
def prf_inf(st):
    return __preposttoin__(st,'<').strip()
def pof_inf(st):
    return __preposttoin__(st,'>').strip()
def pof_prf(st):
    return inf_prf(pof_inf(st)).strip()
def prf_pof(st):
    return inf_pof(prf_inf(st)).strip()
