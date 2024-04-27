from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obwod(self):
        pass

    def info(self):
        print("To jest figura geometryczna.")


class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok ** 2

    def obwod(self):
        return self.bok * 4

    def info(self):
        super().info()
        print(f"Ta figura to Kwadrat. Pole = {
              self.pole()} a Obwód to: {self.obwod()}")


class Prostokat(Figura):
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def pole(self):
        return self.dlugosc * self.szerokosc

    def obwod(self):
        return 2 * (self.dlugosc + self.szerokosc)

    def info(self):
        super().info()
        print(f"Ta figura to Prostokąt. Pole = {
              self.pole()} a Obwód to: {self.obwod()}")


class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return math.pi * (self.promien ** 2)

    def obwod(self):
        return 2 * math.pi * self.promien

    def info(self):
        super().info()
        print(f"Ta figura to Koło. Pole = {
              self.pole():.2f} a Obwód to: {self.obwod():.2f}")


# Testowanie klas
moja_figura = Kwadrat(5)
moja_figura.info()

prostokat = Prostokat(3, 7)
prostokat.info()

kolo = Kolo(4)
kolo.info()
