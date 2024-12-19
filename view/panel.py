from typing import Literal, Optional
from rich.panel import Panel
import random

def panel(renderable, subtitle : Optional[str] = None, subtitle_align = Literal["left","center","right"]):
    one_dark_colors = [
    "#C678DD",  # Purple - Keywords
    "#61AFEF",  # Blue - Function Names
    "#E06C75",  # Red/Pink - Variables & Constants
    "#98C379",  # Green - Strings
    "#D19A66",  # Orange - Numbers
    "#56B6C2",  # Cyan - Operators & Symbols
    "#E5C07B",  # Yellow - Constants
    "#528BFF",  # Brighter Blue - Focused or Active Items
    "#BE5046",  # Dark Red - Error Highlights
    "#C18401",  # Gold - Subtle Accent
    ]
    if subtitle:
        return Panel(renderable=renderable,
                    border_style=random.choice(one_dark_colors),
                    subtitle=f"[white]{subtitle}",
                    subtitle_align=subtitle_align)
    else:
        return Panel(renderable=renderable,
                    border_style=random.choice(one_dark_colors))