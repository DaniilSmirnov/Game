import pygame
from pygame import *

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную


class Country:

    units = []
    provinces = []
    color = {}

    def create(self, id, stability, units, provinces, symbols, color):
        self.id = id
        self.stability = stability
        self.units = units
        self.provinces = provinces
        self.symbols = symbols
        self.color = color

    def provinces_actions(self, action, province):
        if action == 'delete':
            self.provinces.remove(province)
        if action == 'add':
            self.provinces.append(province)

    def units_actions(self, action, unit):
        if action == 'delete':
            self.units.remove(unit)
        if action == 'add':
            self.units.append(unit)


class Unit:

    def create(self, size, mood, id, country_id):
        self.size = size
        self.mood = mood
        self.id = id
        self.country_id = country_id
        Country.units_actions("add", id)


class Province:

    def create(self, id, name):
        self.name = name
        self.id = id


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Типа стратегия")  # Пишем в шапку
    # будем использовать как фон
    background_image = pygame.image.load("Provinces.png").convert()

    while 1:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, [0, 0])

        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()