import streamlit as st
import pandas as pd
import pathlib
st.title("Data")
data=st.file_uploader("Upload a .csv or an excel file")
STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
DOWNLOADS_PATH = (STREAMLIT_STATIC_PATH / "downloads")
if not DOWNLOADS_PATH.is_dir():
    DOWNLOADS_PATH.mkdir()

if data:
    format=data.name
    if format.split('.')[-1]== 'csv':
        df= pd.read_csv(data)
        
    elif format.split('.')[-1]== 'xlsx':
        df=pd.read_excel(data)

    else:
        st.warning("You need to upload a .csv or an excel file.")

    df.columns=["Number"]
    df['Number'] = df['Number'].astype(str)

    st.table(df.head(10))
    st.write("Total Count: " + str( df[df.columns[0]].count()))
    user_input = st.text_input("Please enter the value")
    if user_input:
        df["IsDeleted"]=user_input
        st.table(df.head(10))

    if st.button("Download File"):
        st.markdown("Download from [downloads/mydata.csv](downloads/mydata.csv)")
        df.to_csv(str(DOWNLOADS_PATH / "mydata.csv"), index=False)