from projectapp.nonmodel_db import db_sql


### 입력 처리하기
def setUserInsert(id,pw,name) :
    ### 구문 작성
    sql = """
            Insert Into user (
                user_id, user_pw, user_name
            ) Values (
                '{}', '{}', '{}'
            )
    """.format(id,pw,name)

    return db_sql.setCUD(sql)
