// ============================================================================
//  Projekt C++  –  ZAAWANSOWANY SYSTEM PORTOWY (POJAZDY WODNE)
//  WERSJA 3.0  –  rozszerzone komentarze + dane autora
// ----------------------------------------------------------------------------
//  ▸ Plik       :  pojazdy_port.cpp
//  ▸ Autor      :  Tomasz Królikowski
//  ▸ Nr albumu  :  153790
//  ▸ Kompilacja :  https://rextester.com/l/cpp_online_compiler_gcc  (C++17)
//
//  Cel pliku
//  ----------
//  Demonstracja:
//      1. Dziedziczenia i polimorfizmu na przykładzie różnych jednostek
//         pływających.
//      2. Zarządzania kolejką wejść/wyjść w porcie przy użyciu klasy Port.
//      3. Zastosowania wskaźników inteligentnych (std::shared_ptr).
//      4. Przyspieszonej symulacji czasu (1 s = 50 ms), żeby zmieścić się
//         w czasie wykonania na Rextesterze.
//
//  Jak czytać ten kod?
//  -------------------
//  •  Każdy blok (klasa, metoda, pętla) ma komentarz opisujący CEL i DZIAŁANIE.
//  •  Wszystkie komunikaty wypisywane do konsoli są poprzedzone stemplem
//     [t=XX s] – własny zegar symulacji.
//  •  Sekcja „POLIMORFIZM DEMO” w Port::symuluj() pokazuje wywołania
//     dynamicznie uporządkowane przez mechanizm wirtualnych funkcji.
// ============================================================================

#include <iostream>   // strumienie wejścia/wyjścia
#include <string>     // std::string
#include <vector>     // (nieużyte teraz, ale przyda się do rozbudowy)
#include <memory>     // std::shared_ptr
#include <queue>      // std::queue – kolejka FIFO zgłoszeń
#include <chrono>     // zegar symulacji
#include <thread>     // std::this_thread::sleep_for – pauza jawna
#include <iomanip>    // std::setw – wyrównanie kolumn w logu

// --------------------------- POMOCNICZY KOLOR ANSI ---------------------------
//  Chcemy zielony zegar – na Windows używamy WinAPI, na *nix sekwencji ANSI.
// -----------------------------------------------------------------------------
#ifdef _WIN32
#include <windows.h>
void setColor(int code) { SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), code); }
#else
void setColor(int code) { std::cout << "\033[" << code << "m"; }
#endif
void resetColor() { setColor(0); }

// =============================== KLASA BAZOWA ================================
//  PojazdWodny
//  -----------
//  Abstrakcyjny interfejs wspólny dla wszystkich jednostek.
//  Trzy czysto wirtualne metody wymuszają implementację w klasach potomnych.
// -----------------------------------------------------------------------------
class PojazdWodny {
protected:
    std::string nazwa;        // unikalna nazwa jednostki
    int rok_produkcji;        // rok zwodowania / produkcji
public:
    // Konstruktor przekazujący (move) nazwę – optymalnie dla std::string.
    PojazdWodny(std::string n, int rok)
        : nazwa(std::move(n)), rok_produkcji(rok) {}

    virtual ~PojazdWodny() = default;  // potrzebny dla polimorfizmu

    // Metody czysto wirtualne
    virtual void wypisz_info() const = 0;  // podstawowe dane jednostki
    virtual void rozladunek()        = 0;  // czynności w porcie      
    virtual void zaladunek()         = 0;  // czynności w porcie

    // Getter – przydatny do logowania w klasie Port.
    const std::string& getNazwa() const { return nazwa; }
};

// =============================  KONKRETNE JEDNOSTKI  =========================
//  Każda klasa poniżej implementuje obowiązkowe metody oraz dodaje atrybuty
//  specyficzne (nośność, max głębokość, liczba masztów, moc KM).
// -----------------------------------------------------------------------------

// 1) STATEK TOWAROWY
class Statek : public PojazdWodny {
    double nosnosc_tony;  // maksymalna ładowność
public:
    Statek(std::string n, int rok, double nosnosc)
        : PojazdWodny(std::move(n), rok), nosnosc_tony(nosnosc) {}

    void wypisz_info() const override {
        std::cout << "[Statek]   " << nazwa << " | r." << rok_produkcji
                  << " | nośność: " << nosnosc_tony << " t\n";
    }
    void rozladunek() override {
        std::cout << nazwa << " – rozładunek kontenerów…\n";
    }
    void zaladunek() override {
        std::cout << nazwa << " – załadunek kontenerów…\n";
    }
};

// 2) ŁÓDŹ PODWODNA
class LodzPodwodna : public PojazdWodny {
    double maks_glebokosc;  // w metrach
public:
    LodzPodwodna(std::string n, int rok, double glebokosc)
        : PojazdWodny(std::move(n), rok), maks_glebokosc(glebokosc) {}

    // Metoda unikalna
    void zanurz(double glebokosc) {
        if (glebokosc > maks_glebokosc) glebokosc = maks_glebokosc;
        std::cout << nazwa << " zanurza się na " << glebokosc << " m\n";
    }

    void wypisz_info() const override {
        std::cout << "[Łódź]     " << nazwa << " | r." << rok_produkcji
                  << " | max gł.: " << maks_glebokosc << " m\n";
    }
    void rozladunek() override {
        std::cout << nazwa << " – rozładunek torped…\n";
    }
    void zaladunek() override {
        std::cout << nazwa << " – załadunek torped…\n";
    }
};

