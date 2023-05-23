import psycopg2

conn = psycopg2.connect(database="db_2020_01", user="db_user2020_20", password="db_user@123"
                       , host="116.205.157.173", port=8000)
cur = conn.cursor()


cur.execute('create table test'
           '('
           'test_id varchar(20) primary key'
           ');')

# # 获取结果
# cur.execute('create table employee'
#            '('
#            'employee_id varchar(20) primary key,'
#            'name varchar(20),'
#            'gender varchar(6),'
#            'age int,'
#            'phone_number varchar(20),'
#            'job varchar(20),'
#            'behave varchar(20),'
#            'attendance int,'
#            'mailbox varchar(20),'
#            'nation varchar(20),'
#            'native_place varchar(20)'
#            ');')
# cur.execute('create table salary'
#            '('
#            'salary_id varchar(20) primary key,'
#            'basic_salary int,'
#            'bonus int,'
#            'share_dividend int,'
#            'deduct_absense int'
#            ');')
# cur.execute('create table project'
#            '('
#            'project_id varchar(20) primary key,'
#            'project_content varchar(1000),'
#            'project_progress varchar(20),'
#            'project_state varchar(20)'
#            ');')
# cur.execute('create table department'
#            '('
#            'depart_id varchar(20) primary key,'
#            'depart_ability varchar(100),'
#            'depart_leader_id varchar(20)'
#            ');')
# cur.execute("alter table employee add salary_id varchar(20)")
# cur.execute("alter table employee add foreign key(salary_id) references salary(salary_id)")
# cur.execute("alter table salary add employee_id varchar(20)")
# cur.execute("alter table salary add foreign key(employee_id) references employee(employee_id)")

# cur.execute('alter table employee add depart_id varchar(20)')
# cur.execute("alter table employee add foreign key(depart_id) references department(depart_id)")
# cur.execute("alter table employee add project_id varchar(20)")
# cur.execute("alter table employee add foreign key(project_id) references project(project_id)")
# results = cur.fetchall()
# print(results)
conn.commit()
conn.close()
