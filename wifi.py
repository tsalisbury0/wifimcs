import tkinter as tk
from tkinter import ttk

# Constants for MCS data rates
MCS_DATA_RATES = {
    '802.11b': {
        "20MHz": {
            "800": [1, 2, 5.5, 11],
         },
    },
    '802.11a': {
        "20MHz": {
            "800": [6, 9, 12, 18, 24, 36, 48, 54],
         },
    },
    '802.11g': {
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
            "400": [32.5, 65, 97.5, 130, 195, 260, 292.5, 325, 390, 433.3],
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
            "800": [17.2, 34.4, 51.6, 68.8, 103.2, 137.6, 154.9, 172.1, 206.5, 229.4, 258.1, 286.8],
        },
        "80MHz": {
            "1600": [34, 68, 102, 136, 204, 272, 306, 340, 408, 453, 510, 567],
            "800": [36, 72.1, 108.1, 144.1, 216.2, 288.2, 324.4, 360.3, 432.4, 480.4, 540.4, 600.5],
        },
        "160MHz": {
            "1600": [68, 136, 204, 272, 408, 544, 613, 681, 817, 907, 1021, 1134],
            "800": [72, 144, 216, 288, 432, 576, 649, 721, 865, 961, 1081, 1201],
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
            "800": [72, 144, 216, 288, 432, 576, 649, 721, 865, 961, 1081, 1201, 1297, 1441],
            "1600": [68, 136, 204, 272, 408, 544, 613, 681, 817, 907, 1021, 1134, 1225, 1361],
            "3200": [61, 122, 184, 245, 368, 490, 551, 613, 735, 817, 919, 1021, 1103, 1225],
        },
        "320MHz": {
            "800": [144, 288, 432, 577, 865, 1153, 1297, 1441, 1729, 1922, 2162, 2402, 2594, 2882],
            "1600": [136, 272, 408, 544, 817, 1089, 1225, 1361, 1633, 1815, 2042, 2269, 2450, 2722],
            "3200": [123, 245, 368, 490, 735, 980, 1103, 1225, 1470, 1633, 1838, 2042, 2205, 2450],
            
        },
    },
    '802.11bn': {
        "20MHz": {
            "800": {0: 8.6, 1: 17.2, 2: 25.8, 3: 34.4, 4: 51.6, 5: 68.8, 6: 77.4, 7: 86.0, 8: 103.2, 9: 114.7, 10: 129.0, 11: 143.4, 12: 154.9, 13: 172.1, 15: 4.3, 17: 22.9, 19: 45.9, 20: 57.4, 23: 91.8},
            "1600": {0: 8.1, 1: 16.2, 2: 24.4, 3: 32.5, 4: 48.7, 5: 65.0, 6: 73.1, 7: 81.2, 8: 97.5, 9: 108.3, 10: 121.8, 11: 135.4, 12: 146.3, 13: 162.5, 15: 4.1, 17: 21.6, 19: 43.4, 20: 54.2, 23: 86.7},
            "3200": {0: 7.3, 1: 14.6, 2: 21.9, 3: 29.2, 4: 43.9, 5: 58.5, 6: 65.8, 7: 73.1, 8: 87.7, 9: 97.5, 10: 109.7, 11: 121.9, 12: 131.7, 13: 146.3, 15: 3.7, 17: 19.5, 19: 39.0, 20: 48.8, 23: 78.0},
        },
        "40MHz": {
            "800": {0: 17.2, 1: 34.4, 2: 51.6, 3: 68.8, 4: 103.2, 5: 137.6, 6: 154.9, 7: 172.1, 8: 206.5, 9: 229.4, 10: 258.1, 11: 286.8, 12: 309.7, 13: 344.1, 15: 8.6, 17: 45.9, 19: 91.8, 20: 114.7, 23: 183.5},
            "1600": {0: 16.2, 1: 32.5, 2: 48.7, 3: 65.0, 4: 97.5, 5: 130.0, 6: 146.3, 7: 162.5, 8: 195.0, 9: 216.7, 10: 243.8, 11: 270.9, 12: 292.5, 13: 325.0, 15: 8.1, 17: 43.4, 19: 86.7, 20: 108.3, 23: 173.3},
            "3200": {0: 14.6, 1: 29.2, 2: 43.9, 3: 58.5, 4: 87.7, 5: 117.0, 6: 131.7, 7: 146.3, 8: 175.5, 9: 195.0, 10: 219.4, 11: 243.8, 12: 263.2, 13: 292.5, 15: 7.3, 17: 39.0, 19: 78.0, 20: 97.5, 23: 156.0},
        },
        "80MHz": {
            "800": {0: 36.0, 1: 72.1, 2: 108.1, 3: 144.1, 4: 216.2, 5: 288.2, 6: 324.3, 7: 360.3, 8: 432.4, 9: 480.4, 10: 540.4, 11: 600.4, 12: 648.5, 13: 720.6, 15: 18.0, 17: 96.0, 19: 192.1, 20: 240.1, 23: 384.3},
            "1600": {0: 34.0, 1: 68.1, 2: 102.1, 3: 136.1, 4: 204.2, 5: 272.2, 6: 306.3, 7: 340.3, 8: 408.4, 9: 453.7, 10: 510.4, 11: 567.0, 12: 612.5, 13: 680.6, 15: 17.0, 17: 90.7, 19: 181.4, 20: 226.8, 23: 363.0},
            "3200": {0: 30.6, 1: 61.3, 2: 91.9, 3: 122.5, 4: 183.8, 5: 245.0, 6: 275.7, 7: 306.3, 8: 367.5, 9: 408.3, 10: 459.3, 11: 510.3, 12: 551.2, 13: 612.5, 15: 15.3, 17: 81.6, 19: 163.3, 20: 204.1, 23: 326.7},
        },
        "160MHz": {
            "800": {0: 72.1, 1: 144.1, 2: 216.2, 3: 288.2, 4: 432.4, 5: 576.5, 6: 648.5, 7: 720.6, 8: 864.7, 9: 960.7, 10: 1080.9, 11: 1201.0, 12: 1297.1, 13: 1441.2, 15: 36.0, 17: 192.1, 19: 384.3, 20: 480.4, 23: 768.6},
            "1600": {0: 68.1, 1: 136.1, 2: 204.2, 3: 272.2, 4: 408.4, 5: 544.5, 6: 612.5, 7: 680.6, 8: 816.7, 9: 907.3, 10: 1020.9, 11: 1134.3, 12: 1225.0, 13: 1361.1, 15: 34.0, 17: 181.4, 19: 363.0, 20: 453.7, 23: 725.9},
            "3200": {0: 61.3, 1: 122.5, 2: 183.8, 3: 245.0, 4: 367.5, 5: 490.0, 6: 551.2, 7: 612.5, 8: 735.0, 9: 816.6, 10: 918.8, 11: 1020.9, 12: 1102.5, 13: 1225.0, 15: 30.6, 17: 163.3, 19: 326.7, 20: 408.3, 23: 653.3},
        },
        "320MHz": {
            "800": {0: 144.1, 1: 288.2, 2: 432.4, 3: 576.5, 4: 864.7, 5: 1152.9, 6: 1297.1, 7: 1441.2, 8: 1729.4, 9: 1921.5, 10: 2161.8, 11: 2401.9, 12: 2594.1, 13: 2882.4, 15: 72.1, 17: 384.3, 19: 768.6, 20: 960.7, 23: 1537.2},
            "1600": {0: 136.1, 1: 272.2, 2: 408.4, 3: 544.5, 4: 816.7, 5: 1088.9, 6: 1225.0, 7: 1361.1, 8: 1633.3, 9: 1814.8, 10: 2041.7, 11: 2268.5, 12: 2450.0, 13: 2722.3, 15: 68.1, 17: 363.0, 19: 725.9, 20: 907.3, 23: 1451.8},
            "3200": {0: 122.5, 1: 245.0, 2: 367.5, 3: 490.0, 4: 735.0, 5: 980.0, 6: 1102.5, 7: 1225.0, 8: 1470.0, 9: 1633.3, 10: 1837.5, 11: 2041.6, 12: 2205.0, 13: 2450.0, 15: 61.3, 17: 326.7, 19: 653.3, 20: 816.6, 23: 1306.6},
        },
    },
        '802.11ad': {
        "2.16GHz": {
            "SC-PHY": [27.5, 385, 770, 962.5, 1155, 1251.25, 1540, 1925, 2310, 2502.5, 3080, 3850, 4620],
            "OFDM-PHY": [27.5, 693, 866.25, 1386, 1732.5, 2079, 2772, 3465, 4158, 4504.5, 5197.5, 6237, 6756.75],
            "LPSC-PHY": [27.5, 626, 834, 1112, 1251, 1668, 2224, 2503],
        },
    },
        '802.11ah': {
        "1MHz": {
            "8μs": [0.3, 0.6, 0.9, 1.2, 1.8, 2.4, 2.7, 3.0, 3.6, 4.0, 0.15],
            "4μs": [0.33, 0.67, 1.0, 1.33, 2.0, 2.67, 3.0, 3.34, 4.0, 4.44, 0.17],
        },
        "2MHz": {
            "8μs": [0.65, 1.3, 1.95, 2.6, 3.9, 5.2, 5.85, 6.5, 7.8],
            "4μs": [0.72, 1.44, 2.17, 2.89, 4.33, 5.78, 6.5, 7.22, 8.67],
        },
        "4MHz": {
            "8μs": [1.35, 2.7, 4.05, 5.4, 8.1, 10.8, 12.2, 13.5, 16.2, 18.0],
            "4μs": [1.5, 3.0, 4.5, 6.0, 9.0, 12.0, 13.5, 15.0, 18.0, 20.0],
        },
        "8MHz": {
            "8μs": [2.93, 5.85, 8.78, 11.7, 17.6, 23.4, 26.3, 29.3, 35.1, 39.0],
            "4μs": [3.25, 6.5, 9.75, 13.0, 19.5, 26.0, 29.3, 32.5, 39.0, 43.3],
        },
        "16MHz": {
            "8μs": [5.85, 11.7, 17.6, 23.4, 35.1, 46.8, 52.7, 58.5, 70.2, 78.0],
            "4μs": [6.5, 13.0, 19.5, 26.0, 39.0, 52.0, 58.5, 65.0, 78.0, 86.7],
            
        },
    },
        '802.11af': {
            "6MHz": {
                "5μs": [1.8, 3.6, 5.4, 7.2, 10.8, 14.4, 16.2, 18.0, 21.6, 24.0],
                "3μs": [2.0, 4.0, 6.0, 8.0, 12.0, 16.0, 18.0, 20.0, 24.0, 26.7],
            },
            "8MHz": {
                "5μs": [2.4, 4.8, 7.2, 9.6, 14.4, 19.2, 21.6, 24.0, 28.8, 32.0],
                "3μs": [2.7, 5.3, 8.0, 10.7, 16.0, 21.3, 24.0, 26.7, 32.0, 35.6],
            },
    },
}

