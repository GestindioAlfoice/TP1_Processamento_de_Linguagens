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

    def printHTML(self):
        html=""
        if self.nivel==1:
            if len(self.subtests)>0:
                if self.ok==True:
                    html = '''<div class="test_header_ok">
                                                <h2>''' + self.getPrint() + '''</h2>
                                                <button data-toggle=collapse data-target="#teste''' + str(self.id) + '''" type="button" class="btn btn-success"
                                                    style="transform:translateY(-20%); ">
                                                Ver subtestes
                                                </button>
                                            </div>'''

                    html += '''<div id="teste''' + str(self.id) + '''" class="collapse">'''
                    for sub in self.subtests:
                        html += sub.printHTML()

                    html += '''</div>'''
                else:
                    html = '''<div class="test_header_notok">
                                                <h2>''' + self.getPrint() + '''</h2>
                                                <button data-toggle=collapse data-target="#teste''' + str(self.id) + '''" type="button" class="btn btn-danger"
                                                    style="transform:translateY(-20%); ">
                                                Ver subtestes
                                                </button>
                                            </div>'''

                    html += '''<div id="teste''' + str(self.id) + '''" class="collapse">'''
                    for sub in self.subtests:
                        html += sub.printHTML()

                    html += '''</div>'''
            else:
                if self.ok==True:
                    html='''<div>
                                <div class="test_header_ok">
                                    <h2> '''+ self.getPrint() +'''</h2>
                                </div>
                            </div>'''
                else:
                    html = '''<div>
                                <div class="test_header_notok">
                                    <h2> ''' + self.getPrint() + '''</h2>
                                </div>
                            </div>'''
        else:
            if len(self.subtests) > 0:
                if self.ok== True:
                    margin= (self.nivel-1)*40
                    html+='''<div class="subtest" style="margin-left: '''+str(margin)+'''px">
                                <div class="card w-50">
                                    <div class="subtest_content_ok">
                                        '''+self.getPrint()+'''
                                    </div>
                                </div>
                            </div>'''
                    for sub in self.subtests:
                        html+=sub.printHTML()
                else:
                    margin = (self.nivel - 1) * 40
                    html += '''<div class="subtest" style="margin-left: ''' + str(margin) + '''px">
                                    <div class="card w-50">
                                        <div class="subtest_content_notok">
                                            ''' + self.getPrint() + '''
                                        </div>
                                    </div>
                                </div>'''
                    for sub in self.subtests:
                        html+=sub.printHTML()
            else:
                if self.ok== True:
                    margin = (self.nivel - 1) * 40
                    html += '''<div class="subtest" style="margin-left: ''' + str(margin) + '''px">
                                    <div class="card w-50">
                                        <div class="subtest_content_ok">
                                            ''' + self.getPrint() + '''
                                        </div>
                                    </div>
                                </div>'''
                else:
                    margin = (self.nivel - 1) * 40
                    html += '''<div class="subtest" style="margin-left: ''' + str(margin) + '''px">
                                    <div class="card w-50">
                                        <div class="subtest_content_notok">
                                            ''' + self.getPrint() + '''
                                        </div>
                                    </div>
                                </div>'''
        return html

    def printSTests(self):
        for test_ in self.subtests:
            test_.printTests()




