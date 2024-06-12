from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Define paths to the real and test audio files
real_audio_path = Path("/home/shadyai/PycharmProjects/pyqtProject1/ui/real.mp3")
test_audio_path = Path("/home/shadyai/PycharmProjects/pyqtProject1/ui/lug1.wav")

# Load and preprocess the audio
real_wav = preprocess_wav(real_audio_path)
test_wav = preprocess_wav(test_audio_path)

# Initialize the VoiceEncoder
encoder = VoiceEncoder()

# Compute embeddings
real_embed = encoder.embed_utterance(real_wav)
test_embed = encoder.embed_utterance(test_wav)

# Compute similarity
similarity = np.dot(real_embed, test_embed)

# Define a threshold for determining if the voice is real or fake
# Note: The threshold value (e.g., 0.84) may need to be adjusted based on your specific use case and data
threshold = 0.84

# Determine if the test voice is real or fake
is_real = similarity > threshold
result = "Real" if is_real else "Fake"

# Print the similarity score and the result
print(f"Similarity score: {similarity}")
print(f"The test voice is: {result}")

# Optionally, visualize the similarity score
plt.figure(figsize=(6, 3))
plt.bar(["Similarity"], [similarity], color="blue" if is_real else "red")
plt.axhline(threshold, ls="dashed", label="Prediction threshold", c="black")
plt.ylim(0, 1)
plt.legend()
plt.ylabel("Similarity")
plt.title("Voice Similarity")
plt.show()
