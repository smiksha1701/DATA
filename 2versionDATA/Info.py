"""Prepared by Orgunova Polina K-10"""
from Exceptions import KeysError, DateFError,DateError,WriteError
import Diagnosis as D
import Checks
class Information:
    """Class which stores every student and count subscriptions"""
    def clear(self):#Function that clears the data of an object
        self.meteo_container=[]
        self.total_entries=0
        self.mwp=0
        self.cdlist=[]
        self.ymdict={}
    def sort(self,container):#The function sorts container according to my var
        date_to_print=[]
        for i in container:
            dateofday=[]
            for x in self.meteo_container:
                if(x.find_date(i)):
                    index=x.date_container.index(i)
                    day=x.date_container[index]
                    if (day.a_p>5):
                        dateofday.append((x.id,day.a_p,day.wp))
            dateofday.sort(key=lambda x: (x[1],x[0]))
            date_to_print.append(dateofday)
        return date_to_print
    def __init__(self):
        self.meteo_container=[]
        self.total_entries=0
        self.mwp=0
        self.cdlist=[]
        self.ymdict={}
    def fits_args(self):#returns arguments to check with json one
        for i in self.meteo_container:
            for date in i.date_container:
                if(date.wp>self.mwp):
                    self.mwp=date.wp
        return self.mwp,self.total_entries
    def AddCalendarDate(self,year,month,day,adt,a_p):
        self.CD=Date(year,month,day)
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
    def load(self,rh,mid,year,a_p,adt,hdt,month,day,mdt,wp):#Function that loads the source data
        self.total_entries+=1
        try:
            error_list=Checks.check_id_keys(mid)
            if any(error_list):
                raise KeysError
            else:
                new_meteo=Meteo(mid)
                if new_meteo not in self.meteo_container: 
                    self.AddCalendarDate(year,month,day,adt,a_p)
                    new_meteo.loadDate(year,month,day,rh,a_p,adt,hdt,mdt,wp)#return
                    self.meteo_container.append(new_meteo)#return
                else:
                    index=self.meteo_container.index(new_meteo) 
                    if self.meteo_container[index].find_date(self.CD):
                        raise DateError
                    else:
                        self.AddCalendarDate(year,month,day,adt,a_p)
                        self.meteo_container[index].loadDate(year,month,day,rh,a_p,adt,hdt,mdt,wp)
        except KeysError as e:
            D.diagnosis.append(e)
            D.errors=("keys",error_list)
            raise
        except DateError as e:
            D.diagnosis.append(e)
            raise

    def find_inf(self):
        ninfo=[]
        for i in self.cdlist: 
            self.aadt=i.sadt/i.nmet
            for j in self.meteo_container:
                if(j.find_date(i)):
                    index=j.date_container.index(i)
                    dateinf=j.date_container[index]
                    if(self.aadt<dateinf.adt):
                        ninfo.append(i)
        date_to_print=self.sort(ninfo)
        return ninfo, date_to_print

    def output(self, coding, fname):#The function responsible for preparing and outputting data to a text document
        self.encoding=coding
        self.fname=fname
        ninfo, date_to_print = self.find_inf()
        try:
            print("output {}: ".format(fname), end='')
            with open(fname, "w", encoding=coding)as f:
                for num, i in enumerate(ninfo):
                    year = i.year
                    month = i.month
                    day = i.day
                    sa_p = self.ymdict[(i.year, i.month)]
                    f.write("{: <5} {: <3} {: <3} {: <5}\n".format(year, month, day, sa_p))
                    x = date_to_print[num]
                    for k in x:
                        mid = k[0]
                        a_p = k[1]
                        wp = k[2]
                        f.write("    {: <13} {: <6} {: <6}\n".format(mid, a_p, wp))
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
        self.date_container=[]
    def __eq__(self,other):#A function that checks if a meteostation already exists
        return self.id == other.id
    def find_date(self,date):#A function that checks if a date already exists in the container
        return date in self.date_container
    def loadDate(self,year,month,day,rh,a_p,adt,hdt,mdt,wp):
        """A function that loads a date and
        information about it into a date container"""
        try:
            error_list=Checks.check_Date(year, month, day)
            if any(error_list):
                raise DateFError
            else:
                date=DateInfo(year,month,day)
                date.Load_date_info(rh,a_p,adt,hdt,mdt,wp)
                self.date_container.append(date)
                return adt
        except DateFError as e:
            D.diagnosis.append(e)
            D.errors=("date_error",error_list)
            raise
class Date():
    """Class which stores mark info"""
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def sumofdt(self,adt):
        self.sadt=adt
        self.nmet=1
    def add_adt(self,adt):
        self.sadt+=adt
        self.nmet+=1
    def __eq__(self,other):
        return self.year==other.year and self.month==other.month and self.day==other.day
class DateInfo(Date):
    def Morethanfive(self):
        return
    def Load_date_info(self,rh,a_p,adt,hdt,mdt,wp):
        self.rh=rh
        self.a_p=a_p
        self.adt=adt
        self.hdt=hdt
        self.mdt=mdt
        self.wp=wp