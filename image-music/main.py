from process_image import ProcessImage

def main():
    process = ProcessImage("data/test-art.jpg")
    coords, images = process.divide_image(8)
    images[coords[100][100]].show()

if __name__ == "__main__":
    main()