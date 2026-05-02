import pygame
import random

from config import *
from db import save_score, get_personal_best


pygame.init()

font = pygame.font.SysFont(None, 25)
big_font = pygame.font.SysFont(None, 42)


def draw_text(screen, text, x, y, color=BLACK, big=False):
    used_font = big_font if big else font
    img = used_font.render(text, True, color)
    screen.blit(img, (x, y))


def spawn_position():
    return [
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    ]


def spawn_safe_position(snake, obstacles=None):
    if obstacles is None:
        obstacles = []

    while True:
        pos = spawn_position()

        if pos not in snake and pos not in obstacles:
            return pos


def draw_grid(screen):
    for x in range(0, WIDTH, BLOCK):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, BLOCK):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def create_food(snake, obstacles):
    return {
        "pos": spawn_safe_position(snake, obstacles),
        "value": random.choice([1, 1, 1, 2, 3]),
        "timer": 300
    }


def create_poison(snake, obstacles):
    return {
        "pos": spawn_safe_position(snake, obstacles),
        "timer": 420
    }


def create_powerup(snake, obstacles):
    return {
        "pos": spawn_safe_position(snake, obstacles),
        "kind": random.choice(["shield", "slow", "speed"]),
        "timer": 500
    }


def create_obstacles(count, snake):
    obstacles = []

    for _ in range(count):
        obstacles.append(spawn_safe_position(snake, obstacles))

    return obstacles


def draw_powerup(screen, powerup):
    x, y = powerup["pos"]

    if powerup["kind"] == "shield":
        pygame.draw.rect(screen, BLUE, (x, y, BLOCK, BLOCK))
        draw_text(screen, "S", x + 5, y + 2, WHITE)

    elif powerup["kind"] == "slow":
        pygame.draw.rect(screen, YELLOW, (x, y, BLOCK, BLOCK))
        draw_text(screen, "-", x + 6, y + 2, BLACK)

    elif powerup["kind"] == "speed":
        pygame.draw.rect(screen, RED, (x, y, BLOCK, BLOCK))
        draw_text(screen, "+", x + 5, y + 2, WHITE)


def draw_game_over(screen, score, level, personal_best):
    screen.fill(RED)

    draw_text(screen, "GAME OVER", 210, 90, WHITE, True)
    draw_text(screen, f"Score: {score}", 230, 150, WHITE)
    draw_text(screen, f"Level: {level}", 230, 180, WHITE)
    draw_text(screen, f"Personal best: {personal_best}", 190, 210, WHITE)
    draw_text(screen, "R - retry", 230, 270, WHITE)
    draw_text(screen, "Q - main menu", 215, 300, WHITE)


