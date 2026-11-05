import math
import pygame
from dataclasses import dataclass

# ============================================================
# ANIME ACADEMY — SMART CLASSROOM DIGITAL TWIN
# Computer Graphics Microproject
#
# Main concepts:
#   • 3D coordinates (X, Y, Z)
#   • Cuboids / vertices / edges
#   • Orthographic projection
#   • Front / Top / Side / Isometric views
#   • Translation and scaling to screen coordinates
#   • Interactive object selection
#
# Controls:
#   1 = Front view
#   2 = Top view
#   3 = Side view
#   4 = Isometric view
#   TAB = Select object
#   +/- = Zoom
#   R = Reset zoom
#   G = Toggle grid
#   D = Toggle dimensions
#   H = Toggle help panel
#   ESC = Quit
# ============================================================

WIDTH, HEIGHT = 1400, 820
VIEW_W = 1010
FPS = 60

# ---------- UI colours ----------
BG = (13, 16, 25)
PANEL = (24, 28, 42)
PANEL2 = (31, 36, 54)
WHITE = (240, 242, 250)
MUTED = (157, 166, 188)
GRID = (48, 57, 78)
PINK = (255, 126, 190)
CYAN = (93, 214, 255)
PURPLE = (170, 130, 255)
GREEN = (100, 230, 165)
YELLOW = (255, 208, 105)
RED = (255, 105, 120)

@dataclass
class Vec3:
    x: float
    y: float
    z: float

@dataclass
class Box:
    name: str
    center: Vec3
    size: Vec3
    color: tuple
    category: str = "Furniture"

    def corners(self):
        hx = self.size.x / 2
        hy = self.size.y / 2
        hz = self.size.z / 2

        # index = x_sign, y_sign, z_sign
        return [
            Vec3(self.center.x + sx * hx,
                 self.center.y + sy * hy,
                 self.center.z + sz * hz)
            for sx in (-1, 1)
            for sy in (-1, 1)
            for sz in (-1, 1)
        ]


# ============================================================
# 3D CLASSROOM MODEL
# X = left/right
# Y = height
# Z = front/back
# ============================================================

def build_classroom():
    o = []

    # Room
    o.append(Box("Floor", Vec3(0, 0, 0), Vec3(16, .20, 11),
                 (66, 72, 92), "Structure"))
    o.append(Box("Back Wall", Vec3(0, 4.0, 5.4), Vec3(16, 8, .20),
                 (72, 76, 98), "Structure"))
    o.append(Box("Left Wall", Vec3(-8, 4.0, 0), Vec3(.20, 8, 11),
                 (72, 76, 98), "Structure"))
    o.append(Box("Right Wall", Vec3(8, 4.0, 0), Vec3(.20, 8, 11),
                 (72, 76, 98), "Structure"))

    # Front wall accents / academy header
    o.append(Box("Front Header", Vec3(0, 7.2, -5.35), Vec3(15.5, .55, .18),
                 (120, 72, 145), "Decoration"))

    # Smart board
    o.append(Box("Smart Board", Vec3(0, 4.65, -5.18), Vec3(7.2, 3.1, .18),
                 (65, 190, 235), "Technology"))
    o.append(Box("Smart Board Frame", Vec3(0, 4.65, -5.08), Vec3(7.55, 3.45, .12),
                 (35, 40, 58), "Technology"))

    # Teacher desk + monitor
    o.append(Box("Teacher Desk", Vec3(0, 1.15, -3.65), Vec3(3.6, 1.0, 1.35),
                 (173, 110, 82), "Furniture"))
    o.append(Box("Teacher Monitor", Vec3(0, 1.95, -3.65), Vec3(1.65, .85, .12),
                 (70, 180, 230), "Technology"))

    # Student desks and monitors
    xs = (-3.0, 3.0)
    zs = (-1.0, 1.8, 4.2)

    n = 1
    for z in zs:
        for x in xs:
            o.append(Box(f"Student Desk {n}", Vec3(x, 1.0, z),
                         Vec3(2.7, .85, 1.35), (154, 99, 72), "Furniture"))
            o.append(Box(f"Student Monitor {n}", Vec3(x, 1.72, z-.10),
                         Vec3(1.25, .62, .10), (62, 170, 220), "Technology"))
            n += 1

    # Projector hanging from ceiling
    o.append(Box("Projector", Vec3(0, 6.65, -.6), Vec3(1.4, .55, 1.1),
                 (205, 208, 220), "Technology"))

    # Door
    o.append(Box("Academy Door", Vec3(-5.3, 3.0, -5.18), Vec3(2.1, 5.8, .16),
                 (105, 68, 55), "Structure"))

    # Windows on side wall
    o.append(Box("Sakura Window 1", Vec3(7.85, 4.4, .8), Vec3(.12, 2.7, 2.3),
                 (95, 185, 220), "Decoration"))
    o.append(Box("Sakura Window 2", Vec3(7.85, 4.4, 3.8), Vec3(.12, 2.7, 2.3),
                 (95, 185, 220), "Decoration"))

    # Anime-style decorative panels
    o.append(Box("Academy Emblem", Vec3(-5.2, 6.3, -5.12), Vec3(1.6, 1.0, .10),
                 (210, 105, 165), "Decoration"))
    o.append(Box("Poster A", Vec3(5.2, 3.9, 5.25), Vec3(2.0, 2.5, .10),
                 (150, 105, 210), "Decoration"))

    return o


