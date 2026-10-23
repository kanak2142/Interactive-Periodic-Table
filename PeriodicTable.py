import tkinter as tk
from tkinter import ttk

# ---------------- CATEGORY COLORS ----------------

category_colors = {
"alkali metal":"#ff6b6b",
"alkaline earth metal":"#ffa94d",
"transition metal":"#4dabf7",
"post-transition metal":"#74c0fc",
"metalloid":"#ffd43b",
"nonmetal":"#69db7c",
"halogen":"#b197fc",
"noble gas":"#91a7ff",
"lanthanide":"#f783ac",
"actinide":"#ff922b",
"unknown":"#ced4da"
}

# ---------------- ELEMENT DATA ----------------

elements = [
(1,"H","Hydrogen",1,1,"nonmetal",1.008),
(2,"He","Helium",18,1,"noble gas",4.0026),
(3,"Li","Lithium",1,2,"alkali metal",6.94),
(4,"Be","Beryllium",2,2,"alkaline earth metal",9.012),
(5,"B","Boron",13,2,"metalloid",10.81),
(6,"C","Carbon",14,2,"nonmetal",12.01),
(7,"N","Nitrogen",15,2,"nonmetal",14.01),
(8,"O","Oxygen",16,2,"nonmetal",16.00),
(9,"F","Fluorine",17,2,"halogen",19.00),
(10,"Ne","Neon",18,2,"noble gas",20.18),

(11,"Na","Sodium",1,3,"alkali metal",22.99),
(12,"Mg","Magnesium",2,3,"alkaline earth metal",24.30),
(13,"Al","Aluminium",13,3,"post-transition metal",26.98),
(14,"Si","Silicon",14,3,"metalloid",28.08),
(15,"P","Phosphorus",15,3,"nonmetal",30.97),
(16,"S","Sulfur",16,3,"nonmetal",32.06),
(17,"Cl","Chlorine",17,3,"halogen",35.45),
(18,"Ar","Argon",18,3,"noble gas",39.95),

(19,"K","Potassium",1,4,"alkali metal",39.10),
(20,"Ca","Calcium",2,4,"alkaline earth metal",40.08),
(21,"Sc","Scandium",3,4,"transition metal",44.96),
(22,"Ti","Titanium",4,4,"transition metal",47.87),
(23,"V","Vanadium",5,4,"transition metal",50.94),
(24,"Cr","Chromium",6,4,"transition metal",51.99),
(25,"Mn","Manganese",7,4,"transition metal",54.94),
(26,"Fe","Iron",8,4,"transition metal",55.85),
(27,"Co","Cobalt",9,4,"transition metal",58.93),
(28,"Ni","Nickel",10,4,"transition metal",58.69),
(29,"Cu","Copper",11,4,"transition metal",63.55),
(30,"Zn","Zinc",12,4,"transition metal",65.38),
(31,"Ga","Gallium",13,4,"post-transition metal",69.72),
(32,"Ge","Germanium",14,4,"metalloid",72.63),
(33,"As","Arsenic",15,4,"metalloid",74.92),
(34,"Se","Selenium",16,4,"nonmetal",78.97),
(35,"Br","Bromine",17,4,"halogen",79.90),
(36,"Kr","Krypton",18,4,"noble gas",83.80),

(37,"Rb","Rubidium",1,5,"alkali metal",85.47),
(38,"Sr","Strontium",2,5,"alkaline earth metal",87.62),
(39,"Y","Yttrium",3,5,"transition metal",88.91),
(40,"Zr","Zirconium",4,5,"transition metal",91.22),
(41,"Nb","Niobium",5,5,"transition metal",92.91),
(42,"Mo","Molybdenum",6,5,"transition metal",95.95),
(43,"Tc","Technetium",7,5,"transition metal",98),
(44,"Ru","Ruthenium",8,5,"transition metal",101.07),
(45,"Rh","Rhodium",9,5,"transition metal",102.91),
(46,"Pd","Palladium",10,5,"transition metal",106.42),
(47,"Ag","Silver",11,5,"transition metal",107.87),
(48,"Cd","Cadmium",12,5,"transition metal",112.41),
(49,"In","Indium",13,5,"post-transition metal",114.82),
(50,"Sn","Tin",14,5,"post-transition metal",118.71),
(51,"Sb","Antimony",15,5,"metalloid",121.76),
(52,"Te","Tellurium",16,5,"metalloid",127.60),
(53,"I","Iodine",17,5,"halogen",126.90),
(54,"Xe","Xenon",18,5,"noble gas",131.29),

(55,"Cs","Cesium",1,6,"alkali metal",132.91),
(56,"Ba","Barium",2,6,"alkaline earth metal",137.33),
(57,"La","Lanthanum",3,6,"lanthanide",138.91),
(58,"Ce","Cerium",4,9,"lanthanide",140.12),
(59,"Pr","Praseodymium",5,9,"lanthanide",140.91),
(60,"Nd","Neodymium",6,9,"lanthanide",144.24),
(61,"Pm","Promethium",7,9,"lanthanide",145),
(62,"Sm","Samarium",8,9,"lanthanide",150.36),
(63,"Eu","Europium",9,9,"lanthanide",151.96),
(64,"Gd","Gadolinium",10,9,"lanthanide",157.25),
(65,"Tb","Terbium",11,9,"lanthanide",158.93),
(66,"Dy","Dysprosium",12,9,"lanthanide",162.50),
(67,"Ho","Holmium",13,9,"lanthanide",164.93),
(68,"Er","Erbium",14,9,"lanthanide",167.26),
(69,"Tm","Thulium",15,9,"lanthanide",168.93),
(70,"Yb","Ytterbium",16,9,"lanthanide",173.05),
(71,"Lu","Lutetium",17,9,"lanthanide",174.97),

(72,"Hf","Hafnium",4,6,"transition metal",178.49),
(73,"Ta","Tantalum",5,6,"transition metal",180.95),
(74,"W","Tungsten",6,6,"transition metal",183.84),
(75,"Re","Rhenium",7,6,"transition metal",186.21),
(76,"Os","Osmium",8,6,"transition metal",190.23),
(77,"Ir","Iridium",9,6,"transition metal",192.22),
(78,"Pt","Platinum",10,6,"transition metal",195.08),
(79,"Au","Gold",11,6,"transition metal",196.97),
(80,"Hg","Mercury",12,6,"transition metal",200.59),
(81,"Tl","Thallium",13,6,"post-transition metal",204.38),
(82,"Pb","Lead",14,6,"post-transition metal",207.2),
(83,"Bi","Bismuth",15,6,"post-transition metal",208.98),
(84,"Po","Polonium",16,6,"post-transition metal",209),
(85,"At","Astatine",17,6,"halogen",210),
(86,"Rn","Radon",18,6,"noble gas",222),

(87,"Fr","Francium",1,7,"alkali metal",223),
(88,"Ra","Radium",2,7,"alkaline earth metal",226),
(89,"Ac","Actinium",3,7,"actinide",227),
(90,"Th","Thorium",4,10,"actinide",232.04),
(91,"Pa","Protactinium",5,10,"actinide",231.04),
(92,"U","Uranium",6,10,"actinide",238.03),
(93,"Np","Neptunium",7,10,"actinide",237),
(94,"Pu","Plutonium",8,10,"actinide",244),
(95,"Am","Americium",9,10,"actinide",243),
(96,"Cm","Curium",10,10,"actinide",247),
(97,"Bk","Berkelium",11,10,"actinide",247),
(98,"Cf","Californium",12,10,"actinide",251),
(99,"Es","Einsteinium",13,10,"actinide",252),
(100,"Fm","Fermium",14,10,"actinide",257),
(101,"Md","Mendelevium",15,10,"actinide",258),
(102,"No","Nobelium",16,10,"actinide",259),
(103,"Lr","Lawrencium",17,10,"actinide",266),

(104,"Rf","Rutherfordium",4,7,"transition metal",267),
(105,"Db","Dubnium",5,7,"transition metal",268),
(106,"Sg","Seaborgium",6,7,"transition metal",269),
(107,"Bh","Bohrium",7,7,"transition metal",270),
(108,"Hs","Hassium",8,7,"transition metal",269),
(109,"Mt","Meitnerium",9,7,"unknown",278),
(110,"Ds","Darmstadtium",10,7,"unknown",281),
(111,"Rg","Roentgenium",11,7,"unknown",282),
(112,"Cn","Copernicium",12,7,"transition metal",285),
(113,"Nh","Nihonium",13,7,"unknown",286),
(114,"Fl","Flerovium",14,7,"post-transition metal",289),
(115,"Mc","Moscovium",15,7,"unknown",290),
(116,"Lv","Livermorium",16,7,"post-transition metal",293),
(117,"Ts","Tennessine",17,7,"halogen",294),
(118,"Og","Oganesson",18,7,"noble gas",294)
]



