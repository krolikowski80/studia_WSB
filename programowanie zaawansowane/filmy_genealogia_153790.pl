% ==============================================
%  Projekt Prolog: Baza wiedzy o filmach
%  Autor: Tomasz Królikowski, Nr albumu	153790    
%  Środowisko online do testowania:
%      https://rextester.com/l/prolog_online_compiler
%  Jak uruchomić?
%      1. Skopiuj cały kod do edytora na powyższej stronie.
%      2. Dodaj swoje zapytania w sekcji "Input" lub w konsoli.
%      3. Naciśnij ▶️ Run.
%  Zadanie:
%      • 25 faktów film/5 (tytuł, gatunek, ocena, rok, reżyser).
%      • Co najmniej 3 dodatkowe reguły (poniżej jest ich więcej).
%      • 5 przykładowych zapytań.
%      • Duża liczba komentarzy – w tym pliku KAŻDY blok kodu jest opisany.
% ==============================================

% ------------------------------------------------
%  FAKTY: film/5
%  film(Tytuł, Gatunek, Ocena, Rok, Reżyser).
%      • Tytuł       – atom lub ciąg w apostrofach
%      • Gatunek     – atom w języku polskim (np. dramat, akcja)
%      • Ocena       – liczba całkowita 1..5 (5 = arcydzieło 😉)
%      • Rok         – rok premiery (liczba całkowita)
%      • Reżyser     – atom / ciąg w apostrofach
% ------------------------------------------------

film('Forrest Gump', dramat, 5, 1994, 'Robert Zemeckis').
film('Avengers: Endgame', akcja, 4, 2019, 'Anthony & Joe Russo').
film('The Godfather', dramat, 5, 1972, 'Francis Ford Coppola').
film('Inception', sci_fi, 5, 2010, 'Christopher Nolan').
film('Interstellar', sci_fi, 5, 2014, 'Christopher Nolan').
film('Parasite', thriller, 5, 2019, 'Bong Joon‑ho').
film('The Dark Knight', akcja, 5, 2008, 'Christopher Nolan').
film('Pulp Fiction', kryminalny, 5, 1994, 'Quentin Tarantino').
film('The Shawshank Redemption', dramat, 5, 1994, 'Frank Darabont').
film('Fight Club', dramat, 4, 1999, 'David Fincher').
film('The Matrix', sci_fi, 5, 1999, 'The Wachowskis').
film('Spirited Away', animacja, 5, 2001, 'Hayao Miyazaki').
film('The Social Network', dramat, 4, 2010, 'David Fincher').
film('Whiplash', dramat, 5, 2014, 'Damien Chazelle').
film('Get Out', horror, 4, 2017, 'Jordan Peele').
film('Her', romans, 4, 2013, 'Spike Jonze').
film('Joker', dramat, 4, 2019, 'Todd Phillips').
film('La La Land', musical, 4, 2016, 'Damien Chazelle').
film('Mad Max: Fury Road', akcja, 5, 2015, 'George Miller').
film('Coco', animacja, 4, 2017, 'Lee Unkrich').
film('Spider‑Man: Into the Spider‑Verse', animacja, 5, 2018, 'Bob Persichetti').
film('The Grand Budapest Hotel', komedia, 4, 2014, 'Wes Anderson').
film('Arrival', sci_fi, 4, 2016, 'Denis Villeneuve').
film('Knives Out', kryminalny, 4, 2019, 'Rian Johnson').
film('Your Name', animacja, 5, 2016, 'Makoto Shinkai').

% ------------------------------------------------
%  REGUŁY POMOCNICZE (zapytania zwracają listy)
% ------------------------------------------------

% >>> Filmy danego gatunku (od wersji z przykładu) <<<
filmy_gatunek(Gatunek, ListaFilmow) :-
    findall(Tytul, film(Tytul, Gatunek, _, _, _), ListaFilmow).

% >>> Filmy o ocenie co najmniej X <<<
filmy_ocena(MinOcena, ListaFilmow) :-
    findall(Tytul, (film(Tytul, _, Ocena, _, _), Ocena >= MinOcena), ListaFilmow).

% >>> NOWOŚĆ 1: Filmy konkretnego reżysera <<<
filmy_rezyser(Rezyser, ListaFilmow) :-
    findall(Tytul, film(Tytul, _, _, _, Rezyser), ListaFilmow).

% >>> NOWOŚĆ 2: Filmy z danego roku <<<
filmy_rok(Rok, ListaFilmow) :-
    findall(Tytul, film(Tytul, _, _, Rok, _), ListaFilmow).

