import random,pylab
class loc(object):
    def  __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,xc,yc):
        return loc(self.x+xc,self.y+yc)
    def getch(self):
        return self.x,self.y
class dire(object):
    pos=('n','s','e','w')
    def __init__(self,pt):
        if pt in self.pos :
            self.pt=pt
        else: raise ValueError('in dire__init__')
    def move(self,dist):
        if self.pt =='n':return(0,dist)
        elif self.pt =='s':return(0,-dist)
        elif self.pt =='e':return(dist,0)
        elif self.pt =='w':return(-dist,0)

class field(object):
    def __init__(self,drunk,loc):
        self.drunk=drunk
        self.loc=loc
    def move(self,dire,dist):
        oldloc=self.loc
        xc,yc=dire.move(dist)
        self.loc=oldloc.move(xc,yc)
    def getdr(self):
        return self.drunk
    def getloc(self):
        return self.loc
    
class drunk(object):
    def __init__(self,name):
        self.name=name
    def move(self,field,time=1):
        for t in range(time):
            pt=dire(random.choice(dire.pos))
            field.move(pt,1)

def perform(f,time):
    x=[]
    y=[]
    for t in xrange(time):
        x1,y1=f.getloc().getch()
        x.append(x1)
        y.append(y1)
        print x,y
        f.getdr().move(f)
    pylab.plot(x,y)
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.title('Trajectory of the drunk')


##Test case
##d=drunk('shubham')
##f=field(d,loc(0,0))
##perform(f,2)
##pylab.show()

