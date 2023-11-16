import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from datetime import datetime
import getResult
from getResult import *
import level2_getResult
from level2_getResult import *
import os
from glob import glob
from PIL import Image
from tkinter import ttk
import boto3

# Define the folder path
folder_path = "C:\\Users\\공용PC\\Pictures\\Camera Roll"
material_list = []
symbol = []
stain = []
stain_area = []
caution = []
accessories = []
special = []
result = []
result_save = []
first = []
second = []
image_list = []

input_number = ""
texture = ""
material_list_string = ""
material_list_str = ""

# Connect to the database
cnx = mysql.connector.connect(
    host="database-1.cfigciaxwk2v.us-west-1.rds.amazonaws.com",
    user="admin",
    password="LS202215f!",
    database="lsdb"
)

root = tk.Tk()
root.geometry('1200x1000')

# Create three labels for images
image_labels = [tk.Label(root, bg="white", width=200, height=200) for _ in range(3)]

# Create a dropdown menu for the number of images to load
num_images_var = tk.IntVar()
num_images_dropdown = ttk.Combobox(root, textvariable=num_images_var)
num_images_dropdown['values'] = (1, 2, 3)
num_images_dropdown.grid(row=60, column=0)

import glob


def s3_connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="AKIA32ZTNE6UZ7DNQN5W",
            aws_secret_access_key="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",
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3


def get_recent_files(directory, num_files):
    files = glob.glob(directory + "/*")
    files.sort(key=os.path.getmtime, reverse=True)
    return files[:num_files]


# Define a function to load images
def load_images():
    global image_list
    # Clear all image labels
    for label in image_labels:
        label.grid_forget()  # Forget (remove) the label from the grid
        label.config(image=None)

    # Load images based on the selection in the dropdown
    num_images = num_images_var.get()
    recent_images = get_recent_files(folder_path, num_images)
    for i, image_path in enumerate(recent_images):
        # Open the image
        image = Image.open(image_path)
        # Resize the image
        image = image.resize((200, 200), Image.ANTIALIAS)
        # Convert the image to a PhotoImage
        photo = ImageTk.PhotoImage(image)
        # Create a label for the image
        label = image_labels[i]
        label.config(image=photo)
        label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        # Add the label to the grid
        label.grid(row=61, column=i + 1)
        print(image_path)
        image_list.append(image_path)


load_button = tk.Button(root, text="Load Images", command=load_images)
load_button.grid(row=60, column=1)


def reset_radiobuttons():
    color_var.set('')
    laundry_var.set('')
    stain_var.set('')
    stain_area_var.set('')


# Input number
input_number_label = tk.Label(root, text="Number:")
input_number_label.grid(row=0, column=0)
input_number_entry = tk.Entry(root)
input_number_entry.grid(row=0, column=1)

# Material list display
material_list_label = tk.Label(root)
material_list_label.grid(row=1, column=30, columnspan=3)

# Material selection
material_label = tk.Label(root, text="소재정보:", font=('Helvetica', 12, 'bold'), fg='red')
material_label.grid(row=2, column=30, sticky="W")
material_vars = {}
material_options = ["울", "견", "레이온", "마", "아크릴", "폴리에스터", "나일론", "폴리우레탄", "면", "천연가죽", "고어텍스", "인조가죽"]
for idx, material in enumerate(material_options, start=6):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=material, variable=var)
    # Compute the row and column for the grid
    row = idx // 2
    column = 30 + idx % 2
    cb.grid(row=row, column=column, sticky="W")
    material_vars[material] = var


# Update the Checkbutton states based on the material_list
def update_material_checkbuttons(a):
    # Uncheck all materials first
    for material in material_vars:
        material_vars[material].set(False)

    if a == 0:
        # Check the materials that are in the material_list
        for material in material_list:
            if material in material_vars:
                material_vars[material].set(True)


# Color selection
color_label = tk.Label(root, text="색상:", font=('Helvetica', 12, 'bold'), fg='red')
color_label.grid(row=2, column=0, sticky="W")
color_var = tk.StringVar()
color_options = ["검정", "흰색", "빨강"]
for idx, color in enumerate(color_options, start=3):
    rb = tk.Radiobutton(root, text=color, variable=color_var, value=color)
    rb.grid(row=idx, column=0, sticky="W")

