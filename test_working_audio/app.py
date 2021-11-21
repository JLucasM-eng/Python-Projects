#import libs

import streamlit as st
import librosa
import matplotlib.pyplot as plt #Que tenta replicar os plots do matlab
import numpy as np #para o topico de senoides no python
import librosa.display
from PIL import Image




##LAYOUT==================================================================

st.title("Espectrograma")

st.sidebar.title("Parâmetros")
#width_figure_value = st.sidebar.number_input('Largura da imagem',min_value=18)
#height_figure_value = st.sidebar.number_input('Largura da imagem',min_value=2)

cmap_option = st.sidebar.selectbox('Tema do espectrograma',('magma','jet','gray_r'))

#==========================================================================
sr = 0
y = []
#Carregando o audio
uploaded_file = st.sidebar.file_uploader("Upload your input Audio file", type=["wav","ogg"])


if uploaded_file is not None:
    y, sr = librosa.load(uploaded_file,mono=True,sr=44100)
    print("Caiu no if",uploaded_file.name)
    #audio_file = open(y, 'rb')
    #audio_bytes = audio_file.read()
    #st.audio(audio_file, format='audio/ogg')
    fs = 44100 # Frequencia de amostragem
    #y, sr = librosa.load(fname,mono=True,sr=44100)
    S = librosa.stft(y, n_fft=1000, hop_length=200,win_length=1000)

    S = np.abs(S)
    plt.figure(figsize=(18,7))
    T = librosa.amplitude_to_db(S,ref=np.max)
    librosa.display.specshow(T,y_axis='log',x_axis='time',sr=fs,cmap=cmap_option)
    plt.xlabel('Time[s]')
    plt.ylabel('Frequency [ Hz ]')
    plt.colorbar(format='%2.0f db')
    st.pyplot(plt)
else:
    image = Image.open('utils/notFound.png')
    st.image(image, caption='Áudio não encontrado. Por favor, vá até a barra lateral e realize o upload')

print("Caiu no if",sr)
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
