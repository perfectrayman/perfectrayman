import sys
import time
import threading
from playsound import playsound

# Function to play the music in a separate thread
def play_music():
    playsound('C:/Music/lirik1.mp3')

# Function to print the lyrics with delays
def jalanin_lirik():
    lirik = [
        ("Hold my hand, don’t, don’t tell your friends", 0.06),
        ("Cerita kemarin, Ku ingat permanen", 0.09),
        ("manismu kaya permen, I hope this never end", 0.08),
        ("Oh, can you be my gwen? and i’ll be the spiderman", 0.06),
        ("\nSakit dadaku ku mulai merindu", 0.09),
        ("Ku bayangkan jika kamu tidur di sampingku", 0.07),
        ("Di malam yang semu", 0.08),
        ("pejamkan mataku", 0.07),
        ("Ku bayangkan tubuhmu jika di pelukanku", 0.09),
    ]

    delay = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5, 0.4, 0.7]

    print("\n==Garam Dan Madu==")
    time.sleep(3)

    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='', flush=True)  # Menambahkan flush=True agar karakter langsung muncul
            time.sleep(delay_karakter)
        time.sleep(delay[i])  # Menunggu setelah mencetak satu baris lirik
        print('')  # Pindah ke baris baru setelah lirik selesai

    print("\n code by rayman")

# Start the music playing in a separate thread
music_thread = threading.Thread(target=play_music)
music_thread.start()

# Run the lyrics function while the music is playing
jalanin_lirik()

# Wait for the music thread to finish before exiting
music_thread.join()