# Albero di Natale realizzato da ImMaster26: https://github.com/ImMaster26/albero-natale-python

import time
import random
import os
import pygame

# Controlli dell'import della canzone
try:
    MUSICA_DISPONIBILE = True
except ImportError:
    MUSICA_DISPONIBILE = False

# Configurazione del nome del file audio
PERCORSO_FILE_AUDIO = "lastChristmas.mp3"  # Inserisci il percorso assoluto se necessario, il nome del file deve corrispondere

# Colori delle foglie dell'albero di Natale
ROSSO = '\033[91m'
VERDE = '\033[92m'
GIALLO = '\033[93m'
BLU = '\033[94m'
MAGENTA = '\033[95m'
CIANO = '\033[96m'
BIANCO = '\033[97m'
RESET = '\033[0m'

# Lista di colori da cui il programma pescherà a caso per le luci
COLORI_LUCI = [ROSSO, VERDE, GIALLO, BLU, MAGENTA, CIANO, BIANCO]

ALBERO = [
    "         * ",
    "        *** ",
    "       ***** ",
    "      ******* ",
    "     ********* ",
    "    *********** ",
    "   ************* ",
    "  *************** ",
    " ***************** ",
    "*******************",
    "       |||||       ",
    "       |||||       "
]

# Ogni riga del testo della canzone è: (Testo, Colore)
DATI_CANZONE = [
    ("Last Christmas", ROSSO),
    ("I gave you my heart", VERDE),
    ("But the very next day", GIALLO),
    ("You gave it away", BLU),
    ("This year", MAGENTA),
    ("To save me from tears", CIANO),
    ("I'll give it to someone special", BIANCO),
    ("", RESET),
    ("A face on a lover", ROSSO),
    ("with a fire in his heart", VERDE),
    ("A man under cover", GIALLO),
    ("but you tore me apart", BLU)
]

# Disegna l'albero di Natale
def disegna_frame(lettere_da_mostrare):
    frame = ""
    lettere_rimanenti = lettere_da_mostrare

    # Disegna l'albero di Natale con luci casuali
    for i, riga in enumerate(ALBERO):
        riga_colorata = ""
        for char in riga:
            if char == '*':
                colore = random.choice(COLORI_LUCI)
                riga_colorata += f"{colore}*{RESET}"
            elif char == '|':
                riga_colorata += f"{RESET}|"
            else:
                riga_colorata += " "

        # Gestione del testo della canzone (lettera per lettera)
        pezzo_testo = ""
        idx = i - 2  # Allinea il testo con l'albero

    # Controlliamo se c'è una riga di canzone disponibile per questa altezza dell'albero
        if 0 <= idx < len(DATI_CANZONE):
            testo_completo, colore_riga = DATI_CANZONE[idx]
            lunghezza_riga = len(testo_completo)

            # Effetto karaoke sulla scritta
            if lettere_rimanenti > 0:
                if lettere_rimanenti >= lunghezza_riga:
                    # Mostra tutta la riga se abbiamo abbastanza lettere da mostrare
                    testo_visibile = testo_completo
                    lettere_rimanenti -= lunghezza_riga
                else:
                    testo_visibile = testo_completo[:lettere_rimanenti]
                    lettere_rimanenti = 0

                pezzo_testo = f"    {colore_riga}{testo_visibile}{RESET}" # Aggiungiamo il testo colorato accanto all'albero
            else:
                pezzo_testo = "" # Se non dobbiamo ancora mostrare questa riga, stringa vuota

        frame += riga_colorata + pezzo_testo + "\n"
    return frame

# Avvia la canzone in loop
def avvia_musica():
    if not MUSICA_DISPONIBILE: return
    if os.path.exists(PERCORSO_FILE_AUDIO):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(PERCORSO_FILE_AUDIO)
            pygame.mixer.music.play(-1)
        except:
            pass


def main():
    os.system('') # Abilita i colori
    avvia_musica()

    conteggio_canzone = 0  # Contatore per il testo della canzone

    totale_lettere_canzone = sum(len(riga[0]) for riga in DATI_CANZONE) # Calcolo totale caratteri della canzone

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            print(disegna_frame(conteggio_canzone)) # Stampa solo l'albero di Natale e la canzone

            # Incrementa il contatore delle lettere
            if conteggio_canzone <= totale_lettere_canzone:
                conteggio_canzone += 1

            time.sleep(0.1) # Velocità della canzone

    except KeyboardInterrupt: # Premendo il tasto CTRL+C, ferma il programma e la musica
        if MUSICA_DISPONIBILE:
            try:
                pygame.mixer.music.stop()
            except:
                pass

        print(f"\n{VERDE}Buon Natale da Master!{RESET}") # Messaggio finale che compare alla pressione del tasto


if __name__ == "__main__":
    main()