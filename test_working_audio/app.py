#import libs

import streamlit as st
import librosa
import matplotlib.pyplot as plt #Que tenta replicar os plots do matlab
import numpy as np #para o topico de senoides no python
import librosa.display

#titulo

# cabeçalho

st.title("Espectrograma")

#Carregando o audio
fname = "teste.wav"
fs = 44100 # Frequencia de amostragem
y, sr = librosa.load(fname,mono=True,sr=44100)

S = librosa.stft(y, n_fft=1000, hop_length=200,win_length=1000)

S = np.abs(S)

plt.figure(figsize=(15,4))
T = librosa.amplitude_to_db(S,ref=np.max)
librosa.display.specshow(T,y_axis='log',x_axis='time',sr=fs)
plt.xlabel('Time[s]')
plt.ylabel('Frequency [ Hz ]')
plt.colorbar(format='%2.0f db')


#fig, ax = plt.subplots()
#plt.specgram(y[0:1000000],NFFT=5000,Fs=sr,noverlap=400,cmap='magma')
#plt.xlabel('Time[s]')
#plt.ylabel('Frequency [ Hz ]')
st.pyplot(plt)


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
