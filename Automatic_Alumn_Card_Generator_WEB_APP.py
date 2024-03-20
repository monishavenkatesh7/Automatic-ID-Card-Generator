#!/usr/bin/env python
# coding: utf-8

# In[13]:


# !pip install flask
# !pip install Pillow

from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os


# In[14]:


Template_path = 'static/Template/Template.png'
font_path = 'static/Fonts/Lexend-Medium.ttf'
font_size = 110


def ID_generator(Name,DOB,ID,Program,Year_of_passing,Template_path,photo_path,font_path,font_size):
    image = Image.open(Template_path)
    draw = ImageDraw.Draw(image)

    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype(font_path, size=font_size)

    Name = Name.upper()
    (x, y) = (1734, 1440)
    draw.text((x, y), Name, fill=color, font=font)

    (x, y) = (1734, 1745)
    draw.text((x, y), DOB, fill=color, font=font)

    ID = str(ID)
    (x, y) = (1734, 2045)
    draw.text((x, y), ID, fill=color, font=font)

    (x, y) = (1734, 2350)
    draw.text((x, y), Program, fill=color, font=font)

    Year_of_passing = str(Year_of_passing)
    (x, y) = (1734, 2655)
    draw.text((x, y), Year_of_passing, fill=color, font=font)

    photo = Image.open(photo_path)
    resized_image = photo.resize((1132, 1404))
#     resized_image.save('output_image.jpg')
    image.paste(resized_image,(3475,1445))

#     image.save(Name+'.png')
    return image


# In[15]:


from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

app = Flask(__name__)

# Define paths
# uploads_dir = os.path.join(app.root_path, 'uploads')
# generated_dir = os.path.join(app.root_path, 'Generated')

uploads_dir = os.path.join(app.root_path, 'Temparory/uploads')
generated_dir = os.path.join(app.root_path, 'Temparory/Generated')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        id_number = request.form['id_number']
        program = request.form['program']
        year_of_passing = request.form['year_of_passing']
        uploaded_photo = request.files['photo']
        
        if not (name and dob and id_number and program and year_of_passing and uploaded_photo):
            return '''
                <script>
                    alert("Please fill in all fields and upload a photo.");
                </script>
                <script>
                    window.history.back();
                </script>
            '''

        dob = datetime.strptime(dob, '%Y-%m-%d').strftime('%d/%m/%Y')
        id_number = int(id_number)
        year_of_passing = int(year_of_passing)

        # Handle file upload for photo
        photo_path = os.path.join(uploads_dir, uploaded_photo.filename)
        uploaded_photo.save(photo_path)
        
        # Call your ID_generator function
        generated_image = ID_generator(name,dob,id_number,program,year_of_passing,Template_path,photo_path,font_path,font_size)

        # Save the generated image to 'Generated' folder
        generated_image_path = os.path.join(generated_dir, 'ID_card.png')
        generated_image.save(generated_image_path)

        return f'''
                <div style="position: absolute; top: 10px; right: 10px;">
                <img src="/static/images/College Logo.png" alt="Logo" width="100">
                </div>
                <div style="position: absolute; top: 10px; left: 10px;">
                <img src="/static/images/College Logo.png" alt="Logo" width="100">
                </div>
                <div style="font-family: Arial, sans-serif; max-width: 800px; margin: 2px auto; text-align: center; padding: 2px;">
                <h1 style="color: #333;font-size: 30px;">ABC College Of Engineering</h1>
                </div>
                <div style="font-family: Arial, sans-serif; max-width: 800px; margin: auto; text-align: center; padding: 0px 20px; background-color: #f9f9f9; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <h1 style="color: #333;font-size: 20px;">Automatic ID Card Generator</h1>
                <p>Name: {name}</p>
                <p>Date of Birth: {dob}</p>
                <p>ID: {id_number}</p>
                <p>Program: {program}</p>
                <p>Year of Passing: {year_of_passing}</p>
                <p>Image generated successfully!</p>
                <p><a href="/download" style="text-decoration: none; background-color: #007bff; color: #fff; padding: 10px 20px; border-radius: 5px;" download>Download Image</a></p>
                <form method="get" action="/">
                    <input type="submit" value="Generate Another" style="background-color: #28a745; color: #fff; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                </form>
                <div style="height: 5px;"></div> <!-- Added an empty div for spacing -->
            </div>
        '''

    return '''
                <div style="position: absolute; top: 10px; right: 10px;">
                <img src="/static/images/College Logo.png" alt="Logo" width="100">
                </div>
                <div style="position: absolute; top: 10px; left: 10px;">
                <img src="/static/images/College Logo.png" alt="Logo" width="100">
                </div>
                <div style="font-family: Arial, sans-serif; max-width: 800px; margin: 2px auto; text-align: center; padding: 2px;">
                <h1 style="color: #333;font-size: 30px;">ABC College Of Engineering</h1>
                </div>
                <div style="font-family: Arial, sans-serif; max-width: 800px; margin: auto; text-align: center; padding: 0px 20px; background-color: #f9f9f9; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <h1 style="color: #333;font-size: 20px;">Automatic ID Card Generator</h1>
                <form method="post" enctype="multipart/form-data" style="margin-top: 20px;">
                <div style="margin-bottom: 10px;"><input type="text" name="name" placeholder="Name  (Number of characters should be less than 23 including spaces)" style="padding: 10px; width: 100%;"></div>
                <div style="margin-bottom: 10px;"><input type="date" name="dob" style="padding: 10px; width: 100%;"></div>
                <div style="margin-bottom: 10px;"><input type="number" name="id_number" placeholder="ID" style="padding: 10px; width: 100%;"></div>
                <div style="margin-bottom: 10px;"><input type="text" name="program" placeholder="Program" style="padding: 10px; width: 100%;"></div>
                <div style="margin-bottom: 10px;"><input type="number" name="year_of_passing" placeholder="Year of Passing" style="padding: 10px; width: 100%;"></div>
                <div style="margin-bottom: 10px;">
                    <label for="photo" style="display: block; margin-bottom: 5px;">Please Upload the image near to the size of 1132x1404 else the image will be distorted in the ID Card</label>
                    <input type="file" name="photo" accept="image/*" style="padding: 10px; width: 100%;">
                </div>
                <input type="submit" value="Submit" style="background-color: #007bff; color: #fff; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
            </form>
            <div style="height: 5px;"></div> <!-- Added an empty div for spacing -->
        </div>
    '''

@app.route('/download', methods=['GET'])
def download():
    generated_image_path = os.path.join(generated_dir, 'ID_card.png')
    return send_file(generated_image_path, as_attachment=True)

# Create the uploads and 'Generated' folders if they don't exist
os.makedirs(uploads_dir, exist_ok=True)
os.makedirs(generated_dir, exist_ok=True)

if __name__ == '__main__':
    app.run()
