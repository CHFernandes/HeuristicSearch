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

citiesDistances = {
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
        {"Rostock": 436}, {"Berlin": 193}, {"Dresden": 0}, {"Leipzig": 112}, {"Magdeburg": 227}, {"Lübeck": 471}, {"Braunschweig": 314},
        {"Hannover": 312}, {"Hamburg": 377}, {"Bremen": 404}, {"Munster": 435}, {"Köln": 474}, {"Düsseldorf": 485}, {"München": 359}, {"Ulm": 398},
        {"Ingolstadt": 303}, {"Stuttgart": 412}, {"Baden": 442}, {"Frankfurt": 372}, {"Nürnberg": 259}, {"Mainz": 403}, {"Trier": 522},{"Bonn": 466},
        ],
    "Leipzig": [
        {"Rostock": 400}, {"Berlin": 190}, {"Dresden": 112}, {"Leipzig": 0}, {"Magdeburg": 101}, {"Lübeck": 303}, {"Braunschweig": 163},
        {"Hannover": 214}, {"Hamburg": 294}, {"Bremen": 310}, {"Munster": 335}, {"Köln": 380}, {"Düsseldorf": 389}, {"München": 360}, {"Ulm": 369},
        {"Ingolstadt": 294}, {"Stuttgart": 264}, {"Baden": 383}, {"Frankfurt": 293}, {"Nürnberg": 229}, {"Mainz": 325}, {"Trier": 441},{"Bonn": 375},
        ],
    "Magdeburg": [
        {"Rostock": 295}, {"Berlin": 156}, {"Dresden": 227}, {"Leipzig": 101}, {"Magdeburg": 0}, {"Lübeck": 203}, {"Braunschweig": 77},
        {"Hannover": 132}, {"Hamburg": 280}, {"Bremen": 217}, {"Munster": 276}, {"Köln": 350}, {"Düsseldorf": 350}, {"München": 444}, {"Ulm": 431},
        {"Ingolstadt": 375}, {"Stuttgart": 411}, {"Baden": 415}, {"Frankfurt": 304}, {"Nürnberg": 300}, {"Mainz": 334}, {"Trier": 600},{"Bonn": 351},
        ],
    "Lübeck": [
        {"Rostock": 120}, {"Berlin": 280}, {"Dresden": 471}, {"Leipzig": 303}, {"Magdeburg": 203}, {"Lübeck": 0}, {"Braunschweig": 179},
        {"Hannover": 178}, {"Hamburg": 57}, {"Bremen": 152}, {"Munster": 296}, {"Köln": 412}, {"Düsseldorf": 394}, {"München": 640}, {"Ulm": 610},
        {"Ingolstadt": 569}, {"Stuttgart": 575}, {"Baden": 562}, {"Frankfurt": 438}, {"Nürnberg": 491}, {"Mainz": 460}, {"Trier": 650},{"Bonn": 426},
        ],
    "Braunschweig": [
        {"Rostock": 291}, {"Berlin": 235}, {"Dresden": 314}, {"Leipzig": 163}, {"Magdeburg": 77}, {"Lübeck": 179}, {"Braunschweig": 0},
        {"Hannover": 55}, {"Hamburg": 148}, {"Bremen": 147}, {"Munster": 202}, {"Köln": 287}, {"Düsseldorf": 283}, {"München": 464}, {"Ulm": 432},
        {"Ingolstadt": 394}, {"Stuttgart": 399}, {"Baden": 391}, {"Frankfurt": 270}, {"Nürnberg": 315}, {"Mainz": 297}, {"Trier": 389},{"Bonn": 292},
        ],
    "Hannover": [
        {"Rostock": 327}, {"Berlin": 286}, {"Dresden": 312}, {"Leipzig": 214}, {"Magdeburg": 132}, {"Lübeck": 178}, {"Braunschweig": 55},
        {"Hannover": 0}, {"Hamburg": 132}, {"Bremen": 100}, {"Munster": 152}, {"Köln": 249}, {"Düsseldorf": 240}, {"München": 489}, {"Ulm": 442},
        {"Ingolstadt": 418}, {"Stuttgart": 401}, {"Baden": 385}, {"Frankfurt": 260}, {"Nürnberg": 338}, {"Mainz": 282}, {"Trier": 362},{"Bonn": 258},
        ],
    "Hamburg": [
        {"Rostock": 184}, {"Berlin": 286}, {"Dresden": 377}, {"Leipzig": 294}, {"Magdeburg": 280}, {"Lübeck": 57}, {"Braunschweig": 148},
        {"Hannover": 132}, {"Hamburg": 0}, {"Bremen": 94}, {"Munster": 240}, {"Köln": 357}, {"Düsseldorf": 339}, {"München": 612}, {"Ulm": 573},
        {"Ingolstadt": 541}, {"Stuttgart": 534}, {"Baden": 517}, {"Frankfurt": 391}, {"Nürnberg": 461}, {"Mainz": 412}, {"Trier": 481},{"Bonn": 371},
        ],
    "Bremen": [
        {"Rostock": 301}, {"Berlin": 394}, {"Dresden": 404}, {"Leipzig": 310}, {"Magdeburg": 217}, {"Lübeck": 152}, {"Braunschweig": 147},
        {"Hannover": 100}, {"Hamburg": 94}, {"Bremen": 0}, {"Munster": 149}, {"Köln": 269}, {"Düsseldorf": 248}, {"München": 583}, {"Ulm": 527},
        {"Ingolstadt": 513}, {"Stuttgart": 478}, {"Baden": 452}, {"Frankfurt": 327}, {"Nürnberg": 432}, {"Mainz": 344}, {"Trier": 399},{"Bonn": 286},
        ],
    "Munster": [
        {"Rostock": 458}, {"Berlin": 474}, {"Dresden": 435}, {"Leipzig": 335}, {"Magdeburg": 276}, {"Lübeck": 296}, {"Braunschweig": 202},
        {"Hannover": 152}, {"Hamburg": 240}, {"Bremen": 149}, {"Munster": 0}, {"Köln": 121}, {"Düsseldorf": 99}, {"München": 509}, {"Ulm": 430},
        {"Ingolstadt": 445}, {"Stuttgart": 370}, {"Baden": 331}, {"Frankfurt": 215}, {"Nürnberg": 370}, {"Mainz": 222}, {"Trier": 253},{"Bonn": 142},
        ],
    "Köln": [
        {"Rostock": 601}, {"Berlin": 573}, {"Dresden": 573}, {"Leipzig": 380}, {"Magdeburg": 350}, {"Lübeck": 412}, {"Braunschweig": 287},
        {"Hannover": 249}, {"Hamburg": 357}, {"Bremen": 269}, {"Munster": 121}, {"Köln": 0}, {"Düsseldorf": 34}, {"München": 456}, {"Ulm": 357},
        {"Ingolstadt": 400}, {"Stuttgart": 288}, {"Baden": 238}, {"Frankfurt": 150}, {"Nürnberg": 336}, {"Mainz": 140}, {"Trier": 134},{"Bonn": 25},
        ],
    "Düsseldorf": [
        {"Rostock": 577}, {"Berlin": 564}, {"Dresden": 564}, {"Leipzig": 389}, {"Magdeburg": 350}, {"Lübeck": 394}, {"Braunschweig": 283},
        {"Hannover": 240}, {"Hamburg": 339}, {"Bremen": 248}, {"Munster": 99}, {"Köln": 34}, {"Düsseldorf": 0}, {"München": 487}, {"Ulm": 390},
        {"Ingolstadt": 430}, {"Stuttgart": 322}, {"Baden": 272}, {"Frankfurt": 180}, {"Nürnberg": 363}, {"Mainz": 172}, {"Trier": 164},{"Bonn": 59},
        ],
    "München": [
        {"Rostock": 793}, {"Berlin": 584}, {"Dresden": 359}, {"Leipzig": 360}, {"Magdeburg": 444}, {"Lübeck": 640}, {"Braunschweig": 464},
        {"Hannover": 489}, {"Hamburg": 612}, {"Bremen": 583}, {"Munster": 509}, {"Köln": 456}, {"Düsseldorf": 487}, {"München": 0}, {"Ulm": 120},
        {"Ingolstadt": 70}, {"Stuttgart": 190}, {"Baden": 253}, {"Frankfurt": 306}, {"Nürnberg": 150}, {"Mainz": 318}, {"Trier": 402},{"Bonn": 434},
        ], 
    "Ulm": [
        {"Rostock": 831}, {"Berlin": 622}, {"Dresden": 398}, {"Leipzig": 369}, {"Magdeburg": 431}, {"Lübeck": 610}, {"Braunschweig": 432},
        {"Hannover": 442}, {"Hamburg": 573}, {"Bremen": 527}, {"Munster": 430}, {"Köln": 357}, {"Düsseldorf": 390}, {"München": 120}, {"Ulm": 0},
        {"Ingolstadt": 113}, {"Stuttgart": 73}, {"Baden": 135}, {"Frankfurt": 215}, {"Nürnberg": 142}, {"Mainz": 217}, {"Trier": 287},{"Bonn": 333},
        ],
    "Ingolstadt": [
        {"Rostock": 718}, {"Berlin": 509}, {"Dresden": 303}, {"Leipzig": 294}, {"Magdeburg": 375}, {"Lübeck": 569}, {"Braunschweig": 394},
        {"Hannover": 418}, {"Hamburg": 541}, {"Bremen": 513}, {"Munster": 445}, {"Köln": 400}, {"Düsseldorf": 430}, {"München": 70}, {"Ulm": 113},
        {"Ingolstadt": 0}, {"Stuttgart": 164}, {"Baden": 222}, {"Frankfurt": 251}, {"Nürnberg": 80}, {"Mainz": 266}, {"Trier": 364},{"Bonn": 380},
        ],
    "Stuttgart": [
        {"Rostock": 831}, {"Berlin": 628}, {"Dresden": 412}, {"Leipzig": 264}, {"Magdeburg": 411}, {"Lübeck": 575}, {"Braunschweig": 399},
        {"Hannover": 401}, {"Hamburg": 534}, {"Bremen": 478}, {"Munster": 370}, {"Köln": 288}, {"Düsseldorf": 322}, {"München": 190}, {"Ulm": 73},
        {"Ingolstadt": 164}, {"Stuttgart": 0}, {"Baden": 62}, {"Frankfurt": 154}, {"Nürnberg": 157}, {"Mainz": 151}, {"Trier": 213},{"Bonn": 264},
        ],
    "Baden": [
        {"Rostock": 801}, {"Berlin": 678}, {"Dresden": 442}, {"Leipzig": 383}, {"Magdeburg": 415}, {"Lübeck": 562}, {"Braunschweig": 391},
        {"Hannover": 385}, {"Hamburg": 517}, {"Bremen": 452}, {"Munster": 331}, {"Köln": 238}, {"Düsseldorf": 272}, {"München": 253}, {"Ulm": 135},
        {"Ingolstadt": 222}, {"Stuttgart": 62}, {"Baden": 0}, {"Frankfurt": 126}, {"Nürnberg": 200}, {"Mainz": 110}, {"Trier": 152},{"Bonn": 213},
        ],
    "Frankfurt": [
        {"Rostock": 668}, {"Berlin": 545}, {"Dresden": 372}, {"Leipzig": 293}, {"Magdeburg": 304}, {"Lübeck": 438}, {"Braunschweig": 270},
        {"Hannover": 260}, {"Hamburg": 391}, {"Bremen": 327}, {"Munster": 215}, {"Köln": 150}, {"Düsseldorf": 180}, {"München": 306}, {"Ulm": 215},
        {"Ingolstadt": 251}, {"Stuttgart": 154}, {"Baden": 126}, {"Frankfurt": 0}, {"Nürnberg": 189}, {"Mainz": 32}, {"Trier": 150},{"Bonn": 130},
        ],
    "Nürnberg": [
        {"Rostock": 648}, {"Berlin": 439}, {"Dresden": 259}, {"Leipzig": 229}, {"Magdeburg": 300}, {"Lübeck": 491}, {"Braunschweig": 315},
        {"Hannover": 338}, {"Hamburg": 461}, {"Bremen": 432}, {"Munster": 370}, {"Köln": 336}, {"Düsseldorf": 363}, {"München": 150}, {"Ulm": 142},
        {"Ingolstadt": 80}, {"Stuttgart": 157}, {"Baden": 200}, {"Frankfurt": 189}, {"Nürnberg": 0}, {"Mainz": 211}, {"Trier": 321},{"Bonn": 318},
        ],
    "Mainz": [
        {"Rostock": 697}, {"Berlin": 574}, {"Dresden": 403}, {"Leipzig": 325}, {"Magdeburg": 334}, {"Lübeck": 460}, {"Braunschweig": 297},
        {"Hannover": 282}, {"Hamburg": 412}, {"Bremen": 344}, {"Munster": 222}, {"Köln": 140}, {"Düsseldorf": 172}, {"München": 318}, {"Ulm": 217},
        {"Ingolstadt": 266}, {"Stuttgart": 151}, {"Baden": 110}, {"Frankfurt": 32}, {"Nürnberg": 211}, {"Mainz": 0}, {"Trier": 119},{"Bonn": 117},
        ],
    "Trier": [
        {"Rostock": 762}, {"Berlin": 719}, {"Dresden": 522}, {"Leipzig": 441}, {"Magdeburg": 600}, {"Lübeck": 650}, {"Braunschweig": 389},
        {"Hannover": 362}, {"Hamburg": 481}, {"Bremen": 399}, {"Munster": 253}, {"Köln": 134}, {"Düsseldorf": 164}, {"München": 402}, {"Ulm": 287},
        {"Ingolstadt": 364}, {"Stuttgart": 213}, {"Baden": 152}, {"Frankfurt": 150}, {"Nürnberg": 321}, {"Mainz": 119}, {"Trier": 0},{"Bonn": 113},
        ],
    "Bonn": [
        {"Rostock": 627}, {"Berlin": 600}, {"Dresden": 466}, {"Leipzig": 375}, {"Magdeburg": 351}, {"Lübeck": 426}, {"Braunschweig": 292},
        {"Hannover": 258}, {"Hamburg": 371}, {"Bremen": 286}, {"Munster": 142}, {"Köln": 25}, {"Düsseldorf": 59}, {"München": 434}, {"Ulm": 333},
        {"Ingolstadt": 380}, {"Stuttgart": 264}, {"Baden": 213}, {"Frankfurt": 130}, {"Nürnberg": 318}, {"Mainz": 117}, {"Trier": 113},{"Bonn": 0},
        ],
}

