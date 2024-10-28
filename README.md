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
```

## Użycie

**Szyfrowanie danych:**
- Stwórz klucz oraz wektor inicjalizacyjny (IV) i zakoduj je w formacie Base64.
- Użyj tych wartości do zaszyfrowania wiadomości, która również zostanie zakodowana w formacie Base64.

**Deszyfrowanie danych:**
- Odszyfruj dane, używając tego samego klucza i IV, aby uzyskać oryginalną wiadomość.
- W celu uruchomienia zdeszyfrowanej wiadomości, użyj `exec()` do wykonania kodu (zachowując ostrożność – patrz rozdział Bezpieczeństwo).

## Bezpieczeństwo
Należy pamiętać, że użycie `exec()` jest ryzykowne, gdyż wykonuje dowolny kod Python. Projekt jest przeznaczony wyłącznie do użytku w środowiskach testowych lub zaufanych, gdzie dane wejściowe są bezpieczne.

## Licencja
Ten projekt jest licencjonowany na zasadach licencji MIT.
