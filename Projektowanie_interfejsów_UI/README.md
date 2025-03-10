# Plan Projektu: Aplikacja do Zarządzania Zadaniami (Task Management App)

## 1. Analiza Potrzeb Użytkowników i Zasady Projektowania UI

1. **Zdefiniuj persony (profile użytkowników)**
   - Przykłady:
     - **Jan (22 lata, student)** – musi ogarniać terminy projektów i zadań z uczelni.  
     - **Anna (30 lat, freelancerka)** – potrzebuje zarządzać wieloma zadaniami z różnych zleceń.
   - Wypisz, czego oczekują od aplikacji (np. szybkie dodawanie, czytelne listy).

2. **Określ funkcjonalności aplikacji**
   - Dodawanie zadań (z nazwą, opisem, terminem).
   - Edycja i usuwanie zadań.
   - Oznaczanie zadań jako ukończone.
   - (Opcjonalnie) kategorie, tagi, priorytety.

3. **Poznaj zasady dobrego UI**
   - **Prostota**: nie przeładowuj ekranu.
   - **Intuicyjność**: jasne i wyraźne etykiety przycisków, duże ikony.
   - **Spójność**: ta sama kolorystyka, powtarzalny układ w całej aplikacji.
   - **Dostępność**: odpowiedni kontrast kolorów i wielkość czcionek.

---

## 2. Szkice Interfejsu (Low-Fidelity Wireframes) i Mapa Aplikacji

1. **Rysowanie szkiców głównych ekranów**
   - Ekran główny (lista zadań).
   - Widok dodawania zadania.
   - Ekran ustawień/profilu (opcjonalnie).
   - Wystarczą proste rysunki na kartce lub w programie graficznym – najważniejszy jest układ elementów.

2. **Mapa aplikacji / User Flow**
   - Zastanów się, jak wygląda przepływ użytkownika:
     1. Uruchomienie aplikacji → wyświetlenie listy zadań.
     2. Kliknięcie „+ Dodaj zadanie” → formularz dodawania.
     3. Zatwierdzenie → powrót do listy z nowym zadaniem.
     4. Edycja/oznaczenie zadania jako ukończone → odpowiednio zmieniony stan w liście zadań.
   - Dzięki temu wiesz, jak użytkownik porusza się po Twojej aplikacji.

---

## 3. Tworzenie Prototypu Hi-Fidelity (np. Figma, Adobe XD)

1. **Przeniesienie szkiców do narzędzia**
   - Wybierz program (Figma, Adobe XD itp.).
   - Zaprojektuj realistyczny wygląd ekranów (kolory, czcionki, ikonki).

2. **Dodaj interakcje**
   - Spraw, by prototyp był klikalny – przycisk „Dodaj zadanie” przenosi do widoku formularza.
   - Dzięki temu uzyskasz wrażenie prawdziwej aplikacji, co ułatwia testy.

---

## 4. Testy Użyteczności i Poprawki w Interfejsie

1. **Zorganizuj mini-testy z użytkownikami**
   - Nawet 2–3 osoby wystarczą, by zauważyć potencjalne problemy.
   - Poproś ich o wykonanie konkretnych zadań (dodanie zadania, edycja, oznaczenie jako ukończone).

2. **Notuj problemy i uwagi**
   - Jeśli ktoś pyta, „A gdzie tu się klika?”, to znak, że coś jest mało widoczne.
   - Zbieraj wszystkie komentarze, nawet jeśli wydają się błahe.

3. **Wprowadzaj poprawki**
   - Przesuń przyciski, zmień kolory, dodaj ikony, jeśli to pomoże użytkownikom w nawigacji.

---

## 5. Implementacja Interfejsu (HTML, CSS, JavaScript/React/Vue.js)

1. **Wybór technologii**
   - Jeśli dopiero zaczynasz, możesz zrobić to w czystym **HTML, CSS, JS**.
   - Jeśli czujesz się pewnie, możesz użyć frameworka, np. **React** albo **Vue.js**.

2. **Zakoduj podstawowe widoki**
   - Strona główna (lista zadań).
   - Formularz dodawania zadania.
   - Możliwość edycji i oznaczenia zadania jako ukończone.

3. **Responsywność**
   - Sprawdź, czy aplikacja wyświetla się dobrze na telefonach i komputerach.
   - Zadbaj o elastyczne style (np. `@media` queries w CSS) lub responsywne komponenty w React/Vue.

---

## 6. Finalne Testy i Optymalizacja

1. **Testuj na różnych urządzeniach i przeglądarkach**
   - Chrome, Firefox, Edge, Safari (w miarę możliwości).
   - Telefony i tablety, jeśli możesz.

2. **Optymalizuj wydajność**
   - Kompresuj i zmniejszaj rozmiary obrazów.
   - Usuwaj nieużywane skrypty.
   - Sprawdzaj, czy wszystko ładuje się szybko.

3. **Ostatnie poprawki w UI**
   - Dopieszczaj detale: kolory, marginesy, typografię, by całość wyglądała spójnie i profesjonalnie.

---

## 7. Prezentacja i Dokumentacja Projektu

1. **Prezentacja aplikacji**
   - Pokaż cały flow: od otwarcia aplikacji, przez dodawanie, edytowanie i oznaczanie zadań.
   - Opowiedz, z jakich technologii korzystasz (React, Vue, biblioteki CSS itp.).

2. **Dokumentacja**
   - Opisz kluczowe decyzje: dlaczego taki układ, taka kolorystyka, jakie problemy rozwiązywałeś.
   - Wspomnij o wnioskach z testów użyteczności.
   - Podaj wymagania systemowe (np. przeglądarka w wersji X, Node.js w wersji Y, jeśli potrzeba).

---

# Podsumowanie

1. **Zacznij od małych kroków** – najpierw szkic i prototyp, potem poprawki, a dopiero na końcu pisanie kodu.
2. **Bądź elastyczny** – w trakcie pracy możesz wprowadzać zmiany, jeśli odkryjesz nowe potrzeby albo ulepszenia.
3. **Testuj, testuj i jeszcze raz testuj** – nawet najlepszy pomysł może okazać się niejasny dla użytkowników, dlatego musisz pytać ludzi o opinię.
4. **Korzystaj z materiałów edukacyjnych** – jeśli nie wiesz, jak coś zrobić w React/Vue, Google i dokumentacje to Twoi przyjaciele!
