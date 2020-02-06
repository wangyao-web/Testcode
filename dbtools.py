import pymysql
def query(sql):
    '''
    这是查询数据库的方法
    '''

    db=pymysql.connect(host="localhost",user="root",password="123456",db="wangyao")
    cursor=db.cursor() #获取游标
    try:
        cursor.execute(sql)
        res=cursor.fetchall()
        return res
    except:
        return"语句写错了，好好写！"


def commit(sql):
    '''
    这是修改、增添数据库的方法
    '''
    

    dbs=pymysql.connect(host="localhost",user="root",password="123456",db="wangyao")
    cursor=dbs.cursor()
    try:
        
        cursor.execute(sql)
        dbs.commit()
        dbs.close()
        return True
    except:
        return False

'''
sql="select *from t_class11;"
res1=query(sql)
print (res1)
'''
sql="update t_student set name='王王王' where id=3;"
res=commit(sql)
print(res)






