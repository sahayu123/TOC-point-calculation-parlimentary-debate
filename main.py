import streamlit as st
from problem import Calculate_Toc
st.header("TOC Point Calculator")
st.subheader("Parlimentary Debate")
url=st.text_input("Enter Tabroom link for tournament : ")
col1, col2 = st.columns(2)
with col1: 
    submit=st.button("Calculate")
if submit:
    with col2:
        prog=st.progress(0, text="Starting Point Calculation")
    if url:
        point_calc=Calculate_Toc(url)
        prog.progress(33, text="Retrieving Data...")
        points=point_calc.get_toc_points(prog)
        if points==None:
            st.write("Error, unable to access server")
            st.write("Check if the link is correct")
        else:
            print("Points", points)
            count=0
            lst=["Champion", "Second Place", "Semi Finals", "Quarter Finals", "Octo Finals", "Double Octo Finals", "Triple Octo Finals"]
            for p in points: 
                with col1:
                    st.write(lst[count]+ " : ")
                with col2:
                    st.write(str(p) + " points")
                count=count+1
            prog.progress(100, text="Completed Point Calculation")




