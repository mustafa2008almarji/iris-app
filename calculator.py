import streamlit as st
def calculate_emi(p,n,r):
	  emi= p*(r/100)*((1+(r/100)**n)/(((1+(r/100))**n)-1)
    st.write("emi",emi)
st.title("emi calculator")
p=st.slider("principal",1000,1000000)
tenure=st.slider("loan period",1,30)
roi=st.slider("Rate of interset in %",1,15)
r=roi/12
n=tenure*12
if st.button("calculate emi"):
  calculate_emi(p,n,r)