# ---------------- POPUP CARD ----------------

def show_element(e):

    popup = tk.Toplevel(root)
    popup.title(e[2])
    popup.geometry("300x250")
    popup.configure(bg="#1e1e2f")

    tk.Label(popup,text=e[1],
             font=("Arial",40,"bold"),
             fg="white",
             bg="#1e1e2f").pack(pady=10)

    info=f"""
Atomic Number : {e[0]}
Name          : {e[2]}
Symbol        : {e[1]}
Group         : {e[3]}
Period        : {e[4]}
Category      : {e[5]}
Atomic Mass   : {e[6]}
"""

    tk.Label(popup,text=info,
             font=("Consolas",12),
             bg="#1e1e2f",
             fg="white",
             justify="left").pack()

# ---------------- GRID ----------------

buttons=[]

def create_table():

    for e in elements:

        color = category_colors.get(e[5],"#ced4da")

        btn = tk.Button(table_frame,
                        text=f"{e[1]}\n{e[0]}",
                        bg=color,
                        width=5,
                        height=2,
                        command=lambda el=e:show_element(el))

        btn.grid(row=e[4],column=e[3],padx=2,pady=2)

        btn.bind("<Enter>",lambda event,b=btn:b.config(relief="raised",bd=4))
        btn.bind("<Leave>",lambda event,b=btn:b.config(relief="flat",bd=1))

        buttons.append((btn,e))

