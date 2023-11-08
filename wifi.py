import tkinter as tk
from tkinter import ttk

# Constants for MCS data rates
MCS_DATA_RATES = {
    '802.11b': {
        "20MHz": {
            "800": [1, 2, 5.5, 11],
         },
    },
    '802.11a/g': {
        "20MHz": {
            "800": [6, 9, 12, 18, 24, 36, 48, 54],
         },
         "SuperG": {
            "800": [12, 18, 24, 36, 48, 72, 96, 108],
         },
    },
    '802.11n': {
        "20MHz": {
            "800": [6.5, 13, 19.5, 26, 39, 52, 58.5, 65, 78],
            "400": [7.2, 14.4, 21.7, 28.9, 43.3, 57.8, 65, 72.2, 86.7],
        },
        "40MHz": {
            "800": [13, 26, 39, 52, 78, 104, 117, 130, 156],
            "400": [14.4, 28.9, 43.3, 57.8, 86.7, 115.6, 130, 144.4, 173.3],
        },
    },
    '802.11ac': {
        "20MHz": {
            "800": [6.5, 13, 19.5, 26, 39, 52, 58.5, 65, 78],
            "400": [7.2, 14.4, 21.7, 28.9, 43.3, 57.8, 65, 72.2, 86.7],
        },
        "40MHz": {
            "800": [13.5, 27, 40.5, 54, 81, 108, 121.5, 135, 162, 180],
            "400": [15, 30, 45, 60, 90, 120, 135, 150, 180, 200],
        },
        "80MHz": {
            "800": [29.3, 58.5, 87.8, 117, 175.5, 234, 263.3, 292.5, 351, 390],
            "400": [32.5, 65, 97.5, 130, 195, 260, 292.5, 325, 290, 433.3],
        },
        "160MHz": {
            "800": [58.5, 117, 175.5, 234, 351, 468, 526.5, 585, 702, 780],
            "400": [65, 130, 195, 260, 390, 520, 585, 650, 780, 866.7],
        },
    },
    '802.11ax': {
        "20MHz": {
            "1600": [8, 16, 24, 33, 49, 65, 73, 81, 98, 108, 122, 135],
            "800": [8.6, 17.2, 25.8, 34.4, 51.6, 68.8, 77.4, 86, 103.2, 114.7, 129, 143.4],
        },
        "40MHz": {
            "1600": [16, 33, 49, 65, 98, 130, 146, 163, 195, 217, 244, 271],
            "800": [17.2, 34.4, 51.6, 68.8, 103.2, 146, 163, 195, 217, 244, 271],
        },
        "80MHz": {
            "1600": [34, 68, 102, 136, 204, 272, 306, 340, 408, 453, 510, 567],
            "800": [36, 72.1, 108.1, 144.1, 216.2, 288.2, 324.4, 360.3, 432.4, 480.4, 540.4, 600.5],
        },
        "160MHz": {
            "1600": [68, 136, 204, 272, 408, 544, 613, 681, 817, 907, 1021, 1134],
            "800": [72, 144, 216, 282, 432, 576, 649, 721, 865, 961, 1081, 1201],
        },
    },
    '802.11be': {
        "20MHz": {
            "800": [9, 17, 26, 34, 52, 69, 77, 86, 103, 115, 129, 143, 155, 172],
            "1600": [8, 16, 24, 33, 49, 65, 73, 81, 98, 108, 122, 135, 146, 163],
            "3200": [7, 15, 22, 29, 44, 59, 66, 73, 88, 98, 110, 122, 131, 146],
        },
        "40MHz": {
            "800": [17, 34, 52, 69, 103, 138, 155, 172, 207, 229, 258, 287, 310, 344],
            "1600": [16, 33, 49, 65, 98, 130, 146, 163, 195, 217, 244, 271, 293, 325],
            "3200": [15, 29, 44, 59, 88, 117, 132, 146, 176, 195, 219, 244, 263, 293],
        },
        "80MHz": {
            "800": [36, 72, 108, 144, 216, 288, 324, 360, 432, 480, 540, 600, 649, 721],
            "1600": [34, 68, 102, 136, 204, 272, 306, 340, 408, 453, 510, 567, 613, 681],
            "3200": [31, 61, 92, 123, 184, 245, 276, 306, 368, 408, 459, 510, 551, 613],
        },
        "160MHz": {
            "800": [72, 144, 216, 282, 432, 576, 649, 721, 865, 961, 1081, 1201, 1297, 1441],
            "1600": [68, 136, 204, 272, 408, 544, 613, 681, 817, 907, 1021, 1134, 1225, 1361],
            "3200": [61, 122, 184, 245, 368, 490, 551, 613, 735, 817, 919, 1021, 1103, 1125],
        },
        "320MHz": {
            "800": [144, 288, 432, 577, 865, 1153, 1297, 1441, 1729, 1922, 2162, 2402, 2594, 2882],
            "1600": [136, 272, 408, 544, 817, 1089, 1225, 1361, 1633, 1815, 2042, 2269, 2450, 2772],
            "3200": [123, 245, 368, 490, 735, 980, 1103, 1225, 1470, 1633, 1838, 2042, 2205, 2450],
            
        },
    },
        '802.11ad': {
        "2.16GHz": {
            "SC-PHY": [27.5, 385, 770, 962.5, 1155, 1251.25, 1540, 1925, 2310, 2502.5, 3080, 3850, 4620],
            "OFDM-PHY": [27.5, 693, 866.25, 1386, 1732.5, 2079, 2772, 3465, 4158, 4504.5, 5197.5, 6237, 6756.75],
            "LPSC-PHY": [27.5, 626, 834, 1112, 1251, 1668, 2224, 2503],
        },
    }
}

