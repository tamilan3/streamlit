import streamlit as st
from Database.table import User,cheaker,create_connection, Select
from datetime import datetime
from sqlalchemy import and_
user_id=st.text_input(label="enter id")
if user_id:
    user_id=user_id
    st.write(user_id)
else:
    st.write("")    

option = st.selectbox(
'SELECT YOUR TYPE !',
('login/logout','lunch','break','others'))
st.write('You selected:', option)
left_column,right_column=st.columns(2)
with left_column:
    if user_id and option:
        if st.button(label="START"):
            conn=create_connection()
            users=conn.query(User).filter(User.id==user_id).first()
            if users:
                check = conn.query(cheaker).filter(cheaker.user_id == user_id, cheaker.reason == option).all()
                if check:
                    st.write("you are already login")
                else:  
                    t=datetime.now()
                    start=t.strftime("%Y-%m-%d,%H:%M:%S")
                    user=cheaker(user_id=user_id,start=start,reason=option)
                    conn.add(user)
                    conn.commit()
                    st.write("login initialized")     
            elif not users:
                st.write("you are not a valid user")          
    else:
        st.write("value not provided")              
with right_column:  
    if user_id and option:  
        if st.button(label="END"):
            conn=create_connection()
            users=conn.query(cheaker).filter(cheaker.user_id==user_id).first()
            if users:
                check = conn.query(cheaker).filter(cheaker.reason == option).first()
                date1 = check.start.strftime("%Y-%m-%d")
                date2 =datetime.now().strftime("%Y-%m-%d")
                if check:
                    if date1 == date2:
                        if check.end:
                            st.write("you are logouted")
                        else:
                            check.end=datetime.now()
                            conn.add(check)
                            conn.commit()
                            st.write("time ended succesfully")    
                elif check != True:
                    st.write("it's not true")
            else:
                st.write("you are not authorized to logout")        

# st.title("SQLAlchemy CRUD")

# conn = create_connection()

# name=st.text_input("enter name")
# email=st.text_input("enter email")

# execute,show=st.columns(2)
# with execute:
#     if st.button("add"):
#         if name and email:
#             data=User(id= randint(1,4),name=name,email=email)
#             conn.add(data)
#             conn.commit()
#             st.write("User added on database")
#         else:
#             st.write("Provide correct values")
# with show:
#     if st.button("show"):
#         results =conn.query(User).all()
#         st.table(results)
