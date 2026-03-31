# ui_traffic_light.py
import tkinter as tk
from dataclasses import dataclass


@dataclass(frozen=True)
class LampIds:
    red: int
    yellow: int
    green: int


class TrafficLightWidget(tk.Canvas):
    def __init__(self, master, *, width: int, height: int, bg: str, padding: int, line_w: int,
                 lamp_radius: int, lamp_gap: int, off_color: str):
        super().__init__(master, width=width, height=height, bg=bg, highlightthickness=0)
        self._width = width
        self._height = height
        self._p = padding
        self._lw = line_w
        self._r = lamp_radius
        self._gap = lamp_gap
        self._off = off_color

        self._draw_body_lines()
        self._lamps = self._draw_lamps()

        self.set_all_off()

    def _draw_body_lines(self) -> None:
        # Корпус: рисуем линиями (контур прямоугольника + небольшая "ножка")
        x0, y0 = self._p, self._p
        x1, y1 = self._width - self._p, self._height - self._p

        # Контур корпуса линиями (не create_rectangle, а именно create_line)
        self.create_line(x0, y0, x1, y0, width=self._lw, fill="#e6e6e6")
        self.create_line(x1, y0, x1, y1, width=self._lw, fill="#e6e6e6")
        self.create_line(x1, y1, x0, y1, width=self._lw, fill="#e6e6e6")
        self.create_line(x0, y1, x0, y0, width=self._lw, fill="#e6e6e6")

        # Ножка
        stem_x = (x0 + x1) / 2
        self.create_line(stem_x, y1, stem_x, y1 + 22, width=self._lw, fill="#e6e6e6")

    def _lamp_centers(self):
        # Три центра по вертикали
        usable_h = self._height - 2 * self._p
        total_lamps_h = 3 * (2 * self._r) + 2 * self._gap
        top = self._p + (usable_h - total_lamps_h) / 2 + self._r

        cx = self._width / 2
        cy1 = top
        cy2 = top + (2 * self._r) + self._gap
        cy3 = cy2 + (2 * self._r) + self._gap
        return (cx, cy1), (cx, cy2), (cx, cy3)

    def _draw_lamps(self) -> LampIds:
        (cx1, cy1), (cx2, cy2), (cx3, cy3) = self._lamp_centers()
        red = self.create_oval(cx1 - self._r, cy1 - self._r, cx1 + self._r, cy1 + self._r,
                               outline="#444444", width=2, fill=self._off)
        yellow = self.create_oval(cx2 - self._r, cy2 - self._r, cx2 + self._r, cy2 + self._r,
                                  outline="#444444", width=2, fill=self._off)
        green = self.create_oval(cx3 - self._r, cy3 - self._r, cx3 + self._r, cy3 + self._r,
                                 outline="#444444", width=2, fill=self._off)
        return LampIds(red=red, yellow=yellow, green=green)

    def set_all_off(self) -> None:
        self.itemconfig(self._lamps.red, fill=self._off)
        self.itemconfig(self._lamps.yellow, fill=self._off)
        self.itemconfig(self._lamps.green, fill=self._off)

    def set_red(self, color: str) -> None:
        self.itemconfig(self._lamps.red, fill=color)

    def set_yellow(self, color: str) -> None:
        self.itemconfig(self._lamps.yellow, fill=color)

    def set_green(self, color: str) -> None:
        self.itemconfig(self._lamps.green, fill=color)