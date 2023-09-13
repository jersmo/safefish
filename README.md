# Safefish - 
Safe fishing bot for roblox fishing simulator and bonus chest opener

This script provides automated mouse and keyboard actions to simulate fishing in the roblox game Fishing Simulator. It uses image recognition to detect fish and air bubbles on the screen and performs actions accordingly.

> **Note**: This is a being  used a method to teach a child to code.  It may not get updated regularly.

> **Disclaimer**: Using this script can theoretically get you banned from the game or Roblox platform. Use at your own risk and always respect the terms of service of the game and platform.

## Features

-   Simulates mouse clicks and movements.
-   Detects fish and air bubbles using pixel color recognition.
-   Uses human-like mouse movement, clicks, and random timings to simulate human interaction
-   Keeps track of the number of fish caught.
-   Sells fish or exits when the inventory is full.

## Prerequisites

-   Python 3.8

## Installation

1. Clone the repository:

```batch
git clone https://github.com/jersmo/safefish.git
```

2. Navigate to the project directory:

```batch
cd safefish
```

3. Install the required packages:

```batch
pip install -r requirements.txt
```

## Usage

1. Start the roblox game Fishing Simulator
2. Set the following before you run the script -
```batch
CATCH_COUNT = 96  # Sell after you catch how many fish?  Backpack size minus slots used with equipment
FISHING_DELAY = .25  # .25 for main, .41 for perfect balance and total noob - Lower is faster
FISHING_RANDOM = .2  # Random delay to add to casts to make less bannable, .2 or .1 for mains .05 for total noob.
FISHING_POLE_SLOT = 1  # What slot is fishing pole in?
TIME_FOR_BUBBLES = 4  # Max time to wait after casting to detect bubbles.  Noobs might need 5 or 6
SELL_ANYWHERE = True  # If you purchased sell anywhere.  Otherwise the script will exit.

OPEN_CHESTS = False  # If you want to use this script to open chests only.  You'll need to set the coords below
OPEN_CHEST_X = 922  # Use Mpos to get coords of the bottom of the white E box you need to press.  MUST BE WHITE
OPEN_CHEST_Y = 511  # Same ^
```
3. Position the game window such that the script can detect the necessary pixels (Fullscreen is recommended on a 1920x1080 screen)
4. Run the script:

```batch
python safefish.py
```

4. The script will start simulating fishing actions. Press 'CTRL+C' to stop the script.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.