citiesCost = {
   "Rostock": [{"Rostock": 0}, {"Berlin": 230}, {"Magdeburg": 332}, {"Lübeck": 140}],
   "Berlin": [{"Berlin": 0}, {"Rostock": 230}, {"Magdeburg": 155}, {"Dresden": 191}],
   "Dresden": [{"Dresden": 0}, {"Berlin": 191}, {"Leipzig": 112}],
   "Leipzig": [{"Leipzig": 0}, {"Dresden": 112}, {"Magdeburg": 125}, {"Nürnberg": 282}],
   "Magdeburg": [{"Magdeburg": 0}, {"Rostock": 332}, {"Berlin": 155}, {"Leipzig": 125}, {"Braunschweig": 96}, {"Lübeck": 337}],
   "Lübeck": [{"Lübeck": 0}, {"Rostock": 140}, {"Magdeburg": 337}, {"Braunschweig": 259}, {"Hannover": 210}, {"Hamburg": 67}],
   "Braunschweig": [{"Braunschweig": 0}, {"Lübeck": 259}, {"Magdeburg": 96}, {"Nürnberg": 458}, {"Mainz": 363}, {"Düsseldorf": 349}, {"Munster": 253}, {"Hannover": 64}],
   "Hannover": [{"Hannover": 0}, {"Lübeck": 210}, {"Braunschweig": 64}, {"Munster": 195}, {"Bremen": 124}, {"Hamburg": 152}],
   "Hamburg": [{"Hamburg": 0}, {"Lübeck": 67}, {"Hannover": 152}, {"Bremen": 123}],
   "Bremen": [{"Bremen": 0}, {"Hamburg": 123}, {"Hannover": 124}, {"Munster": 171}],
   "Munster": [{"Munster": 0}, {"Bremen": 171}, {"Hannover": 195}, {"Braunschweig": 253}, {"Düsseldorf": 123}, {"Köln": 156}],
   "Köln":[{"Köln": 0}, {"Düsseldorf": 40},{"Bonn": 30},{"Munster": 156}, {"Mainz": 177}],
   "Düsseldorf":[{"Düsseldorf": 0}, {"Munster": 123},{"Köln": 40},{"Mainz": 214},{"Braunschweig": 349}],
   "München":[{"München": 0}, {"Ulm": 140},{"Ingolstadt": 83}],
   "Ulm":[{"Ulm": 0}, {"Ingolstadt": 159},{"München": 140},{"Stuttgart": 94}],
   "Ingolstadt":[{"Ingolstadt": 0}, {"Ulm": 159},{"München": 83},{"Stuttgart": 238},{"Nürnberg": 95}],
   "Stuttgart":[{"Stuttgart": 0}, {"Frankfurt": 207},{"Baden": 80},{"Ulm": 94},{"Ingolstadt": 238}],
   "Baden":[{"Baden": 0}, {"Frankfurt": 144},{"Stuttgart": 80}],
   "Frankfurt":[{"Frankfurt": 0}, {"Nürnberg": 225},{"Mainz": 40},{"Trier": 194},{"Baden": 144},{"Stuttgart": 207}],
   "Nürnberg": [{"Nürnberg": 0}, {"Frankfurt": 225}, {"Ingolstadt": 95},{"Leipzig": 282},{"Braunschweig": 458},{"Mainz": 255}],
   "Mainz": [{"Mainz": 0}, {"Frankfurt": 40},{"Trier": 156},{"Nürnberg": 255},{"Braunschweig": 363},{"Düsseldorf": 214},{"Köln": 177},{"Bonn": 159}],
   "Trier": [{"Trier": 0}, {"Bonn": 161},{"Frankfurt": 194},{"Mainz": 156}],
   "Bonn":[{"Bonn": 0}, {"Trier": 161},{"Mainz": 159},{"Köln": 30}],
}

