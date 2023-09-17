import re
from fpdf import FPDF
from datetime import date


def main():
    values = user_input()
    todayDate = date.today()
    Training = Program_table_create(values[5][0], values[4][0], values[6][0])
    #Training = Program_table_create(100, 200, 300)
    #print(values)
    #print(FFM)
    pdf = PDF()
    pdf.add_page()
    maxweight_ffmi = max_potent(values[0], values[7], values[1], values[3])
    Infos = [
        ("Date", f"{todayDate}", "MaxWeight", f"{maxweight_ffmi[1]}-{maxweight_ffmi[2]} kg (current bodyfat)"),
        ("Weight", f"{values[0]} {values[7]}", "FFMI", f"{maxweight_ffmi[0]}"),
        ("Height", f"{values[1]} cm", "Bench", f"{values[4][0]} {values[4][1]}"),
        ("Age", f"{values[2]} yo", "Squat", f"{values[5][0]} {values[5][1]}"),
        ("Bodyfat", f"{values[3]} %", "Deadlift", f"{values[6][0]} {values[6][1]}"),
        ]
    pdf.set_font("Times", size=12)

    with pdf.table(
        width=190,
        col_widths=(40, 40, 40, 60),
        text_align=("CENTER", "LEFT", "CENTER", "LEFT"),
        line_height=2 * pdf.font_size,
        ) as table:
        for data_row in Infos:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

    pdf.set_font("Times", size=8)
    pdf.ln(5)

    with pdf.table(
        width=190,
        col_widths=(15, 30, 30, 30, 30, 30, 30),
        line_height=2 * pdf.font_size,
        ) as table:
        for data_row in Training:
            row = table.row()
            for datum in data_row:
                if datum in ["Monday - Squat","Wednesday - Bench","Friday - Deadlift"]:
                    row.cell(datum, colspan=2)
                else:
                    row.cell(datum)


    #for i in range(1, 23):
    #    pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
    pdf.output("Training.pdf")

    #link: https://pyfpdf.github.io/fpdf2/Tables.html


def user_input():
    weight = input("What's your weight? (kg / lbs) :")
    while not re.search(r"^([0-9]{1,3}) ?(kg|lbs)$", weight):
        weight = input("Wrong input, what's your weight? (precise kg or lbs) :")
    #print(weight)
    #weight = lbs_convert(weight)
    #print(weight)
    unit = re.search(r"^([0-9]{1,3}) ?(kg|lbs)$", weight).group(2)
    weight = re.search(r"^([0-9]{1,3}) ?(kg|lbs)$", weight).group(1)


    height = input("whats is your height? (in cm) :")
    while not re.search(r"^([0-9]{1,3}) ?(?:cm)?$", height):
        height = input("Wrong input, what's your height? (in cm) :")
    height = int(re.search(r"^([0-9]{1,3}) ?(?:cm)?$", height).group(1))

    age = input("whats is your age? (in years) :")
    while not re.search(r"^([0-9]{1,3})$", age):
        age = input("Wrong input, whats is your age? (in years) :")
    age = int(re.search(r"^([0-9]{1,3})$", age).group(1))

    #print("it's okay if you dont know you bodyfat, we will put the average value for your age")
    bodyfat = input("do you know your bodyfat? (if you dont know write 20%) :")
    while not re.search(r"^[0-9]{1,2} ?(%| )?$", bodyfat):
        bodyfat = input("Wrong input, whats is your bodyfat? (if you dont know write 20%) :")
    bodyfat = int(re.search(r"^([0-9]{1,2}) ?(%| )?$", bodyfat).group(1))

    bench = how_heavy("bench")
    squat = how_heavy("squat")
    deadl = how_heavy("deadl")

    #experience = input("have you ever trained for at least 6 months every week in you life (yes/no):")
    return weight, height, age, bodyfat, bench, squat, deadl, unit


def how_heavy(context: str):
    value = input(f"How heavy do you {context} for 5 reps ? (precise kg or lbs) :")
    while not re.search(r"^([0-9]{1,3}) ?(kg|lbs)$", value):
        value = input(f"Wrong input. How much do you {context} for 5 reps ? (precise kg or lbs) :")
    weight = re.search(r"^([0-9]{1,3}) ?(kg|lbs)$", value).group(1)
    unit = re.search(r"^([0-9]{1,3}) ?(kg|lbs)$", value).group(2)
    return round(int(weight)*1.15, 1), unit

def lbs_convert(value: int, unit: str):
    '''
    unit = re.search(r"^([0-9]{1,3}) ?(kg|lbs)$", input).group(2)
    value = int(re.search(r"^([0-9]{1,3}) ?(kg|lbs)$", input).group(1))
    if unit == "lbs":
        value = value * 0.453592
    '''
    if unit == "lbs":
        value = value * 0.453592
    return round(value, 1), unit


def max_potent(weight: int, unit: str, height: int, bodyfat: int) -> tuple:
    weight = lbs_convert(int(weight), unit)[0]
    Norm_FFMI = (weight*(100-bodyfat)/100)/((height/100)**2)+(6.3*(1.8-(height/100)))
    max_weight = (25*((height/100)**2)+(6.3*(1.8-(height/100))))/((100-bodyfat)/100)
    max_weight2 = (height - 100) * (1+((bodyfat+4)/100))
    return round(Norm_FFMI, 1), round(max_weight, 1), round(max_weight2, 1)

def Program_table_create(maxB,maxS,maxD):
    Table = []
    max_values = [maxB, maxS, maxD]

    for line in range(22):
        if line == 0:
            row = ["","Monday - Squat","","Wednesday - Bench","","Friday - Deadlift",""]
        elif line == 1:
            row = ["Weeks","Warm-up","Sets","Warm-up","Sets","Warm-up","Sets"]
        else:
            g = 1+((line-2)*0.01)
            row = ["","","","","","",""]
            row[0] = f"Week {line-1}"

            for i, max_value in enumerate(max_values):
                row[2*i + 1] = f"{int(max_value*0.4*g)}x5-{int(max_value*0.5*g)}x5-{int(max_value*0.6*g)}x3"

            for i, max_value in enumerate(max_values):
                if line in [2, 6, 10, 14, 18]:
                    row[2*i + 2] = f"{int(max_value*0.65*g)}x5-{int(max_value*0.75*g)}x5-{int(max_value*0.85*g)}x5+"
                elif line in [3, 7, 11, 15, 19]:
                    row[2*i + 2] = f"{int(max_value*0.70*g)}x3-{int(max_value*0.80*g)}x3-{int(max_value*0.90*g)}x3+"
                elif line in [4, 8, 12, 16, 20]:
                    row[2*i + 2] = f"{int(max_value*0.75*g)}x5-{int(max_value*0.85*g)}x3-{int(max_value*0.95*g)}x1+"
                elif line in [5, 9, 13, 17, 21]:
                    row[2*i + 1] = f"{int(max_value*0.4*g)}x5-{int(max_value*0.5*g)}x5-{int(max_value*0.6*g)}x5"
        Table.append(row)
    return Table

class PDF(FPDF):
    def header(self):
        self.image("logoG.png", 10, 0, 38)
        self.set_font("helvetica", "B", 15)
        self.cell(45)
        self.cell(100, 10, "5 Months strenght-oriented program", border=1, align="C")
        self.ln(22)

if __name__ == "__main__":
    main()

