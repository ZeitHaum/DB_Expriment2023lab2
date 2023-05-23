from DBInfo import db_lis
from DBInfo import db_names
import psycopg2
import Operations

#建立连接
db_connection = psycopg2.connect(database="db_2020_01", user="db_user2020_20", password="db_user@123"
                       , host="116.205.157.173", port=8000) #填入对应的参数
def myexit():
    db_connection.close()
    exit()

def isnum(string):
    try:
        float(string)
        return True
    except:
        return False

def error(bl:bool,error_msg:str)->None:
    if(not bl):
        print("Error! "+ error_msg)
    assert(bl)
    
def todo():
    error(False,"该部分未完成!")
    
def deal_service(opt:int,db_name_id:int)->None:
    now_db = db_lis[db_name_id]
    if(opt==1):
        #增添
        print("请输入{0}属性值(注意外键应确保存在,否则请输出null)".format(db_names[db_name_id]))
        val_lis = []
        attr_lis = []
        for xi in range(len(now_db.attribute_list)):
            print(xi+1,end=".")
            print(now_db.attribute_list[xi],end="")
            if(now_db.foreign_mask[xi]==1):
                print("[外键]",end = "")
            print(" ",end="")
            val_s = input()
            if(val_s!="null"):
                val = now_db.attribute_list_type[xi](val_s)
                val_lis.append(val)
                attr_lis.append(now_db.attribute_list[xi])
        Operations.add(db_connection,db_names[db_name_id],val_lis,attr_lis)
            
    elif(opt==2):
        #删除
        todo()
    elif(opt==3):
        #查询
        todo()
    elif(opt==4):
        #修改
        todo()
    elif(opt==5):
        #执行SQL语句
        todo()
    else:
        error(0)
    print("输入任意内容回到开始菜单")
    input()
    begin_service()
    
def begin_service():
    print("""
菜单(请输入序号选择对应的操作):
1.增添
2.删除
3.查询
4.修改
5.执行SQL语句
6.退出
          """)
    opt = int(input())
    error(opt>=1 and opt<=6,"错误的输入!")
    db_name_id = 0
    if(opt==6):
        myexit()
    else:
        print("""
菜单(请选择数据库表):
1.Employee
2.SalaryInfo
3.Project
4.Department
5.AttendanceInfo
6.Pacitipate_project
7.退出程序    
              """)
        db_name_id = int(input())
        error(opt>=1 and opt<=7,"错误的输入")
        if(db_name_id==7):
            myexit()
        else:
            deal_service(opt,db_name_id-1)
        

if __name__ == "__main__":
    begin_service()