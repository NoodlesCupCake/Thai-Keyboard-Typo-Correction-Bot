# Thai Keyboard Typo Correction Bot

This Discord bot helps correct common English keyboard typos into Thai characters. It's designed to convert English typos into Thai text based on a predefined mapping.

## Features

- **Typo Correction**: Automatically converts common English typos into Thai characters.
- **Command Support**: Use the `!ome` command to process and correct messages.

## Requirements

- Python 3.8+
- `discord.py` library
- `python-dotenv` library

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file** in the root directory with the following content:

    ```env
    DISCORD_TOKEN=your_discord_bot_token_here
    ```

4. **Run the bot**:

    ```bash
    python bot.py
    ```

## Commands

- `!ome <message>`: Convert the provided message from English typos to Thai characters and send the corrected message.

## Code Overview

- **`bot.py`**: Contains the main bot logic.
  - **`eng2thai`**: A dictionary mapping English typos to Thai characters.
  - **`on_ready`**: Logs a message when the bot starts.
  - **`on_message`**: Converts the provided message to Thai characters when the `!ome` command is used.

## Example

1. **User sends**: `!ome -uhgdup0wxme'ko,kd c9jdHvpkdwfh9y',kg9b,gd,gs,nvogfb, gLihk`
2. **Bot responds**: `จริง ๆ ตั้งใจจะพิมพ์ว่า "ขี้เกียจไปทำงานมาก แต่ก็อยากได้ตังมาเติมเกมเหมทอนเดิม เศร้า"`

