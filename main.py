import streamlit as st
import time

st.title("Streamit入門")

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラムです。')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')


option = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', option

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション', condition
