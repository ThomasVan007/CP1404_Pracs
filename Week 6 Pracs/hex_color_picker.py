HEX_COLOR_NAMES = {"WHITE": "#FFFFFF", "SILVER	": "#C0C0C0",
                   "GRAY": "#808080", "BLACK": "#000000",
                   "RED": "#FF0000", "MAROON": "#800000",
                   "YELLOW": "#FFFF00", "OLIVE": "#808000",
                   "LIME": "#00FF00", "GREEN": "#008000"}
# print(STATE_NAMES)

color = input("Enter the name of a color: ").upper()
while color != "":
    if color in HEX_COLOR_NAMES:
        print(color, "is", HEX_COLOR_NAMES[color], "in Hex Code!")
    else:
        print("Invalid color name")
    color = input("Enter the name of a color: ").upper()
