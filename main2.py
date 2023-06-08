from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")


def minimum_cost():
    # Παράμετροι
    num_simulations = 1000
    num_periods = 10
    cost_reduction_rate = 0.02
    initial_cost = 100.0

    # Δημιουργήστε δεδομένα κόστους
    costs = np.zeros((num_periods, num_simulations))
    costs[0] = initial_cost

    for period in range(1, num_periods):
        costs[period] = costs[period - 1] * (1 - cost_reduction_rate)

    # Βρείτε το ελάχιστο κόστος σε προσομοιώσεις για κάθε περίοδο
    min_costs = np.min(costs, axis=1)

    # Οικόπεδο ελάχιστο κόστος παραγωγής με την πάροδο του χρόνου
    plt.figure(figsize=(12, 6))
    plt.plot(range(num_periods), min_costs)
    plt.xlabel('Περίοδος')
    plt.ylabel('Ελάχιστο Κόστος')
    plt.title('Ελάχιστο κόστος παραγωγής Διαχρονικά')
    plt.grid(True)
    plt.show()


def megisto_kostos():
    # Παράμετροι
    num_simulations = 1000
    num_periods = 10
    cost_growth_rate = 0.05
    initial_cost = 100.0

    # Δημιουργήστε δεδομένα κόστους
    costs = np.zeros((num_periods, num_simulations))
    costs[0] = initial_cost

    for period in range(1, num_periods):
        costs[period] = costs[period - 1] * (1 + cost_growth_rate)

    # Βρείτε το μέγιστο κόστος σε προσομοιώσεις για κάθε περίοδο
    max_costs = np.max(costs, axis=1)

    # Οικόπεδο μέγιστο κόστος παραγωγής με την πάροδο του χρόνου
    plt.figure(figsize=(12, 6))
    plt.plot(range(num_periods), max_costs)
    plt.xlabel('Περίοδος')
    plt.ylabel('Μέγιστο Κόστος')
    plt.title('Μέγιστο Κόστος Παραγωγής Διαχρονικά')
    plt.grid(True)
    plt.show()


def stoxastiko_modelo():
    # Παράμετροι
    num_simulations = 1000
    num_steps = 100
    initial_price = 100.0
    volatility = 0.2
    drift = 0.05

    # Δημιουργήστε τυχαίες κανονικές αποδόσεις
    returns = np.random.normal(drift, volatility, (num_steps, num_simulations))

    # Δημιουργήστε έναν πίνακα για την αποθήκευση προσομοιωμένων τιμών
    prices = np.zeros((num_steps, num_simulations))
    prices[0] = initial_price

    # Προσομοίωση κινήσεων τιμών
    for step in range(1, num_steps):
        prices[step] = prices[step - 1] * (1 + returns[step])

    # Σχεδιάστε τις προσομοιωμένες διαδρομές τιμών
    plt.figure(figsize=(12, 6))
    plt.plot(prices[:, :10])  # Σχεδιάστε τις πρώτες 10 προσομοιώσεις
    plt.xlabel('Χρονικά Βήματα')
    plt.ylabel('Τιμή')
    plt.title('Στοχαστικό μοντέλο τιμής')
    plt.grid(True)
    plt.show()


def sindiasmos_grammwn_gia_elaxisto_kostos():
    # Παράμετροι
    num_lines = 5
    num_combinations = 10
    costs = np.random.rand(num_combinations) * 100

    # Βρείτε συνδυασμούς με ελάχιστο κόστος
    min_cost_combinations = np.argsort(costs)[:num_lines]

    # Δημιουργία πίνακα συνδυασμών
    combinations = np.zeros((num_combinations, num_lines))
    for i, comb_idx in enumerate(min_cost_combinations):
        binary = bin(comb_idx)[2:].zfill(num_lines)
        combinations[i] = np.array(list(binary), dtype=int)

    # Συνδυασμοί οικοπέδων με ελάχιστο κόστος
    plt.figure(figsize=(12, 6))
    plt.imshow(combinations, cmap='Greys', aspect='auto')
    plt.xlabel('Γραμμή παραγωγής')
    plt.ylabel('Συνδυασμός')
    plt.title('Συνδυασμοί Γραμμών Παραγωγής για Ελάχιστο Κόστος')
    plt.xticks(range(num_lines))
    plt.yticks(range(num_lines))
    plt.grid(True, color='black')
    plt.show()