# Function to calculate data rate
def calculate_data_rate():
    # Get user input values
    standard = standard_combo.get()
    bandwidth = bandwidth_combo.get()
    mcs_index = int(mcs_combo.get())
    guard_interval = guard_interval_combo.get()
    spatial_streams = int(spatial_streams_entry.get())

    # Check if entered values are valid keys in MCS_DATA_RATES dictionary
    if standard in MCS_DATA_RATES and bandwidth in MCS_DATA_RATES[standard] and guard_interval in MCS_DATA_RATES[standard][bandwidth]:
        data_rate = MCS_DATA_RATES[standard][bandwidth][guard_interval][mcs_index] * spatial_streams
        result_label["text"] = f"{data_rate} Mbps"
    else:
        result_label["text"] = "Invalid input values"

# Create the main window
root = tk.Tk()
root.title("Wi-Fi Data Rate Calculator")

# Wi-Fi Standard selection
standard_label = tk.Label(root, text="Wi-Fi Standard:")
standard_label.grid(row=0, column=0)
standard_combo = ttk.Combobox(root, values=["802.11b", "802.11a/g", "802.11n", "802.11ac", "802.11ax", "802.11ad", "802.11be"])
standard_combo.grid(row=0, column=1)
standard_combo.set("802.11b")

# MCS selection
mcs_label = tk.Label(root, text="MCS:")
mcs_label.grid(row=1, column=0)
mcs_combo = ttk.Combobox(root, values=[str(i) for i in range(14)])
mcs_combo.grid(row=1, column=1)
mcs_combo.set("0")

# Bandwidth selection
bandwidth_label = tk.Label(root, text="Bandwidth:")
bandwidth_label.grid(row=2, column=0)
bandwidth_combo = ttk.Combobox(root, values=["20MHz", "SuperG", "40MHz", "80MHz", "160MHz", "320MHz", "1.08GHz", "2.16GHz", "4.32GHz", "6.48GHz", "8.64GHz"])
bandwidth_combo.grid(row=2, column=1)
bandwidth_combo.set("20MHz")

# Guard Interval selection
guard_interval_label = tk.Label(root, text="GI (Sub-6) (ns) / MOD (mmWave):")
guard_interval_label.grid(row=3, column=0)
guard_interval_combo = ttk.Combobox(root, values=["400", "800", "1600", "3200", "SC-PHY", "OFDM-PHY", "LPSC-PHY"])
guard_interval_combo.grid(row=3, column=1)
guard_interval_combo.set("800")

# Spatial Streams entry
spatial_streams_label = tk.Label(root, text="MIMO/MU-MIMO:")
spatial_streams_label.grid(row=4, column=0)
spatial_streams_entry = ttk.Combobox(root, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",])
spatial_streams_entry.grid(row=4, column=1)
spatial_streams_entry.set("1")

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_data_rate)
calculate_button.grid(row=5, column=0, columnspan=2)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=2)

root.mainloop()
