import pygame
import math
import datetime
from collections import deque


SHAPE_TOOLS = {
    "line",
    "rect",
    "circle",
    "square",
    "right_triangle",
    "equilateral_triangle",
    "rhombus",
}


def get_square_rect(start, end):
    """Return pygame.Rect for a perfect square between two mouse positions."""
    x1, y1 = start
    x2, y2 = end

    side = min(abs(x2 - x1), abs(y2 - y1))

    if x2 < x1:
        x1 -= side
    if y2 < y1:
        y1 -= side

    return pygame.Rect(x1, y1, side, side)


def get_right_triangle_points(start, end):
    """Return 3 points for a right triangle."""
    x1, y1 = start
    x2, y2 = end
    return [(x1, y1), (x1, y2), (x2, y2)]


def get_equilateral_triangle_points(start, end):
    """Return 3 points for an equilateral triangle."""
    x1, y1 = start
    x2, y2 = end

    side = abs(x2 - x1)
    height = int(side * math.sqrt(3) / 2)
    direction = 1 if y2 > y1 else -1

    return [
        (x1, y1),
        (x1 + side, y1),
        (x1 + side // 2, y1 + direction * height),
    ]


def get_rhombus_points(start, end):
    """Return 4 points for a rhombus."""
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    return [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy),
    ]


def draw_shape(surface, tool, color, start_pos, end_pos, brush_size):
    """
    Draw selected shape on the given surface.
    Used for both real drawing on canvas and live preview on screen.
    """
    if tool == "line":
        pygame.draw.line(surface, color, start_pos, end_pos, brush_size)

    elif tool == "rect":
        rect = pygame.Rect(
            start_pos[0],
            start_pos[1],
            end_pos[0] - start_pos[0],
            end_pos[1] - start_pos[1],
        )
        rect.normalize()
        pygame.draw.rect(surface, color, rect, brush_size)

    elif tool == "circle":
        radius = int(math.dist(start_pos, end_pos))
        pygame.draw.circle(surface, color, start_pos, radius, brush_size)

    elif tool == "square":
        pygame.draw.rect(
            surface,
            color,
            get_square_rect(start_pos, end_pos),
            brush_size,
        )

    elif tool == "right_triangle":
        pygame.draw.polygon(
            surface,
            color,
            get_right_triangle_points(start_pos, end_pos),
            brush_size,
        )

    elif tool == "equilateral_triangle":
        pygame.draw.polygon(
            surface,
            color,
            get_equilateral_triangle_points(start_pos, end_pos),
            brush_size,
        )

    elif tool == "rhombus":
        pygame.draw.polygon(
            surface,
            color,
            get_rhombus_points(start_pos, end_pos),
            brush_size,
        )


def draw_continuous(surface, tool, color, last_pos, current_pos, brush_size, eraser_color):
    """
    Draw pencil or eraser while mouse is held.
    Returns the new last_pos.
    """
    if tool == "pencil":
        pygame.draw.line(surface, color, last_pos, current_pos, brush_size)
        return current_pos

    if tool == "eraser":
        pygame.draw.line(surface, eraser_color, last_pos, current_pos, brush_size * 4)
        return current_pos

    return last_pos


def save_canvas(canvas):
    """Save canvas as PNG with timestamp."""
    filename = datetime.datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
    pygame.image.save(canvas, filename)
    print("Saved:", filename)


def flood_fill(surface, pos, fill_color, top_limit=0):
    """
    Flood fill using get_at() and set_at().
    top_limit protects toolbar area from filling.
    """
    width, height = surface.get_size()
    x, y = pos

    if not (0 <= x < width and 0 <= y < height):
        return

    if y < top_limit:
        return

    target_color = surface.get_at((x, y))
    fill_color = pygame.Color(fill_color)

    if target_color == fill_color:
        return

    queue = deque()
    queue.append((x, y))

    while queue:
        px, py = queue.popleft()

        if px < 0 or px >= width or py < top_limit or py >= height:
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), fill_color)

        queue.append((px + 1, py))
        queue.append((px - 1, py))
        queue.append((px, py + 1))
        queue.append((px, py - 1))