def play(screen, clock, username, settings):
    x = WIDTH // 2
    y = HEIGHT // 2

    dx = 0
    dy = 0

    snake = []
    length = 1

    score = 0
    level = 1
    speed = 10

    shield = False
    active_power = None
    power_timer = 0

    personal_best = get_personal_best(username)
    score_saved = False

    obstacles = []
    food = create_food(snake, obstacles)
    poison = create_poison(snake, obstacles)
    powerup = create_powerup(snake, obstacles)

    running = True
    game_over = False

    while running:
        while game_over:
            if not score_saved:
                save_score(username, score, level)
                personal_best = max(personal_best, score)
                score_saved = True

            draw_game_over(screen, score, level, personal_best)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return "retry"

                    if event.key == pygame.K_q:
                        return "menu"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

                if event.key == pygame.K_LEFT and dx != BLOCK:
                    dx, dy = -BLOCK, 0

                elif event.key == pygame.K_RIGHT and dx != -BLOCK:
                    dx, dy = BLOCK, 0

                elif event.key == pygame.K_UP and dy != BLOCK:
                    dx, dy = 0, -BLOCK

                elif event.key == pygame.K_DOWN and dy != -BLOCK:
                    dx, dy = 0, BLOCK

        x += dx
        y += dy

        head = [x, y]

        # Wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            if shield:
                shield = False

                x = max(0, min(x, WIDTH - BLOCK))
                y = max(0, min(y, HEIGHT - BLOCK))
                head = [x, y]
            else:
                game_over = True

        # Self collision
        if head in snake[:-1]:
            if shield:
                shield = False
            else:
                game_over = True

        # Obstacle collision
        if head in obstacles:
            if shield:
                shield = False
            else:
                game_over = True

        snake.append(head)

        if len(snake) > length:
            del snake[0]

        # Food timer
        food["timer"] -= 1

        if food["timer"] <= 0:
            food = create_food(snake, obstacles)

        # Poison timer
        poison["timer"] -= 1

        if poison["timer"] <= 0:
            poison = create_poison(snake, obstacles)

        # Powerup timer
        powerup["timer"] -= 1

        if powerup["timer"] <= 0:
            powerup = create_powerup(snake, obstacles)

        # Eat food
        if head == food["pos"]:
            length += food["value"]
            score += 10 * food["value"]
            food = create_food(snake, obstacles)

        # Eat poison
        if head == poison["pos"]:
            length -= 2
            score = max(0, score - 10)
            poison = create_poison(snake, obstacles)

            if length <= 1:
                game_over = True

        # Eat powerup
        if head == powerup["pos"]:
            if active_power is None:
                active_power = powerup["kind"]

                if active_power == "shield":
                    shield = True
                    power_timer = 999999

                elif active_power == "slow":
                    power_timer = 300

                elif active_power == "speed":
                    power_timer = 180

            powerup = create_powerup(snake, obstacles)

        # Level up
        new_level = score // 50 + 1

        if new_level > level:
            level = new_level
            speed += 2

            if level >= 3:
                obstacles = create_obstacles(level - 2, snake)

        # Powerup effects
        current_speed = speed

        if active_power == "slow":
            current_speed = max(5, speed - 4)

        elif active_power == "speed":
            current_speed = speed + 4

        if active_power:
            power_timer -= 1

            if power_timer <= 0:
                if active_power == "shield":
                    shield = False

                active_power = None

        # Draw
        screen.fill(WHITE)

        if settings.get("grid", True):
            draw_grid(screen)

        # Draw food
        fx, fy = food["pos"]
        pygame.draw.rect(screen, GREEN, (fx, fy, BLOCK, BLOCK))
        draw_text(screen, str(food["value"]), fx + 5, fy + 2, WHITE)

        # Draw poison
        px, py = poison["pos"]
        pygame.draw.rect(screen, PURPLE, (px, py, BLOCK, BLOCK))
        draw_text(screen, "P", px + 5, py + 2, WHITE)

        # Draw powerup
        draw_powerup(screen, powerup)

        # Draw obstacles
        for obstacle in obstacles:
            ox, oy = obstacle
            pygame.draw.rect(screen, DARK_RED, (ox, oy, BLOCK, BLOCK))

        # Draw snake
        snake_color = settings.get("snake_color", BLACK)

        for part in snake:
            pygame.draw.rect(screen, snake_color, (*part, BLOCK, BLOCK))

        # Shield visual
        if shield and snake:
            pygame.draw.rect(screen, BLUE, (*snake[-1], BLOCK, BLOCK), 3)

        # UI
        draw_text(screen, f"Score: {score}", 10, 10, BLACK)
        draw_text(screen, f"Level: {level}", 10, 30, BLACK)
        draw_text(screen, f"Best: {personal_best}", 10, 50, BLACK)

        if active_power == "shield":
            draw_text(screen, "Power: Shield", 430, 10, BLUE)

        elif active_power == "slow":
            draw_text(screen, f"Power: Slow {power_timer // 60}s", 400, 10, BLACK)

        elif active_power == "speed":
            draw_text(screen, f"Power: Speed {power_timer // 60}s", 395, 10, RED)

        pygame.display.update()
        clock.tick(current_speed)

    return "menu"