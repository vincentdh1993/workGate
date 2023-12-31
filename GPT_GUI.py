import io
import requests
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2
from PIL import Image, ImageTk
import getResult
from getResult import *


material_list = []
symbol=[]
stain = []
stain_area = []
caution=[]
accessories = []
special = []
result = []
result_save = []
first = []
second = []

barcode = ""
image_url = ""
texture = ""
material_list_string=""
material_list_str=""
cap = cv2.VideoCapture(0)
# Connect to the database
cnx = mysql.connector.connect(
    host="database-1.cfigciaxwk2v.us-west-1.rds.amazonaws.com",
    user="admin",
    password="LS202215f!",
    database="lsdb"
)


def reset_radiobuttons():
    color_var.set('')
    laundry_var.set('')
    stain_var.set('')
    stain_area_var.set('')

def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(io.BytesIO(response.content))


def update_material_list_label(a):
    global material_list
    global material_list_str
    # Check if the material_list is empty
    if a==-1:
        material_list_str = "DB 존재하지않음"
    else:
        # Convert the material_list to a string
        material_list_str = ', '.join(material_list)

    # Update the label
    # material_list_label.config(text="Material List: " + material_list_str)
    material_list_label.config(text="Material List: " + material_list_str, font=("Helvetica", 12, "bold"), fg='green')


root = tk.Tk()
root.geometry('1200x1000')

# Barcode input
barcode_label = tk.Label(root, text="Barcode:")
barcode_label.grid(row=0, column=0)
barcode_entry = tk.Entry(root)
barcode_entry.grid(row=0, column=1)

# Bind <Return> event to the barcode entry
def on_barcode_entry_return(event):
    load_image_button.invoke()

barcode_entry.bind('<Return>', on_barcode_entry_return)

def load_image():
    global barcode
    global url
    global material_list
    global material_list_string
    material_list_string = tk.StringVar()

    cursor = cnx.cursor()
    barcode = barcode_entry.get()
    print(barcode,"@@@")
    # Create a cursor

    # Execute a query
    query = "SELECT * FROM lsdb.rf WHERE id = '"+barcode+"';"
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()
    url = results[0][7]
    print(url)
    cursor.close()


    url2=[]
    cursor = cnx.cursor()
    query2 = "SELECT * FROM lsdb.carelabel WHERE id = '"+barcode+"';"
    cursor.execute(query2)
    results2 = cursor.fetchall()
    print(results2,"$$$$$$$$$$$")
    if len(results2) == 0:
        update_material_list_label(-1)
        update_material_checkbuttons(-1)
        pass
    else:
        url2 = results2[0][6]
        texture = results2[0][4]
        # Close the cursor and connection
        cursor.close()
        print(url2)
        texture_list = texture.split("\n")
        texture_list = [line.split("/")[0].strip() for line in texture_list]
        texture_list = list(set(texture_list))
        material_list = [element for element in texture_list if len(element) > 0]
        update_material_checkbuttons(0)
        # 울,견,레이온,마,아크릴,폴리에스터,나일론,폴리우레탄,면
        print(material_list)

        # Call the function to update the material list label
        update_material_list_label(0)

    if url:
        image = load_image_from_url(url)
        # Resize the image to fit into a 300x300 area while keeping its aspect ratio
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # keep a reference to prevent garbage collection
    else:
        tk.messagebox.showinfo("Error", "Please input a URL.")

    if len(url2)!=0:
        image2 = load_image_from_url(url2)
        # Resize the image to fit into a 300x300 area while keeping its aspect ratio
        image2.thumbnail((300, 300))
        photo2 = ImageTk.PhotoImage(image2)
        image_label2.config(image=photo2)
        image_label2.image = photo2  # keep a reference to prevent garbage collection
    else:
        image2 = Image.new('RGB', (100, 100), 'white')
        photo2 = ImageTk.PhotoImage(image2)
        image_label2.config(image=photo2)
        image_label2.image = photo2  # keep a reference to prevent garbage collection


    # Clear the barcode entry
    barcode_entry.delete(0, tk.END)


# Load image button
load_image_button = tk.Button(root, text="Load Image", command=load_image)
load_image_button.grid(row=0, column=2)

# Image display
image_label = tk.Label(root)
image_label.grid(row=1, column=0, columnspan=3)

image_label2 = tk.Label(root)
image_label2.grid(row=1, column=2, columnspan=3)

# Material list display
material_list_label = tk.Label(root)
material_list_label.grid(row=1, column=30, columnspan=3)



# Material selection
material_label = tk.Label(root, text="소재정보:", font=('Helvetica', 12, 'bold'), fg='red')
material_label.grid(row=2, column=30, sticky="W")
material_vars = {}
material_options = ["울", "견", "레이온", "마", "아크릴", "폴리에스터", "나일론", "폴리우레탄", "면"]
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
laundry_options = ["물세탁", "드라이"]
for idx, symbol in enumerate(laundry_options, start=3):
    rb = tk.Radiobutton(root, text=symbol, variable=laundry_var, value=symbol)
    rb.grid(row=idx, column=1, sticky="W")

