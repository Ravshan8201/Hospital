import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
F_Name STRING ,
Phone_Num INTEGER,
DOM STRING,
ZAKAZ STRING,
DAY_ STRING,
TIME_ STRING,
Lang INTEGER ,
Stage INTEGER

)
""")
first_insert = """
INSERT INTO Users VALUES ("{}", " ", " ", " ", " ", " ", " ", " ", "{}")
"""
upd_DAY_ = """
UPDATE Users 
SET DAY_ = "{}" 
WHERE TG_ID = "{}"
"""
select_DAY_ = """
SELECT DAY_
From Users
WHERE TG_ID = "{}"
"""

upd_TIME_ = """
UPDATE Users 
SET TIME_ = "{}" 
WHERE TG_ID = "{}"
"""
select_TIME_ = """
SELECT TIME_
From Users
WHERE TG_ID = "{}"
"""

upd_DOM = """
UPDATE Users 
SET DOM = "{}" 
WHERE TG_ID = "{}"
"""
select_DOM = """
SELECT DOM
From Users
WHERE TG_ID = "{}"
"""



get_id = """
SELECT TG_ID 
FROM Users
Where TG_ID = "{}"
"""
upd_name = """
UPDATE Users 
SET F_Name = "{}" 
WHERE TG_ID = "{}"
"""
select_name = """
SELECT F_Name
From Users
WHERE TG_ID = "{}"
"""

update_phone_num = """
UPDATE Users 
SET Phone_Num = "{}"
WHERE TG_ID = "{}"
"""
select_num = """
SELECT Phone_Num 
FROM Users
WHERE TG_ID = "{}"
"""


lang = """
UPDATE Users
SET lang = "{}"
WHERE TG_ID = "{}"
"""
lang_select = """
SELECT Lang
FROM Users
WHERE TG_ID = "{}"
"""

stagee = """
UPDATE Users
SET Stage = "{}"
WHERE TG_ID = "{}"
"""
stage = """
SELECT Stage
FROM Users
WHERE TG_ID = "{}"
"""

upd_ZAKAZ = """
UPDATE Users
SET ZAKAZ = "{}"
WHERE TG_ID = "{}"
"""
select_ZAKAZ = """
SELECT ZAKAZ
FROM Users
WHERE TG_ID = "{}"
"""
conn.commit()
