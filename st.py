import streamlit as st

# Title of the app
st.title("CGPA Calculator")

# Input fields for SGPA in each semester
a = st.number_input("SGPA in semester 1:", min_value=0.0, max_value=10.0, step=0.01)
b = st.number_input("SGPA in semester 2:", min_value=0.0, max_value=10.0, step=0.01)
c = st.number_input("SGPA in semester 3:", min_value=0.0, max_value=10.0, step=0.01)
d = st.number_input("SGPA in semester 4:", min_value=0.0, max_value=10.0, step=0.01)
e = st.number_input("SGPA in semester 5:", min_value=0.0, max_value=10.0, step=0.01)
f = st.number_input("SGPA in semester 6:", min_value=0.0, max_value=10.0, step=0.01)

# Button to calculate CGPA
if st.button("Calculate CGPA"):
    TOTAL = ((a * 19) + (b * 19) + (c * 23) + (d * 19) + (e * 25) + (f * 21)) / (19 + 19 + 23 + 19 + 25 + 21)
    st.write(f"Your CGPA after 6 semesters is: {TOTAL:.2f}")