# Stain info
stain_label = tk.Label(root, text="얼룩정보:", font=('Helvetica', 12, 'bold'), fg='red')
stain_label.grid(row=2, column=2, sticky="W")
stain_var = tk.StringVar()
stain_options = ["수용성", "지용성", "없음"]
for idx, stain in enumerate(stain_options, start=3):
    rb = tk.Radiobutton(root, text=stain, variable=stain_var, value=stain)
    rb.grid(row=idx, column=2, sticky="W")

# Stain area info
stain_area_label = tk.Label(root, text="얼룩범위:", font=('Helvetica', 12, 'bold'), fg='blue')
stain_area_label.grid(row=10, column=0, sticky="W")
stain_area_var = tk.StringVar()
stain_area_options = ["국부", "광범위", "없음"]
for idx, area in enumerate(stain_area_options, start=11):
    rb = tk.Radiobutton(root, text=area, variable=stain_area_var, value=area)
    rb.grid(row=idx, column=0, sticky="W")


# Cautions info
cautions_label = tk.Label(root, text="이염/탈색:", font=('Helvetica', 12, 'bold'), fg='blue')
cautions_label.grid(row=10, column=1, sticky="W")
cautions_vars = {}
cautions_options = ["원색계열", "흰색+a", "인디고염료","다색조합","탈색"]
for idx, caution in enumerate(cautions_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=caution, variable=var)
    cb.grid(row=idx, column=1, sticky="W")
    cautions_vars[caution] = var
    # cautions_vars.append(var)

# Cautions-2 info
cautions2_label = tk.Label(root, text="손상/수축", font=('Helvetica', 12, 'bold'), fg='blue')
cautions2_label.grid(row=10, column=2, sticky="W")
cautions2_vars = {}
cautions2_options = ["시스루", "레이스", "시어서커", "플리츠", "트위드", "스티치", "올풀림 디자인", "코듀로이(골덴)", "벨벳", "기모", "찌든때"]
for idx, caution in enumerate(cautions2_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=caution, variable=var)
    cb.grid(row=idx, column=2, sticky="W")
    cautions2_vars[caution]= var
    # cautions2_vars.append(var)

# Accessories info
accessories_label = tk.Label(root, text="악세서리:", font=('Helvetica', 12, 'bold'), fg='blue')
accessories_label.grid(row=10, column=3, sticky="W")
accessories_vars = {}
accessories_options = ["접착물", "부착물", "없음"]
for idx, accessory in enumerate(accessories_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=accessory, variable=var)
    cb.grid(row=idx, column=3, sticky="W")
    accessories_vars[accessory] = var
    # accessories_vars.append(var)

# Cautions-2 info
cautions3_label = tk.Label(root, text="악세서리-세부", font=('Helvetica', 12, 'bold'), fg='blue')
cautions3_label.grid(row=10, column=30, sticky="W")
cautions3_vars = {}  # changed from list to dictionary
cautions3_options = ["큐빅", "프린트", "페인트비즈", "인조가죽패치", "메탈류", "지퍼/심", "큐빅단추"]
for idx, caution in enumerate(cautions3_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=caution, variable=var)
    cb.grid(row=idx, column=30, sticky="W")
    cautions3_vars[caution] = var  # store the variable associated with the text
# accessories_detail = [k for k, v in cautions2_vars.items() if v.get()]

# Special info
special_label = tk.Label(root, text="특수기능", font=('Helvetica', 12, 'bold'), fg='blue')
special_label.grid(row=10, column=40, sticky="W")
special_vars = []
special_vars = {}
special_options = ["충전재", "발수코팅", "아웃도어"]
for idx, special in enumerate(special_options, start=11):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=special, variable=var)
    cb.grid(row=idx, column=40, sticky="W")
    special_vars[special] = var
    # special_vars.append(var)
# special_detail = [k for k, v in special_vars.items() if v.get()]

# Extra information
extra_label = tk.Label(root, text="Additional Information:")
extra_label.grid(row=34, column=0, sticky="W")
extra_entry = tk.Entry(root, width=50)
extra_entry.grid(row=34, column=1, sticky="W")

