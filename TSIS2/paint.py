import pygame

from tools import (
    SHAPE_TOOLS,
    draw_shape,
    draw_continuous,
    flood_fill,
    save_canvas
)


pygame.init()

# Fullscreen window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

TOOLBAR_HEIGHT = 90

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (170, 170, 170)
RED = (220, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 220)
YELLOW = (240, 240, 50)

# Canvas
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Current settings
color = BLACK
brush_size = 5
tool = "pencil"

# Drawing state
drawing = False
start_pos = None
last_pos = None

# Text state
typing = False
text_pos = None
typed_text = ""

# Fonts
font = pygame.font.SysFont(None, 22)
text_font = pygame.font.SysFont(None, 36)

# Tool buttons
tool_buttons = {}

tools = [
    ("PENCIL", "pencil"),
    ("LINE", "line"),
    ("RECT", "rect"),
    ("CIRCLE", "circle"),
    ("SQUARE", "square"),
    ("R TRI", "right_triangle"),
    ("EQ TRI", "equilateral_triangle"),
    ("RHOMBUS", "rhombus"),
    ("FILL", "fill"),
    ("TEXT", "text"),
    ("ERASER", "eraser")
]


def make_buttons():
    tool_buttons.clear()

    start_x = 260
    button_w = 85
    button_h = 35
    gap = 8

    for i, item in enumerate(tools):
        name, tool_name = item
        x = start_x + i * (button_w + gap)
        y = 10
        tool_buttons[tool_name] = pygame.Rect(x, y, button_w, button_h)


def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))

    # Color buttons
    colors = [BLACK, RED, GREEN, BLUE, YELLOW]

    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (10 + i * 45, 10, 35, 35))

        # Border around selected color
        if color == c:
            pygame.draw.rect(screen, BLACK, (10 + i * 45, 10, 35, 35), 3)

    # Tool buttons
    for name, tool_name in tools:
        rect = tool_buttons[tool_name]

        if tool == tool_name:
            pygame.draw.rect(screen, (120, 120, 120), rect)
        else:
            pygame.draw.rect(screen, DARK_GRAY, rect)

        pygame.draw.rect(screen, BLACK, rect, 1)
        screen.blit(font.render(name, True, BLACK), (rect.x + 5, rect.y + 10))

    # Brush size buttons
    pygame.draw.rect(screen, DARK_GRAY, (10, 55, 40, 25))
    screen.blit(font.render("S", True, BLACK), (25, 60))

    pygame.draw.rect(screen, DARK_GRAY, (60, 55, 40, 25))
    screen.blit(font.render("M", True, BLACK), (75, 60))

    pygame.draw.rect(screen, DARK_GRAY, (110, 55, 40, 25))
    screen.blit(font.render("L", True, BLACK), (125, 60))

    screen.blit(font.render(f"Size: {brush_size}", True, BLACK), (170, 60))

    help_text = "1/2/3 = size | Ctrl+S = save | ESC = exit"
    screen.blit(font.render(help_text, True, BLACK), (280, 60))


def handle_toolbar_click(x, y):
    global color, tool, brush_size

    # Colors
    if 10 < x < 45:
        color = BLACK
    elif 55 < x < 90:
        color = RED
    elif 100 < x < 135:
        color = GREEN
    elif 145 < x < 180:
        color = BLUE
    elif 190 < x < 225:
        color = YELLOW

    # Tools
    for tool_name, rect in tool_buttons.items():
        if rect.collidepoint(x, y):
            tool = tool_name

    # Sizes
    if 10 < x < 50 and 55 < y < 80:
        brush_size = 2
    elif 60 < x < 100 and 55 < y < 80:
        brush_size = 5
    elif 110 < x < 150 and 55 < y < 80:
        brush_size = 10


def draw_preview():
    if not drawing or start_pos is None:
        return

    if tool in SHAPE_TOOLS:
        end_pos = pygame.mouse.get_pos()
        draw_shape(screen, tool, color, start_pos, end_pos, brush_size)


make_buttons()

running = True

while running:
    clock.tick(120)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if typing:
                if event.key == pygame.K_RETURN:
                    text_surface = text_font.render(typed_text, True, color)
                    canvas.blit(text_surface, text_pos)

                    typing = False
                    typed_text = ""
                    text_pos = None

                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    typed_text = ""
                    text_pos = None

                elif event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]

                else:
                    typed_text += event.unicode

            else:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_1:
                    brush_size = 2

                elif event.key == pygame.K_2:
                    brush_size = 5

                elif event.key == pygame.K_3:
                    brush_size = 10

                elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    save_canvas(canvas)

        # Mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if y < TOOLBAR_HEIGHT:
                handle_toolbar_click(x, y)

            else:
                if tool == "fill":
                    flood_fill(canvas, event.pos, color, TOOLBAR_HEIGHT)

                elif tool == "text":
                    typing = True
                    text_pos = event.pos
                    typed_text = ""

                else:
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos

        # Mouse up
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                end_pos = event.pos

                if tool in SHAPE_TOOLS:
                    draw_shape(canvas, tool, color, start_pos, end_pos, brush_size)

            drawing = False
            start_pos = None
            last_pos = None

    # Pencil and eraser while mouse is held
    if drawing:
        mx, my = pygame.mouse.get_pos()

        if my > TOOLBAR_HEIGHT:
            last_pos = draw_continuous(
                canvas,
                tool,
                color,
                last_pos,
                (mx, my),
                brush_size,
                WHITE
            )

    # Draw canvas
    screen.blit(canvas, (0, 0))

    # Shape preview
    draw_preview()

    # Text preview
    if typing and text_pos:
        preview = text_font.render(typed_text, True, color)
        screen.blit(preview, text_pos)

    # Toolbar must be on top
    draw_toolbar()

    pygame.display.update()


pygame.quit()