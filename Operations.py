from DBInfo import db_name_map
import psycopg2
def list_to_tuplestr(lis)->str:
    return str(tuple(lis))

#不要引号
def list_to_tuplestr_withoutSymbol(lis)->str:
    ret_str = "("
    for i in range(len(lis)):
        if(i!=0):
            ret_str+=","
        ret_str += str(lis[i])
    ret_str+=")"
    return ret_str

def add(db_connection,db_name:str,values:list,attr_lis)->None:
    command = "INSERT INTO " + db_name + list_to_tuplestr_withoutSymbol(attr_lis)  + "VALUES " + list_to_tuplestr(values)
    print("Log(add): add command:{0}".format(command))
    db_cursor = db_connection.cursor()
    db_cursor.execute(command)
    db_connection.commit()
    print("Log(add): add successfully!")

def delete(db_connection,db_name:str,attr:str,lval:str,rval:str)->None:
    command = ""
    if(lval==rval and type(lval)!=int):
        command = "DELETE FROM " + db_name + " WHERE " + attr + " =  \'" + str(lval) + "\'"
    else:
        command = "DELETE FROM " + db_name + " WHERE " + attr + " >= " + str(lval) + " AND " + attr + " <= " + str(rval)
    print("Log(del): delete command:{0}".format(command))
    db_cursor = db_connection.cursor()
    db_cursor.execute(command)
    db_connection.commit()
    print("Log(del): delete successfully!")
    
def query(db_connection,db_name:str,attr:str,lval:str,rval:str)->None:
    command = ""
    if(attr == None):
        command = "SELECT * from " + db_name
    else:
        if(lval==rval and type(lval)!=int):
            command = "SELECT * from " + db_name + " WHERE " + attr + "= \'" + str(lval) + "\'"
        else:
            command = "SELECT * from " + db_name + " WHERE " + attr + ">=" + str(lval) + " AND " + attr + " <= " + str(rval)
    print("Log(query): query command:{0}".format(command))
    db_cursor = db_connection.cursor()
    db_cursor.execute(command)
    db_connection.commit()
    print("查找结果:" + str(db_cursor.fetchall()))
    print("Log(query): query successfully complete.")
    
def update(db_connection,db_name:str,attr:str,lval:str,rval:str,new_attr:str,new_val:str)->None:
    command = ""
    if(lval==rval and type(lval)!=int):
        command = "UPDATE " + db_name + " SET " + str(new_attr) + " = " + str(new_val) + " WHERE " + attr + " = \'" + str(lval) + "\'"
    else:
        command = "UPDATE " + db_name + " SET " + str(new_attr) + " = " + str(new_val) + " WHERE " + attr + " >= " + str(lval) + " AND " + attr + " <= " + str(rval)
    print("Log(update): query command:{0}".format(command))
    db_cursor = db_connection.cursor()
    db_cursor.execute(command)
    db_connection.commit()
    print("Log(update): query successfully complete.")