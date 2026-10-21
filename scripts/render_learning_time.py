"""Render the README total and calendar from confirmed daily minutes."""

from datetime import date, timedelta
from html import escape
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
START_MARKER = "<!-- learning-time:start -->"
END_MARKER = "<!-- learning-time:end -->"
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
THEMES = {
    "light": {
        "background": "#ffffff", "border": "#d1d9e0", "text": "#59636e",
        "empty": "#d1d9e0", "zero": "#ebedf0",
        "greens": ("#9be9a8", "#40c463", "#30a14e", "#216e39"),
    },
    "dark": {
        "background": "#0d1117", "border": "#30363d", "text": "#9198a1",
        "empty": "#30363d", "zero": "#161b22",
        "greens": ("#0e4429", "#006d32", "#26a641", "#39d353"),
    },
}


def duration(minutes):
    hours, remainder = divmod(minutes, 60)
    if not hours:
        return f"{remainder} min"
    return f"{hours} h" + (f" {remainder} min" if remainder else "")


def day_label(day):
    return f"{day.day} {MONTHS[day.month - 1]} {day.year}"


def load_record():
    record = json.loads((ROOT / "data/learning-time.json").read_text())
    if record["timezone"] != "Asia/Kolkata":
        raise ValueError("Daily dates must use India time.")
    started = date.fromisoformat(record["started_on"])
    as_of = date.fromisoformat(record["as_of"])
    if started > as_of:
        raise ValueError("The tracking start must not be after the calendar date.")
    days = {}
    for key, minutes in record["days"].items():
        day = date.fromisoformat(key)
        if not started <= day <= as_of:
            raise ValueError(f"Recorded date is outside the tracking period: {key}")
        if type(minutes) is not int or not 0 <= minutes <= 1440:
            raise ValueError(f"Daily minutes must be an integer from 0 to 1440: {key}")
        days[day] = minutes
    return started, as_of, days


def colour(minutes, theme):
    if minutes is None:
        return theme["background"]
    if minutes == 0:
        return theme["zero"]
    level = 0 if minutes < 60 else 1 if minutes < 120 else 2 if minutes < 240 else 3
    return theme["greens"][level]


def render_calendar(started, as_of, days, theme_name):
    theme = THEMES[theme_name]
    # Sunday begins each column, as in GitHub's contribution calendar.
    week_start = as_of - timedelta(days=(as_of.weekday() + 1) % 7)
    first = week_start - timedelta(weeks=52)
    total = duration(sum(days.values()))
    description = (
        f"Daily learning time from {day_label(first)} to {day_label(as_of)}. "
        f"Tracking began {day_label(started)}. Total recorded: {total}. "
        "Outlined squares have no entry. Filled grey means a reported zero. "
        "Green levels are under 1 hour, 1 to under 2 hours, "
        "2 to under 4 hours, and 4 hours or more."
    )
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="860" height="190" '
        'viewBox="0 0 860 190" role="img" aria-labelledby="title description">',
        '<title id="title">Bitcoin learning time</title>',
        f'<desc id="description">{escape(description)}</desc>',
        '<style>text{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;'
        f'font-size:11px;fill:{theme["text"]}' + '}</style>',
        f'<rect x="0.5" y="0.5" width="859" height="189" rx="10" '
        f'fill="{theme["background"]}" stroke="{theme["border"]}"/>',
    ]
    # Skip a short partial month at the left edge to avoid overlapping labels.
    previous_month = None
    for column in range(53):
        sunday = first + timedelta(weeks=column)
        if sunday.month != previous_month:
            if column or sunday.day <= 14:
                out.append(f'<text x="{46 + column * 15}" y="26">{MONTHS[sunday.month - 1]}</text>')
            previous_month = sunday.month
    for row, label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        out.append(f'<text x="12" y="{50 + row * 15}">{label}</text>')
    for offset in range((as_of - first).days + 1):
        day = first + timedelta(days=offset)
        minutes = days.get(day)
        column, row = divmod(offset, 7)
        label = "Not tracked yet" if day < started else "Not reported" if minutes is None else duration(minutes)
        stroke = theme["empty"] if minutes is None else "none"
        out.append(
            f'<rect data-date="{day.isoformat()}" x="{46 + column * 15}" '
            f'y="{40 + row * 15}" width="12" height="12" rx="2" '
            f'fill="{colour(minutes, theme)}" stroke="{stroke}" stroke-width="0.6">'
            f'<title>{day_label(day)}: {label}</title></rect>'
        )
    out.append(f'<text x="22" y="173">Since {day_label(started)}</text>')
    legend = (("No entry", None, 104), ("0", 0, 48), ("&lt;1h", 1, 72),
              ("1–&lt;2h", 60, 86), ("2–&lt;4h", 120, 86), ("4h+", 240, 62))
    x = 327
    for label, minutes, spacing in legend:
        stroke = theme["empty"] if minutes is None else "none"
        out.append(f'<rect x="{x}" y="162" width="12" height="12" rx="2" '
                   f'fill="{colour(minutes, theme)}" stroke="{stroke}" stroke-width="0.6"/>')
        out.append(f'<text x="{x + 18}" y="173">{label}</text>')
        x += spacing
    out.append('</svg>')
    return "\n".join(out) + "\n"


def main():
    started, as_of, days = load_record()
    total = duration(sum(days.values()))
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    for theme in THEMES:
        (assets / f"learning-time-{theme}.svg").write_text(
            render_calendar(started, as_of, days, theme), encoding="utf-8"
        )
    section = f'''{START_MARKER}
**Total learning time: {total}**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/learning-time-dark.svg">
  <img src="assets/learning-time-light.svg" alt="Daily Bitcoin learning time. Total: {total}. Outlined squares have no entry; green squares show recorded time.">
</picture>
{END_MARKER}'''
    path = ROOT / "README.md"
    readme = path.read_text()
    if START_MARKER in readme or END_MARKER in readme:
        if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
            raise ValueError("README must have one complete learning-time section.")
        start, end = readme.index(START_MARKER), readme.index(END_MARKER)
        if end < start:
            raise ValueError("README learning-time markers are out of order.")
        readme = readme[:start] + section + readme[end + len(END_MARKER):]
    else:
        readme = readme.rstrip() + "\n\n" + section + "\n"
    path.write_text(readme, encoding="utf-8")
    print(f"Updated calendar through {as_of}: {total} total.")


if __name__ == "__main__":
    main()
