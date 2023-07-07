import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/digitalstun/mllinks.svg?logo=github&style=social)](https://gitHub.com/digitalstun/mllinks)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('randy.png'))

st.header('Randolph Lafayette')

st.info('Developer, Director, Cinematographer, AI Advocate & Support Specialist')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/channel/UCnAUn4WRpHu6Y7XR0O26iEQ', 'Cinematography and Film', icon_size)
st_button('bigcartel', 'https://mrlafayette.bigcartel.com/products', 'Visit Big Cartel Store', 16)
st_button('instagram', 'https://www.instagram.com/mr_lafayette', 'Follow me on Instagram', '24')
st_button('twitter', 'https://twitter.com/digitalstun', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/randolph-lafayette-303721139/', 'Follow me on LinkedIn', icon_size)
# st_button('medium', 'https://', 'Read my blogs, icon_size)
# st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
# st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
