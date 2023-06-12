import db_util_def as db_util


# 회원 가입 함수
def signUp():
    ### DB 접속 정보 받아오기
    conn, cursor = db_util.getDBConn_Cursor()    

    sql='''
    INSERT INTO table1 
    VALUES('id4', 'LEE', 'male', 'as@naver.com',  'pw1')
    '''
    # 구문 실행
    cursor.execute(sql)

    ### DB 접속 해제하기
    db_util.DBClose(cursor, conn)

def getView() :
    ### DB 접속 정보 받아오기
    conn, cursor = db_util.getDBConn_Cursor()

    sql = """
        Select id From table1 
    """

    ### 구문 실행하기
    cursor.execute(sql)

    ### 결과 추출하기
    a = cursor.fetchall()

    ### DB 접속 해제하기
    db_util.DBClose(cursor, conn)

    return a

print(getView())


