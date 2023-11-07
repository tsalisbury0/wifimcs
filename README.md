# Wi-Fi MCS Speed Calculator

This is a Python script with a graphical user interface (GUI) that allows you to calculate MCS (Modulation and Coding Scheme) speeds for various Wi-Fi standards, including 802.11a, 802.11b, 802.11g/SuperG, 802.11n, 802.11ac, 802.11ax, and 802.11be. You can select the desired parameters such as bandwidth, guard interval, spatial streams, and MCS index to determine the data rate.

## Features

- Calculate MCS speeds for different Wi-Fi standards.
- Support for various bandwidth options (20MHz, SuperG, 40MHz, 80MHz, 160MHz, 320MHz).
- Choose between different guard intervals (400ns, 800ns, 1600ns, 3200ns).
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
- Selectable standard: python3 wifi.py


4. The GUI will open, and you can start using the MCS speed calculator.

## Usage

1. Select the desired bandwidth from the available options (20MHz, SuperG, 40MHz, 80MHz, 160MHz, 320MHz).

2. Choose the guard interval (e.g., 400ns, 800ns, 1600ns, 3200ns).

3. Specify the number of spatial streams you want to consider (typically 1 or more).

4. Enter the MCS index you wish to calculate (within the supported range).

5. Click the "Calculate MCS Speed" button to view the calculated MCS speed in Mbps.

6. The result will be displayed in the GUI.

## Supported Wi-Fi Standards

- 802.11a
- 802.11b
- 802.11g
- 802.11n
- 802.11ac
- 802.11ax
- 802.11be

## Disclaimer

This script provides a simplified model for educational purposes and does not account for real-world complexities in wireless networks. The calculated MCS speeds may not precisely match actual Wi-Fi performance due to various environmental factors and channel conditions.

-802.11a/b/g has no MIMO or 400ns/1600ns/3200ns Guard Intervals
-802.11b only has MCS 0-4 and Bandwidth of 20MHz
-802.11a/g only has MCS 0-7 (Only 802.11g has SuperG A.K.A. 40MHz/802.11a is 20MHz only)
-802.11n only has MCS 0-8 and MIMO up to 4 and Bandwidth up to 40MHz
-802.11ac only has MCS 0-8, MIMO up to 8 and Bandwidth up to 160MHz
-802.11ax only has MCS 0-11, MIMO up to 8 and Bandwidth up to 160MHz
-802.11be only has MCS 0-13, MIMO up to 16 and Bandwidth up to 320MHz

## To Be Added

Will take time to gather data on 802.11ad and 802.11ay but I intend to add them soon.

## Acknowledgments

- Inspired by the 802.11a, 802.11b, 802.11g/SuperG, 802.11n, 802.11ac, 802.11ax, and 802.11be Wi-Fi standards.

## Author

Tyler
