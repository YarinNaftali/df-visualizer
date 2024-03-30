import streamlit as st

from api import upload_dataframe, get_all_records
from dataframe_handlers import get_dataframe_from_csv


def upload_and_display_dataframe():
    """
    Uploads a CSV file and displays it as a DataFrame.

    1. Upload a CSV file to the Backend.
    2. (backend) Log the operation.
    3. Fetch the DataFrame csv file from the Backend.
    4. (backend) Log the operation.
    5. Display the DataFrame.
    """

    uploaded_file = st.file_uploader("Upload a CSV file", type=".csv")
    if uploaded_file is not None:
        uploaded_df = get_dataframe_from_csv(uploaded_file)
        if upload_dataframe(uploaded_df):
            st.success("File uploaded successfully.")
            st.subheader("Uploaded DataFrame:")
            st.dataframe(uploaded_df)
            return uploaded_df
        else:
            st.error("File upload failed.")
            return None
    else:
        st.info("Please upload a CSV file to proceed.")
        return None


def show_database_records():
    records = get_all_records()
    if records:
        st.subheader("Database Records:")
        st.table(records)
    else:
        st.info("No records found in the database.")


def main():
    st.title("Full-Stack Data Exploration App")
    upload_and_display_dataframe()
    show_database_records()


if __name__ == "__main__":
    main()
