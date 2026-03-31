# traffic light.py
import tkinter as tk

import config
from controller import Phase, TrafficLightController
from ui_traffic_light import TrafficLightWidget


def main() -> None:
    root = tk.Tk()
    root.title(config.WINDOW_TITLE)
    root.configure(bg=config.BG)
    root.resizable(False, False)

    widget = TrafficLightWidget(
        root,
        width=config.WIDTH,
        height=config.HEIGHT,
        bg=config.BG,
        padding=config.PADDING,
        line_w=config.LINE_W,
        lamp_radius=config.LAMP_RADIUS,
        lamp_gap=config.LAMP_GAP,
        off_color=config.OFF,
    )
    widget.pack(padx=14, pady=14)

    phases = [
        Phase(
            name="RED",
            duration_ms=config.RED_MS,
            set_on=lambda: widget.set_red(config.RED_ON),
            set_off=lambda: widget.set_red(config.OFF),
            off_all=widget.set_all_off,
        ),
        Phase(
            name="YELLOW",
            duration_ms=config.YELLOW_MS,
            set_on=lambda: widget.set_yellow(config.YELLOW_ON),
            set_off=lambda: widget.set_yellow(config.OFF),
            off_all=widget.set_all_off,
        ),
        Phase(
            name="GREEN",
            duration_ms=config.GREEN_MS,
            set_on=lambda: widget.set_green(config.GREEN_ON),
            set_off=lambda: widget.set_green(config.OFF),
            off_all=widget.set_all_off,
        ),
    ]

    controller = TrafficLightController(
        root_after=root.after,
        phases=phases,
        blink_enabled=config.BLINK_ENABLED,
        blink_period_ms=config.BLINK_PERIOD_MS,
    )
    controller.start()

    root.mainloop()


if __name__ == "__main__":
    main()