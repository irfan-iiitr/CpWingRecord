import streamlit as st
import gspread
import pandas as pd

st.write("Hello, world!")

users=['Irfan', 'Keshav']
passwords={'Irfan':'1231','Keshav':'321'}

login=False

def dataa(nx,newy,today):
    st.write("hello")


def display(name,marks,prevmarks):
    st.write("Display")
    gc=gspread.service_account(filename="C:\\Users\\dell\\Desktop\\s\\cp-record-bf5048351612.json")
    sh=gc.open_by_key("1zKYFxWl2AIXbwG-uwE26uGtt5p3TiTUU1c2fyM9nJ0g")
    current_sheet=sh.worksheet("Sheet1")
    x=pd.DataFrame(current_sheet.get_all_values())
    # st.dataframe(x)
    cell = current_sheet.find(name)
    values_list = current_sheet.col_values(cell.col)

    # st.write(values_list)
    l=len(values_list)


    newx=cell.col
    nx=int(newx)
    newy=l
    # st.write(nx,l,marks)

    
    current_sheet.update_cell(l+1,nx,marks)
    if prevmarks:
        current_sheet.update_cell(l,nx,prevmarks)
    x=pd.DataFrame(current_sheet.get_all_values())
    st.table(x)
    st.write("updated")

    




def generate_login_form():
    # Create a form with two input fields for name and password
    name = st.text_input("Enter your name")
    password = st.text_input("Enter your password", type="password")
    marks=st.text_input("Enter todays marks")
    prevmarks=st.text_input("update last days marks or else leave blank")

    # Print the user inputs
    if st.button("Submit"):
        if name in users:
            if password == passwords[name]:
                login=True
                st.write("Correct")
                display(name,marks,prevmarks)
            else:
                st.write("Wrong password")
        else:
            st.write("Wrong username or password")

# Call the function to display the login form
generate_login_form()



