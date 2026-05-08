import chainlit as cl
from src.llm import ask_order


@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [])


@cl.on_message
async def main(message: cl.Message):
    user_input = message.content

    chat_history = cl.user_session.get("chat_history")

    
    chat_history = chat_history[-14:]

    response = ask_order(chat_history, user_input)

    await cl.Message(content=response).send()

    # Update memory
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": response})

    cl.user_session.set("chat_history", chat_history)