from PIL import Image

from kgy import vision


def test_invariance():
    image_1 = Image.open("tests/images/tiger_1.jpg")
    image_2 = Image.open("tests/images/tiger_2.jpg")

    representation_1 = vision(image_1)
    representation_2 = vision(image_2)

    assert representation_1 == representation_2


    
def test_contrast_1():
    image_1 = Image.open("tests/images/tiger_1.jpg")
    image_2 = Image.open("tests/images/dog.jpg")

    representation_1 = vision(image_1)
    representation_2 = vision(image_2)

    assert not representation_1 == representation_2


def test_contrast_2():
    image_1 = Image.open("tests/images/tiger_2.jpg")
    image_2 = Image.open("tests/images/dog.jpg")

    representation_1 = vision(image_1)
    representation_2 = vision(image_2)

    assert not representation_1 == representation_2