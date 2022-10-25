from process_image import ProcessImage
from color_average import ColorAverage
import json
import os

def main():

    process = ProcessImage("data/test-art.jpg")
    coords, images = process.divide_image(8)


    j = json.dumps(coords.tolist())
    f_name = 'sample.json'
    out_dir = "../ui/interactive-art-VUE/src/assets"
    with open(os.path.join(out_dir, f_name), "w") as outfile:
        outfile.write(j)
    
    # i = 0
    # for image in images:
    #     print(i)
    #     image.show()
    #     i+=1

if __name__ == "__main__":
    main()