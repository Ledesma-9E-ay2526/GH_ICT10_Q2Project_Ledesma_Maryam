# Student Showcase
from pyscript import display, document


# SEATWORK I: CANDIDATE VERIFICATION SYSTEM
def view_user(e):

    document.getElementById("result").innerHTML = " "

    member_input1 = str(document.getElementById("first_name").value)

    member_input2 = str(document.getElementById("last_name").value)

    full_name_input = f"{member_input1} {member_input2}"

    varsity_members = [
        "Maryam Ledesma",
        "Alyssa Valdez",
        "Josua Ibanez",
        "Cathrice Rodriguez"
    ]

    member_checker = full_name_input in varsity_members

    display_message = (
        f"Sorry, you were not accepted into varsity.",
        f"Congratulations {member_input1} {member_input2}, you were accepted into varsity!"
    )

    display(display_message[member_checker], target="result")



# SKILLS TEST: NON-METAL ELEMENTS
# Dictionary: key is the symbol, value is a tuple
# containing the name, atomic number, and atomic mass.

non_metal_elements = {

    "Cl": ("Chlorine", 17, 35.45),

    "P": ("Phosphorus", 15, 30.974),

    "Ne": ("Neon", 10, 20.180),

    "He": ("Helium", 2, 4.0026),

    "C": ("Carbon", 6, 12.011),

    "N": ("Nitrogen", 7, 14.007),

    "O": ("Oxygen", 8, 15.999),

    "F": ("Fluorine", 9, 18.998),

    "H": ("Hydrogen", 1, 1.008),

    "S": ("Sulfur", 16, 32.06),

    "Ar": ("Argon", 18, 39.948),

    "Se": ("Selenium", 34, 78.971),

    "Br": ("Bromine", 35, 79.904),

    "Kr": ("Krypton", 36, 83.798),

    "I": ("Iodine", 53, 126.904),

    "Rn": ("Radon", 86, 222),

    "Xe": ("Xenon", 54, 131.293)

}


# Tuple used when the symbol is not in the dictionary

not_found = (
    "Does not exist in the non-metals list",
    "N/A",
    "N/A"
)


def search_element(e):

    # Getting the value from the input field

    symbol = document.getElementById("symbol").value

    symbol = symbol.strip().capitalize()

    # Clearing the old result

    document.getElementById("element_result").innerHTML = ""

    # Getting the tuple or not_found if the symbol is not in the dictionary

    info = non_metal_elements.get(symbol, not_found)

    # Unpacking the tuple

    name, number, mass = info

    # Displaying the results

    display("Element Symbol: " + symbol, target="element_result")

    display("Element Name: " + name, target="element_result")

    display("Atomic Number: " + str(number), target="element_result")

    display("Atomic Mass: " + str(mass), target="element_result")



# DRILL #2: SCHOOL CLUB MEMBERS

grade7 = {

    "Ariana Grande",

    "Jessie James",

    "Nicki Minaj"

}


grade8 = {

    "Nina Doberman",

    "Jack Black",

    "Gordon Ramsay"

}


grade9 = {

    "Simone Williams",

    "John Cena",

    "Justin Bieber"

}


grade10 = {

    "Joe Jonas",

    "Nick Jonas",

    "Reiko Turner"

}


# COMBINE ALL GRADE SETS

all_members = grade7 | grade8 | grade9 | grade10


# FUNCTION TO ADD A NEW CLUB MEMBER

def add_member(e):

    # GET THE INPUT VALUES

    first_name = document.getElementById("club_first_name").value.strip()

    last_name = document.getElementById("club_last_name").value.strip()

    # COMBINE FIRST NAME AND LAST NAME

    new_member = f"{first_name} {last_name}".strip()

    # CREATE A SET FOR THE NEW MEMBER

    new_member_set = {new_member}

    # USE UNION TO ADD THE NEW MEMBER

    updated_members = all_members | new_member_set

    # SORT THE MEMBERS

    member_list = "<br>".join(sorted(updated_members))

    # GET THE TOTAL NUMBER OF MEMBERS

    total_members = len(updated_members)

    # DISPLAY THE RESULTS USING AN F-STRING

    result = f"""
    <h5>All Members:</h5>
    {member_list}
    <hr>
    <b>Total Members: {total_members}</b>
    """

    display(result, target="member_output")
