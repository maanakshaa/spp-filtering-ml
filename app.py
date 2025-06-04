import streamlit as st
import pandas as pd
from PIL import Image

# --- Load Logo ---
logo = Image.open("sastra_logo.jpeg")
resized_logo = logo.resize((700, 120))
# --- Sidebar Navigation ---
st.sidebar.image(logo, use_container_width=True)
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate", [
    "Overview",
    "OneFilterResults",
    "TwoFilterResults",
    "ThreeFilterResults (DTR)",
    "Multicollinearity",
    "Full Comparison Table"
])
st.sidebar.markdown("---")
st.sidebar.markdown("**Maanakshaa Sree R**  \n**Dr. G.R. Brindha**")

# --- Load Data ---
single_df = pd.read_csv("SingleFilterModelResults.csv")
two_df = pd.read_csv("TwoFilterModelResults.csv")
three_df = pd.read_csv("ThreeFilterModelResults_DTR.csv")

# --- Page 1: Overview ---
if page == "Overview":
    st.markdown("<h4 style='text-align: center;'>Stacked Noise Filtering and Optimized Predictive Modeling for Real-Time Stencil Printing Process (SPP)</h4>", unsafe_allow_html=True)

    st.markdown("##### Project Overview")
    st.markdown("""
    This project presents a comprehensive study on enhancing prediction accuracy in the **Stencil Printing Process (SPP)** 
    using advanced **filtering techniques** and **machine learning models**.

    We evaluated the performance of models like:
    - **Decision Tree Regressor (DTR)**
    - **Support Vector Regressor (SVR)**
    - **Artificial Neural Networks (ANN)**

    on three key target variables:
    - **Volume**
    - **Offset X**
    - **Offset Y**

    To improve data quality and model reliability, various signal denoising filters were applied:
    - **Median, Gaussian, DTCWT, Savitzky-Golay, Bilateral**, and **Multivariate filters**

    The study was carried out in three stages:
    1. **Single Filter Evaluation** – Assessed how individual filters impact each model’s prediction performance.
    2. **Two-Filter Combinations** – Analyzed synergistic effects of filter pairs on RMSE and MAE metrics.
    3. **Three-Filter Stacking (DTR only)** – Evaluated the impact of advanced stacking strategies using DTR for further refinement.

    Additionally, a **multicollinearity analysis** was performed to remove redundant features, which significantly reduced errors and improved model stability.
    """)
# --- Page 2: One Filter Results ---
elif page == "OneFilterResults":
    st.header("Single Filter + Model Results")
    selected_model = st.selectbox("Choose Filter + Model Combination", single_df["Model Combination"].unique())
    target = st.selectbox("Choose Target Variable", ["Volume", "OffsetX", "OffsetY"])
    
    row = single_df[single_df["Model Combination"] == selected_model].iloc[0]
    rmse = row[f"RMSE {target}"]
    mae = row[f"MAE {target}"]
    
    st.metric("RMSE", f"{rmse:.4f}")
    st.metric("MAE", f"{mae:.4f}")

# --- Page 3: Two Filter Results ---
elif page == "TwoFilterResults":
    st.header("Two Filter + Model Results")
    selected_model = st.selectbox("Choose Model", two_df["Model"].unique())
    selected_filter = st.selectbox("Choose Filter + Model Combination", two_df["Filter + Model"].unique())
    target = st.selectbox("Choose Target Variable", ["Volume", "OffsetX", "OffsetY"])

    row = two_df[(two_df["Model"] == selected_model) & (two_df["Filter + Model"] == selected_filter)]

    if not row.empty:
        row = row.iloc[0]
        target_map = {
            "OffsetX": "X",
            "OffsetY": "Y",
            "Volume": "Volume"
        }
        rmse_col = f"RMSE {target_map[target]}"
        mae_col = f"MAE {target_map[target]}"
        rmse = row[rmse_col]
        mae = row[mae_col]

        st.metric("RMSE", f"{rmse:.4f}")
        st.metric("MAE", f"{mae:.4f}")
    else:
        st.warning("No matching data found for the selected filter and model combination.")
elif page == "ThreeFilterResults (DTR)":
    st.header("3-Filter Stacking - DTR")
    df_3filter = pd.read_csv("ThreeFilterModelResults_DTR.csv")

    # Dropdowns for filter combination and target variable
    selected_combination = st.selectbox(
        "Choose Filter Combination",
        df_3filter["Filter 1 Filter 2 Filter 3"]
    )

    selected_target = st.selectbox(
        "Choose Target Variable",
        ["OffsetX", "OffsetY", "Volume"]
    )

    # Filter the row
    row = df_3filter[df_3filter["Filter 1 Filter 2 Filter 3"] == selected_combination]

    if not row.empty:
        mae = row[f"MAE {selected_target}"].values[0]
        rmse = row[f"RMSE {selected_target}"].values[0]

        st.subheader(f"{selected_combination} - {selected_target}")
        st.metric("RMSE", f"{rmse:.4f}")
        st.metric("MAE", f"{mae:.4f}")
    else:
        st.warning("No data found for the selected combination.")
# --- Page 5: Multicollinearity ---
elif page == "Multicollinearity":
    st.header("Multicollinearity Impact")
    before = Image.open("before_multicollinearity.png")
    after = Image.open("after_multicollinearity.png")
    
    st.subheader("Before Removal")
    st.image(before, caption="Before Multicollinearity Removal", use_container_width=True)
    
    st.subheader("After Removal")
    st.image(after, caption="After Multicollinearity Removal", use_container_width=True)
    


# --- Page 6: Full Comparison Table ---
elif page == "Full Comparison Table":
    st.header("Full Filter + Model Comparison")
    
    st.subheader("Single Filter + Model")
    st.dataframe(single_df)

    st.subheader("Two Filter + Model")
    st.dataframe(two_df)

    st.subheader("Three Filter + Model (DTR)")
    st.dataframe(three_df)
