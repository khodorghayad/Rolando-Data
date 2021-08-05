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

st.title("Data")
data=st.file_uploader("Upload a .gz  file")


if data:

    df = pd.read_csv(data, compression='gzip', header=0, sep=',', quotechar='"')
    
    df.columns=["Number"]
    df['Number'] = df['Number'].astype(str)

    # st.table(df.head(10))
    # st.write("Total Count: " + str( df[df.columns[0]].count()))
    user_input = st.text_input("Please enter the value")

    STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
    DOWNLOADS_PATH = (STREAMLIT_STATIC_PATH / "downloads")
    if not DOWNLOADS_PATH.is_dir():
        DOWNLOADS_PATH.mkdir()

    if user_input:
        df["IsDeleted"]=user_input
        st.table(df.head(10))

    if st.button("Download File"):
        st.markdown("Download from [downloads/dndlist.csv.gz](downloads/dndlist.csv.gz)")
        df.to_csv(str(DOWNLOADS_PATH / "dndlist.csv.gz"), index=False,compression="gzip")
