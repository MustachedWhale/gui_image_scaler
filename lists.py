# Directory creation list.
dir_list = [('4x5in.jpg', '4x5 Aspect Ratio'), ('4x6in.jpg', '2x3 Aspect Ratio'), ('5x7in.jpg', '5x7 Aspect Ratio'), ('6x8in.jpg', '3x4 Aspect Ratio'), ('11x14in.jpg', '11x14 Aspect Ratio'), ('A5P.jpg', 'ISO Sizes'),
            ('5x4in.jpg', '5x4 Aspect Ratio'), ('6x4in.jpg', '3x2 Aspect Ratio'), ('7x5in.jpg', '7x5 Aspect Ratio'), ('8x6in.jpg', '4x3 Aspect Ratio'), ('14x11in.jpg', '14x11 Aspect Ratio'), ('A5L.jpg', 'ISO Sizes')]

# List of images for each aspect ratio.
ar_list = [
    # Portrait
    # 4x5 Aspect Ratio
    ['4x5in.jpg', '8x10in.jpg', '12x15in.jpg', '16x20in.jpg'],
    # 2x3 Aspect Ratio
    ['4x6in.jpg', '6x9in.jpg', '8x12in.jpg', '10x15in.jpg', '12x18in.jpg', '16x24in.jpg', '20x30in.jpg', '24x36in.jpg'],
    # 5x7 Aspect Ratio
    ['5x7in.jpg'],
    # 3x4 Aspect Ratio
    ['6x8in.jpg', '9x12in.jpg', '12x16in.jpg', '15x20in.jpg', '18x24in.jpg'],
    # 11x14 Aspect Ratio
    ['11x14in.jpg'],
    # ISO Sizes
    ['A5P.jpg', 'A4P.jpg', 'A3P.jpg', 'A2P.jpg', 'A1P.jpg'],

    # Landscape
    # 5x4 Aspect Ratio
    ['5x4in.jpg', '10x8in.jpg', '15x12in.jpg', '20x16in.jpg'],
    # 3x2 Aspect Ratio
    ['6x4in.jpg', '9x6in.jpg', '12x8in.jpg', '15x10in.jpg', '18x12in.jpg', '24x16in.jpg', '30x20in.jpg', '36x24in.jpg'],
    # 7x5 Aspect Ratio
    ['7x5in.jpg'],
    # 4x3 Aspect Ratio
    ['8x6in.jpg', '12x9in.jpg', '16x12in.jpg', '20x15in.jpg', '24x18in.jpg'],
    # 14x11 Aspect Ratio
    ['14x11in.jpg'],
    # ISO Sizes
    ['A5L.jpg', 'A4L.jpg', 'A3L.jpg', 'A2L.jpg', 'A1L.jpg'],

    # Square
    ['8x8in.jpg', '10x10in.jpg', '12x12in.jpg', '16x16in.jpg']
]

# Size list.
size_list = [
    # Portrait
    # 4x5 Aspect Ratio
    {'4x5in.jpg': [1200, 1500], '8x10in.jpg': [2400, 3000], '12x15in.jpg': [3600, 4500], '16x20in.jpg': [4800, 6000]},
    # 2x3 Aspect Ratio
    {'4x6in.jpg': [1200, 1800], '6x9in.jpg': [1800, 2700], '8x12in.jpg': [2400, 3600], '10x15in.jpg': [3000, 4500], '12x18in.jpg': [3600, 5400], '16x24in.jpg': [4800, 7200], '20x30in.jpg': [6000, 9000], '24x36in.jpg': [7200, 10800]},
    # 5x7 Aspect Ratio
    {'5x7in.jpg': [1500, 2100]},
    # 3x4 Aspect Ratio
    {'6x8in.jpg': [1800, 2400], '9x12in.jpg': [2700, 3600], '12x16in.jpg': [3600, 4800], '15x20in.jpg': [4500, 6000], '18x24in.jpg': [5400, 7200]},
    # 11x14 Aspect Ratio
    {'11x14in.jpg': [3300, 4200]},
    # ISO Sizes
    {'A5P.jpg': [1749, 2481], 'A4P.jpg': [2481, 3508], 'A3P.jpg': [3508, 4962], 'A2P.jpg': [4961, 7016], 'A1P.jpg': [7016, 9934]},

    # Landscape
    # 5x4 Aspect Ratio
    {'5x4in.jpg': [1500, 1200], '10x8in.jpg': [3000, 2400], '15x12in.jpg': [4500, 3600], '20x16in.jpg': [6000, 4800]},
    # 3x2 Aspect Ratio
    {'6x4in.jpg': [1800, 1200], '9x6in.jpg': [2700, 1800], '12x8in.jpg': [3600, 2400], '15x10in.jpg': [4500, 3000], '18x12in.jpg': [5400, 3600], '24x16in.jpg': [7200, 4800], '30x20in.jpg': [9000, 6000], '36x24in.jpg': [10800, 7200]},
    # 7x5 Aspect Ratio
    {'7x5in.jpg': [2100, 1500]},
    # 4x3 Aspect Ratio
    {'8x6in.jpg': [2400, 1800], '12x9in.jpg': [3600, 2700], '16x12in.jpg': [4800, 3600], '20x15in.jpg': [6000, 4500], '24x18in.jpg': [7200, 5400]},
    # 14x11 Aspect Ratio
    {'14x11in.jpg': [4200, 3300]},
    # ISO Sizes
    {'A5L.jpg': [2481, 1749], 'A4L.jpg': [3508, 2481], 'A3L.jpg': [4961, 3508], 'A2L.jpg': [7016, 4961], 'A1L.jpg': [9934, 7016]},

    # Square
    {'8x8in.jpg': [2400, 2400], '10x10in.jpg': [3000, 3000], '12x12in.jpg': [3600, 3600], '16x16in.jpg': [4800, 4800]}
    ]