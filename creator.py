import os
import sys

def create_empty_wav_files(num_files, folder):
    # Crear la carpeta si no existe
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Crear los archivos .wav vacíos
    for i in range(1, num_files + 1):
        filename = f"{i:03d}.wav"
        filepath = os.path.join(folder, filename)
        with open(filepath, 'w') as f:
            pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python creacion.py <numero_de_archivos> <carpeta_destino>")
        sys.exit(1)

    num_files = int(sys.argv[1])
    folder = sys.argv[2]

    create_empty_wav_files(num_files, folder)
    print(f"Se crearon {num_files} archivos .wav vacíos en la carpeta '{folder}'.")