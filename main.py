# crash counts: 5, bsod counts: 1, all bc this uses too much memory LOL, so make sure u close most programs so it can run flawlessly
import os
import json
from PIL import Image
data = {"fps": 30, "batches": 1, "totalframes": 0} # change the number to the FPS of your video, the video i used has 30 so ykwtd
batch = {}
def hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
if not os.path.isdir("output"):
    os.mkdir("output")
for filename in os.listdir("frames"):
    f = os.path.join("frames", filename)
    if os.path.isfile(f):
        data["totalframes"] += 1
        print(data["totalframes"])
        if len(batch) == 150:
            print(f"dumping batch {str(data['batches'])}...")
            with open(os.path.join("output", f"batch{str(data['batches'])}.json"), "w") as file:
                json.dump(batch, file)
            data['batches'] += 1
            batch = {}
        batch[str(data["totalframes"])] = {}
        img = Image.open(f).convert("RGB")
        pix = img.load()
        def set(x, y):
            try:
                batch[str(data["totalframes"])][f"{str(x)},{str(y)}"] = hex(pix[x, y])
            except Exception as e:
                input(f"[err] {e}, press ENTER to try again.")
                set(x, y)
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                set(x, y)
if not os.path.isfile(f"batch{str(data['batches'])}.json"):
    print(f"dumping batch {str(data['batches'])}...")
    with open(os.path.join("output", f"batch{str(data['batches'])}.json"), "w") as file:
        json.dump(batch, file)
print(f"dumping data")
with open(os.path.join("output", "data.json"), "w") as file:
    json.dump(data, file)