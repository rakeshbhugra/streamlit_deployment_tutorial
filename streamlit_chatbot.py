import streamlit as st
import litellm
from dotenv import load_dotenv
import os
from copy import deepcopy

load_dotenv()

def get_ai_response(messages):
    
    if os.getenv("OPENAI_API_KEY") is None:
        st.title("Error: OPENAI_API_KEY not found in environment variables.")

    system_prompt = "You are always angry and rude. Answer in a very short and rude manner."
    
    messages_copy = deepcopy(messages)
    
    messages_copy.insert(0, {"role": "system", "content": system_prompt})

    response = litellm.completion(
        model="gpt-4.1-mini",
        messages=messages_copy
    )
    return response.choices[0].message.content


def main():
    
    st.set_page_config(
        page_title="Rakesh's Chatbot",    # Browser tab title
        page_icon="🤖",           # Browser tab icon
        layout="centered"         # Page layout style
    )

    # Create the page header
    st.title("🤖 Rakesh's Chatbot")
    st.markdown("---")  # Horizontal line separator

    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hello! How what do you want to know?"
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
                # response = f"Echo: {prompt}"  # Replace with actual AI call
                response = get_ai_response(st.session_state.messages)
                st.markdown(response)
        
        # Step 4: Store AI response in conversation history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()