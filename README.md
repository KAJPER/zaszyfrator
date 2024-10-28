# Zaszyfrator

**Zaszyfrator** to narzędzie do szyfrowania i deszyfrowania danych w języku Python z wykorzystaniem algorytmu AES w trybie CFB (Cipher Feedback Mode). Projekt ten został stworzony z myślą o prostym zabezpieczaniu i odczycie zaszyfrowanych treści, przydatny w zastosowaniach, gdzie wymagana jest dodatkowa warstwa ochrony danych.

## Funkcjonalności
- **Szyfrowanie i deszyfrowanie** przy użyciu algorytmu AES (Advanced Encryption Standard) w trybie CFB
- **Przechowywanie klucza i wektora inicjalizacyjnego** (IV) w formacie Base64
- **Łatwe kodowanie i dekodowanie** zaszyfrowanych wiadomości przy użyciu Pythonowego modułu `cryptography`

## Wymagania
- Python 3.6+
- Moduł `cryptography`

## Instalacja
Aby zainstalować wymagane zależności, wykonaj:
```bash
pip install cryptography
