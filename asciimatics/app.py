# from random import randint
# from time import sleep

from asciimatics.screen import ManagedScreen

@ManagedScreen
def app(screen=None):
    # screen.clear()
    while True:
        screen.print_at('hello world', x=10, y=3, colour=screen.COLOUR_RED, bg=screen.COLOUR_YELLOW)
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return

        screen.move(0, 0)
        screen.draw(20, 0)
        screen.draw(20, 8)
        screen.draw(0, 8)
        screen.draw(0, 0)

        # screen.move(1, 1)
        # screen.draw(1, 10, char='x')

        poly_top_left_x = 60
        poly_top_left_y = 0
        poly_width = 20
        poly_height = 2
        screen.fill_polygon(
            polygons=[
                [
                    (poly_top_left_x, poly_top_left_y), # top left
                    (poly_top_left_x + poly_width, poly_top_left_y), # top right
                    (poly_top_left_x + poly_width, poly_height), # bottom right
                    (poly_top_left_x, poly_top_left_y + poly_height), # bottom left
                ],
            ],
            colour=3,
        )

        screen.refresh()
        # sleep(2)

app()
