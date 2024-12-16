from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
import time

def loading(bars: list[tuple[str, float]]):
    """
    Menampilkan beberapa loading bar dengan teks dan durasi yang ditentukan,
    serta menambahkan loading total di bagian bawah.
    
    Args:
        bars (list[tuple[str, float]]): Daftar tuple berupa (teks, durasi).
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        transient=True,
    ) as progress:
        tasks = []

        # Tambahkan semua bar dengan teks dan durasi masing-masing
        total_duration = sum(duration for _, duration in bars)
        total_task = progress.add_task("[bold green]Memuat", total=100)

        for text, duration in bars:
            task = progress.add_task(f"[cyan]{text}", total=100)
            tasks.append((task, duration))

        # Proses semua bar secara berurutan
        completed = 0
        for task, duration in tasks:
            for _ in range(100):
                time.sleep(duration / 100)
                progress.update(task, advance=1)

                # Update progress untuk Total
                completed += (duration / total_duration) / 100 * 100
                progress.update(total_task, completed=completed)