SPATIAL_STREAM_LIMITS = {
    '802.11b': {
        'min': 1,
        'max': 1,
    },
    '802.11a': {
        'min': 1,
        'max': 1,
    },
    '802.11g': {
        'min': 1,
        'max': 1,
    },
    '802.11ah': {
        'min': 1,
        'max': 4,
    },
    '802.11n': {
        'min': 1,
        'max': 4,
    },
    '802.11ac': {
        'min': 1,
        'max': 8,
    },
    '802.11ax': {
        'min': 1,
        'max': 8,
    },
    '802.11ad': {
        'min': 1,
        'max': 1,
    },
    '802.11be': {
        'min': 1,
        'max': 16,
    },
    '802.11af': {
        'min': 1,
        'max': 4,
    },
    '802.11bn': {
        'min': 1,
        'max': 8,
    },
}

# MCS indices offered per standard. Most standards use consecutive indices from
# 0 upwards, but 802.11bn adds finer steps and skips the unused indices.
MCS_INDEX_OPTIONS = {
    '802.11bn': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 19, 20, 23],
}

# Function to look up the per-stream rate for an MCS index. Rates are stored as
# a list indexed by MCS index, or as an MCS index keyed dict for standards that
# skip indices.
def get_mcs_rate(rate_table, mcs_index):
    if isinstance(rate_table, dict):
        return rate_table.get(mcs_index)
    if 0 <= mcs_index < len(rate_table):
        return rate_table[mcs_index]
    return None

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
        mcs_rate = get_mcs_rate(MCS_DATA_RATES[standard][bandwidth][guard_interval], mcs_index)
        if mcs_rate is None:
            result_label["text"] = f"MCS {mcs_index} is not defined for {standard} {bandwidth}"
        else:
            data_rate = mcs_rate * spatial_streams
            result_label["text"] = f"{round(data_rate, 2)} Mbps"
    else:
        result_label["text"] = "Invalid input values"


