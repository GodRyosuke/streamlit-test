import streamlit as st
import mysql.connector

# connection = connection = mysql.connector.connect(host='192.168.2.2',
#                                                   user='wander',
#                                                   password='password',
#                                                   database='streamlit_database')
# mysqlとの接続
@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])
conn = init_connection()

@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from pets;")

# Print results.
for row in rows:
    st.write(f"{row[1]} has a :{row[2]}:")
    
st.title("ワンダーのアプリ")
st.caption('これはテスト用で開発したWebアプリです。')
st.subheader('環境構築')
st.text('研究室でロボットを用いた自動溶接作業を開発しています')


with st.form(key='profile_form'):
    name = st.text_input('名前')
    address = st.text_input("住所")

    submit_button = st.form_submit_button('送信')
    cancel_button = st.form_submit_button('キャンセル')
    if (submit_button):
        st.text(f'ようこそ{name}さん！{address}が登録されました！')

code = '''
#include <iostream>
int main(int argc ,char** argv)
{
    std::cout << "hello world\\n";
    return 0;
}

'''
st.code(code, language='cpp')
st.text('開発で使用したdocker fileは次のようになります。')
code = '''
FROM python:3.10
RUN apt-get update && apt-get install -y --no-install-recommends \\
    apt-utils git curl vim unzip openssh-client wget \\
    build-essential cmake \\
    libopenblas-dev \\
    libglib2.0-0 \\
    libsm6 \\
    libxext6 \\
    libxrender-dev \\
    sudo

RUN sudo apt-get upgrade -y && sudo apt-get update
RUN pip install --upgrade pip
RUN pip install streamlit
'''
st.code(code, language='docker')
