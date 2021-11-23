#import libs

import streamlit as st
import librosa
import matplotlib.pyplot as plt #Que tenta replicar os plots do matlab
import numpy as np #para o topico de senoides no python
import librosa.display
from PIL import Image




##LAYOUT==================================================================

st.title("Espectrograma")
#st.beta_set_page_config(page_title='EspectroApp', page_icon = 'utils/pngTeste.ico', layout = 'wide', initial_sidebar_state = 'auto')
st.sidebar.title("Upload de arquivo")

uploaded_file = st.sidebar.file_uploader("Upload your input Audio file", type=["wav","ogg"])

showPlay = st.sidebar.checkbox('Visualizar player de áudio')
showWave = st.sidebar.checkbox('Visualizar Waveform')

st.sidebar.title("Configurações e parâmetros")
#width_figure_value = st.sidebar.number_input('Largura da imagem',min_value=18)
#height_figure_value = st.sidebar.number_input('Largura da imagem',min_value=2)

cmap_option = st.sidebar.selectbox('Tema do espectrograma',('magma','jet','gray_r'))

axisScale = st.sidebar.selectbox('Escala do eixo y',('log','linear'))

#==========================================================================
sr = 0
y = []
#Carregando o audio



if uploaded_file is not None:
    y, sr = librosa.load(uploaded_file,mono=True,sr=44100)
        #print("Caiu no if",uploaded_file.name)
        #audio_file = open(y, 'rb')
        #audio_bytes = audio_file.read()
        #st.audio(audio_file, format='audio/ogg')
    fs = 44100 # Frequencia de amostragem
        #y, sr = librosa.load(fname,mono=True,sr=44100)
    S = librosa.stft(y,win_length=2000)

    S = np.abs(S)
    plt.figure(figsize=(18,7))
    T = librosa.amplitude_to_db(S,ref=np.max)

    if not showWave:
        
        librosa.display.specshow(T,y_axis=axisScale,x_axis='time',sr=fs,cmap=cmap_option)
        plt.xlabel('Time[s]')
        plt.ylabel('Frequency [ Hz ]')
        plt.colorbar(format='%2.0f db')
        st.pyplot(plt)
    
    if showWave:
        fig, (ax, ax2) = plt.subplots(nrows=2, sharex=True)
        librosa.display.specshow(T,y_axis=axisScale,x_axis='time',sr=fs,cmap=cmap_option,ax=ax )
        librosa.display.waveshow(y, sr=sr, alpha=0.5, ax=ax2)
        #ax.set_xlabel('Time[s]')
        #plt.set_ylabel('Frequency [ Hz ]')
        st.pyplot(fig)

    if showPlay:
        st.audio(uploaded_file, format="audio/wav", start_time=0)
else:
    image = Image.open('utils/notFound.png')
    st.image(image, caption='Áudio não encontrado. Por favor, vá até a barra lateral e realize o upload')

#print("Caiu no if",sr)
fname = "teste.wav"



#fig, ax = plt.subplots()
#plt.specgram(y[0:1000000],NFFT=5000,Fs=sr,noverlap=400,cmap='magma')
#plt.xlabel('Time[s]')
#plt.ylabel('Frequency [ Hz ]')

#audio_file = open('teste.wav', 'rb')
#audio_bytes = audio_file.read()
#st.audio(audio_bytes, format='audio/ogg')


#plt.colorbar(format='%2.0f db')
#audio_file = open(fname, 'rb')
#audio_bytes = audio_file.read()
#st.audio(audio_bytes, format='audio/ogg')
#nome dos usuarios
#user_input = st.sidebar.text_input("Digite seu nome")
 
#Escrevendo o nome do usuário
#st.write("Paciente",user_input)


#grafico

#graf = st.bar_chart(user_input_variables)
