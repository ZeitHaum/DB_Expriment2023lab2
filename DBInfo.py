###提供数据库信息
class DB:
    def __init__ (self,a_lis:list,a_type:list,foreign_mask:list)->None:
        assert(len(a_lis)==len(a_type))
        assert(len(a_lis)==len(foreign_mask))
        self.attribute_list = a_lis
        self.attribute_list_type = a_type
        self.foreign_mask = foreign_mask
    

db_lis = list()
db_name_map = dict()
db_names = [
"Employee",
"SalaryInfo",
"Project",
"Department",
"AttendanceInfo",
"Pacitipate_project"]

db_lis.append(DB(["E_ID","E_NAME","E_AGE","E_PHONE_NUMBER","E_GENDER","E_EMAIL","S_ID","D_ID"],
                 [int,str,int,str,str,str,int,int],
                 [0,0,0,0,0,0,1,1]
                 ))
db_name_map["Employee"] = db_lis[-1]
db_lis.append(DB(["S_ID","BASESAL","EXTRASAL","E_ID"],
                 [int,int,int,int],
                 [0,0,0,1]
                 ))
db_name_map["SalaryInfo"] = db_lis[-1]
db_lis.append(DB(["P_ID","P_NAME","P_CONTENT","P_PROGRESS"],
                 [int,str,str,str],
                 [0,0,0,0]
                 ))
db_name_map["Project"] = db_lis[-1]
db_lis.append(DB(["D_ID","D_NAME","D_ADDR"],
                 [int,str,str],
                 [0,0,0]
                 ))
db_name_map["Department"] = db_lis[-1]
db_lis.append(DB(["A_ID","ARRIVETIME","LEAVETIME","E_ID"],
                 [int,str,str,int],
                 [0,0,0,1]
                 ))
db_name_map["AttendanceInfo"] = db_lis[-1]
db_lis.append(DB(["P_ID","S_ID","E_ID"],
                 [int,int,int],
                 [1,1,1]
                 ))
db_name_map["Pacitipate_project"] = db_lis[-1]