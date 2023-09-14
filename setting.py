import openpyxl as xl
from PIL import Image
import glob

# Create the frames
frames = []
duration_frame = []
time = 1000
imgs = glob.glob("C:\\ipa_log\\100\\*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
    duration_frame.append(time)
duration_frame[-1] = 3*time
# Save into a GIF file that loops forever
frames[0].save('C:\\ipa_log\\100\\png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=duration_frame, loop=0)
