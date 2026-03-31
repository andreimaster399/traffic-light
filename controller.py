# controller.py
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass(frozen=True)
class Phase:
    name: str
    duration_ms: int
    set_on: Callable[[], None]     # включить нужную лампу
    set_off: Callable[[], None]    # выключить эту лампу (обычно в OFF)
    off_all: Callable[[], None]    # выключить все лампы


class TrafficLightController:
    def __init__(self, *, root_after, phases: list[Phase], blink_enabled: bool, blink_period_ms: int):
        self._after = root_after  # root.after
        self._phases = phases
        self._blink_enabled = blink_enabled
        self._blink_period = blink_period_ms

        self._phase_idx = 0
        self._phase_end_after_id: Optional[str] = None
        self._blink_after_id: Optional[str] = None
        self._blink_state_on = True

    def start(self) -> None:
        self._run_phase()

    def _run_phase(self) -> None:
        phase = self._phases[self._phase_idx]
        phase.off_all()

        self._blink_state_on = True
        if self._blink_enabled:
            self._tick_blink(phase)
        else:
            phase.set_on()

        # Планируем окончание фазы
        self._phase_end_after_id = self._after(phase.duration_ms, self._next_phase)

    def _tick_blink(self, phase: Phase) -> None:
        if self._blink_state_on:
            phase.set_on()
        else:
            phase.set_off()

        self._blink_state_on = not self._blink_state_on
        self._blink_after_id = self._after(self._blink_period, lambda: self._tick_blink(phase))

    def _next_phase(self) -> None:
        self._phase_idx = (self._phase_idx + 1) % len(self._phases)
        self._run_phase()