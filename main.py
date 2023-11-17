import replicate
import streamlit as st

import os
#from dotenv import load_dotenv 

#load_dotenv()


replicate = replicate.Client(api_token='r**********************eU')

#  Use replicate deployed LLaVA instance for image to text
prompt = ("""You are an insurance underwriter. As an insurance underwriter, your primary task is to assess vehicle damage based on uploaded images. Your goal is to determine the estimated percentage of damage and extract relevant details from the image, utilizing your knowledge and expertise in the field.

 Do not add anything which is not asked.""")

model_url = "yorickvp/llava-13b:2facb4a474a0462c15041b78b1ad70952ea46b5ec6ad29583c0b29dbd4249591"

st.image("https://www.needhamco.com/wp-content/uploads/2018/06/virtusa.png" ,width= 75)
st.header("Upload an Image For Analysis")
file = st.file_uploader("", type=["jpeg","jpg", "png"])

with st.sidebar:
    st.markdown("<h1 style='text-align:center;font-family:Georgia'> About </h1>", unsafe_allow_html=True)
    st.markdown("""LLaVA is an open-source, multi-modal language model.It demonstrates good abilities in visual understanding of the image.
                 The model is required to analyze uploaded images of vehicles and assess the percentage of damage. 
                It needs to leverage its knowledge and expertise to estimate the extent of the damage accurately. The goal is to provide an assessment of the damage percentage and extract relevant details from the image to support insurance underwriting decisions.""")
    
    url = 'https://llava-vl.github.io/'

    st.markdown(f'''
             <a href={url}><button style="background-color:White;">llava</button></a>
                ''',unsafe_allow_html=True)
    
    
if file:
    st.image(file)
    output = replicate.run(model_url, input={"image": file, "prompt": prompt})
    response = []
    for item in output:
        response.append(item)
    response = ''.join(response)
    response = response.split('.')
    response = list(filter(None, response))
    st.snow()
    st.write(response)
