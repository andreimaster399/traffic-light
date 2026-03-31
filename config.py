# config.py

WINDOW_TITLE = "Светофор"
BG = "#111111"

# Размеры
WIDTH = 220
HEIGHT = 420
PADDING = 18
LINE_W = 4

# Лампы
LAMP_RADIUS = 42
LAMP_GAP = 18

# Цвета (включено/выключено)
RED_ON = "#ff2d2d"
YELLOW_ON = "#ffd400"
GREEN_ON = "#18d36b"
OFF = "#2b2b2b"

# Длительности фаз (мс)
# config.py

RED_MS = 5000
YELLOW_MS = 3000
GREEN_MS = 5000

# Мигание внутри активной фазы
BLINK_PERIOD_MS = 350  # как часто менять on/off
BLINK_ENABLED = True   # если False — будет просто гореть без мигания