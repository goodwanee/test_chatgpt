import openai
import streamlit as st

#챗지피티에게 요청하는 함수
def askGPT(prompt,apikey):
    client = openai.OpenAI(api_key=apikey)
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    finalResponse = response.choices[0].message.content
    return finalResponse

# main 함수
def main():
    st.set_page_config(page_title="광고문구 생성 프로그램")

    #session_state 초기화
    if "OPENAI_API" not in st.session_state: 
        st.session_state["OPENAI_API"] =""

    with st.sidebar:
        open_apikey = st.text_input(label='OPEN API 키',placeholder='Enter your api key')
        
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
            st.markdown('---') 
        
    st.header(':bee:광고문구 생성 프로그램:bee:')
    st.markdown('---')

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input('제품명',placeholder='')
        strenghth = st.text_input('제품특징',placeholder='')
        keywords = st.text_input('필수포함 키워드',placeholder='')

    with col2:   
          brand = st.text_input('브랜드명',placeholder='애플,올리브영...')
          toneManner = st.text_input('톤앤매너',placeholder='발랄하게,유머러스하게,감성적으로...')
          valeu = st.text_input('브랜드핵심가치',placeholder='필요시작성')


    if st.button("광고문구생성"):
        prompt = f'''
        아래 내용을 참고해서 1~2줄짜리 광고문구 5개 작성해줘.  
        -제품명:{name}
        -브랜드명:{brand}
        -브랜드 핵심가치{valeu}
        -제품특징:{strenghth}
        -톤앤매너:{toneManner}
        -필수포함키워드:{keywords}         
    '''  
        st.info(askGPT(prompt,st.session_state["OPENAI_API"]))

if __name__ =="__main__":
    main()      