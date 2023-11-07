# Wi-Fi MCS Speed Calculator

This is a Python script with a graphical user interface (GUI) that allows you to calculate MCS (Modulation and Coding Scheme) speeds for various Wi-Fi standards, including 802.11n, 802.11ac, 802.11ax, and 802.11be. You can select the desired parameters such as bandwidth, guard interval, spatial streams, and MCS index to determine the data rate.

## Features

- Calculate MCS speeds for different Wi-Fi standards.
- Support for various bandwidth options (20MHz, 40MHz, 80MHz, 160MHz, 320MHz).
- Choose between different guard intervals (800ns, 1600ns, 3200ns).
- Specify the number of spatial streams.
- Select the MCS index within the supported range.

## Prerequisites

- Python 3.x installed on your system.
- Python3 tkinter module

## How to Use

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Run the script using the following command:
- 802.11n: python3 wifi4.py
- 802.11ac: python3 wifi5.py
- 802.11ax: python3 wifi6.py
- 802.11be: python3 wifi7.py


4. The GUI will open, and you can start using the MCS speed calculator.

## Usage

1. Select the desired bandwidth from the available options (20MHz, 40MHz, 80MHz, 160MHz, 320MHz).

2. Choose the guard interval (e.g., 800ns, 1600ns, 3200ns).

3. Specify the number of spatial streams you want to consider (typically 1 or more).

4. Enter the MCS index you wish to calculate (within the supported range).

5. Click the "Calculate MCS Speed" button to view the calculated MCS speed in Mbps.

6. The result will be displayed in the GUI.

## Supported Wi-Fi Standards

- 802.11n
- 802.11ac
- 802.11ax
- 802.11be

## Disclaimer

This script provides a simplified model for educational purposes and does not account for real-world complexities in wireless networks. The calculated MCS speeds may not precisely match actual Wi-Fi performance due to various environmental factors and channel conditions.

## Acknowledgments

- Inspired by the 802.11n, 802.11ac, 802.11ax, and 802.11be Wi-Fi standards.

## Author

Tyler
