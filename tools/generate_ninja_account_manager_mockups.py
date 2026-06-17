"""Generate public-safe NinjaAccountManager mock demo captures.

The images are synthetic portfolio assets. They use fake account names, fake
orders, and sanitized runtime labels so the public site can show the integration
shape without exposing live account data, order history, strategy names, or logs.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parents[1] / "site" / "media"
WIDTH = 1600
HEIGHT = 900


COLORS = {
    "bg": "#f5f8fb",
    "panel": "#ffffff",
    "ink": "#17202a",
    "muted": "#5b6675",
    "line": "#dce3ea",
    "teal": "#147c72",
    "blue": "#315f9f",
    "red": "#a9413b",
    "amber": "#a66a17",
    "green_soft": "#dff4ed",
    "blue_soft": "#e3ecfa",
    "red_soft": "#f7e3e1",
    "amber_soft": "#f7ecd9",
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf"]
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


FONTS = {
    "title": font(48, True),
    "h2": font(30, True),
    "h3": font(23, True),
    "body": font(21),
    "small": font(17),
    "mono": font(18),
    "mono_bold": font(18, True),
}


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str = COLORS["line"]) -> None:
    draw.rounded_rectangle(box, radius=12, fill=fill, outline=outline, width=2)


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, fill: str = COLORS["ink"], style: str = "body") -> None:
    draw.text(xy, value, fill=fill, font=FONTS[style])


def label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, fill: str = COLORS["teal"]) -> None:
    text(draw, xy, value.upper(), fill=fill, style="small")


def badge(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, fill: str, ink: str = COLORS["ink"]) -> None:
    x, y = xy
    w = max(110, len(value) * 12 + 28)
    draw.rounded_rectangle((x, y, x + w, y + 38), radius=8, fill=fill, outline=COLORS["line"])
    text(draw, (x + 14, y + 9), value, fill=ink, style="small")


def table(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], headers: list[str], rows: list[list[str]]) -> None:
    x1, y1, x2, y2 = box
    rounded(draw, box, COLORS["panel"])
    col_w = (x2 - x1 - 32) // len(headers)
    y = y1 + 22
    for i, header in enumerate(headers):
        text(draw, (x1 + 18 + i * col_w, y), header, COLORS["muted"], "small")
    y += 34
    draw.line((x1 + 18, y, x2 - 18, y), fill=COLORS["line"], width=2)
    y += 16
    for row in rows:
        for i, value in enumerate(row):
            style = "mono_bold" if i == 0 else "mono"
            text(draw, (x1 + 18 + i * col_w, y), value, COLORS["ink"], style)
        y += 38
        draw.line((x1 + 18, y - 8, x2 - 18, y - 8), fill="#edf2f6", width=1)


def base(title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, WIDTH, 86), fill=COLORS["panel"], outline=COLORS["line"])
    draw.rounded_rectangle((34, 22, 80, 66), radius=8, fill=COLORS["ink"])
    text(draw, (47, 32), "NI", "#ffffff", "h3")
    text(draw, (104, 18), title, COLORS["ink"], "title")
    text(draw, (106, 66), subtitle, COLORS["muted"], "small")
    badge(draw, (1264, 24), "MOCK DATA", COLORS["green_soft"], COLORS["teal"])
    badge(draw, (1400, 24), "SIM ONLY", COLORS["blue_soft"], COLORS["blue"])
    return img, draw


def draw_dashboard() -> None:
    img, draw = base(
        "NinjaAccountManager",
        "Public-safe synthetic dashboard capture: mocked account stream, positions, orders, and market data",
    )

    label(draw, (42, 124), "Connection")
    rounded(draw, (42, 154, 1548, 232), COLORS["panel"])
    badge(draw, (70, 174), "WebSocket listening", COLORS["green_soft"], COLORS["teal"])
    badge(draw, (294, 174), "NinjaTrader simulated", COLORS["blue_soft"], COLORS["blue"])
    badge(draw, (520, 174), "0 live orders", COLORS["amber_soft"], COLORS["amber"])
    text(draw, (760, 181), "Endpoint ws://127.0.0.1:8765/ws", COLORS["muted"], "mono")

    cards = [
        ("BALANCE", "$100,000.00", COLORS["ink"]),
        ("REALIZED P&L", "+$425.00", COLORS["teal"]),
        ("UNREALIZED P&L", "-$38.50", COLORS["red"]),
        ("BUYING POWER", "$398,600.00", COLORS["ink"]),
        ("OPEN POSITIONS", "2", COLORS["ink"]),
        ("ACTIVE ORDERS", "3", COLORS["ink"]),
    ]
    x = 42
    for header, value, color in cards:
        rounded(draw, (x, 270, x + 235, 390), COLORS["panel"])
        label(draw, (x + 20, 296), header, COLORS["muted"])
        text(draw, (x + 20, 332), value, color, "h2")
        x += 250

    table(
        draw,
        (42, 430, 760, 810),
        ["Account", "Balance", "Realized", "Unrealized", "Buying power"],
        [
            ["DEMO-OPS-01", "$100,000.00", "+$425.00", "-$38.50", "$398,600"],
            ["DEMO-OPS-02", "$50,000.00", "$0.00", "$0.00", "$199,400"],
        ],
    )
    table(
        draw,
        (800, 430, 1548, 810),
        ["Instrument", "Bid", "Ask", "Last", "Volume"],
        [
            ["NQ DEMO", "19,852.25", "19,852.50", "19,852.25", "38,104"],
            ["ES DEMO", "5,628.00", "5,628.25", "5,628.25", "28,771"],
            ["RTY DEMO", "2,121.60", "2,121.70", "2,121.70", "12,509"],
        ],
    )
    text(draw, (42, 846), "All values are generated fixtures. No real account names, broker state, logs, signals, or strategy parameters are shown.", COLORS["muted"], "small")
    img.save(OUT_DIR / "ninja-account-manager-dashboard.png")


def draw_strategy_console() -> None:
    img, draw = base(
        "NinjaAccountManager Strategy Console",
        "Synthetic runtime integration capture: API status, operator controls, strategy events, and safety gates",
    )

    rounded(draw, (42, 126, 600, 780), COLORS["panel"])
    label(draw, (70, 154), "Strategy runtime")
    status_rows = [
        ("API Endpoint", "tcp://127.0.0.1:8766"),
        ("API Clients", "1 synthetic client"),
        ("NT Connections", "1 simulated bridge"),
        ("Execution Mode", "SIM"),
        ("Runtime State", "InPosition"),
        ("Intake", "Enabled after operator confirm"),
        ("Heartbeat", "Healthy"),
        ("Recovery", "Clear"),
        ("Account", "DEMO-OPS-01"),
        ("Instrument", "NQ DEMO"),
        ("Template", "public-demo-template"),
        ("Position", "Long qty=1 avg=19844.25"),
        ("Protective Stop", "19824.25"),
        ("Target", "40 ticks"),
    ]
    y = 206
    for key, value in status_rows:
        text(draw, (70, y), key, COLORS["muted"], "small")
        text(draw, (258, y - 2), value, COLORS["ink"], "mono")
        y += 35
    badge(draw, (70, 712), "No active runtime warnings", COLORS["green_soft"], COLORS["teal"])

    rounded(draw, (632, 126, 1548, 390), COLORS["panel"])
    label(draw, (660, 154), "Operator test harness")
    controls = [
        ("Enable Intake", COLORS["green_soft"]),
        ("Request Snapshot", COLORS["blue_soft"]),
        ("Flatten + Disable", COLORS["red_soft"]),
        ("Cancel Working", COLORS["amber_soft"]),
        ("Send HEARTBEAT", COLORS["blue_soft"]),
        ("Send EXIT_ALL", COLORS["red_soft"]),
    ]
    x, y = 660, 202
    for name, fill in controls:
        badge(draw, (x, y), name, fill)
        x += 216
        if x > 1360:
            x = 660
            y += 58
    text(draw, (660, 334), "Live routing hidden. Public demo uses fixture commands and disabled order submission.", COLORS["muted"], "small")

    table(
        draw,
        (632, 430, 1548, 780),
        ["Time", "Event", "Signal ID", "Runtime", "Summary"],
        [
            ["10:31:02", "ACCEPTED", "public-demo-01", "Idle", "fixture command accepted"],
            ["10:31:04", "ENTRY", "public-demo-01", "EntryPending", "bridge dispatch"],
            ["10:31:05", "FILLED", "public-demo-01", "InPosition", "demo fill @ 19844.25"],
            ["10:31:05", "STOP", "public-demo-01", "InPosition", "protective stop active"],
            ["10:31:05", "TARGET", "public-demo-01", "InPosition", "target active"],
        ],
    )
    text(draw, (42, 846), "This screen is generated from a redacted fixture modeled after source-level AppState and StrategySnapshot fields.", COLORS["muted"], "small")
    img.save(OUT_DIR / "ninja-account-manager-strategy.png")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    draw_dashboard()
    draw_strategy_console()


if __name__ == "__main__":
    main()
