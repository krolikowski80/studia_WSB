% Definicje filmów (Tytuł, Gatunek, Ocena, Rok, Reżyser)
film('The Shawshank Redemption', dramat, 5, 1994, 'Frank Darabont').
film('The Godfather', dramat, 5, 1972, 'Francis Ford Coppola').
film('The Dark Knight', akcja, 5, 2008, 'Christopher Nolan').
film('Pulp Fiction', kryminał, 5, 1994, 'Quentin Tarantino').
film('Schindler\'s List', dramat, 5, 1993, 'Steven Spielberg').
film('The Lord of the Rings: Return of the King', fantasy, 5, 2003, 'Peter Jackson').
film('Forrest Gump', dramat, 5, 1994, 'Robert Zemeckis').
film('Inception', sci-fi, 5, 2010, 'Christopher Nolan').
film('Fight Club', thriller, 5, 1999, 'David Fincher').
film('The Matrix', sci-fi, 5, 1999, 'Lana Wachowski').
film('Goodfellas', kryminał, 5, 1990, 'Martin Scorsese').
film('Interstellar', sci-fi, 5, 2014, 'Christopher Nolan').
film('Whiplash', dramat, 5, 2014, 'Damien Chazelle').
film('The Prestige', thriller, 5, 2006, 'Christopher Nolan').
film('Django Unchained', western, 5, 2012, 'Quentin Tarantino').
film('Gladiator', historyczny, 5, 2000, 'Ridley Scott').
film('Titanic', romans, 5, 1997, 'James Cameron').
film('The Revenant', dramat, 4, 2015, 'Alejandro G. Iñárritu').
film('The Green Mile', dramat, 5, 1999, 'Frank Darabont').
film('The Silence of the Lambs', thriller, 5, 1991, 'Jonathan Demme').
film('Se7en', kryminał, 5, 1995, 'David Fincher').
film('Parasite', dramat, 5, 2019, 'Bong Joon-ho').
film('Joker', dramat, 5, 2019, 'Todd Phillips').
film('Avengers: Endgame', akcja, 4, 2019, 'Anthony Russo').
film('Hereditary', horror, 4, 2018, 'Ari Aster').

% Filmy wg Gatunku
filmy_gatunek(Gatunek, ListaFilmow) :-
    findall(Tytul, film(Tytul, Gatunek, _, _, _), ListaFilmow).

% Filmy wg Oceny
filmy_ocena(MinOcena, ListaFilmow) :-
    findall(Tytul, (film(Tytul, _, Ocena, _, _), Ocena >= MinOcena), ListaFilmow).

% Filmy wg Reżysera
filmy_rezyser(Rezyser, ListaFilmow) :-
    findall(Tytul, film(Tytul, _, _, _, Rezyser), ListaFilmow).

% Filmy wg Roku Wydania
filmy_rok(Rok, ListaFilmow) :-
    findall(Tytul, film(Tytul, _, _, Rok, _), ListaFilmow).

% Filmy wg Zakresu Lat
filmy_zakres_lat(RokOd, RokDo, ListaFilmow) :-
    findall(Tytul, (film(Tytul, _, _, Rok, _), Rok >= RokOd, Rok =< RokDo), ListaFilmow).

% Filmy wg Gatunku i Oceny
filmy_gatunek_ocena(Gatunek, MinOcena, ListaFilmow) :-
    findall(Tytul, (film(Tytul, Gatunek, Ocena, _, _), Ocena >= MinOcena), ListaFilmow).

% Filmy wg Reżysera i Oceny
filmy_rezyser_ocena(Rezyser, MinOcena, ListaFilmow) :-
    findall(Tytul, (film(Tytul, _, Ocena, _, Rezyser), Ocena >= MinOcena), ListaFilmow).

% Wyświetlanie wyników zapytań
wyswietl_filmy_gatunek(Gatunek) :-
    filmy_gatunek(Gatunek, ListaFilmow),
    write('Filmy gatunku '), write(Gatunek), write(': '),
    write(ListaFilmow), nl.

wyswietl_filmy_ocena(MinOcena) :-
    filmy_ocena(MinOcena, ListaFilmow),
    write('Filmy z oceną co najmniej '), write(MinOcena), write(': '),
    write(ListaFilmow), nl.

wyswietl_filmy_rezyser(Rezyser) :-
    filmy_rezyser(Rezyser, ListaFilmow),
    write('Filmy reżysera '), write(Rezyser), write(': '),
    write(ListaFilmow), nl.

wyswietl_filmy_rok(Rok) :-
    filmy_rok(Rok, ListaFilmow),
    write('Filmy wydane w roku '), write(Rok), write(': '),
    write(ListaFilmow), nl.

wyswietl_filmy_zakres_lat(RokOd, RokDo) :-
    filmy_zakres_lat(RokOd, RokDo, ListaFilmow),
    write('Filmy wydane między '), write(RokOd), write(' a '), write(RokDo), write(': '),
    write(ListaFilmow), nl.

wyswietl_filmy_gatunek_ocena(Gatunek, MinOcena) :-
    filmy_gatunek_ocena(Gatunek, MinOcena, ListaFilmow),
    write('Filmy gatunku '), write(Gatunek), write(' z oceną co najmniej '), write(MinOcena), write(': '),
    write(ListaFilmow), nl.

wyswietl_filmy_rezyser_ocena(Rezyser, MinOcena) :-
    filmy_rezyser_ocena(Rezyser, MinOcena, ListaFilmow),
    write('Filmy reżysera '), write(Rezyser), write(' z oceną co najmniej '), write(MinOcena), write(': '),
    write(ListaFilmow), nl.

% Przykładowe zapytania
:- wyswietl_filmy_gatunek(dramat).
:- wyswietl_filmy_ocena(4).
:- wyswietl_filmy_rezyser('Christopher Nolan').
:- wyswietl_filmy_rok(1999).
:- wyswietl_filmy_zakres_lat(2000, 2010).
:- wyswietl_filmy_gatunek_ocena(dramat, 5).
:- wyswietl_filmy_rezyser_ocena('Quentin Tarantino', 5).
