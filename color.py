    CLASSES = ('background', 'building', 'road', 'water', 'barren', 'forest',
               'agricultural')

    PALETTE = [[255, 255, 255], [255, 0, 0], [255, 255, 0], [0, 0, 255],
               [159, 129, 183], [0, 255, 0], [255, 195, 128]]

COLOR_MAP = OrderedDict({
    'background': (0, 0, 0),
    'ship': (0, 0, 63),
    'storage_tank': (0, 191, 127),
    'baseball_diamond': (0, 63, 0),
    'tennis_court': (0, 63, 127),
    'basketball_court': (0, 63, 191),
    'ground_Track_Field': (0, 63, 255),
    'bridge': (0, 127, 63),
    'large_Vehicle': (0, 127, 127),
    'small_Vehicle': (0, 0, 127),
    'helicopter': (0, 0, 191),
    'swimming_pool': (0, 0, 255),
    'roundabout': (0, 63, 63),
    'soccer_ball_field': (0, 127, 191),
    'plane': (0, 127, 255),
    'harbor': (0, 100, 155),
})

NEW_COLOR_MAP = {
    'background': (255, 255, 255),
    'barren': (159, 129, 183),
    'road': (255, 255, 0),
    'building': (255, 0, 0),
    'forest': (0, 255, 0),
    'water': (0, 0, 255),
    'background': (0, 0, 0),
    'ship': (0, 0, 63),
    'storage_tank': (0, 191, 127),
    'baseball_diamond': (0, 63, 0),
    'tennis_court': (0, 63, 127),
    'basketball_court': (0, 63, 191),
    'ground_Track_Field': (0, 63, 255),
    'bridge': (0, 127, 63),
    'large_Vehicle': (0, 127, 127),
    'small_Vehicle': (0, 0, 127),
    'helicopter': (0, 0, 191),
    'swimming_pool': (0, 0, 255),
    'roundabout': (0, 63, 63),
    'soccer_ball_field': (0, 127, 191),
    'plane': (0, 127, 255),
    'harbor': (0, 100, 155),
}