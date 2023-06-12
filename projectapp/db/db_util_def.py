import sqlite3

# db 접속 기능 함수
def getDBConn_Cursor() :
    conn = sqlite3.connect("user.db", isolation_level=None)
    # 커서 획득
    curosr = conn.cursor()

    return conn, curosr

def DBClose(cursor, conn) :

    conn.commit() 
    ### 커서(cursor) 반환하기
    cursor.close()
    
    ### 접속(connect) 접속 해제
    conn.close()