OBJECTS = build_classroom()


# ============================================================
# ORTHOGRAPHIC PROJECTION
# ============================================================

def project_point(p, view, scale, origin):
    """
    Convert a 3D point (X,Y,Z) into 2D screen coordinates.

    FRONT:
        sx = X
        sy = Y

    TOP:
        sx = X
        sy = -Z

    SIDE:
        sx = Z
        sy = Y

    ISOMETRIC:
        An orthographic axonometric-style transformation.
        No perspective division is performed.
    """

    if view == "FRONT":
        sx = p.x
        sy = p.y

    elif view == "TOP":
        sx = p.x
        sy = -p.z

    elif view == "SIDE":
        sx = p.z
        sy = p.y

    else:  # ISO
        angle = math.radians(30)
        sx = (p.x - p.z) * math.cos(angle)
        sy = p.y - (p.x + p.z) * math.sin(angle)

    return (
        int(origin[0] + sx * scale),
        int(origin[1] - sy * scale)
    )


# Corner connections of a cuboid.
EDGES = [
    (0, 1), (0, 2), (0, 4),
    (1, 3), (1, 5),
    (2, 3), (2, 6),
    (3, 7),
    (4, 5), (4, 6),
    (5, 7),
    (6, 7)
]


def adjust_color(color, amount):
    return tuple(max(0, min(255, int(c + amount))) for c in color)


def draw_box(screen, obj, view, origin, scale, selected=False):
    corners = obj.corners()
    pts = [project_point(p, view, scale, origin) for p in corners]

    # In isometric mode, draw filled faces for a stronger 3D appearance.
    if view == "ISO":
        faces = [
            ([0, 1, 3, 2], 18),
            ([4, 6, 7, 5], -12),
            ([0, 4, 5, 1], 5),
            ([2, 3, 7, 6], 15),
            ([0, 2, 6, 4], -5),
            ([1, 5, 7, 3], 8),
        ]

        for ids, delta in faces:
            face_color = adjust_color(obj.color, delta)
            pygame.draw.polygon(screen, face_color, [pts[i] for i in ids])
            pygame.draw.polygon(screen, (20, 22, 31),
                                [pts[i] for i in ids], 1)

    edge_color = YELLOW if selected else adjust_color(obj.color, 35)
    width = 3 if selected else 1

    for a, b in EDGES:
        pygame.draw.line(screen, edge_color, pts[a], pts[b], width)


