from Database.table import create_connection,cheaker
from sqlalchemy import and_
from datetime import datetime


con=create_connection()

user_id = 1
reason = "lunch"
check = con.query(cheaker).filter(and_(cheaker.user_id == user_id, cheaker.reason == reason)).first()

date = check.start.strftime("%Y-%m-%d")

check.end = date

con.add(check)
con.commit()

print(date)

