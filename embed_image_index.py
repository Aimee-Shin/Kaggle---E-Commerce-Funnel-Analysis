
import base64
import os

image_path = 'dau_trends_by_hour_of_day_heatmap.png'
html_path = 'index.html'

with open(image_path, 'rb') as img_file:
    b64_string = base64.b64encode(img_file.read()).decode('utf-8')

with open(html_path, 'r', encoding='utf-8') as html_file:
    content = html_file.read()

# Construct the new image tag
new_img_tag = f'<img src="data:image/png;base64,{b64_string}" alt="DAU Trends by Hour of Day Heatmap"'

# Replace the old image tag
# The current line in file is: <img src="dau_trends_by_hour_of_day_heatmap.png" alt="DAU Trends by Hour of Day Heatmap"
target_string = '<img src="dau_trends_by_hour_of_day_heatmap.png" alt="DAU Trends by Hour of Day Heatmap"'

if target_string in content:
    new_content = content.replace(target_string, new_img_tag)
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(new_content)
    print("Successfully embedded base64 image in index.html.")
else:
    print("Target string not found in index.html.")
