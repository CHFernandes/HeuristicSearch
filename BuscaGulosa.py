citiesArray = [
    "Rostock",
    "Berlin",
    "Dresden",
    "Leipzig",
    "Magdeburg",
    "Lübeck",
    "Braunschweig",
    "Hannover",
    "Hamburg",
    "Bremen",
    "Munster",
    "Köln",
    "Düsseldorf",
    "München", 
    "Ulm",
    "Ingolstadt",
    "Stuttgart",
    "Baden",
    "Frankfurt",
    "Nürnberg",
    "Mainz",
    "Trier",
    "Bonn",
]

citiesRoutes = {
   "Rostock": ["Berlin", "Magdeburg", "Lübeck"],
   "Berlin": ["Rostock", "Magdeburg", "Dresden"],
   "Dresden": ["Berlin", "Leipzig"],
   "Leipzig": ["Dresden", "Magdeburg", "Nürnberg"],
   "Magdeburg": ["Rostock", "Berlin", "Leipzig", "Braunschweig", "Lübeck"],
   "Lübeck": ["Rostock", "Magdeburg", "Braunschweig", "Hannover", "Hamburg"],
   "Braunschweig": ["Lübeck", "Magdeburg", "Nürnberg", "Mainz", "Düsseldorf", "Munster", "Hannover"],
   "Hannover": ["Lübeck", "Braunschweig", "Munster", "Bremen", "Hamburg"],
   "Hamburg": ["Lübeck", "Hannover", "Bremen"],
   "Bremen": ["Hamburg", "Hannover", "Munster"],
   "Munster": ["Bremen", "Hannover", "Braunschweig", "Düsseldorf", "Köln"],
   "Köln":["Düsseldorf","Bonn","Munster" ],
   "Düsseldorf":["Munster","Köln","Mainz","Braunschweig"],
   "München":["Ulm","Ingolstadt"],
   "Ulm":["Ingolstadt","München","Stuttgart"],
   "Ingolstadt":["Ulm","München","Stuttgart","Nürnberg"],
   "Stuttgart":["Frankfurt","Baden","Ulm","Ingolstadt"],
   "Baden":[ "Frankfurt","Stuttgart"],
   "Frankfurt":["Nürnberg","Mainz","Trier","Baden","Stuttgart"],
   "Nürnberg": ["Frankfurt", "Ingolstadt","Leipzig","Braunschweig","Mainz" ],
   "Mainz": ["Frankfurt","Trier","Nürnberg","Braunschweig","Düsseldorf","Köln","Bonn" ],
   "Trier": ["Bonn","Frankfurt","Mainz"],
   "Bonn":["Trier","Mainz","Köln" ],
}

citiesDistances: {
    "Rostock": [
        {"Rostock": 0}, {"Berlin": 250}, {"Dresden": 436}, {"Leipzig": 400}, {"Magdeburg": 295}, {"Lübeck": 120}, {"Braunschweig": 291},
        {"Hannover": 327}, {"Hamburg": 184}, {"Bremen": 301}, {"Munster": 458}, {"Köln": 601}, {"Düsseldorf": 577}, {"München": 793}, {"Ulm": 831},
        {"Ingolstadt": 718}, {"Stuttgart": 831}, {"Baden": 801}, {"Frankfurt": 668}, {"Nürnberg": 648}, {"Mainz": 697}, {"Trier": 762},{"Bonn": 627},
        ],
    "Berlin": [
        {"Rostock": 250}, {"Berlin": 0}, {"Dresden": 193}, {"Leipzig": 190}, {"Magdeburg": 156}, {"Lübeck": 280}, {"Braunschweig": 235},
        {"Hannover": 286}, {"Hamburg": 286}, {"Bremen": 394}, {"Munster": 474}, {"Köln": 573}, {"Düsseldorf": 564}, {"München": 584}, {"Ulm": 622},
        {"Ingolstadt": 509}, {"Stuttgart": 628}, {"Baden": 678}, {"Frankfurt": 545}, {"Nürnberg": 439}, {"Mainz": 574}, {"Trier": 719},{"Bonn": 600},
        ],
    "Dresden": [
        {"Rostock": 436}, {"Berlin": 193}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Leipzig": [
        {"Rostock": 400}, {"Berlin": 190}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Magdeburg": [
        {"Rostock": 295}, {"Berlin": 156}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Lübeck": [
        {"Rostock": 120}, {"Berlin": 280}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Braunschweig": [
        {"Rostock": 291}, {"Berlin": 235}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Hannover": [
        {"Rostock": 327}, {"Berlin": 286}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Hamburg": [
        {"Rostock": 184}, {"Berlin": 286}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Bremen": [
        {"Rostock": 301}, {"Berlin": 394}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Munster": [
        {"Rostock": 458}, {"Berlin": 474}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Köln": [
        {"Rostock": 601}, {"Berlin": 573}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Düsseldorf": [
        {"Rostock": 577}, {"Berlin": 564}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "München": [
        {"Rostock": 793}, {"Berlin": 584}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ], 
    "Ulm": [
        {"Rostock": 831}, {"Berlin": 622}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Ingolstadt": [
        {"Rostock": 718}, {"Berlin": 509}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Stuttgart": [
        {"Rostock": 831}, {"Berlin": 628}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Baden": [
        {"Rostock": 801}, {"Berlin": 678}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Frankfurt": [
        {"Rostock": 668}, {"Berlin": 545}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Nürnberg": [
        {"Rostock": 648}, {"Berlin": 439}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Mainz": [
        {"Rostock": 697}, {"Berlin": 574}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Trier": [
        {"Rostock": 762}, {"Berlin": 719}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
    "Bonn": [
        {"Rostock": 627}, {"Berlin": 600}, {"Dresden": 0}, {"Leipzig": 0}, {"Magdeburg": 0}, {"Lübeck": 0}, {"Braunschweig": 0},
        {"Hannover": 0}, {"Hamburg": 0}, {"Bremen": 0}, {"Munster": 0}, {"Köln": 0}, {"Düsseldorf": 0}, {"München": 0}, {"Ulm": 0},
        {"Ingolstadt": 0}, {"Stuttgart": 0}, {"Baden": 0}, {"Frankfurt": 0}, {"Nürnberg": 0}, {"Mainz": 0}, {"Trier": 0},{"Bonn": 0},
        ],
}
