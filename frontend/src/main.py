import streamlit as st
import pandas as pd
import plotly.express as px  # Use Plotly for more flexibility and interactivity

def upload_and_display_dataframe():
    uploaded_file = st.file_uploader("Upload a CSV file", type=".csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Uploaded DataFrame:")
        st.dataframe(df)
        return df
    else:
        st.info("Please upload a CSV file to proceed.")
        return None

def choose_and_plot_columns(df):
    if df is not None:
        col1, col2 = st.multiselect("Choose two or more columns to plot:", df.columns, min_selections=2)
        if col1 and col2:
            x, y = col1, col2
            fig = px.scatter(df, x=x, y=y)  # Create interactive scatter plot
            st.plotly_chart(fig, use_container_width=True)  # Include chart
        else:
            st.info("Please select at least two columns to plot.")

def main():
    st.title("Full-Stack Data Exploration App")
    df = upload_and_display_dataframe()
    if df is not None:
        choose_and_plot_columns(df)

if __name__ == "__main__":
    main()
