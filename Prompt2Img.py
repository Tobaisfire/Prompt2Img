import streamlit as st

from diffusers import StableDiffusionPipeline

def prompt2img(model,prompt):
    if model == 'Stable-1':
        modelid = "runwayml/stable-diffusion-v1-5"
        device = "gpu"

        pipe = StableDiffusionPipeline.from_pretrained(modelid)
        pipe.to(device)
        pipe.enable_attention_slicing()
        image1 = pipe(prompt).images
        return image1[0]


st.set_page_config(layout="wide")
add_selectbox = st.sidebar.selectbox(
    "Action You need to Perform",
    ("Select","Prompt2Img", "About")
)

print(add_selectbox)

if add_selectbox == 'Prompt2Img':
    model = st.radio(
    "Choose Model",
    ('Stable-1','Stable-2'))

    if model == 'Stable-1':
        st.write('Stable-1')

        Prompt = st.text_input(
        "Enter Your Prompt",

        key="placeholder",)

        if Prompt != None:
            st.write(Prompt)
            image = prompt2img(model,Prompt)
            st.image(image)

        
        


    if model == 'Stable-2':
        st.write('Stable-2')
        prompt = st.text_input(
        "Enter Your Prompt",

        key="placeholder",
    )