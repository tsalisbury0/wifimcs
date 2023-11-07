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
            "LongGI": [13, 26, 39, 52, 78, 104, 117, 130, 156],
            "ShortGI": [14.4, 28.9, 43.3, 57.8, 86.7, 115.6, 130, 144.4, 173.3],
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
window.title("802.11n MCS Speed Calculator")

# Bandwidth selection
bandwidth_label = tk.Label(window, text="Select Bandwidth:")
bandwidth_label.pack()

bandwidth_var = tk.StringVar(value="20MHz")
bandwidth_radio_20 = tk.Radiobutton(window, text="20MHz", variable=bandwidth_var, value="20MHz")
bandwidth_radio_40 = tk.Radiobutton(window, text="40MHz", variable=bandwidth_var, value="40MHz")
bandwidth_radio_20.pack()
bandwidth_radio_40.pack()

# Guard interval selection
guard_interval_label = tk.Label(window, text="Select Guard Interval:")
guard_interval_label.pack()

guard_interval_var = tk.StringVar(value="LongGI")
guard_interval_radio_longgi = tk.Radiobutton(window, text="LongGI", variable=guard_interval_var, value="LongGI")
guard_interval_radio_shortgi = tk.Radiobutton(window, text="ShortGI", variable=guard_interval_var, value="ShortGI")
guard_interval_radio_longgi.pack()
guard_interval_radio_shortgi.pack()

# Spatial Streams selection
spatial_streams_label = tk.Label(window, text="Number of Spatial Streams (1-4):")
spatial_streams_label.pack()

spatial_streams_var = tk.StringVar(value="1")
spatial_streams_entry = tk.Entry(window, textvariable=spatial_streams_var)
spatial_streams_entry.pack()

# MCS index selection
mcs_label = tk.Label(window, text="Select MCS Index (0-7 for 20MHz, 0-7 for 40MHz) (8 256QAM):")
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
