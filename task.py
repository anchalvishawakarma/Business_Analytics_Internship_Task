import random
import matplotlib.pyplot as plt
import seaborn as sns

# Create dummy data: random messages with sentiment scores
dummy_data = [
    {"message": "Stock X is rising fast! Everyone should buy.", "sentiment": random.uniform(0.5, 1)},
    {"message": "Stock Y is crashing. It's a disaster!", "sentiment": random.uniform(-1, -0.5)},
    {"message": "Stock Z is stable for now. No significant changes.", "sentiment": random.uniform(-0.1, 0.1)},
    {"message": "Stock A looks promising. Many are expecting a big jump.", "sentiment": random.uniform(0.3, 0.7)},
    {"message": "Stock B is unpredictable. It's very volatile these days.", "sentiment": random.uniform(-0.2, 0.2)},
    # Add more dummy data as needed
]

# Print the dummy data
for entry in dummy_data:
    print(f"Message: {entry['message']} | Sentiment Score: {entry['sentiment']}")
# Extract the sentiment scores from the dummy data
sentiment_scores = [entry['sentiment'] for entry in dummy_data]

# Plot the sentiment score distribution
plt.figure(figsize=(8, 6))
sns.histplot(sentiment_scores, bins=10, kde=True)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()
# Analyze positive, negative, and neutral sentiment messages
positive_messages = [entry['message'] for entry in dummy_data if entry['sentiment'] > 0.2]
negative_messages = [entry['message'] for entry in dummy_data if entry['sentiment'] < -0.2]
neutral_messages = [entry['message'] for entry in dummy_data if -0.2 <= entry['sentiment'] <= 0.2]

print("Positive Messages:")
for msg in positive_messages:
    print(f"- {msg}")

print("\nNegative Messages:")
for msg in negative_messages:
    print(f"- {msg}")

print("\nNeutral Messages:")
for msg in neutral_messages:
    print(f"- {msg}")
