import typer
from PIL import Image


def main(imageFaileName: str):

    im = Image.open(imageFileName)
    im.show()


if __name__ == "__main__":
    typer.run(main)


