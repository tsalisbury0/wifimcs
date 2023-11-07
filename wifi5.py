import tkinter as tk

def calculate_mcs_speed():
    bandwidth = bandwidth_var.get()
    guard_interval = guard_interval_var.get()
    spatial_streams = int(spatial_streams_var.get())
    mcs_index = int(mcs_var.get())

    mcs_table = {
        "20MHz": {
            "LongGI": [6.5, 13, 19.5, 26, 39, 52, 58.5, 65, 78],
            "ShortGI": [7.2, 14.4, 21.7, 28.9, 43.3, 57.8, 65, 72.2, 86.7],
        },
        "40MHz": {
            "LongGI": [13.5, 27, 40.5, 54, 81, 108, 121.5, 135, 162, 180],
            "ShortGI": [15, 30, 45, 60, 90, 120, 135, 150, 180, 200],
        },
        "80MHz": {
            "LongGI": [29.3, 58.5, 87.8, 117, 175.5, 234, 263.3, 292.5, 351, 390],
            "ShortGI": [32.5, 65, 97.5, 130, 195, 260, 292.5, 325, 290, 433.3],
        },
        "160MHz": {
            "LongGI": [58.5, 117, 175.5, 234, 351, 468, 526.5, 585, 702, 780],
            "ShortGI": [65, 130, 195, 260, 390, 520, 585, 650, 780, 866.7],
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
window.title("802.11ac MCS Speed Calculator")

# Bandwidth selection
bandwidth_label = tk.Label(window, text="Select Bandwidth:")
bandwidth_label.pack()

bandwidth_var = tk.StringVar(value="20MHz")
bandwidth_radio_20 = tk.Radiobutton(window, text="20MHz", variable=bandwidth_var, value="20MHz")
bandwidth_radio_40 = tk.Radiobutton(window, text="40MHz", variable=bandwidth_var, value="40MHz")
bandwidth_radio_80 = tk.Radiobutton(window, text="80MHz", variable=bandwidth_var, value="80MHz")
bandwidth_radio_160 = tk.Radiobutton(window, text="160MHz", variable=bandwidth_var, value="160MHz")
bandwidth_radio_20.pack()
bandwidth_radio_40.pack()
bandwidth_radio_80.pack()
bandwidth_radio_160.pack()

# Guard interval selection
guard_interval_label = tk.Label(window, text="Select Guard Interval:")
guard_interval_label.pack()

guard_interval_var = tk.StringVar(value="LongGI")
guard_interval_radio_longgi = tk.Radiobutton(window, text="LongGI", variable=guard_interval_var, value="LongGI")
guard_interval_radio_shortgi = tk.Radiobutton(window, text="ShortGI", variable=guard_interval_var, value="ShortGI")
guard_interval_radio_longgi.pack()
guard_interval_radio_shortgi.pack()

# Spatial Streams selection
spatial_streams_label = tk.Label(window, text="Number of Spatial Streams (1-8):")
spatial_streams_label.pack()

spatial_streams_var = tk.StringVar(value="1")
spatial_streams_entry = tk.Entry(window, textvariable=spatial_streams_var)
spatial_streams_entry.pack()

# MCS index selection
mcs_label = tk.Label(window, text="Select MCS Index (0-9 for 20/40/80/160MHz):")
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