def run_sensitivity_analysis():
    num_simulations = 1000
    uniform_min = -50
    uniform_max = 50
    normal_mean = 0
    normal_std_dev = 50

    uniform_costs = np.random.uniform(uniform_min, uniform_max, num_simulations)
    normal_costs = np.random.normal(normal_mean, normal_std_dev, num_simulations)

    total_costs_uniform = 3 * uniform_costs
    total_costs_normal = 3 * normal_costs

    percentage_change_uniform = (total_costs_uniform - np.mean(total_costs_uniform)) / np.mean(
        total_costs_uniform) * 100
    percentage_change_normal = (total_costs_normal - np.mean(total_costs_normal)) / np.mean(total_costs_normal) * 100

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(percentage_change_uniform, bins=30, edgecolor='black')
    plt.xlabel('Ποσοστιαία Αλλαγή')
    plt.ylabel('Συχνότητα')
    plt.title('Ανάλυση Ευαισθησίας - Ομοιόμορφη Κατανομή')

    plt.subplot(1, 2, 2)
    plt.hist(percentage_change_normal, bins=30, edgecolor='black')
    plt.xlabel('Ποσοστιαία Αλλαγή')
    plt.ylabel('Συχνότητα')
    plt.title('Ανάλυση Ευαισθησίας - Κανονική Κατανομή')

    plt.tight_layout()
    plt.show()


def button_about():
    output_label.config(text="Factory Production Lines Simulation. \n  \n"
                             "Created for Hellenic Open University  \n as a project \n"
                             " from \n Antoniou Konstantinos   \n"
                             "Giannopoulos Xaralampos\n"
                             " Vardalachakis Dimitrios.  \n"
                             "version 1.0 \n")
    #update_plot(right_frame)


def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


root = Tk()
root.geometry("1000x1000")
root.title("Production Lines")

# Create left frame for buttons
left_frame = Frame(root, width=500, height=1000, bg="lightgray")
left_frame.pack(side=LEFT, fill=Y)

# Create buttons in left frame
button_one = Button(left_frame, text="Μέγιστο Κόστος", command=megisto_kostos, width=30)
button_one.pack(pady=10)
button_two = Button(left_frame, text="Ελάχιστο Κόστος", command=minimum_cost, width=30)
button_two.pack(pady=10, )
button_three = Button(left_frame, text="Συνδυασμοί γραμμών παραγωγής\nγια ελαχιστο κοστος",
                      command=sindiasmos_grammwn_gia_elaxisto_kostos, width=30, height=2)
button_three.pack(pady=10)
button_four = Button(left_frame, text="Στοχαστικού μοντέλο", command=stoxastiko_modelo, width=30)
button_four.pack(pady=10)
button_five = Button(left_frame, text="Γραφική παράσταση ευαισθησίας",
                     command=run_sensitivity_analysis, width=30)
button_five.pack(pady=10)
button_about = Button(left_frame, text="About", command=button_about, width=30)
button_about.pack(pady=10)

# Create exit button
exit_button = Button(left_frame, text="Exit", command=exit_program, width=20)
exit_button.pack(pady=10)

# Create right frame for output label
right_frame = Frame(root, width=500, height=1000, bg="white")
right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Add border between left and right frames
separator = Frame(root, width=10, height=1000, bg="black")
separator.pack(side=LEFT, fill=Y)

# Add output label to right frame
output_label = Label(right_frame, text="", font=("Arial", 20), bg="white", padx=50, pady=50)
output_label.pack(expand=True)

root.mainloop()
