import streamlit as st

def main():
    st.set_page_config(
        page_title="AI Chatbot",    # Browser tab title
        page_icon="🤖",           # Browser tab icon
        layout="centered"         # Page layout style
    )

    # Create the page header
    st.title("🤖 AI Chatbot")
    st.markdown("---")  # Horizontal line separator

if __name__ == "__main__":
    main()