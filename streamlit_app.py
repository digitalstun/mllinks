import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

# st.write("[![Star](https://github.com/digitalstun)")
st.write("[![Star](https://img.shields.io/github/stars/digitalstun/mllinks.svg?logo=github&style=social)](https://gitHub.com/digitalstun/mllinks)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('randy.png'))

st.header('Randolph Lafayette')

st.info('Developer, Film Director, Cinematographer, AI Advocate & Support Specialist')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/channel/UCnAUn4WRpHu6Y7XR0O26iEQ', 'Cinematography and Film YouTube', icon_size)
# st_button('Shop', 'https://mrlafayette.bigcartel.com/products', 'Shop T-Shirts, Prints & Apparel', icon_size)
# st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
# st_button('medium', 'https://', 'Read my blogs, icon_size)
st_button('twitter', 'https://twitter.com/digitalstun', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/randolph-lafayette-303721139/', 'Follow me on LinkedIn', icon_size)
# st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
# st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
