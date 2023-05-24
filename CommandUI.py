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
        print("输入任意内容回到开始菜单")
        input()
        begin_service()
    
def todo():
    error(False,"该部分未完成!")
    
def deal_service(opt:int,db_name_id:int)->None:
    if(opt==1):
        now_db = db_lis[db_name_id]
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
        print("""
菜单(请选择删除的方式)
1.按主键删除
2.按属性值删除(删除所有属性值为指定值的数据)
3.按属性范围删除(删除所有属性值为指定范围的数据)
4.退出
              """)
        del_opt = int(input())
        error(del_opt>=1 and del_opt<=4,"错误的输入")
        attr = str()
        lval = str()
        rval = str()
        if(del_opt==1):
            print("请输入主键值(名称:{0},类型{1}):".format(db_lis[db_name_id].attribute_list[0],str(db_lis[db_name_id].attribute_list_type[0])),end = "")
            attr = db_lis[db_name_id].attribute_list[0]
            lval = db_lis[db_name_id].attribute_list_type[0](input())
            rval = lval
        elif(del_opt==2):
            available_str = Operations.list_to_tuplestr_withoutSymbol(db_lis[db_name_id].attribute_list)
            print("请输入属性名,可选的属性名有{0}:".format(available_str),end="")
            attr = str(input())
            at_id = db_lis[db_name_id].attribute_list.index(attr)
            print("请输入属性值,属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            lval = db_lis[db_name_id].attribute_list_type[at_id](input())
            rval = lval
            
        elif(del_opt==3):
            available_str = Operations.list_to_tuplestr_withoutSymbol(db_lis[db_name_id].attribute_list) 
            print("请输入属性名,可选的属性名有{0}:".format(available_str),end="")
            attr = str(input())
            at_id = db_lis[db_name_id].attribute_list.index(attr)          
            print("请输入属性下限(包含),属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            lval = db_lis[db_name_id].attribute_list_type[at_id](input())
            print("请输入属性上限(包含),属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            rval = db_lis[db_name_id].attribute_list_type[at_id](input())
        else:
            myexit()
        Operations.delete(db_connection,db_names[db_name_id],attr,lval,rval)
    elif(opt==3):
        #查询
        print("""
菜单(请选择查询的方式)
1.显示该表所有数据
2.按主键查询
3.按属性值查询(查询所有属性值为指定值的数据)
4.按属性范围查询(查询所有属性值为指定范围的数据)
5.退出
              """)
        query_opt = int(input())
        error(query_opt>=1 and query_opt<=4,"错误的输入")
        attr = str()
        lval = str()
        rval = str()
        if(query_opt==1):
            attr = None
        elif(query_opt==2):
            print("请输入主键值(名称:{0},类型{1}):".format(db_lis[db_name_id].attribute_list[0],str(db_lis[db_name_id].attribute_list_type[0])),end = "")
            attr = db_lis[db_name_id].attribute_list[0]
            lval = db_lis[db_name_id].attribute_list_type[0](input())
            rval = lval
        elif(query_opt==3):
            available_str = Operations.list_to_tuplestr_withoutSymbol(db_lis[db_name_id].attribute_list)
            print("请输入属性名,可选的属性名有{0}:".format(available_str),end="")
            attr = str(input())
            at_id = db_lis[db_name_id].attribute_list.index(attr)
            print("请输入属性值,属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            lval = db_lis[db_name_id].attribute_list_type[at_id](input())
            rval = lval
            
        elif(query_opt==4):
            available_str = Operations.list_to_tuplestr_withoutSymbol(db_lis[db_name_id].attribute_list) 
            print("请输入属性名,可选的属性名有{0}:".format(available_str),end="")
            attr = str(input())
            at_id = db_lis[db_name_id].attribute_list.index(attr)          
            print("请输入属性下限(包含),属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            lval = db_lis[db_name_id].attribute_list_type[at_id](input())
            print("请输入属性上限(包含),属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            rval = db_lis[db_name_id].attribute_list_type[at_id](input())
        else:
            myexit()
        Operations.query(db_connection,db_names[db_name_id],attr,lval,rval)
    elif(opt==4):
        #修改
        print("""
菜单(请选择修改的方式)
1.按主键修改
2.按属性值修改(修改所有属性值为指定值的数据)
3.按属性范围修改(修改所有属性值为指定范围的数据)
4.退出
              """)
        up_opt = int(input())
        error(up_opt>=1 and up_opt<=4,"错误的输入")
        attr = str()
        lval = str()
        rval = str()
        new_attr = str()
        new_val = str()
        if(up_opt==1):
            print("请输入主键值(名称:{0},类型{1}):".format(db_lis[db_name_id].attribute_list[0],str(db_lis[db_name_id].attribute_list_type[0])),end = "")
            attr = db_lis[db_name_id].attribute_list[0]
            lval = db_lis[db_name_id].attribute_list_type[0](input())
            rval = lval
            print("请输入要修改的键值名,可选的属性名有{0}:".format(available_str),end="")
            new_attr = str(input())
            print("请输入修改后的属性值,属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            new_val = db_lis[db_name_id].attribute_list_type[at_id](input())
        elif(up_opt==2):
            available_str = Operations.list_to_tuplestr_withoutSymbol(db_lis[db_name_id].attribute_list[1:])
            print("请输入属性名,可选的属性名有{0}:".format(available_str),end="")
            attr = str(input())
            at_id = db_lis[db_name_id].attribute_list.index(attr)
            print("请输入属性值,属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            lval = db_lis[db_name_id].attribute_list_type[at_id](input())
            rval = lval
            print("请输入要修改的键值名,可选的属性名有{0}:".format(available_str),end="")
            new_attr = str(input())
            if(new_attr==db_lis[db_name_id].attribute_list[0]):
                error(0,"不可以修改主键值!")
            print("请输入修改后的属性值,属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            new_val = db_lis[db_name_id].attribute_list_type[at_id](input())
        elif(up_opt==3):
            available_str = Operations.list_to_tuplestr_withoutSymbol(db_lis[db_name_id].attribute_list) 
            print("请输入属性名,可选的属性名有{0}:".format(available_str),end="")
            attr = str(input())
            at_id = db_lis[db_name_id].attribute_list.index(attr)          
            print("请输入属性下限(包含),属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            lval = db_lis[db_name_id].attribute_list_type[at_id](input())
            print("请输入属性上限(包含),属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            rval = db_lis[db_name_id].attribute_list_type[at_id](input())
            print("请输入要修改的键值名,可选的属性名有{0}:".format(available_str),end="")
            new_attr = str(input())
            print("请输入修改后的属性值,属性类型应为{0}:".format(str(db_lis[db_name_id].attribute_list_type[at_id])),end="")
            new_val = db_lis[db_name_id].attribute_list_type[at_id](input())
        else:
            myexit()
        Operations.update(db_connection,db_names[db_name_id],attr,lval,rval,new_attr,new_val)
    elif(opt==5):
        #执行SQL语句
        print("请输入命令:",end="")
        command = str(input())
        db_cursor = db_connection.cursor()
        db_cursor.execute(command)
        db_connection.commit()
        try:
            print(db_cursor.fetchall())
        except:
            pass
        print("Log(SQL): Execution successfully complete.")
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
        if(opt<=4):
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
        else:
            deal_service(opt,None)
        

if __name__ == "__main__":
    begin_service()