# ---------------- LIVE SEARCH ----------------

def search(event):

    q=search_var.get().lower()

    for btn,e in buttons:

        if q in e[2].lower() or q in e[1].lower():
            btn.config(relief="solid",bd=4)
        else:
            btn.config(relief="flat",bd=1)

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("ChemQuest – Interactive Periodic Table")
root.geometry("1400x800")
root.configure(bg="#1e1e2f")

title=tk.Label(root,
text="ChemQuest 🔬 Interactive Periodic Table",
font=("Arial",26,"bold"),
bg="#1e1e2f",
fg="white")

title.pack(pady=10)

# ---------------- ELEMENT POPUP SEARCH BOX ----------------

search_panel = tk.Frame(root, bg="#2a2a3d", padx=15, pady=10)
search_panel.pack(pady=10)

tk.Label(
    search_panel,
    text="🔍 Element Info Finder",
    font=("Arial",12,"bold"),
    fg="white",
    bg="#2a2a3d"
).grid(row=0,column=0,columnspan=2,pady=(0,5))

element_input = tk.Entry(
    search_panel,
    font=("Arial",12),
    width=25
)

element_input.grid(row=1,column=0,padx=5)

def open_element_from_input(event=None):

    query = element_input.get().lower().strip()

    for e in elements:
        if query == e[2].lower() or query == e[1].lower():
            show_element(e)
            return

    error = tk.Toplevel(root)
    error.title("Not Found")
    error.geometry("250x120")
    error.configure(bg="#1e1e2f")

    tk.Label(
        error,
        text="Element not found!",
        font=("Arial",12,"bold"),
        fg="white",
        bg="#1e1e2f"
    ).pack(pady=20)

    tk.Button(
        error,
        text="OK",
        command=error.destroy,
        bg="#ff6b6b",
        fg="white"
    ).pack()

search_button = tk.Button(
    search_panel,
    text="Open Info",
    command=open_element_from_input,
    bg="#00adb5",
    fg="white",
    font=("Arial",10,"bold"),
    padx=10
)

search_button.grid(row=1,column=1,padx=5)

# Press ENTER to search
element_input.bind("<Return>", open_element_from_input)

# TABLE

table_frame=tk.Frame(root,bg="#1e1e2f")
table_frame.pack(pady=20)

create_table()

root.mainloop()
