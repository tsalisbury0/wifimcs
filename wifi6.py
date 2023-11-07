import tkinter as tk

def calculate_mcs_speed():
    bandwidth = bandwidth_var.get()
    guard_interval = guard_interval_var.get()
    spatial_streams = int(spatial_streams_var.get())
    mcs_index = int(mcs_var.get())

    mcs_table = {
        "20MHz": {
            "LongGI": [12.8, 25.6, 38.4, 51.2, 64, 76.8, 89.6, 102.4, 115.2, 128],
            "ShortGI": [14.4, 28.8, 43.2, 57.6, 72, 86.4, 100.8, 115.2, 129.6, 144],
        },
        "40MHz": {
            "LongGI": [25.6, 51.2, 76.8, 102.4, 128, 153.6, 179.2, 204.8, 230.4, 256],
            "ShortGI": [28.8, 57.6, 86.4, 115.2, 144, 172.8, 201.6, 230.4, 259.2, 288],
        },
        "80MHz": {
            "LongGI": [51.2, 102.4, 153.6, 204.8, 256, 307.2, 358.4, 409.6, 460.8, 512],
            "ShortGI": [57.6, 115.2, 172.8, 230.4, 288, 345.6, 403.2, 460.8, 518.4, 576],
        },
        "160MHz": {
            "LongGI": [102.4, 204.8, 307.2, 409.6, 512, 614.4, 716.8, 819.2, 921.6, 1024],
            "ShortGI": [115.2, 230.4, 345.6, 460.8, 576, 691.2, 806.4, 921.6, 1036.8, 1152],
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
window.title("802.11ax MCS Speed Calculator")

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

