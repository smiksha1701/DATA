"""Prepered by Sakevich Michael K-11"""
from exceptions import KeysError, DataFError,DataError,WriteError
import Diagnosis as D
import checker
class Information:
    """Class which stores every student and count subscriptions"""
    def sort(self,container):#sorts container according to my var 
        data_to_print=[]
        for i in container:
            dataofday=[]
            for x in self.meteo_container:
                if(x.find_data(i)):
                    index=x.data_container.index(i)
                    day=x.data_container[index]
                    if (day.a_p>5):
                        dataofday.append((x.id,day.a_p,day.wp))
            dataofday.sort(key=lambda x: (x[1],x[0]))
            data_to_print.append(dataofday)
        return data_to_print
    def __init__(self):
        self.meteo_container=[]
        self.total_enties=0
        self.mwp=0
        self.cdlist=[]
        self.ymdict={}
    def clear(self):#clears Information data
        self.meteo_container=[]
        self.total_enties=0
        self.mwp=0
        self.cdlist=[]
        self.ymdict={} 
    def fits_args(self):#returns arguments to check with json one
        for i in self.meteo_container:
            for date in i.data_container:
                if(date.wp>self.mwp):
                    self.mwp=date.wp
        return self.mwp,self.total_enties
    def AddCalendarData(self,year,month,day,adt,a_p):
        self.CD=Data(year,month,day)
        if(self.CD in self.cdlist):
            index=self.cdlist.index(self.CD) 
            self.cdlist[index].add_adt(adt)
        else:
            self.CD.sumofdt(adt)
            self.cdlist.append(self.CD)
        if((year,month) not in self.ymdict): 
            self.ymdict[(year,month)]=a_p
        else:
            self.ymdict[(year,month)]+=a_p
    def input(self,rh,mid,year,a_p,adt,hdt,month,
    day,mdt,wp):#Fills Information
        self.total_enties+=1
        try:
            error_list=checker.check_keys(mid)
            if any(error_list):
                raise KeysError
            else:
                new_meteo=Meteo(mid)
                if new_meteo not in self.meteo_container: 
                    self.AddCalendarData(year,month,day,adt,a_p)
                    new_meteo.loadData(year,month,day,rh,a_p,adt,hdt,mdt,wp)#return
                    self.meteo_container.append(new_meteo)#return
                else:
                    index=self.meteo_container.index(new_meteo) 
                    if self.meteo_container[index].find_data(self.CD):
                        raise DataError
                    else:
                        self.AddCalendarData(year,month,day,adt,a_p)
                        self.meteo_container[index].loadData(year,month,day,rh,a_p,adt,hdt,mdt,wp)
        except KeysError as e:
            D.diagnosis.append(e)
            D.errors=("keys_error",error_list)
            raise
        except DataError as e:
            D.diagnosis.append(e)
            raise
    def _output(self, coding, fname):#Doing everything to output answer
        self.encoding=coding
        self.fname=fname

        ninfo=[]
        
        for i in self.cdlist: 
            self.aadt=i.sadt/i.kmet
            for j in self.meteo_container:
                if(j.find_data(i)):
                    index=j.data_container.index(i)
                    datainf=j.data_container[index] 
                    if(self.aadt<datainf.adt):
                        ninfo.append(i)
        data_to_print=self.sort(ninfo)
        try:
            print("output {}: ".format(fname), end='')
            with open(fname,"w",encoding=coding)as f:
                for num,i in enumerate(ninfo):
                    year=i.year
                    month=i.month
                    day=i.day
                    sa_p=self.ymdict[(i.year,i.month)]
                    f.write("{: <5} {: <3} {: <3} {: <5}\n".format(year,month,day,sa_p))
                    x=data_to_print[num]
                    for k in x:
                        mid=k[0]
                        a_p=k[1]
                        wp=k[2]
                        f.write("                  {: <13} {: <6} {: <6}\n".format(mid,a_p,wp))
            print("OK")
        except WriteError as e:
            D.diagnosis.append(e)
            D.errors
class Meteo:
    """Class which contains all marks of student it FC and group
    and needed information about him(her)(rating, if he(she) has no "tails" 
    and how many mark 3 he(she) has"""
    def __init__(self,id):
        self.id=id
        self.data_container=[]
    def __eq__(self,other):#To check if student exists already 
        return self.id == other.id
    def find_data(self,data):#finds if this course is already in students marks
        return data in self.data_container
    def loadData(self,year,month,day,rh,a_p,adt,hdt,mdt,wp):#fills mark of student
        try:
            error_list=checker.check_Data(year,month,day)
            if any(error_list):
                raise DataFError
            else:
                data=DataInfo(year,month,day)
                data.Load_data_info(rh,a_p,adt,hdt,mdt,wp)
                self.data_container.append(data)
                return adt
        except DataFError as e:
            D.diagnosis.append(e)
            D.errors=("data_error",error_list)
            raise
class Data():
    """Class which stores mark info"""
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def sumofdt(self,adt):
        self.sadt=adt
        self.kmet=1
    def add_adt(self,adt):
        self.sadt+=adt
        self.kmet+=1
    def __eq__(self,other):
        return self.year==other.year and self.month==other.month and self.day==other.day
class DataInfo(Data):
    def Morethanfive(self):
        return
    def Load_data_info(self,rh,a_p,adt,hdt,mdt,wp):
        self.rh=rh
        self.a_p=a_p
        self.adt=adt
        self.hdt=hdt
        self.mdt=mdt
        self.wp=wp