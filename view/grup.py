from rich.panel import Panel
from rich.console import Group

def grup(*text):
    grup_text = Group(*text)
    return Panel.fit(grup_text)