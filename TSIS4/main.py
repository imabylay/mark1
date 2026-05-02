import json
import pygame

from config import WIDTH, HEIGHT, WHITE, BLACK, GREEN, RED, BLUE, YELLOW, GRAY
from game import play
from db import get_top_scores


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake TSIS4")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 25)

SETTINGS_FILE = "settings.json"


def load_settings():
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "snake_color": [0, 0, 0],
            "grid": True,
            "sound": True
        }


def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)


settings = load_settings()


def draw_text(text, x, y, color=WHITE, small=False):
    used_font = small_font if small else font
    image = used_font.render(text, True, color)
    screen.blit(image, (x, y))


def get_username():
    name = ""

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text("Enter name:", 200, 120)
        draw_text(name, 200, 180)
        draw_text("Press Enter to start", 180, 250, WHITE, True)
        draw_text("ESC - back to menu", 195, 280, WHITE, True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

                if event.key == pygame.K_RETURN:
                    if name.strip() != "":
                        return name.strip()

                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                elif len(name) < 12 and event.unicode.isprintable():
                    name += event.unicode


def leaderboard():
    while True:
        clock.tick(60)
        screen.fill(BLACK)

        scores = get_top_scores()

        draw_text("TOP 10", 240, 40)

        if not scores:
            draw_text("No scores yet", 210, 130, WHITE, True)

        for i, score_data in enumerate(scores):
            username = score_data[0]
            score = score_data[1]
            level = score_data[2]

            line = f"{i + 1}. {username} - Score: {score} | Level: {level}"
            draw_text(line, 70, 100 + i * 28, WHITE, True)

        draw_text("Press any key to return", 180, 350, YELLOW, True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                return "menu"


def settings_screen():
    global settings

    colors = {
        "black": [0, 0, 0],
        "green": [50, 200, 50],
        "blue": [50, 80, 220],
        "red": [220, 50, 50]
    }

    color_names = list(colors.keys())

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        current_color_name = "black"

        for name, value in colors.items():
            if settings["snake_color"] == value:
                current_color_name = name

        draw_text("SETTINGS", 210, 50)

        draw_text(f"1 - Snake color: {current_color_name}", 150, 130, WHITE, True)
        draw_text(f"2 - Grid: {settings['grid']}", 150, 170, WHITE, True)
        draw_text(f"3 - Sound: {settings['sound']}", 150, 210, WHITE, True)

        draw_text("ESC - back to menu", 190, 310, YELLOW, True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_settings(settings)
                    return "menu"

                if event.key == pygame.K_1:
                    index = color_names.index(current_color_name)
                    next_color = color_names[(index + 1) % len(color_names)]
                    settings["snake_color"] = colors[next_color]
                    save_settings(settings)

                elif event.key == pygame.K_2:
                    settings["grid"] = not settings["grid"]
                    save_settings(settings)

                elif event.key == pygame.K_3:
                    settings["sound"] = not settings["sound"]
                    save_settings(settings)


def menu():
    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text("SNAKE", 250, 70, GREEN)

        draw_text("1 - Play", 230, 140)
        draw_text("2 - Leaderboard", 200, 190)
        draw_text("3 - Settings", 210, 240)
        draw_text("ESC - Quit", 210, 290)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "play"

                elif event.key == pygame.K_2:
                    return "leaderboard"

                elif event.key == pygame.K_3:
                    return "settings"

                elif event.key == pygame.K_ESCAPE:
                    return "quit"


state = "menu"

while state != "quit":
    if state == "menu":
        state = menu()

    elif state == "play":
        username = get_username()

        if username is None:
            state = "quit"

        elif username == "menu":
            state = "menu"

        else:
            result = play(screen, clock, username, settings)

            if result == "retry":
                state = "play"
            else:
                state = result

    elif state == "leaderboard":
        state = leaderboard()

    elif state == "settings":
        state = settings_screen()


pygame.quit()