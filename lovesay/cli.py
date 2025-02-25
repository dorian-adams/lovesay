from typing import Optional
import typer
import lovesay.love as lovesay
import shutil

app = typer.Typer(add_completion=False)

@app.command()
def love(
    quote: Optional[str] = typer.Argument(None, help="An arbitrary message to print", show_default=False),
    color: str = typer.Option('catppuccin', "--color", "-c", help="The name of your preferred color scheme"),
    max_width: int = typer.Option(shutil.get_terminal_size()[0], "--max-width", help="Set a max width for quotes, must be less than the terminal can fit.")
):
    """
    Supported color schemes: catppuccin, dracula, nord, gruvbox, onedark, tokyonight, rosepine, ayu, palenight, and gogh 
    """
    lovesay.main(quote, color, max_width)

def main():
    app()
