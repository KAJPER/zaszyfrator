import tkinter as tk
from tkinter import filedialog, messagebox
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Klucz i IV do szyfrowania (dla uproszczenia są statyczne; lepiej przechowywać je bezpiecznie)
key = base64.b64decode('eoLk1etu78w2JJkJx22vT9rfQHPPtPhttJv5sYnXrUY=')  # przykładowy klucz
iv = base64.b64decode('XnS/IdmdwRw4SVIAh/9dtA==')  # przykładowy IV

# Funkcja szyfrowania danych
def encrypt_data(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(encrypted_data).decode("utf-8")

# Funkcja deszyfrowania danych
def decrypt_data(encrypted_data):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(base64.b64decode(encrypted_data)) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded_data) + unpadder.finalize()

# Funkcja generująca zaszyfrowany plik
def generate_encrypted_executable(source_file, output_file):
    with open(source_file, "rb") as f:
        source_code = f.read()

    # Szyfrujemy kod źródłowy
    encrypted_code = encrypt_data(source_code)

    # Kod samorozpakowujący
    decryption_script = f"""
### made by kajpa###
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

key = base64.b64decode('eoLk1etu78w2JJkJx22vT9rfQHPPtPhttJv5sYnXrUY=')
iv = base64.b64decode('XnS/IdmdwRw4SVIAh/9dtA==')

def decrypt_data(encrypted_data):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(base64.b64decode(encrypted_data)) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded_data) + unpadder.finalize()

encrypted_code = "{encrypted_code}"
exec(decrypt_data(encrypted_code).decode("utf-8"))
"""

    # Zapisujemy plik zaszyfrowany z samorozpakowującym skryptem
    with open(output_file, "w") as f:
        f.write(decryption_script)
    
    messagebox.showinfo("Sukces", f"Wygenerowano zaszyfrowany plik: {output_file}")

# Funkcja odszyfrowania pliku
def decrypt_file(encrypted_file, output_file):
    with open(encrypted_file, "r") as f:
        lines = f.readlines()
    encrypted_code = lines[-2].split('= ')[1].strip().strip('"')

    # Odszyfrowujemy kod i zapisujemy do nowego pliku
    decrypted_code = decrypt_data(encrypted_code)
    with open(output_file, "wb") as f:
        f.write(decrypted_code)
    
    messagebox.showinfo("Sukces", f"Odszyfrowano plik: {output_file}")

# Funkcja wyboru pliku i szyfrowania
def encrypt_file():
    source_file = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if source_file:
        output_file = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if output_file:
            generate_encrypted_executable(source_file, output_file)

# Funkcja wyboru pliku do odszyfrowania
def decrypt_file_prompt():
    encrypted_file = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if encrypted_file:
        output_file = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if output_file:
            decrypt_file(encrypted_file, output_file)

# Tworzenie GUI
root = tk.Tk()
root.title("Szyfrowanie i Odszyfrowywanie Plików Python")
root.geometry("400x200")

# Przycisk do szyfrowania pliku
encrypt_button = tk.Button(root, text="Zaszyfruj Plik", command=encrypt_file, width=20)
encrypt_button.pack(pady=10)

# Przycisk do odszyfrowania pliku
decrypt_button = tk.Button(root, text="Odszyfruj Plik", command=decrypt_file_prompt, width=20)
decrypt_button.pack(pady=10)

# Uruchomienie aplikacji
root.mainloop()
