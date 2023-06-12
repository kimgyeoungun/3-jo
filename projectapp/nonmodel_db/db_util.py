import sqlite3

class DB_Util :

    ### 생성자 정의하기
    def __init__(self):
        ### 클래스 생성과 동시에 DB 연결 및 커서 받아오는 기능 수행
        self.getDBConn_Cursor()

    ##### - DB접속 기능 함수 정의
    def getDBConn_Cursor(self) :
        self.conn  = sqlite3.connect('./db.sqlite3')
        self.cursor = self.conn.cursor()


  ##### - 데이터 입력(C), 수정(U), 삭제(D) 처리 기능 정의
    def setCUD(self, sql):
        ### 구문 실행하기
        self.cursor.execute(sql)

        ### 데이터 수정/삭제/입력 시에 아래 적용해야함
        self.conn.commit()
 
        ### DB 접속 해제하기
        self.DBClose()


    ##### - 커서 및 connect 접속 해제하는 기능 정의
    def DBClose(self) :
        ### 커서(cursor) 반환하기
        self.cursor.close()
        
        ### 접속(connect) 접속 해제
        self.conn.close()