#Tengo que instalar las librerias para poder importarlas, estoy resolviendo eso T.T

import numpy as np
import sounddevice as sd
import time
from playsound import playsound

# Parametros de deteccion de aplauso
CLAP_THRESHOLD = 0.3  # sensivilidad para captar el sonido de aplauso
CLAP_DURATION = 0.2   # duracion minima entre aplausos (seconds)
RESPONSE_SOUND = "response_sound.mp3"  # S va a reemplazar una vez se tenga el archivo de sonido

# Funcion que reproduce sonido de respuesta
def play_response_sound():
    print("Playing response sound...")
    playsound(RESPONSE_SOUND)

# Funcion que detecta el sonido de aplauso desde el input
def detect_clap():
    def audio_callback(indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 10
        if volume_norm > CLAP_THRESHOLD:
            print(f"Clap detected with volume: {volume_norm}")

            # Reproducir sonida en lo que se aplauda
            play_response_sound()

    # input del microfono
    with sd.InputStream(callback=audio_callback):
        print("Listening for claps...")
        sd.sleep(10000)  # Listen for 10 seconds (adjust as needed)

# Funcion principal que detecta sonido
if __name__ == "__main__":
    try:
        detect_clap()
    except KeyboardInterrupt:
        print("\nProgram terminated.")
