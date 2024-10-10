from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Your Telegram API credentials
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE_NUMBER'
channel_username = 'CHANNEL_USERNAME_OR_ID'  # The username or ID of the Telegram channel

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Connect to the client
client.connect()

# Authenticate if not already done
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

# Function to scrape messages from the Telegram channel
def scrape_channel(channel, limit=100):
    messages = []
    history = client(GetHistoryRequest(
        peer=channel,
        offset_id=0,
        offset_date=None,
        add_offset=0,
        limit=limit,
        max_id=0,
        min_id=0,
        hash=0
    ))

    for message in history.messages:
        if message.message:  # Exclude empty messages
            messages.append(message.message)
    return messages

# Fetch the target channel
channel = client.get_entity(channel_username)

# Scrape messages from the Telegram channel
messages = scrape_channel(channel)

# Create a DataFrame from the scraped messages
df = pd.DataFrame(messages, columns=['Message'])

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Perform sentiment analysis on each message
df['Sentiment'] = df['Message'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# Save the DataFrame with messages and sentiment scores to a CSV file
df.to_csv('telegram_sentiment.csv', index=False)
print("Scraping and sentiment analysis completed, saved to telegram_sentiment.csv")

# Visualize the sentiment distribution
sns.histplot(df['Sentiment'], kde=True)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Close the Telegram client connection
client.disconnect()
