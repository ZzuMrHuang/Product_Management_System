from PyQt5.QtSql import QSqlQuery
from Utils import openDB
import time


#登录成功时，插入数据
def insert_info(userId):
    db = openDB()
    query = QSqlQuery()
    LoginTime = time.strftime("%Y-%m-%d %H:%M:%S")
    insert_sql = "INSERT INTO Login_info (id,userId,loginTime,isLogining) VALUES (NULL,'%s', '%s','%s')"% \
                 (userId, LoginTime, True)
    print(insert_sql)
    query.exec(insert_sql)
    db.commit()
    db.close()

#退出登录时,将此登录用户的登陆状态改为False
def update_currentLoginState():
    db = openDB()
    query = QSqlQuery()
    search_sql = "SELECT * FROM Login_info WHERE isLogining ='%s'"% True
    query.exec_(search_sql)

    if (query.next()):
        thisId = query.value(0)
        update_sql = "UPDATE Login_info SET isLogining = '%s' WHERE id='%s'" % (False, thisId)
        query.exec_(update_sql)
    else:
        print('....')

    db.commit()
    db.close()

#获取当前用户id，返回用户id
#返回值：用户id
def getCurrentUserId():
    db = openDB()
    query = QSqlQuery()
    search_sql = "SELECT * FROM Login_info WHERE isLogining='%s'"% True

    query.exec_(search_sql)
    if(query.next()):
        userid = query.value(1)
        db.commit()
        db.close()
    else:
        userid = -1
    return userid

#删除登录时间时间超过一个月的数据记录
def delOverOneMonthItem():
    db = openDB()
    query = QSqlQuery()
    #获取前一个月的时间
    struct_time = ( time.localtime().tm_year,time.localtime().tm_mon-1,time.localtime().tm_mday,
                    time.localtime().tm_hour,time.localtime().tm_min,time.localtime().tm_sec,
                    time.localtime().tm_wday,time.localtime().tm_yday,time.localtime().tm_isdst
                   )
    OneMonthAgo = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)

    delete_sql = "DELETE FROM Login_info WHERE loginTime < '%s'" %OneMonthAgo
    query.exec_(delete_sql)
    db.commit()
    db.close()


# if __name__ == "__main__":
#     delOverOneMonthItem()