from time import time

class time_tracker:
    def __init__(self):
        self.data = {}
        self.ctr = 1

    def time_diff(self,lst,col=1):
        diff = None
        #for i in range(len(lst)-1,-1,-1):
        #    tmp = lst[i][col]
        #    diff = diff-tmp if diff is not None else tmp
        diff = lst[-1][col]-lst[0][col]
        return diff

    def note_time(self,what,info):
        if not self.data.get(what):
            self.data[what]={'index':self.ctr,'info':[]}
            self.ctr += 1
        self.data[what]['info'].append([info,time()])

    def calculate(self):
        for what in self.data.keys():
           self.data[what]['time'] = self.time_diff(self.data[what]['info'],1)

    def sort(self):
        sd = {}
        for item in self.data.items():
            sd[item[1]['index']] = item
        sk = list(sd.keys())
        sk.sort()
        sorted_data = []
        for k in sk:
            sorted_data.append(sd[k])
        self.sorted_data = sorted_data

    def print_summary(self):
        if not self.sorted_data:
            return
        for sd in self.sorted_data: #this is a list
            print(sd[0],':',sd[1]['time'],'seconds')

    def summary(self):
        self.calculate()
        self.sort()
        self.print_summary()


#from time_tracker import time_tracker as tcc
#tc = tcc()
#tc.note_time('hello','begin')
#tc.note_time('hello','begin oo')
#tc.note_time('hello','begin end')
#tc.note_time('hello1','begin')
#tc.note_time('hello1','begin end')
#tc.summary()


from time_tracker import time_tracker as tcc
tc = tcc()
tc.note_time('hello1','begin')
tc.note_time('hello1','begin end')
tc.summary()
