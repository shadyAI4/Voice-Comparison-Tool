# import wave
# import contextlib
#
#
# def extract_wav_metadata(audio_file_path):
#     metadata = {}
#
#     with contextlib.closing(wave.open(audio_file_path, 'rb')) as wav_file:
#         metadata['nchannels'] = wav_file.getnchannels()
#         metadata['sampwidth'] = wav_file.getsampwidth()
#         metadata['framerate'] = wav_file.getframerate()
#         metadata['nframes'] = wav_file.getnframes()
#         metadata['comptype'] = wav_file.getcomptype()
#         metadata['compname'] = wav_file.getcompname()
#         duration = wav_file.getnframes() / wav_file.getframerate()
#         metadata['duration'] = duration
#
#     return metadata
#
#
# audio_file_path = '/home/shadyai/PycharmProjects/pyqtProject1/ui/suspect.wav'
# metadata = extract_wav_metadata(audio_file_path)
#
# if metadata:
#     print("Metadata found in the WAV file:")
#     for key, value in metadata.items():
#         print(f"{key}: {value}")
# else:
#     print("No metadata available in the WAV file.")


import wave
import contextlib


# def extract_wav_metadata(audio_file_path):
#     metadata = {}
#
#     with contextlib.closing(wave.open(audio_file_path, 'rb')) as wav_file:
#         metadata['nchannels'] = wav_file.getnchannels()
#         metadata['sampwidth'] = wav_file.getsampwidth()
#         metadata['framerate'] = wav_file.getframerate()
#         metadata['nframes'] = wav_file.getnframes()
#         metadata['comptype'] = wav_file.getcomptype()
#         metadata['compname'] = wav_file.getcompname()
#         duration = wav_file.getnframes() / wav_file.getframerate()
#         metadata['duration'] = duration
#
#     return metadata
#
#
# audio_file_path = '/home/shadyai/PycharmProjects/pyqtProject1/ui/suspect.wav'
# metadata = extract_wav_metadata(audio_file_path)
#
# if metadata:
#     print("Metadata found in the WAV file:")
#     for key, value in metadata.items():
#         print(f"{key}: {value}")
# else:
#     print("No metadata available in the WAV file.")




# from mutagen import File
#
# # Load the audio file
# audio = File('/home/shadyai/PycharmProjects/pyqtProject1/ui/Dizasta Vina Feat. J cob - Top Shelf.mp3')
#
# # Check if tags are available
# if audio.tags:
#     # Print all metadata
#     for tag in audio.tags.keys():
#         print(f"{tag}: {audio.tags[tag]}")
# else:
#     print("No tags found in the audio file.")







# import os
# import hashlib
# from datetime import datetime
# from pydub.utils import mediainfo
# from mutagen import File
#
# # Function to get file hash
# def get_file_hash(file_path, hash_function='md5'):
#     hash_func = getattr(hashlib, hash_function)()
#     with open(file_path, 'rb') as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_func.update(chunk)
#     return hash_func.hexdigest()
#
# # Function to get file timestamps
# def get_file_timestamps(file_path):
#     stats = os.stat(file_path)
#     creation_time = datetime.fromtimestamp(stats.st_ctime)
#     modification_time = datetime.fromtimestamp(stats.st_mtime)
#     return creation_time, modification_time
#
# # File path
# file_path = '/home/shadyai/PycharmProjects/pyqtProject1/ui/suspect.wav'
#
# # Get basic file metadata using pydub
# info = mediainfo(file_path)
#
# # Get file hash
# file_hash = get_file_hash(file_path)
#
# # Get file timestamps
# creation_time, modification_time = get_file_timestamps(file_path)
#
# # Load the audio file with mutagen to get more metadata if available
# audio = File(file_path)
#
# # Print collected metadata
# print(f"File Format: {info.get('format_name')}")
# print(f"Codec: {info.get('codec_name')}")
# print(f"Bit Rate: {info.get('bit_rate')}")
# print(f"Sample Rate: {info.get('sample_rate')}")
# print(f"Channels: {info.get('channels')}")
# print(f"File Hash (MD5): {file_hash}")
# print(f"Creation Time: {creation_time}")
# print(f"Modification Time: {modification_time}")
#
# # Print additional metadata from mutagen if available
# if audio:
#     print("Additional Metadata:")
#     for tag in audio.tags.keys():
#         print(f"{tag}: {audio.tags[tag]}")
# else:
#     print("No additional metadata found with mutagen.")
#



# import wave
#
# def get_device_info(file_path):
#     try:
#         with wave.open(file_path, 'rb') as wf:
#             metadata = {
#                 "channels": wf.getnchannels(),
#                 "sample_width": wf.getsampwidth(),
#                 "frame_rate": wf.getframerate(),
#                 "frame_count": wf.getnframes(),
#                 # Add more metadata fields as needed
#             }
#             return metadata
#     except Exception as e:
#         print("Error:", e)
#         return None
#
# # Usage example
# file_path = "/home/shadyai/PycharmProjects/pyqtProject1/ui/suspect.wav"
# device_info = get_device_info(file_path)
# if device_info:
#     print("Device Information:")
#     for key, value in device_info.items():
#         print(f"{key}: {value}")


# import eyed3
#
# audi2 =eyed3.load('/home/shadyai/PycharmProjects/pyqtProject1/ui/fake.mp3')
#
# print(dir(audi2.tag))




# import pyaudio
#
# def get_recording_device_info():
#     p = pyaudio.PyAudio()
#     info = p.get_host_api_info_by_index(0)
#     num_devices = info.get('deviceCount')
#
#     device_info = []
#
#     for i in range(num_devices):
#         device = p.get_device_info_by_host_api_device_index(0, i)
#         if device.get('maxInputChannels') > 0:  # Check if it's an input (recording) device
#             device_info.append({
#                 'name': device.get('name'),
#                 'manufacturer': device.get('manufacturer'),
#                 'model': device.get('model')
#             })
#
#     p.terminate()
#     return device_info
#
# if __name__ == "__main__":
#     recording_devices = get_recording_device_info()
#     print("Recording Devices:")
#     for i, device in enumerate(recording_devices, start=1):
#         print(f"Device {i}:")
#         print(f"Name: {device['name']}")
#         print(f"Manufacturer: {device['manufacturer']}")
#         print(f"Model: {device['model']}")
#         print()


#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView
from os import path

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setWindowTitle("PDF Viewer")
        self.setGeometry(0, 28, 1000, 750)
        self.centralWidget = QWidget(self)

        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.webView.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.setCentralWidget(self.webView)

    def url_changed(self):
        self.setWindowTitle(self.webView.title())

    def go_back(self):
        self.webView.back()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    if len(sys.argv) > 1:
        win.webView.setUrl(QUrl(f"file://{sys.argv[1]}"))
    else:
        wd = path.dirname(sys.argv[0])
        test_pdf = "test.pdf"
        win.webView.setUrl(QUrl(f"file://{wd}/{test_pdf}"))
    sys.exit(app.exec_())