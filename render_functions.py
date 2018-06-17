import libtcodpy as libdcod

def render_all(con, entities, screen_width, screen_height):
    # Draw all entities in the list
    for entity in entities:
        draw_entity(con, entity)

    libdcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libdcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def clear_entity(con, entity):
    # Erase the character that represents this object
    libdcod.console_put_char(con, entity.x, entity.y, ' ', libdcod.BKGND_NONE)
