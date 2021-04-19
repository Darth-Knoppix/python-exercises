import typer
import requests
from bs4 import BeautifulSoup

app = typer.Typer()

def get_meta_tags(html: str):
    page = BeautifulSoup(html, 'html.parser')
    return page.head.find_all('meta')

@app.command()
def audit(url: str):
    response = None
    try:
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        typer.secho("The URL doesn't have a valid protocol, try adding http:// or https://", fg=typer.colors.BRIGHT_RED)
    
    all_tags = get_meta_tags(response.content)
    og_tags = [tag for tag in all_tags if tag.get('property', '').startswith('og:')]
    longest_tag_len = max([len(tag['property']) for tag in og_tags]) - 4
    typer.secho("Open Graph Properties\n", bold=True)

    for tag in og_tags:
        message = "* "
        prop_parts = tag['property'].split(':')
        message += typer.style(prop_parts[0], fg=typer.colors.WHITE, dim=True)
        message += ":"
        message += typer.style(prop_parts[1].ljust(longest_tag_len), fg=typer.colors.GREEN)
        message += " = "
        message += typer.style(tag.get('content', '-'), fg=typer.colors.BLUE)
        typer.echo(message)


    typer.echo()


@app.command()
def interactive():
    url = typer.prompt("What URL would you like to audit?")
    if url is None:
        typer.echo("You need to specify a URL!")
    audit(url)


if __name__ == "__main__":
    app()