import streamlit as st
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from llm.model import get_llm
from tools.calculator import calculator
from tools.nasa import nasa_tool


st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("🤖 AI Assistant")

st.markdown(
    """
This assistant can decide when to use tools:
- **Calculator** for math questions
- **NASA tool** for space-related questions
- **LLM only** for general questions
"""
)


@st.cache_resource
def load_agent():
    llm = get_llm()

    tools = [
        calculator,
        nasa_tool,
    ]

    prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        handle_parsing_errors=True,
    )


agent_executor = load_agent()


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = agent_executor.invoke(
                    {"input": user_input}
                )
                answer = response["output"]

                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as err:
                st.error(f"Error: {err}")