# Laundry symbol selection
laundry_label = tk.Label(root, text="세탁부호:", font=('Helvetica', 12, 'bold'), fg='red')
laundry_label.grid(row=2, column=1, sticky="W")
laundry_var = tk.StringVar()
symbol_vars={}
laundry_options = ["물세탁", "드라이", "손세탁"]
for idx, symbol in enumerate(laundry_options, start=3):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root,text=symbol,variable=var)
    cb.grid(row=idx, column=1, sticky="W")
    symbol_vars[symbol] = var


# Stain info
stain_label = tk.Label(root, text="얼룩정보:", font=('Helvetica', 12, 'bold'), fg='red')
stain_label.grid(row=2, column=2, sticky="W")
stain_var = tk.StringVar()
stain_vars = {}
stain_options = ["수용성", "지용성", "찌든오염", "없음"]
for idx, stain in enumerate(stain_options, start=3):

    var = tk.BooleanVar()
    cb = tk.Checkbutton(root,text=stain,variable=var)
    cb.grid(row=idx, column=2, sticky="W")
    stain_vars[stain] = var




# Stain area info
stain_area_label = tk.Label(root, text="특수의류:", font=('Helvetica', 12, 'bold'), fg='blue')
stain_area_label.grid(row=10, column=0, sticky="W")
stain_area_var = tk.StringVar()
stain_area_options = ["모자", "털모자", "넥타이", "스카프", "수영복", "특수의류 아님"]
for idx, area in enumerate(stain_area_options, start=11):
    rb = tk.Radiobutton(root, text=area, variable=stain_area_var, value=area)
    rb.grid(row=idx, column=0, sticky="W")

# Cautions info
cautions_label = tk.Label(root, text="수축요인:", font=('Helvetica', 12, 'bold'), fg='blue')
cautions_label.grid(row=10, column=1, sticky="W")
shrink_vars = {}
cautions_options = ["비닐형태", "꽈배기원단", "트위드", "코듀로이/벨벳", "안감(폴리)", "고무소재", "수축/팽창", "스크래치", "소재강도"]
for idx, caution in enumerate(cautions_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=caution, variable=var)
    cb.grid(row=idx, column=1, sticky="W")
    shrink_vars[caution] = var

# Cautions-2 info
cautions2_label = tk.Label(root, text="손상/수축", font=('Helvetica', 12, 'bold'), fg='blue')
cautions2_label.grid(row=10, column=2, sticky="W")
status_vars = {}
cautions2_options = ["세탁불가", "손상진행", "탈색진행", "이염발생"]
for idx, caution in enumerate(cautions2_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=caution, variable=var)
    cb.grid(row=idx, column=2, sticky="W")
    status_vars[caution] = var

# Accessories info
accessories_label = tk.Label(root, text="다지인:", font=('Helvetica', 12, 'bold'), fg='blue')
accessories_label.grid(row=10, column=3, sticky="W")
design_vars = {}
accessories_options = ["접착물", "부착물", "없음"]
for idx, accessory in enumerate(accessories_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=accessory, variable=var)
    cb.grid(row=idx, column=3, sticky="W")
    design_vars[accessory] = var

# Cautions-2 info
cautions3_label = tk.Label(root, text="디자인-세부", font=('Helvetica', 12, 'bold'), fg='blue')
cautions3_label.grid(row=10, column=30, sticky="W")
design_detail_vars = {}
cautions3_options = ["프린트", "페인트", "큐빅", "비즈", "메탈", "패치", "반짝이", "레이스", "시스루", "올풀림"]
for idx, caution in enumerate(cautions3_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=caution, variable=var)
    cb.grid(row=idx, column=30, sticky="W")
    design_detail_vars[caution] = var