# Create the main window
root = tk.Tk()
root.title("Wi-Fi Data Rate Calculator")

# Function to update spatial stream options
def update_spatial_stream_options(event):
    selected_standard = standard_combo.get()
    
    if selected_standard in SPATIAL_STREAM_LIMITS:
        min_limit = SPATIAL_STREAM_LIMITS[selected_standard]['min']
        max_limit = SPATIAL_STREAM_LIMITS[selected_standard]['max']
        spatial_streams_options = [str(i) for i in range(min_limit, max_limit + 1)]
        spatial_streams_entry['values'] = spatial_streams_options
        spatial_streams_entry.set(spatial_streams_options[0])  # Set the default value

# Define the update_options function
def update_options(event, combo):
    selected_standard = combo.get()
    
    if selected_standard in MCS_DATA_RATES:
        # Update available bandwidth options based on the selected standard
        bandwidth_options = list(MCS_DATA_RATES[selected_standard].keys())
        bandwidth_combo['values'] = bandwidth_options
        bandwidth_combo.set(bandwidth_options[0])  # Set the default value

        # Update available guard interval options based on the selected standard and bandwidth
        selected_bandwidth = bandwidth_combo.get()
        if selected_bandwidth in MCS_DATA_RATES[selected_standard]:
            guard_interval_options = list(MCS_DATA_RATES[selected_standard][selected_bandwidth].keys())
            guard_interval_combo['values'] = guard_interval_options
            guard_interval_combo.set(guard_interval_options[0])  # Set the default value

        # Update the selectable MCS indices, since 802.11bn skips some of them
        mcs_options = [str(i) for i in MCS_INDEX_OPTIONS.get(selected_standard, range(14))]
        mcs_combo['values'] = mcs_options
        mcs_combo.set(mcs_options[0])

        # Update spatial stream options if applicable
        update_spatial_stream_options(event)
    else:
        # Handle the case where the selected combination doesn't exist in the data dictionary
        print("Selected combination not found in data dictionary")