// 3) ŻAGLOWIEC
class Zaglowiec : public PojazdWodny {
    int liczba_masztow;
public:
    Zaglowiec(std::string n, int rok, int maszty)
        : PojazdWodny(std::move(n), rok), liczba_masztow(maszty) {}

    // Metoda unikalna
    void postaw_zagle() { std::cout << nazwa << " stawia " << liczba_masztow << " żagli.\n"; }

    void wypisz_info() const override {
        std::cout << "[Żaglowiec] " << nazwa << " | r." << rok_produkcji
                  << " | maszty: " << liczba_masztow << "\n";
    }
    void rozladunek() override { std::cout << nazwa << " – rozładunek ładunku…\n"; }
    void zaladunek() override { std::cout << nazwa << " – załadunek ładunku…\n"; }
};

// 4) HOLOWNIK – bonusowa jednostka pomocnicza
class Holownik : public PojazdWodny {
    int moc_koni;
public:
    Holownik(std::string n, int rok, int moc)
        : PojazdWodny(std::move(n), rok), moc_koni(moc) {}

    void wypisz_info() const override {
        std::cout << "[Holownik] " << nazwa << " | r." << rok_produkcji
                  << " | moc: " << moc_koni << " KM\n";
    }
    void rozladunek() override { std::cout << nazwa << " – pomoc manewrowa…\n"; }
    void zaladunek() override  { std::cout << nazwa << " – tankowanie paliwa…\n"; }
};

// ================================  PORT  ====================================
//  Model – jedno nabrzeże ❯ FIFO kolejka zgłoszeń.
//  Wywołania metod wirtualnych realizują **polimorfizm** (Port nie zna klas).
// -----------------------------------------------------------------------------
class Port {
    // Struktura opisująca przyjęcie jednostki
    struct Zdarzenie {
        std::shared_ptr<PojazdWodny> pojazd;   // wskaźnik na jednostkę (tylko bazowy typ!)
        std::chrono::seconds czas_pobytu;      // ile „sekund” cumuje
    };

    std::queue<Zdarzenie> kolejka;             // kolejka zgłoszeń
    std::chrono::seconds zegar{0};             // zegar symulacji
    static constexpr std::chrono::milliseconds TIK{50}; // 1 s symulacji = 50 ms real

    // Wypisywanie prefixu czasu w zielonym kolorze
    void log(const std::string& txt) {
        setColor(2);
        std::cout << "[t=" << std::setw(3) << zegar.count() << " s] ";
        resetColor();
        std::cout << txt << '\n';
    }
public:
    // Zgłoszenie jednostki do portu
    void przyjmij(const std::shared_ptr<PojazdWodny>& p,
                  std::chrono::seconds pobyt = std::chrono::seconds(5))
    {
        log(p->getNazwa() + " zgłasza wejście.");
        kolejka.push({p, pobyt});
    }

    // Główna pętla symulacji portu
    void symuluj() {
        while (!kolejka.empty()) {
            auto zd = kolejka.front();
            kolejka.pop();

            // Faza wejścia
            log(zd.pojazd->getNazwa() + " wpływa.");

            // ------- POLIMORFIZM DEMO ------------------------------------
            //  Trzy wywołania poniżej są late‑binding: wywołują funkcje
            //  STATEK / ŁÓDŹ / ŻAGLOWIEC / HOLOWNIK – zgodnie z rzeczywistym
            //  typem, mimo iż port ma tylko wskaźnik do PojazdWodny.
            //----------------------------------------------------------------
            zd.pojazd->rozladunek();
            zd.pojazd->zaladunek();
            zd.pojazd->wypisz_info();
            //----------------------------------------------------------------

            // Faza cumowania – odliczamy sekundy symulacji
            for (int i = 0; i < zd.czas_pobytu.count(); ++i) {
                std::this_thread::sleep_for(TIK);
                ++zegar;
            }

            // Faza wyjścia
            log(zd.pojazd->getNazwa() + " opuszcza port.\n");
        }
        log("Port pusty – symulacja zakończona.\n");
    }
};

// ================================== MAIN ====================================
//  Tworzymy trzy jednostki, zgłaszamy je do portu i uruchamiamy symulację.
// -----------------------------------------------------------------------------
int main() {
    // 1. Tworzenie jednostek (shared_ptr = prosty zarządzacz pamięcią)
    auto titanic = std::make_shared<Statek>       ("Titanic",        1912, 52000);
    auto orzel   = std::make_shared<LodzPodwodna> ("Orzeł",          2020, 300);
    auto darml   = std::make_shared<Zaglowiec>    ("Dar Młodzieży", 1982, 3);

    // 2. Tworzymy port i zgłaszamy ruch jednostek (różny czas pobytu)
    Port gdansk;
    gdansk.przyjmij(titanic, std::chrono::seconds(3));
    gdansk.przyjmij(orzel,   std::chrono::seconds(3));
    gdansk.przyjmij(darml,   std::chrono::seconds(3));

    // 3. Start symulacji
    std::cout << "\n=== POLIMORFIZM DEMO – Port obsługuje różne klasy bez ich znajomości ===\n";
    gdansk.symuluj();

    return 0;
}
