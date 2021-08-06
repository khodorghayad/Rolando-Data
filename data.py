import streamlit as st
import pandas as pd
import pathlib
st.set_page_config (page_title="Data")
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
<title>
Data
</title>

"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("DND LIST")
data=st.file_uploader("Upload a .gz  file",type="gz")


if data:
    # file_name=data.name
    # file_extension= file_name.split('.')[-1]
    
    df = pd.read_csv(data, compression='gzip', header=0, sep=',', quotechar='"')
    
    df.columns=["Number"]
    df['Number'] = df['Number'].astype(str)
    df.drop_duplicates('Number',inplace=True)
    st.table(df.head(10))
    st.write("Total Count: " + str( df[df.columns[0]].count()))
    options=['0','1']
    
    user_input =st.selectbox("Select a value for IsDeleted",  options)



    if user_input:
        df["IsDeleted"]=user_input
        st.table(df.head(10))

    STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
    DOWNLOADS_PATH = (STREAMLIT_STATIC_PATH / "downloads")
    if not DOWNLOADS_PATH.is_dir():
        DOWNLOADS_PATH.mkdir()

    if st.button("Download File"):
        if st._is_running_with_streamlit:
            st.markdown("Click on the link to start downloading [downloads/dndlistupdated.csv.gz](downloads/dndlistupdated.csv.gz)")
        else :
            df.to_csv(str(DOWNLOADS_PATH / "dndlistupdated.csv.gz"), index=False)

        
        