def get_result():
    global result,first,second
    global stain_area
    global result_save
    first = []
    second = []
    result = []
    material_list = [k for k, v in material_vars.items() if v.get()]
    accessories_detail2 = [k for k, v in cautions3_vars.items() if v.get()]
    special_detail = [k for k, v in special_vars.items() if v.get()]
    accessories_detail1 = [k for k, v in accessories_vars.items() if v.get()]
    caution_detail2 = [k for k, v in cautions2_vars.items() if v.get()]
    caution_detail1 = [k for k, v in cautions_vars.items() if v.get()]
    stain_area = [stain_area_var.get()]
    stain_type = [stain_var.get()]
    color = [color_var.get()]
    symbol = [laundry_var.get()]
    extra = extra_entry.get()
    accessories_total = accessories_detail1 + accessories_detail2

    stain = stain_type
    stain_area = stain_area
    caution = caution_detail1 + caution_detail2
    accessories = accessories_total
    special = special_detail
    print("@@@@@@@@@@@@")
    print(material_list)
    print(symbol)
    print(stain)
    print(stain_area)
    print(caution)
    print(accessories)
    print(special)
    print(color)
    first = getResult.getFirst(result,material_list, symbol, stain, stain_area,caution,accessories,special,color)
    second = getResult.getSecond(first,material_list, symbol, stain, stain_area,caution,accessories,special,color)
    result = getResult.getColor(second,color)
    print("=========")
    print(first)
    print(second)
    print(result)
    # Update the result label
    result_label.config(text="Result: " + str(result))
    result_save = result
    first = []
    second = []
    result = []

# Save button
# def save_data():
#     # The actual function will save the data to the AWS database
#     messagebox.showinfo("Info", "Data Saved")

def save_data():
    global stain_area
    global result_save
    accessories_detail2 = [k for k, v in cautions3_vars.items() if v.get()]
    special_detail = [k for k, v in special_vars.items() if v.get()]
    accessories_detail1 = [k for k, v in accessories_vars.items() if v.get()]
    caution_detail2 = [k for k, v in cautions2_vars.items() if v.get()]
    caution_detail1 = [k for k, v in cautions_vars.items() if v.get()]
    stain_area = [stain_area_var.get()]
    stain_type = [stain_var.get()]
    color = [color_var.get()]
    symbol = [laundry_var.get()]
    extra = extra_entry.get()
    real_answer = real_answer_entry.get()
    accessories_total = accessories_detail1 + accessories_detail2
    print(result_save,"@@@@@@@@@@@@@@$$$$$")
    # Create a cursor
    cursor = cnx.cursor()

    # Create SQL command
    query = """INSERT INTO lsdb.data_collect_CW (id, color, symbol, stain_type, stain_area, caution_detail1, caution_detail2, accessories_total, special_detail, extra, original_answer, real_answer)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                   ON DUPLICATE KEY UPDATE color=%s, symbol=%s, stain_type=%s, stain_area=%s, caution_detail1=%s, caution_detail2=%s, accessories_total=%s, special_detail=%s, extra=%s, original_answer=%s, real_answer=%s"""

    # Execute SQL command
    cursor.execute(query, (
        barcode, str(color), str(symbol), str(stain_type), str(stain_area), str(caution_detail1), str(caution_detail2),
        str(accessories_total), str(special_detail), extra, str(result_save), real_answer, str(color), str(symbol),
        str(stain_type),
        str(stain_area),
        str(caution_detail1), str(caution_detail2), str(accessories_total), str(special_detail), extra,
        str(result_save), real_answer))

    # Commit changes
    cnx.commit()

    # Close cursor
    cursor.close()

    print(barcode)
    # The actual function will save the data to the AWS database
    messagebox.showinfo("Info", "Data Saved "+barcode)
    reset_radiobuttons()
    stain = stain_type
    stain_area = stain_area
    caution = caution_detail1+caution_detail2
    accessories = accessories_total
    special = special_detail
    print("@@@@@@@@@@@@")
    print(result_save, "@@@@@@@@@@@@@@$$$$$")
    print(material_list)
    print(symbol)
    print(stain)
    print(stain_area)
    print(caution)
    print(accessories)
    print(special)
    print(color)
reset_radiobuttons()


get_result_button = tk.Button(root, text="Get Result", command=get_result, width=20, height = 2)
get_result_button.grid(row=50, column=0, sticky="W")  # adjust the grid arguments as needed
# Result display
result_label = tk.Label(root)
result_label.grid(row=46, column=0, columnspan=3)

# Extra information
real_answer_label = tk.Label(root, text="장인세탁법 (수정 필요시):")
real_answer_label.grid(row=47, column=0, sticky="W")
real_answer_entry = tk.Entry(root, width=50)
real_answer_entry.grid(row=47, column=1, sticky="W")

# Create a 5-row gap between the buttons
for i in range(51, 55):
    root.grid_rowconfigure(i, minsize=20)  # adjust the minsize value as needed


# save_button = tk.Button(root, text="Save Data", command=save_data)
save_button = tk.Button(root, text="Save Data", command=save_data, width=20, height=2)
save_button.grid(row=55, column=0)

root.mainloop()
cnx.close()