# Wi-Fi Standard selection
standard_label = tk.Label(root, text="Wi-Fi Standard:")
standard_label.grid(row=0, column=0)
standard_combo = ttk.Combobox(root, values=["802.11b", "802.11a", "802.11g", "802.11n", "802.11ac", "802.11af", "802.11ah", "802.11ax", "802.11ad", "802.11be", "802.11bn"])
standard_combo.grid(row=0, column=1)
standard_combo.set("802.11b")
standard_combo.bind("<<ComboboxSelected>>", lambda event, combo=standard_combo: update_options(event, combo))

# MCS selection
mcs_label = tk.Label(root, text="MCS:")
mcs_label.grid(row=1, column=0)
mcs_combo = ttk.Combobox(root, values=[str(i) for i in range(14)])
mcs_combo.grid(row=1, column=1)
mcs_combo.set("0")

# Bandwidth selection
bandwidth_label = tk.Label(root, text="Bandwidth:")
bandwidth_label.grid(row=2, column=0)
bandwidth_combo = ttk.Combobox(root, values=["1MHz", "2MHz", "4MHz", "6MHz", "8MHz", "16MHz", "20MHz", "SuperG", "40MHz", "80MHz", "160MHz", "320MHz", "2.16GHz"])
bandwidth_combo.grid(row=2, column=1)
bandwidth_combo.set("20MHz")

# Guard Interval selection
guard_interval_label = tk.Label(root, text="GI (Sub-6) (ns) / MOD (mmWave):")
guard_interval_label.grid(row=3, column=0)
guard_interval_combo = ttk.Combobox(root, values=["3μs", "4μs", "5μs", "6μs", "8μs", "400", "800", "1600", "3200", "SC-PHY", "OFDM-PHY", "LPSC-PHY"])
guard_interval_combo.grid(row=3, column=1)
guard_interval_combo.set("800")

# Spatial Streams entry
spatial_streams_label = tk.Label(root, text="SISO/MIMO/MU-MIMO:")
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
