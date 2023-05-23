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
    
