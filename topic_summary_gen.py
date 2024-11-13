from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser


def generate_topic_summary(system_info, topic_name, model_name):
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_info),
            ("human", "{user_input}"),
        ]
    )

    messages = chat_template.format_messages(user_input=topic_name)

    llm = ChatOllama(
        model=model_name,
        temperature=0
    )

    ai_msg = llm.invoke(messages)
    chain = chat_template | llm | StrOutputParser()

    # print(ai_msg)
    # print(chain.invoke({"user_input": topic_name}))

    output_text = chain.invoke({"user_input": topic_name})
    return output_text

