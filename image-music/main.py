from process_image import ProcessImage
import json
import os

def main():
    data_dir = "../ui/interactive-art-VUE/src/assets"
    process = ProcessImage("test-art.jpg", data_dir)
    coords, images = process.divide_image(8)

    j = json.dumps(coords.tolist())
    f_name = 'test-art.json'
    with open(os.path.join(data_dir, f_name), "w") as outfile:
        outfile.write(j)

if __name__ == "__main__":
    main()