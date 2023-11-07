import tkinter as tk

def calculate_mcs_speed():
    bandwidth = bandwidth_var.get()
    guard_interval = guard_interval_var.get()
    spatial_streams = int(spatial_streams_var.get())
    mcs_index = int(mcs_var.get())

    mcs_table = {
        "20MHz": {
            "LongGI": [8, 16, 24, 32, 48, 64, 72, 80, 96, 104],
            "ShortGI": [8.8, 17.6, 26.4, 35.3, 52.9, 70.6, 79, 88.2, 105.8, 117.7],
        },
        "40MHz": {
            "LongGI": [17, 34, 51, 68, 102, 136, 153, 170, 204, 221],
            "ShortGI": [19.2, 38.5, 57.8, 77, 115.5, 154, 173, 192, 230, 250],
        },
        "80MHz": {
            "LongGI": [34, 68, 102, 136, 204, 272, 306, 340, 408, 442],
            "ShortGI": [38, 76, 114, 152, 228, 304, 342, 380, 456, 494],
        },
        "160MHz": {
            "LongGI": [68, 136, 204, 272, 408, 544, 612, 680, 816, 884],
            "ShortGI": [76, 152, 228, 304, 456, 608, 684, 760, 912, 988],
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

