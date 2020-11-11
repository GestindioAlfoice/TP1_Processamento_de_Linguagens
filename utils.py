# As nossas funções uteis

def readFile(filename):
    fh = open(filename, mode="r")
    contents = fh.read()
    fh.close()
    return contents

def getNivel(string):
    ws = len(string) - len(string.lstrip())
    ws=ws/4
    ws+=1
    return int(ws)



class Test:
    def __init__(self, id, ok, desc,nivel):
        self.id = id
        self.ok = ok
        self.desc = desc
        self.nivel=nivel
        self.subtests=[]

    def getPrint(self):
        if self.ok:
            return "ok %s - %s" % (self.id, self.desc)
        else:
            return "not ok %s - %s" % (self.id, self.desc)

    def printTests(self):
        tabs=""
        for x in range(self.nivel-1):
            tabs += "\t"
        print("%s%s"% (tabs,self.getPrint()))
        if self.subtests:
            self.printSTests()

    def printSTests(self):
        for test_ in self.subtests:
            test_.printTests()




