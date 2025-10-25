import streamlit as st
from plagiarism_detector import check_plagiarism_in_folder

st.title("🔍 Project Report Plagiarism Checker")
st.write("Upload a folder containing `.txt` files of project reports.")

# Choose a folder
folder_path = st.text_input("Enter the path to the folder with .txt reports:", value="reports")

if st.button("Check Plagiarism"):
    if folder_path:
        try:
            results = check_plagiarism_in_folder(folder_path)
            if results:
                st.success(f"Found {len(results)} potential plagiarism case(s):")
                for res in results:
                    st.write(f"🚨 **{res['file1']}** ⟷ **{res['file2']}**: `{res['score']}`")
            else:
                st.success("✅ No plagiarism detected above the threshold.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please provide a valid folder path.")
