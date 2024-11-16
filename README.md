# Python Telegram GIF Bot  

⚠️ **This repository is no longer maintained. Use at your own risk.**  

## Overview  
This is a simple Python bot that automatically sends a GIF in response to every message it receives. The bot is designed for use with Telegram and leverages the Telegram Bot API.  

## Requirements  
- Python 3.8  
- A bot token obtained from [@BotFather](https://t.me/BotFather) on Telegram.  
- A GIF file ID from Telegram.  

## Setup Guide  

### 1. Clone the Repository  
Clone the repository to your local machine:  
```bash  
git clone https://github.com/JustTrott/telegram-gif-python-bot.git 
cd telegram-gif-python-bot
```  

### 2. Install Python 3.8  
Ensure you have Python 3.8 installed. You can download it from [python.org](https://www.python.org/downloads/).  

### 3. Install Dependencies  
Install the required Python packages using the following command:  
```bash  
pip install -r requirements.txt  
```  

### 4. Get Your Bot Token and GIF File ID  
1. **Obtain Bot Token:**  
   - Chat with [@BotFather](https://t.me/BotFather) on Telegram.  
   - Follow the instructions to create a new bot and get your bot token.  

2. **Get GIF File ID:**  
   - Send a GIF to [@userinfobot](https://t.me/userinfobot) or any Telegram bot debugging tool that provides file IDs.  
   - Copy the file ID of your desired GIF.    

### 5. Run the Bot  
Start the bot by running the following command:  
```bash  
python bot.py  
```  

Your bot is now up and running! It will send the specified GIF in response to every message it receives.  

## Notes  
- This project is no longer actively maintained. Feel free to fork and modify it as needed.  

## License  
This project is open-source and available under the [MIT License](LICENSE).  
