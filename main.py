import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamit")

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

# st.dataframe(df, width=500, height=200)
# st.bar_chart(df)

# df1 = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.dataframe(df1, width=500, height=200)
# st.map(df1)

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

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1, 11))
# )

# 'あなたの好きな数字は、', option, 'です'
# if st.checkbox('Show Image'):
#     img = Image.open('tenjin_4_p6w8ekj7.jpg')
#     st.image(img, caption='under the same sky', use_column_width=True)