# Special info
special_label = tk.Label(root, text="특수기능", font=('Helvetica', 12, 'bold'), fg='blue')
special_label.grid(row=10, column=40, sticky="W")
special_vars = {}
special_options = ["충전재", "의류패턴", "물빠짐의류"]
for idx, special in enumerate(special_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=special, variable=var)
    cb.grid(row=idx, column=40, sticky="W")
    special_vars[special] = var

# Extra information
extra_label = tk.Label(root, text="Additional Information:")
extra_label.grid(row=34, column=0, sticky="W")
extra_entry = tk.Entry(root, width=50)
extra_entry.grid(row=34, column=1, sticky="W")

# Extra information
real_answer_label = tk.Label(root, text="장인세탁법 (수정 필요시):")
real_answer_label.grid(row=47, column=0, sticky="W")
real_answer_entry = tk.Entry(root, width=50)
real_answer_entry.grid(row=47, column=1, sticky="W")


# Get Result function
def get_result():
    global result, first, second
    global stain_area
    global result_save
    first = []
    second = []
    result = []

    special_material = [k for k,  v in special_vars.items() if v.get()]
    symbol_list = [k for k,  v in symbol_vars.items() if v.get()]
    stain_type = [k for k, v in stain_vars.items() if v.get()]
    material_list = [k for k, v in material_vars.items() if v.get()]
    design_detail = [k for k, v in design_detail_vars.items() if v.get()]
    design_list = [k for k, v in design_vars.items() if v.get()]
    status_list = [k for k, v in status_vars.items() if v.get()]
    shrink_list = [k for k, v in shrink_vars.items() if v.get()]
    special_clothes = [stain_area_var.get()]
    color = [color_var.get()]
    accessories_total = design_list + design_detail

    stain_list = stain_type
    stain_area = stain_area
    design_list = accessories_total
    special_clothes = special_clothes
    # design_list = status_list+accessories
    print("=====의류정보=====")
    print(color)
    print(symbol_list)
    print(stain_list)
    print(material_list)
    print(special_clothes)
    print(shrink_list)

    print(status_list)
    print(design_list)
    print(special_material)
    print("=========")

    level1_result = level2_getResult.level1_2(special_clothes, symbol_list, material_list)
    print("1&2", level1_result)
    level3_result = level2_getResult.level3(level1_result, symbol_list, material_list, shrink_list, status_list, special_material)
    print("3", level3_result)
    level4_result = level2_getResult.level4(level3_result, symbol_list, material_list, shrink_list, status_list, special_material)
    print("4", level4_result)
    level5_result = level2_getResult.level5(level3_result, symbol_list, material_list, shrink_list, status_list, special_material,
                           stain_list)
    print("5", level5_result)
    level6_result = level2_getResult.level6(level4_result, symbol_list, material_list, shrink_list, status_list, special_material,
                           design_list)
    print("6", level6_result)


    # Update the result label
    result_label.config(text="Result: " + str(level5_result+level6_result))
    result_save = result
    first = []
    second = []
    result = []


get_result_button = tk.Button(root, text="Get Result", command=get_result, width=20, height=2)
get_result_button.grid(row=50, column=0, sticky="W")  # adjust the grid arguments as needed

# Result display
result_label = tk.Label(root)
result_label.grid(row=46, column=0, columnspan=3)


