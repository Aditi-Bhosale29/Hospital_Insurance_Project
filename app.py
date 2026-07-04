import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

#st.title("Insurance Price Prediction App")
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Insurance Price Predictor",
    page_icon="💰",
    layout="wide"
)
# ---------------- TITLE ----------------
st.markdown(
"""
# 🏥 Insurance Price Prediction

### Predict your Insurance Charges instantly 
"""
)
st.write("---")
#---------------- LOAD MODEL ----------------
df = pd.read_csv("insurance.csv")

model = pickle.load(open("model.pkl", "rb"))

# ---------------- SIDEBAR ----------------

st.sidebar.header("📋 Customer Details")

age = st.sidebar.selectbox(
    "👤 Age",
    sorted(df["age"].unique())
)

sex = st.sidebar.selectbox(
    "🚻 Gender",
    ["male", "female"]
)

bmi = st.sidebar.number_input(
    "⚖ BMI",
    min_value=10.0,
    max_value=60.0,
    value=22.0
)

children = st.sidebar.number_input(
    "👶 Children",
    min_value=0,
    max_value=10,
    step=1
)

smoker = st.sidebar.selectbox(
    "🚬 Smoker",
    ["yes", "no"]
)

region = st.sidebar.selectbox(
    "🌍 Region",
    ["northeast","northwest","southeast","southwest"]
)

if st.sidebar.button("💰 Predict Charges"):

    st.subheader("📄 Customer Details")
    st.write("Age: ", age)
    st.write("gender: ", sex)
    st.write("bmi : ", str(bmi))
    st.write("number of childer: ", str(children))
    st.write(" region: ", region)

    columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    myinput = [[19,"female",27,0,"yes","southwest"]]
    myinput = pd.DataFrame(data = myinput,columns = columns)

    st.write(myinput)
    result = model.predict(myinput)
    if result[0,0] < 0:
        st.error("❌ Invalid Prediction")
    else:
        st.balloons()

        st.success("Prediction Completed Successfully!")

        #st.success( str(round(result[0,0])))
        st.metric(
            label="Estimated Insurance Charge",
            value=f"₹ {result[0,0]:,.2f}"
        )



#---- Background color gradient ----
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#74ebd5,#ACB6E5);
}
</style>
""",unsafe_allow_html=True)

st.markdown("---")

#----Footer -----
st.markdown(
    "<center>Developed with ❤️ using Streamlit</center>"
    "<center>Created by Aditi Bhosale</center>",
    unsafe_allow_html=True,
)
#---- Graph ----
# predicted = result[0,0]

# years = np.arange(1,11)

# cost = predicted*(1+0.06)**(years-1)

# fig, ax = plt.subplots(figsize=(8,4))

# ax.plot(years,cost,
#         marker='o',
#         linewidth=3)

# ax.set_title("Estimated Insurance Cost Over Time")

# ax.set_xlabel("Years")

# ax.set_ylabel("Premium (₹)")

# ax.grid(True)

# st.pyplot(fig)