def draw_grid(screen, view, origin, scale):
    # Reference grid. It is intentionally simple so that the
    # projection of the classroom remains easy to understand.
    if view == "ISO":
        return

    if view == "FRONT":
        for x in range(-9, 10):
            a = project_point(Vec3(x, 0, 0), view, scale, origin)
            b = project_point(Vec3(x, 8, 0), view, scale, origin)
            pygame.draw.line(screen, GRID, a, b, 1)

        for y in range(0, 9):
            a = project_point(Vec3(-9, y, 0), view, scale, origin)
            b = project_point(Vec3(9, y, 0), view, scale, origin)
            pygame.draw.line(screen, GRID, a, b, 1)

    elif view == "TOP":
        for x in range(-9, 10):
            a = project_point(Vec3(x, 0, -6), view, scale, origin)
            b = project_point(Vec3(x, 0, 6), view, scale, origin)
            pygame.draw.line(screen, GRID, a, b, 1)

        for z in range(-6, 7):
            a = project_point(Vec3(-9, 0, z), view, scale, origin)
            b = project_point(Vec3(9, 0, z), view, scale, origin)
            pygame.draw.line(screen, GRID, a, b, 1)

    elif view == "SIDE":
        for z in range(-6, 7):
            a = project_point(Vec3(0, 0, z), view, scale, origin)
            b = project_point(Vec3(0, 8, z), view, scale, origin)
            pygame.draw.line(screen, GRID, a, b, 1)

        for y in range(0, 9):
            a = project_point(Vec3(0, y, -6), view, scale, origin)
            b = project_point(Vec3(0, y, 6), view, scale, origin)
            pygame.draw.line(screen, GRID, a, b, 1)


# ============================================================
# UI
# ============================================================

def draw_text(screen, font, value, pos, color=WHITE):
    screen.blit(font.render(value, True, color), pos)


def draw_axis_legend(screen, view, font):
    draw_text(screen, font, "X = width   Y = height   Z = depth",
              (22, HEIGHT - 32), MUTED)
    draw_text(screen, font, f"Projection: {view}",
              (VIEW_W - 190, HEIGHT - 32), CYAN)


def draw_dashboard(screen, fonts, selected, view, zoom, show_grid, show_dims):
    title, font, small = fonts

    pygame.draw.rect(screen, PANEL, (VIEW_W, 0, WIDTH - VIEW_W, HEIGHT))

    draw_text(screen, title, "🌸 ANIME ACADEMY", (1040, 28), PINK)
    draw_text(screen, font, "SMART CLASSROOM DIGITAL TWIN",
              (1040, 66), CYAN)

    pygame.draw.line(screen, (60, 67, 90),
                     (1035, 104), (1370, 104), 1)

    draw_text(screen, small, "CURRENT VIEW", (1040, 125), MUTED)
    draw_text(screen, title, view, (1040, 150), GREEN)

    draw_text(screen, small, "DIGITAL TWIN STATUS", (1040, 215), MUTED)

    status = [
        ("Occupancy", "28 students"),
        ("Temperature", "24 °C"),
        ("Lighting", "72 %"),
        ("Projector", "ONLINE"),
        ("Smart Board", "ONLINE"),
    ]

    y = 245
    for label, value in status:
        draw_text(screen, small, label, (1040, y), WHITE)
        draw_text(screen, small, value, (1210, y), GREEN)
        y += 27

    draw_text(screen, small, "SELECTED OBJECT", (1040, 405), MUTED)
    draw_text(screen, font, selected.name, (1040, 430), YELLOW)
    draw_text(screen, small, f"Category: {selected.category}",
              (1040, 462), WHITE)

    draw_text(screen, small,
              f"Center: ({selected.center.x:g}, "
              f"{selected.center.y:g}, {selected.center.z:g})",
              (1040, 488), WHITE)

    draw_text(screen, small,
              f"Size: ({selected.size.x:g}, "
              f"{selected.size.y:g}, {selected.size.z:g})",
              (1040, 514), WHITE)

    draw_text(screen, small, "GRAPHICS FEATURES", (1040, 565), MUTED)

    features = [
        "✓ 3D coordinate system",
        "✓ Orthographic projection",
        "✓ Multiple engineering views",
        "✓ Wireframe geometry",
        "✓ Interactive selection",
        "✓ Digital-twin dashboard",
    ]

    for i, item in enumerate(features):
        draw_text(screen, small, item, (1040, 590 + i * 22), WHITE)

    # Small state indicators at bottom
    draw_text(screen, small, f"Zoom: {zoom:.1f}x", (1040, 742), CYAN)
    draw_text(screen, small, f"Grid: {'ON' if show_grid else 'OFF'}",
              (1160, 742), CYAN)
    draw_text(screen, small, f"Dim: {'ON' if show_dims else 'OFF'}",
              (1270, 742), CYAN)


