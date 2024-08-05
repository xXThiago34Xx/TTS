from gtts import gTTS
from playsound import playsound

nombre_archivo = 'audio.mp3'

def texto_a_audio(texto, nombre_archivo):
    # Crear el objeto gTTS con el texto y el idioma
    tts = gTTS(text=texto, lang='es')
    
    # Guardar el archivo de audio
    tts.save(nombre_archivo)
    print(f"Audio guardado como {nombre_archivo}")

    # Reproducir el archivo de audio
    playsound(nombre_archivo)

if __name__ == "__main__":
    while True:
        # Texto que deseas convertir a audio
        texto = input("TTS: ")
        
        # Llamar a la función para convertir el texto a audio y reproducirlo
        texto_a_audio(texto, nombre_archivo)
