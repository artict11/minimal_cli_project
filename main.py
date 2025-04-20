import typer

app = typer.Typer()

@app.command()
def generate(path: str):
    print("🔥 CLI работает!")
    print("Файл:", path)

if __name__ == "__main__":
    app()