% >>> NOWOŚĆ 3: Czy film jest klasykiem? <<<
% Klasykiem nazwiemy film wydany w XX wieku (rok <= 2000)
film_klasyk(Tytul) :-
    film(Tytul, _, _, Rok, _), Rok =< 2000.

% >>> NOWOŚĆ 4: Najlepiej oceniany film w obrębie gatunku <<<
% (jeśli kilka ma tę samą najwyższą ocenę – wszystkie przejdą)
najlepsza_ocena(Gatunek, Tytul) :-
    film(Tytul, Gatunek, OcenaMax, _, _),
    \+ (film(_, Gatunek, OcenaInna, _, _), OcenaInna > OcenaMax).

% ------------------------------------------------
%  "Ładne" wypisywanie wyników na ekran
% ------------------------------------------------

wyswietl_filmy_gatunek(Gatunek) :-
    filmy_gatunek(Gatunek, Lista),
    write('Filmy gatunku '), write(Gatunek), write(': '), nl,
    writeln(Lista), nl.

wyswietl_filmy_ocena(Min) :-
    filmy_ocena(Min, Lista),
    format('Filmy z ocena >= ~w: ~n', [Min]),
    writeln(Lista), nl.

wyswietl_filmy_rezyser(Rezyser) :-
    filmy_rezyser(Rezyser, Lista),
    format('Filmy rezysera ~w:~n', [Rezyser]),
    writeln(Lista), nl.

wyswietl_filmy_rok(Rok) :-
    filmy_rok(Rok, Lista),
    format('Filmy z roku ~w:~n', [Rok]),
    writeln(Lista), nl.

% ------------------------------------------------
%  PRZYKŁADOWE ZAPYTANIA
%  (możesz je skopiować do trybu interaktywnego)
% ------------------------------------------------
% :- wyswietl_filmy_gatunek(animacja).
% :- wyswietl_filmy_ocena(5).
% :- wyswietl_filmy_rezyser('Christopher Nolan').
% :- wyswietl_filmy_rok(2019).
% :- najlepsza_ocena(sci_fi, Tytuł).
% ------------------------------------------------


% ============================================================

% =========================================================
%  Projekt Prolog – Drzewo genealogiczne (≈ 20 osób)
%  Autor: Tomasz Królikowski, Nr albumu	153790    
%  Środowisko online do testowania:
%      https://rextester.com/l/prolog_online_compiler
%      (Rextester uruchamia SWI‑Prolog w trybie „wszystko‑na‑raz”).
%  Jak uruchomić w Rextesterze?
%      1. Skopiuj cały kod do edytora.
%      2. W polu *Input* wpisz zapytania (każde zakończone kropką).
%      3. Kliknij ▶️ Run – wyniki pojawią się pod kodem.
%
%  🔹 3 szybkie sposoby, by NIE zobaczyć komunikatu „Action? … char_code -1”
%  ──────────────────────────────────────────────────────────
%   Rextester nie przekazuje kolejnych klawiszy po pierwszej odpowiedzi,
%   dlatego tradycyjne „;”/Enter kończy się błędem. Użyj zamiast tego:
%      •  once/1     – zwraca tylko pierwsze rozwiązanie.
%            once(ojciec(piotr, Kto)).
%      •  findall/3  – zbiera wszystkie odpowiedzi w liście.
%            findall(D, ojciec(piotr, D), Lista).
%      •  „wypisz_*” – gotowe predykaty z tego pliku (korzystają z setof/3).
%            wypisz_dzieci(piotr).
%   Pełny tryb interaktywny (z „;”) uzyskasz w https://swish.swi-prolog.org
% =========================================================

% ---------------------------------------------------------
%  FAKTY – płeć
% ---------------------------------------------------------

%  ♂ Mężczyźni
mezczyzna(jan).
mezczyzna(adam).
mezczyzna(piotr).
mezczyzna(pawel).
mezczyzna(marek).
mezczyzna(tomek).
mezczyzna(bartek).
mezczyzna(kuba).
mezczyzna(robert).
mezczyzna(karol).

%  ♀ Kobiety
kobieta(anna).
kobieta(elzbieta).
kobieta(kasia).
kobieta(agata).
kobieta(magda).
kobieta(ola).
kobieta(ewa).
kobieta(zosia).
kobieta(maria).
kobieta(dorota).

% ---------------------------------------------------------
%  FAKTY – relacje rodzicielskie
%  rodzic(Rodzic, Dziecko).
% ---------------------------------------------------------

