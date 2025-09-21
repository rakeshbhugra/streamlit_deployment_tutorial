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

    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hello! How can I assist you today?"
        }] 

        
    for message in st.session_state.messages:
        # Use Streamlit's chat_message component for proper styling
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            
    if prompt := st.chat_input("Ask me anything..."):
        
        # Step 1: Store user message in conversation history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Step 2: Display the user's message immediately
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Step 3: Get and display the AI response
        with st.chat_message("assistant"):
            # Show a thinking spinner while waiting for AI response
            with st.spinner("Thinking..."):
                response = f"Echo: {prompt}"  # Replace with actual AI call
                st.markdown(response)
        
        # Step 4: Store AI response in conversation history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()