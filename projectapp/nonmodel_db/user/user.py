from projectapp.nonmodel_db import db_sql


### 입력 처리하기
def setUserInsert(id,name,gender,email,pw) :
    ### 구문 작성
    sql = """
            Insert Into user Values (
                '{}', '{}', '{}', '{}', '{}'
            )
    """.format(id,name,gender,email,pw)

    return db_sql.setCUD(sql)

### 회원 전체 조회하기
def getAllId() :

    ### 구문 작성
    sql = """
        Select user_id
        From user
    """

    return db_sql.getList(sql)