import pygame
from racer import play_game
from ui import draw_text, draw_button
from persistence import load_json, save_json, SETTINGS_FILE, LEADERBOARD_FILE


pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (240, 220, 50)
GREEN = (50, 200, 80)
RED = (220, 40, 40)

settings = load_json(SETTINGS_FILE, {
    "sound": True,
    "car_color": "red",
    "difficulty": "normal"
})


def menu_screen():
    play_btn = pygame.Rect(150, 220, 200, 55)
    leaderboard_btn = pygame.Rect(150, 290, 200, 55)
    settings_btn = pygame.Rect(150, 360, 200, 55)
    quit_btn = pygame.Rect(150, 430, 200, 55)

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text(screen, "RACER", 190, 120)
        draw_button(screen, "PLAY", play_btn)
        draw_button(screen, "LEADERBOARD", leaderboard_btn)
        draw_button(screen, "SETTINGS", settings_btn)
        draw_button(screen, "QUIT", quit_btn)

        draw_text(screen, "Use mouse to select", 165, 520, WHITE, True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos):
                    return "play"

                if leaderboard_btn.collidepoint(event.pos):
                    return "leaderboard"

                if settings_btn.collidepoint(event.pos):
                    return "settings"

                if quit_btn.collidepoint(event.pos):
                    return "quit"


def username_screen():
    name = ""

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text(screen, "ENTER YOUR NAME", 125, 180)
        draw_text(screen, name, 190, 270)
        draw_text(screen, "Press Enter to start", 145, 360, WHITE, True)
        draw_text(screen, "Backspace = delete | ESC = menu", 125, 395, WHITE, True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

                if event.key == pygame.K_RETURN and name.strip() != "":
                    return name.strip()

                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                elif len(name) < 10 and event.unicode.isprintable():
                    name += event.unicode


def leaderboard_screen():
    leaderboard = load_json(LEADERBOARD_FILE, [])
    back_btn = pygame.Rect(150, 600, 200, 55)

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text(screen, "TOP 10", 200, 60)

        if not leaderboard:
            draw_text(screen, "No scores yet", 170, 180, WHITE, True)
        else:
            for i, item in enumerate(leaderboard[:10]):
                name = item.get("name", "Player")
                score = item.get("score", 0)
                distance = item.get("distance", 0)

                text = f"{i + 1}. {name} | Score: {score} | Dist: {distance}"
                draw_text(screen, text, 50, 120 + i * 40, WHITE, True)

        draw_button(screen, "BACK", back_btn)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return "menu"


def settings_screen():
    global settings

    back_btn = pygame.Rect(150, 580, 200, 55)

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text(screen, "SETTINGS", 180, 70)

        sound_color = GREEN if settings["sound"] else RED

        draw_text(screen, f"Sound: {settings['sound']}", 120, 170, sound_color)
        draw_text(screen, f"Car color: {settings['car_color']}", 120, 230, WHITE)
        draw_text(screen, f"Difficulty: {settings['difficulty']}", 120, 290, YELLOW)

        draw_text(screen, "Press S - toggle sound", 120, 380, WHITE, True)
        draw_text(screen, "Press C - change car color", 120, 410, WHITE, True)
        draw_text(screen, "Press D - change difficulty", 120, 440, WHITE, True)

        draw_button(screen, "BACK", back_btn)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    settings["sound"] = not settings["sound"]
                    save_json(SETTINGS_FILE, settings)

                elif event.key == pygame.K_c:
                    colors = ["red", "blue", "green"]

                    if settings["car_color"] not in colors:
                        settings["car_color"] = "red"

                    index = colors.index(settings["car_color"])
                    settings["car_color"] = colors[(index + 1) % len(colors)]
                    save_json(SETTINGS_FILE, settings)

                elif event.key == pygame.K_d:
                    levels = ["easy", "normal", "hard"]

                    if settings["difficulty"] not in levels:
                        settings["difficulty"] = "normal"

                    index = levels.index(settings["difficulty"])
                    settings["difficulty"] = levels[(index + 1) % len(levels)]
                    save_json(SETTINGS_FILE, settings)

                elif event.key == pygame.K_ESCAPE:
                    return "menu"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return "menu"


state = "menu"

while state != "quit":
    if state == "menu":
        state = menu_screen()

    elif state == "play":
        username = username_screen()

        if username is None:
            state = "quit"

        elif username == "menu":
            state = "menu"

        else:
            state = play_game(screen, clock, username, settings)

    elif state == "leaderboard":
        state = leaderboard_screen()

    elif state == "settings":
        state = settings_screen()


pygame.quit()