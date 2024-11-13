# LinkedIn Connection Removal Automation

Automate the removal of LinkedIn connections using Python and Selenium. This script logs in to your LinkedIn account, navigates to your connections, and removes each connection one-by-one with delays to mimic human behavior, minimizing the risk of account bans.

## Features
- **Automated Login**: Securely logs in to your LinkedIn account using credentials stored in an `.env` file.
- **Human-like Interaction**: Each step includes a delay to replicate human timing, helping to avoid detection.
- **Looped Removal**: Continuously removes connections until there are none left.

## Requirements
- Python 3.x
- Firefox browser
- `selenium`, `python-dotenv`

## Setup and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/linkedin-connection-remover.git
   cd linkedin-connection-remover
   ```
2. Install the required libraries:
   ```bash
   pip install selenium python-dotenv
   ```
3. Set up a `.env` file in the project directory with your LinkedIn login credentials:
   ```bash
   EMAIL=your_email@example.com
   PASSWORD=your_password
   ```
4. Run the script:
   ```bash
   python app.py
   ```
5. Sit back as the script removes connections one-by-one.
