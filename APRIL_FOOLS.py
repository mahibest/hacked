import streamlit as st
import time
st.set_page_config("hacked")
def is_april_fools():
    st.write("To fix the hacked computer you must delete whole os and restart to get a new fresh one.")
    if st.button("delete os and all its contents"):
        st.write("deleting app")
        time.sleep(3)
        return True
    else:
        return False
if is_april_fools():
    st.balloons()
    st.header("April Fools 🤣")
    f"p.s today is April 1st"
    "from mahilini 😜"
