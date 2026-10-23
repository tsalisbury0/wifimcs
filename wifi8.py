import tkinter as tk

# UHR-MCS data rates in Mbps for a single spatial stream, full-bandwidth RUs,
# with a 0.8 microsecond guard interval (IEEE P802.11bn/D2.0, Clause 38.5).
# Wi-Fi 8 keeps the 802.11be PHY (4096-QAM, up to 320MHz, up to 8 spatial
# streams) and adds finer MCS steps at indices 15, 17, 19, 20 and 23.
UHR_MCS_RATES_800NS_GI = {
    "20MHz": {
        0: 8.6, 1: 17.2, 2: 25.8, 3: 34.4, 4: 51.6, 5: 68.8, 6: 77.4, 7: 86.0,
        8: 103.2, 9: 114.7, 10: 129.0, 11: 143.4, 12: 154.9, 13: 172.1,
        15: 4.3, 17: 22.9, 19: 45.9, 20: 57.4, 23: 91.8,
    },
    "40MHz": {
        0: 17.2, 1: 34.4, 2: 51.6, 3: 68.8, 4: 103.2, 5: 137.6, 6: 154.9, 7: 172.1,
        8: 206.5, 9: 229.4, 10: 258.1, 11: 286.8, 12: 309.7, 13: 344.1,
        15: 8.6, 17: 45.9, 19: 91.8, 20: 114.7, 23: 183.5,
    },
    "80MHz": {
        0: 36.0, 1: 72.1, 2: 108.1, 3: 144.1, 4: 216.2, 5: 288.2, 6: 324.3, 7: 360.3,
        8: 432.4, 9: 480.4, 10: 540.4, 11: 600.4, 12: 648.5, 13: 720.6,
        15: 18.0, 17: 96.0, 19: 192.1, 20: 240.1, 23: 384.3,
    },
    "160MHz": {
        0: 72.1, 1: 144.1, 2: 216.2, 3: 288.2, 4: 432.4, 5: 576.5, 6: 648.5, 7: 720.6,
        8: 864.7, 9: 960.7, 10: 1080.9, 11: 1201.0, 12: 1297.1, 13: 1441.2,
        15: 36.0, 17: 192.1, 19: 384.3, 20: 480.4, 23: 768.6,
    },
    "320MHz": {
        0: 144.1, 1: 288.2, 2: 432.4, 3: 576.5, 4: 864.7, 5: 1152.9, 6: 1297.1, 7: 1441.2,
        8: 1729.4, 9: 1921.5, 10: 2161.8, 11: 2401.9, 12: 2594.1, 13: 2882.4,
        15: 72.1, 17: 384.3, 19: 768.6, 20: 960.7, 23: 1537.2,
    },
}

# Guard interval in microseconds, keyed by the label shown in the GUI.
GUARD_INTERVALS = {
    "800ns": 0.8,
    "1600ns": 1.6,
    "3200ns": 3.2,
}

# OFDM symbol duration excluding the guard interval, in microseconds.
SYMBOL_TIME = 12.8


def build_mcs_table():
    """Expand the 0.8us guard interval rates to the longer guard intervals.

    The FFT symbol time is fixed at 12.8us, so a rate only scales by
    13.6 / (12.8 + GI) when the guard interval changes.
    """
    return {
        bandwidth: {
            gi_label: {
                mcs: round(rate * (SYMBOL_TIME + 0.8) / (SYMBOL_TIME + gi), 1)
                for mcs, rate in rates.items()
            }
            for gi_label, gi in GUARD_INTERVALS.items()
        }
        for bandwidth, rates in UHR_MCS_RATES_800NS_GI.items()
    }


MCS_TABLE = build_mcs_table()
MCS_INDICES = sorted(MCS_TABLE["20MHz"]["800ns"])


def calculate_mcs_speed():
    bandwidth = bandwidth_var.get()
    guard_interval = guard_interval_var.get()

    try:
        spatial_streams = int(spatial_streams_var.get())
        mcs_index = int(mcs_var.get())
    except ValueError:
        result_label.config(text="Spatial streams and MCS index must be whole numbers.")
        return

    if spatial_streams < 1 or spatial_streams > 8:
        result_label.config(text="Wi-Fi 8 supports 1 to 8 spatial streams.")
        return

    rate = MCS_TABLE[bandwidth][guard_interval].get(mcs_index)
    if rate is None:
        result_label.config(
            text=f"Invalid MCS index for {bandwidth}. Valid indices: "
            + ", ".join(str(i) for i in MCS_INDICES)
            + "."
        )
        return

    total_speed = rate * spatial_streams
    result_label.config(
        text=f"MCS-{mcs_index} Speed for {bandwidth} with {guard_interval} Guard Interval, "
        f"{spatial_streams} Spatial Streams: {rate} Mbps (Total: {round(total_speed, 2)} Mbps)"
    )


# Create the main window
window = tk.Tk()
window.title("802.11bn MCS Speed Calculator")

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
spatial_streams_label = tk.Label(window, text="Number of Spatial Streams (1-8):")
spatial_streams_label.pack()

spatial_streams_var = tk.StringVar(value="1")
spatial_streams_entry = tk.Entry(window, textvariable=spatial_streams_var)
spatial_streams_entry.pack()

# MCS index selection
mcs_label = tk.Label(window, text="Select MCS Index (0-13, 15, 17, 19, 20, 23):")
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