def findCostByKey(city, neighbor):
    neighborArray = citiesCost.get(city)
    for visited in neighborArray:
        if visited.get(neighbor):
            return visited.get(neighbor)

print("Selecione uma cidade de partida: \n")

i = 0

while i < len(citiesArray):
    nextItem = str(i+1)
    print(nextItem + " - " + citiesArray[i])
    i+=1

print()
selectedCityId = int(input())
selectedCityId-=1

selectedCity = citiesArray[selectedCityId]

print("Selecione uma cidade de parada \n")

i = 0

while i < len(citiesArray):
    nextItem = str(i+1)
    print(nextItem + " - " + citiesArray[i])
    i+=1

print()
selectedEndingCityId = int(input())
selectedEndingCityId-=1

selectedEndingCity = citiesArray[selectedEndingCityId]

print()

limit = int(input("Selecione um limite em Km \n"))
print()

found = False
visited = {}
i = 1
city = selectedCity
sumCosts = 0
visited[city] = i 

while found == False:
    lessDistantCity = None
    lessDistantSum = None
    currentSum = sumCosts
    cityValue = 0
    for neighbor in citiesRoutes.get(city):
        currentSum = sumCosts + findCostByKey(city, neighbor) + citiesDistances[neighbor][selectedEndingCityId][selectedEndingCity]
        if lessDistantCity == None and lessDistantSum == None:
            if not visited.get(neighbor):
                lessDistantCity = neighbor
                lessDistantSum = currentSum
                cityValue = citiesDistances[neighbor][selectedEndingCityId][selectedEndingCity]
        elif citiesDistances[lessDistantCity][selectedEndingCityId][selectedEndingCity] > citiesDistances[neighbor][selectedEndingCityId][selectedEndingCity] and lessDistantSum > currentSum:
            if not visited.get(neighbor):
                lessDistantCity = neighbor
                lessDistantSum = currentSum
                cityValue = citiesDistances[neighbor][selectedEndingCityId][selectedEndingCity]
    i += 1
    city = lessDistantCity
    sumCosts = lessDistantSum - cityValue
    if sumCosts > limit:
        print("Limite Excedido")
        break
    visited[city] = i

    if city == selectedEndingCity:
        found = True
    
print(sumCosts)
print(visited)