def draw_help(screen, font, small):
    overlay = pygame.Surface((VIEW_W, HEIGHT), pygame.SRCALPHA)
    overlay.fill((10, 12, 18, 225))
    screen.blit(overlay, (0, 0))

    draw_text(screen, font, "CONTROLS", (70, 90), PINK)

    controls = [
        "1  Front Orthographic View",
        "2  Top Orthographic View",
        "3  Side Orthographic View",
        "4  Isometric Orthographic View",
        "TAB  Select next object",
        "+ / -  Zoom",
        "R  Reset zoom",
        "G  Toggle grid",
        "D  Toggle dimensions",
        "H  Toggle this help",
        "ESC  Exit",
    ]

    for i, line in enumerate(controls):
        draw_text(screen, small, line, (75, 140 + i * 32), WHITE)

    draw_text(screen, small,
              "Goal: convert one 3D classroom into multiple 2D views.",
              (75, 540), CYAN)
    draw_text(screen, small,
              "Anime styling is the theme; orthographic projection is",
              (75, 570), MUTED)
    draw_text(screen, small,
              "the Computer Graphics concept being demonstrated.",
              (75, 595), MUTED)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(
        "Anime Academy — Smart Classroom Digital Twin"
    )

    clock = pygame.time.Clock()

    title = pygame.font.SysFont("segoeui", 26, bold=True)
    font = pygame.font.SysFont("segoeui", 18)
    small = pygame.font.SysFont("segoeui", 15)

    fonts = (title, font, small)

    view = "ISO"
    selected_index = 0

    zoom = 1.0
    show_grid = True
    show_dims = True
    show_help = False

    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_1:
                    view = "FRONT"

                elif event.key == pygame.K_2:
                    view = "TOP"

                elif event.key == pygame.K_3:
                    view = "SIDE"

                elif event.key == pygame.K_4:
                    view = "ISO"

                elif event.key == pygame.K_TAB:
                    selected_index = (
                        selected_index + 1
                    ) % len(OBJECTS)

                elif event.key in (pygame.K_EQUALS, pygame.K_PLUS):
                    zoom = min(1.6, zoom + .1)

                elif event.key == pygame.K_MINUS:
                    zoom = max(.6, zoom - .1)

                elif event.key == pygame.K_r:
                    zoom = 1.0

                elif event.key == pygame.K_g:
                    show_grid = not show_grid

                elif event.key == pygame.K_d:
                    show_dims = not show_dims

                elif event.key == pygame.K_h:
                    show_help = not show_help

        screen.fill(BG)

        # Main viewport
        pygame.draw.rect(screen, (17, 20, 30),
                         (0, 0, VIEW_W, HEIGHT))

        # Projection scale and center
        scale = 58 * zoom
        origin = (VIEW_W // 2 - 15, 510)

        if show_grid:
            draw_grid(screen, view, origin, scale)

        # Draw objects
        for i, obj in enumerate(OBJECTS):
            draw_box(
                screen,
                obj,
                view,
                origin,
                scale,
                selected=(i == selected_index)
            )

        selected = OBJECTS[selected_index]

        # View title
        draw_text(screen, title,
                  f"🌸 ANIME ACADEMY — {view} VIEW",
                  (22, 22), WHITE)

        draw_text(screen, small,
                  "Digital Twin • Orthographic Projection",
                  (24, 57), MUTED)

        if show_dims:
            draw_text(screen, small,
                      f"{selected.name}: "
                      f"{selected.size.x:g} × "
                      f"{selected.size.y:g} × "
                      f"{selected.size.z:g}",
                      (24, 84), YELLOW)

        draw_axis_legend(screen, view, small)

        draw_dashboard(
            screen,
            fonts,
            selected,
            view,
            zoom,
            show_grid,
            show_dims
        )

        if show_help:
            draw_help(screen, font, small)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
