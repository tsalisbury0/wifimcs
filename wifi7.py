import tkinter as tk

def calculate_mcs_speed():
    bandwidth = bandwidth_var.get()
    guard_interval = guard_interval_var.get()
    spatial_streams = int(spatial_streams_var.get())
    mcs_index = int(mcs_var.get())

    mcs_table = {
        "20MHz": {
            "800ns": [9, 17, 26, 34, 52, 69, 77, 86, 103, 115, 129, 143, 155, 172],
            "1600ns": [8, 16, 24, 33, 49, 65, 73, 81, 98, 108, 122, 135, 146, 163],
            "3200ns": [7, 15, 22, 29, 44, 59, 66, 73, 88, 98, 110, 122, 131, 146],
        },
        "40MHz": {
            "800ns": [17, 34, 52, 69, 103, 138, 155, 172, 207, 229, 258, 287, 310, 344],
            "1600ns": [16, 33, 49, 65, 98, 130, 146, 163, 195, 217, 244, 271, 293, 325],
            "3200ns": [15, 29, 44, 59, 88, 117, 132, 146, 176, 195, 219, 244, 263, 293],
        },
        "80MHz": {
            "800ns": [36, 72, 108, 144, 216, 288, 324, 360, 432, 480, 540, 600, 649, 721],
            "1600ns": [34, 68, 102, 136, 204, 272, 306, 340, 408, 453, 510, 567, 613, 681],
            "3200ns": [31, 61, 92, 123, 184, 245, 276, 306, 368, 408, 459, 510, 551, 613],
        },
        "160MHz": {
            "800ns": [72, 144, 216, 282, 432, 576, 649, 721, 865, 961, 1081, 1201, 1297, 1441],
            "1600ns": [68, 136, 204, 272, 408, 544, 613, 681, 817, 907, 1021, 1134, 1225, 1361],
            "3200ns": [61, 122, 184, 245, 368, 490, 551, 613, 735, 817, 919, 1021, 1103, 1125],
        },
        "320MHz": {
            "800ns": [144, 288, 432, 577, 865, 1153, 1297, 1441, 1729, 1922, 2162, 2402, 2594, 2882],
            "1600ns": [136, 272, 408, 544, 817, 1089, 1225, 1361, 1633, 1815, 2042, 2269, 2450, 2772],
            "3200ns": [123, 245, 368, 490, 735, 980, 1103, 1225, 1470, 1633, 1838, 2042, 2205, 2450],
        },
    }

    if bandwidth in mcs_table and guard_interval in mcs_table[bandwidth]:
        max_mcs_index = len(mcs_table[bandwidth][guard_interval]) - 1
        if mcs_index >= 0 and mcs_index <= max_mcs_index:
            mcs_speed = mcs_table[bandwidth][guard_interval][mcs_index]
            total_speed = mcs_speed * spatial_streams
            result_label.config(text=f"MCS-{mcs_index} Speed for {bandwidth} with {guard_interval} Guard Interval, {spatial_streams} Spatial Streams: {mcs_speed} Mbps (Total: {total_speed} Mbps)")
        else:
            result_label.config(text="Invalid MCS index for selected bandwidth and guard interval.")
    else:
        result_label.config(text="Invalid bandwidth or guard interval.")

# Create the main window
window = tk.Tk()
window.title("802.11be MCS Speed Calculator")

# Bandwidth selection
bandwidth_label = tk.Label(window, text="Select Bandwidth:")
bandwidth_label.pack()

bandwidth_var = tk.StringVar(value="20MHz")
bandwidth_radio_20 = tk.Radiobutton(window, text="20MHz", variable=bandwidth_var, value="20MHz")
bandwidth_radio_40 = tk.Radiobutton(window, text="40MHz", variable=bandwidth_var, value="40MHz")
bandwidth_radio_80 = tk.Radiobutton(window, text="80MHz", variable=bandwidth_var, value="80MHz")
bandwidth_radio_160 = tk.Radiobutton(window, text="160MHz", variable=bandwidth_var, value="160MHz")
bandwidth_radio_320 = tk.Radiobutton(window, text="320MHz", variable=bandwidth_var, value="320MHz")
bandwidth_radio_20.pack()
bandwidth_radio_40.pack()
bandwidth_radio_80.pack()
bandwidth_radio_160.pack()
bandwidth_radio_320.pack()

# Guard interval selection
guard_interval_label = tk.Label(window, text="Select Guard Interval:")
guard_interval_label.pack()

guard_interval_var = tk.StringVar(value="800ns")
guard_interval_radio_800ns = tk.Radiobutton(window, text="800ns", variable=guard_interval_var, value="800ns")
guard_interval_radio_1600ns = tk.Radiobutton(window, text="1600ns", variable=guard_interval_var, value="1600ns")
guard_interval_radio_3200ns = tk.Radiobutton(window, text="3200ns", variable=guard_interval_var, value="3200ns")
guard_interval_radio_800ns.pack()
guard_interval_radio_1600ns.pack()
guard_interval_radio_3200ns.pack()

# Spatial Streams selection
spatial_streams_label = tk.Label(window, text="Number of Spatial Streams (1-16):")
spatial_streams_label.pack()

spatial_streams_var = tk.StringVar(value="1")
spatial_streams_entry = tk.Entry(window, textvariable=spatial_streams_var)
spatial_streams_entry.pack()

# MCS index selection
mcs_label = tk.Label(window, text="Select MCS Index (0-13 for selected bandwidth and guard interval):")
mcs_label.pack()

mcs_var = tk.StringVar(value="0")
mcs_entry = tk.Entry(window, textvariable=mcs_var)
mcs_entry.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate MCS Speed", command=calculate_mcs_speed)
calculate_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI main loop
window.mainloop()

