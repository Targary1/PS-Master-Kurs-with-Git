import pygame


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()  # Framerate
        self.running = True
        self.spaceship = Spaceship(self, 370, 515)  # self parameter referenziert auf das game objekt

        self.background_img = pygame.image.load("spr_space_himmel.png")


        while self.running:  # wenn etwas permanent angezeigt werden soll, dann innerhalb der game loop
            self.clock.tick(60)  # Framerate
            #  self.screen.fill((0, 255, 0))  # Reihenfolge vom Zeichnen der Elemente auf dem Feld von Bedeutung
            self.screen.blit(self.background_img, (0, 0))  # Bild wird immer in der linken oberen Ecke gesetzt
            self.spaceship.update()

            for event in pygame.event.get():   # event method is arbitrary user input (keyboard, mouse, etc.)
                if event.type == pygame.QUIT:  # for schleife iteriert über alle eingehenden befehle
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-10)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(10)

                # Werte wieder auf null setzen, sodass schiff nicht immer weiterfliegt sobal taste einmal gedrückt
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(10)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(-10)

            pygame.display.update()  # sorgt dafür das Screen jedes mal in der loop geupdatet wird.


class Spaceship:
    def __init__(self, game, x, y):  # Referenz auf game wird übergeben, sodass deren Inhalte adressiert werden können
        self.x = x
        self.y = y
        self.change_x = 0
        self.game = game
        self.spaceship_img = pygame.image.load("spr_spaceship.png")

    def move(self, speed):
        self.change_x += speed

    def update(self):
        self.x += self.change_x
        if self.x < 0:
            self.x = 0
        elif self.x > 800 - 64:
            self.x = 800 - 64  # Breite des Schiffes berücksichtigen (Pixelbreite = 64)
        self.game.screen.blit(self.spaceship_img, (self.x, self.y))



if __name__ == "__main__":
    game = Game(800, 600)
    print(__file__)

