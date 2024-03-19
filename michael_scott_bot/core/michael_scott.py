import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from datasets import load_dataset
import pandas as pd
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title ="Get advice from the regional manager, Michael Scott! Ask me a question!")
st.title('🦜🔗 Get advice from the regional manager, Michael Scott! Ask me a question!')
st.image('michael_scott.jpg', caption='Michael Scott')
openai_api_key_1 = os.environ.get("OPENAI_KEY", None)
openai_api_key_2 = st.sidebar.text_input('OpenAI API Key', type='password')

if openai_api_key_1:
    openai_api_key = openai_api_key_1
else:
    openai_api_key = openai_api_key_2

assert openai_api_key

def generate_response(topic):
    llm = ChatOpenAI(openai_api_key=openai_api_key)
    dataset = load_dataset("jxm/the_office_lines")
    train = dataset["train"]
    df_train = pd.DataFrame(train) 
    df_train_scott = df_train["Michael" == df_train["speaker"]]
    filtered_df = df_train_scott[df_train_scott['line_text'].str.len() > 25]
    concatenated_string = filtered_df["line_text"].str.cat(sep='\n')

    # TODO: Using RAG maybe better - that way, our context can be shorter.
    
    template = f'You are Michael Scott, the regional manager of Dunder Mifflin. The below is how he talks \n {concatenated_string[0:10000]}. It is very important you emuluate his style and give advice or your comments about {topic}. Keep your blog post very short. Remember, Michale Scott often includes a mix of self-centeredness, and misguided attempts at humor but he is a really nice guy and his heart is in the right place.'

    prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("user", "{input}")
    ])
    
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    response = chain.invoke({"input": topic})

    return st.info(response)

with st.form('myform'):
    topic_text = st.text_input('Advice on:', '')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(topic_text)
