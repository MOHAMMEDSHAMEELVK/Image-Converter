# PIKSEL

It is simple python image converter.
A command-line image format tool using which we can convert image format, resize the image. One can pass a single image path or image folder. 

## Team members
1.MOHAMMED SHAMEEL VK( https://github.com/shameel1133 )<br>
2.C A Muhammed Aman ( https://github.com/amanmuhammed )

## Team Id
### Python / 372

## Link to product walkthrough
<a href="https://www.loom.com/share/e5e70e691c1e4e7b934c836efbeeb225">Application walkthrough video</a>
<BR>
<a href="https://piksel-app.herokuapp.com/">Live App</a>

## How it Works ?
### step 1 :type the (python resizer.py) command in command line 

### step 2 :select the image 

### step 3 :select the commant


## Libraries used:

- [Pillow](https://python-pillow.org/)


## How to configure Instructions for setting up project

Install pillow using pip:

```bash
pip install pillow
```

## How to Run

```bash
Usage:
python resizer.py [input file name] [operation] [argument]

Operations:
-f : Format image(png to jpg and vice versa)
Example 1: python resizer.py image.jpeg -f png
Example 2: python resizer.py image.png -f jpeg

-r : Resize image
Example 1: python resizer.py image.jpeg -r 200x200
Example 2: python resizer.py image.png -r 250x200
```

## Examples

1. Image format conversion

```bash
python resizer.py image.jpeg -f png
```

2. Image resizing

```bash
python resizer.py image.jpeg -r 200x200
```