% Pokolenie 1 → 2
rodzic(jan,    piotr).
rodzic(anna,   piotr).
rodzic(jan,    kasia).
rodzic(anna,   kasia).

rodzic(adam,   pawel).
rodzic(elzbieta,pawel).
rodzic(adam,   agata).
rodzic(elzbieta,agata).

% Pokolenie 2 → 3
rodzic(piotr,  ola).
rodzic(magda,  ola).
rodzic(piotr,  tomek).
rodzic(magda,  tomek).

rodzic(kasia,  bartek).
rodzic(pawel,  bartek).
rodzic(kasia,  ewa).
rodzic(pawel,  ewa).

rodzic(agata,  kuba).
rodzic(marek,  kuba).
rodzic(agata,  zosia).
rodzic(marek,  zosia).

% Dodatkowa gałąź
rodzic(robert, karol).
rodzic(maria,  karol).
rodzic(robert, dorota).
rodzic(maria,  dorota).

% ---------------------------------------------------------
%  FAKTY – związki małżeńskie
%  malzenstwo/2 (uporządkowane – traktujemy jak skierowane)
% ---------------------------------------------------------

malzenstwo(jan,    anna).
malzenstwo(adam,   elzbieta).
malzenstwo(piotr,  magda).
malzenstwo(kasia,  pawel).
malzenstwo(agata,  marek).
malzenstwo(robert, maria).

% ---------------------------------------------------------
%  REGUŁY POMOCNICZE
% ---------------------------------------------------------

% Małżonkowie – symetria
malzonkowie(X, Y) :- malzenstwo(X, Y).
malzonkowie(X, Y) :- malzenstwo(Y, X).

% Ojciec / matka
ojciec(O, D) :- mezczyzna(O), rodzic(O, D).
matka(M, D)  :- kobieta(M),  rodzic(M, D).

% Rodzeństwo – wspólny rodzic, różne osoby (możliwe duplikaty)
rodzenstwo(X, Y) :- rodzic(R, X), rodzic(R, Y), X \= Y.

% Brat / siostra
brat(B, X)    :- mezczyzna(B), rodzenstwo(B, X).
siostra(S, X) :- kobieta(S),  rodzenstwo(S, X).

% Dziadkowie / dziadek / babcia
dziadkowie(DZ, W) :- rodzic(DZ, P), rodzic(P, W).

dziadek(D, W) :- mezczyzna(D), dziadkowie(D, W).

babcia(B, W) :- kobieta(B), dziadkowie(B, W).

% Wujek / ciocia
wujek(WU, X)  :- brat(WU, P),   rodzic(P, X).
ciocia(CI, X) :- siostra(CI, P), rodzic(P, X).

% Kuzynostwo
kuzyn(K, X) :- rodzic(RK, K), rodzic(RX, X), rodzenstwo(RK, RX), K \= X.

% Przodek / potomek (rekurencyjnie)
przodek(A, D) :- rodzic(A, D).
przodek(A, D) :- rodzic(A, X), przodek(X, D).

potomek(D, A) :- przodek(A, D).

% ---------------------------------------------------------
%  "Ładne" wypisywanie *(bez duplikatów!)*
% ---------------------------------------------------------

wypisz_rodzenstwo(Osoba) :-
    setof(R, rodzenstwo(Osoba, R), Lista), !,
    format('Rodzeństwo ~w: ~w~n', [Osoba, Lista]).
wypisz_rodzenstwo(Osoba) :-
    format('~w nie ma rodzeństwa.~n', [Osoba]).

wypisz_dzieci(Osoba) :-
    setof(D, rodzic(Osoba, D), Lista), !,
    format('Dzieci ~w: ~w~n', [Osoba, Lista]).
wypisz_dzieci(Osoba) :-
    format('~w nie ma dzieci.~n', [Osoba]).

% ---------------------------------------------------------
%  PRZYKŁADOWE ZAPYTANIA (w polu *Input*)
% ---------------------------------------------------------
%  wypisz_dzieci(piotr).
%  wypisz_rodzenstwo(bartek).
%  ojciec(piotr, Kto).                      % TYLKO w SWISH/lokalnym, aby móc wcisnąć „;”
%  once(ojciec(piotr, Kto)).                % tylko pierwsze dziecko
%  findall(D, ojciec(piotr, D), Lista).     % lista wszystkich dzieci
%  wypisz_dzieci(piotr).                    % wersja „ładna” z pliku
% ---------------------------------------------------------
% 