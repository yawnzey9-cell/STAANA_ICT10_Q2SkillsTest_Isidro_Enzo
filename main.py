from pyscript import document

placeholder = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222),
}

def element_checker(e):
    document.getElementById("result").innerHTML = " "

    element1 = document.getElementById("element_name").value.strip().title()

    result = placeholder.get(
        element1, ("Element not found", "-", "-")
    )

    if element1 not in placeholder:
        document.getElementById("result").innerHTML = (
            '<p class="error">That symbol does not exist in the '
            "non-metals list.</p>"
        )
    else:
        document.getElementById("result").innerHTML = f"""
        <div class="row"><span>Symbol</span><strong>{element1}</strong></div>
        <div class="row"><span>Element</span><strong>{result[0]}</strong></div>
        <div class="row"><span>Atomic Number</span>
            <strong>{result[1]}</strong></div>
        <div class="row"><span>Atomic Mass</span>
            <strong>{result[2]}</strong></div>
        """