# Save Data function
def save_data():
    global stain_area
    global result_save
    global image_list
    image1_fullname = ""
    image2_fullname = ""
    image3_fullname = ""
    current_time = str(datetime.now())
    accessories_detail2 = [k for k, v in design_detail_vars.items() if v.get()]
    special_clothes = [k for k, v in special_vars.items() if v.get()]
    design_list = [k for k, v in design_vars.items() if v.get()]
    status_list = [k for k, v in status_vars.items() if v.get()]
    shrink_list = [k for k, v in shrink_vars.items() if v.get()]
    stain_area = [stain_area_var.get()]
    stain_type = [stain_var.get()]
    color = [color_var.get()]
    symbol = [laundry_var.get()]
    extra = extra_entry.get()
    real_answer = real_answer_entry.get()
    accessories_total = design_list + accessories_detail2
    input_number = input_number_entry.get()

    # Create a cursor
    cursor = cnx.cursor()

    # Check if the id already exists
    cursor.execute("SELECT 1 FROM lsdb.data_collect_SP2 WHERE id = %s", (input_number,))
    if cursor.fetchone() is not None:
        # Ask the user if they want to overwrite the existing entry
        overwrite = messagebox.askyesno("Info", input_number + "번 id가 이미 존재합니다.덮어쓸까요?")
        if overwrite:
            # If the user chooses to overwrite, delete the existing entry
            cursor.execute("DELETE FROM lsdb.data_collect_SP2 WHERE id = %s", (input_number,))
        else:
            # If the user chooses not to overwrite, return without saving
            return

    # Define image variables
    image1 = image_list[0] if len(image_list) > 0 else None
    image2 = image_list[1] if len(image_list) > 1 else None
    image3 = image_list[2] if len(image_list) > 2 else None

    print(image1, image2, image3, "&&&&&&")
    s3 = s3_connection()
    image1_rename = input_number + "-1" if len(image_list) > 0 else None
    image2_rename = input_number + "-2" if len(image_list) > 1 else None
    image3_rename = input_number + "-3" if len(image_list) > 2 else None
    print(image1_rename)
    print(image2_rename)
    print(image3_rename)

    if image1_rename:
        image1_fullname = "https://lsolution-data-storage.s3.ap-northeast-2.amazonaws.com/data_collect_SP/" + image1_rename + ".jpg"
        try:
            s3.upload_file(image1, "lsolution-data-storage", "data_collect_SP/" + image1_rename + ".jpg",
                           ExtraArgs={'ContentType': "image/jpeg"})

        except Exception as e:
            print(e)
    else:
        print("Not exists")
    if image2_rename:
        image2_fullname = "https://lsolution-data-storage.s3.ap-northeast-2.amazonaws.com/data_collect_SP/" + image2_rename + ".jpg"
        try:
            s3.upload_file(image2, "lsolution-data-storage", "data_collect_SP/" + image2_rename + ".jpg",
                           ExtraArgs={'ContentType': "image/jpeg"})
        except Exception as e:
            print(e)
    else:
        print("Not exists")
    if image3_rename:
        image3_fullname = "https://lsolution-data-storage.s3.ap-northeast-2.amazonaws.com/data_collect_SP/" + image3_rename + ".jpg"
        try:
            s3.upload_file(image3, "lsolution-data-storage", "data_collect_SP/" + image3_rename + ".jpg",
                           ExtraArgs={'ContentType': "image/jpeg"})
        except Exception as e:
            print(e)
    else:
        print("Not exists")

    # Create SQL command
    query = """
        INSERT INTO lsdb.data_collect_SP2 
        (
            id, color, symbol, stain_type, stain_area, shrink_list, status_list,
            accessories_total, special_clothes, extra, original_answer, real_answer,
            created_time, image1, image2, image3
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    print(image1_fullname, type(image1_fullname))
    # Execute SQL command
    # https://lsolution-data-storage.s3.ap-northeast-2.amazonaws.com/data_collect_SP/12-2.jpg
    cursor.execute(query, (
        input_number, str(color), str(symbol), str(stain_type), str(stain_area),
        str(shrink_list), str(status_list), str(accessories_total),
        str(special_clothes), extra, str(result_save), real_answer, current_time,
        image1_fullname, image2_fullname, image3_fullname
    ))

    # Commit changes
    cnx.commit()

    # Close cursor
    cursor.close()

    # The actual function will save the data to the AWS database
    messagebox.showinfo("Info", "저장되었습니다! id: " + input_number)
    reset_radiobuttons()
    stain = stain_type
    stain_area = stain_area
    caution = shrink_list + status_list
    accessories = accessories_total
    special = special_clothes
    print(image_list, "$%$%$%$%$")
    print(material_list)
    print(symbol)
    print(stain)
    print(stain_area)
    print(caution)
    print(accessories)
    print(special)
    print(color)
    image_list = []


reset_radiobuttons()

save_button = tk.Button(root, text="Save Data", command=save_data, width=20, height=2)
save_button.grid(row=55, column=0)

root.mainloop()
cnx.close()
