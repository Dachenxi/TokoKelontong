from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
import time

def loading(duration=3):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Loading...", total=100)
        for _ in range(100):
            time.sleep(duration / 100)
            progress.update(task, advance=1)