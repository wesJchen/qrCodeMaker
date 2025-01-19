import streamlit as st

class StyleHelper:

    @staticmethod
    def load_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    @staticmethod
    def line_break(lines):
        for _ in range(int(lines)):
            st.write(" ")