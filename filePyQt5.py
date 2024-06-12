import csv
import os

import librosa
import numpy as np
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QTimer, Qt, QUrl
from PySide2.QtGui import QColor
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QVBoxLayout, QWidget, QFileDialog, QMainWindow, QApplication, QGraphicsDropShadowEffect, \
    QMessageBox, QLabel, QTextEdit
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from reportlab.lib.units import inch
from scipy.io import wavfile
from scipy.signal import spectrogram
from df.enhance import enhance, init_df, load_audio, save_audio
from df.utils import download_file
from datetime import datetime
import pyqtgraph as pg
from mutagen import File
from pydub.utils import mediainfo
import hashlib

from pydub import AudioSegment

import new

import main

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle, SimpleDocTemplate, Image, Spacer
from reportlab.lib import colors

from resemblyzer import preprocess_wav, VoiceEncoder
from pydub import AudioSegment
import argparse
import pydub
import random
import os
import sys
import time
from colorama import *
import main_home
from welcome import Ui_SplashScreen
from loader import Ui_SplashScreen as Loader_UI
from loader_dialog import Ui_Dialog

# import new

counter = 0
jumper = 10


class MainHome(new.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainHome, self).__init__()
        self.setupUi(self)

        # ************************* DEFINING VARIOUS BUTTON ACTIONS AND CONNECT THEM TO THE FUNCTION HANDLEER********************************************

        self.pushButton.clicked.connect(self.upload_crime_voice)
        self.pushButton_2.clicked.connect(self.upload_suspect_voice)
        self.pushButton_3.clicked.connect(self.process_and_display_results)
        self.pushButton_8.clicked.connect(self.process_and_filter_voice_clips)
        self.pushButton_34.clicked.connect(self.upload_page)
        self.pushButton_35.clicked.connect(self.home_page)
        self.pushButton_9.clicked.connect(self.authenticate_page)
        # Connect play and stop buttons to their respective functions
        self.pushButton_6.clicked.connect(self.play_audio_supect)
        self.pushButton_7.clicked.connect(self.stop_audio_suspect)

        self.pushButton_4.clicked.connect(self.play_audio)
        self.pushButton_5.clicked.connect(self.stop_audio)
        self.pushButton_14.clicked.connect(self.filter_page)

        self.pushButton_10.clicked.connect(self.play_audio_filter)
        self.pushButton_11.clicked.connect(self.stop_audio_filter)
        self.pushButton_13.clicked.connect(self.play_audio_supect_filter)
        self.pushButton_12.clicked.connect(self.stop_audio_suspect_filter)
        self.pushButton_15.clicked.connect(self.send_data_to_compare)
        self.pushButton_21.clicked.connect(self.compare_page)
        self.pushButton_16.clicked.connect(self.genarate_report_page)
        self.pushButton_18.clicked.connect(self.genarate_report_page)
        self.pushButton_20.clicked.connect(self.report_button_page)

        self.pushButton_24.clicked.connect(self.single_speaker_selection)
        self.pushButton_25.clicked.connect(self.mult_speaker_selection)
        self.pushButton_26.clicked.connect(self.upload_audio_trim)
        self.pushButton_27.clicked.connect(self.play_audio_trim)
        self.pushButton_28.clicked.connect(self.pause_audio_trim)
        self.pushButton_29.clicked.connect(self.trim_audio)
        self.pushButton_30.clicked.connect(self.single_speaker_selection)


        self.pushButton_33.clicked.connect(self.authenticate_page)
        self.pushButton_31.clicked.connect(self.show_uploaded_clips)
        self.pushButton_32.clicked.connect(self.metadata_page)

        self.pushButton_18.clicked.connect(self.view_report)

        # ***************************** CREATING FIGURES FOR DATA WITH NOISE*************************************************************************************?????????????

        self.figure_waveform_crime = Figure()
        self.canvas_waveform_crime = FigureCanvas(self.figure_waveform_crime)
        self.figure_waveform_crime.set_size_inches(10, 6)
        self.gridLayout_6.addWidget(self.create_canvas_widget(self.canvas_waveform_crime))
        # self.gridLayout_10.addWidget(self.create_canvas_widget(self.canvas_waveform_crime))

        self.figure_spectrogram_crime = Figure()
        self.canvas_spectrogram_crime = FigureCanvas(self.figure_spectrogram_crime)
        self.figure_spectrogram_crime.set_size_inches(10, 6)
        self.gridLayout_8.addWidget(self.canvas_spectrogram_crime)
        # self.gridLayout_11.addWidget(self.canvas_spectrogram_crime)

        self.figure_waveform_suspect = Figure()
        self.canvas_waveform_suspect = FigureCanvas(self.figure_waveform_suspect)
        self.figure_waveform_suspect.set_size_inches(10, 6)
        self.gridLayout_7.addWidget(self.canvas_waveform_suspect)

        self.figure_spectrogram_suspect = Figure()
        self.canvas_spectrogram_suspect = FigureCanvas(self.figure_spectrogram_suspect)
        self.figure_spectrogram_suspect.set_size_inches(10, 6)
        self.gridLayout_9.addWidget(self.canvas_spectrogram_suspect)

        # ***************************** CREATING FIGURES FOR DATA WITHOUT NOISE*************************************************************************************?????????????

        self.figure_waveform_crime1 = Figure()
        self.canvas_waveform_crime1 = FigureCanvas(self.figure_waveform_crime1)
        self.figure_waveform_crime1.set_size_inches(10, 6)
        self.gridLayout_20.addWidget(self.create_canvas_widget(self.canvas_waveform_crime1))

        self.figure_spectrogram_crime1 = Figure()
        self.canvas_spectrogram_crime1 = FigureCanvas(self.figure_spectrogram_crime1)
        self.figure_spectrogram_crime1.set_size_inches(10, 6)
        self.gridLayout_21.addWidget(self.canvas_spectrogram_crime1)

        self.figure_waveform_suspect1 = Figure()
        self.canvas_waveform_suspect1 = FigureCanvas(self.figure_waveform_suspect1)
        self.figure_waveform_suspect1.set_size_inches(10, 6)
        self.gridLayout_22.addWidget(self.canvas_waveform_suspect1)

        self.figure_spectrogram_suspect1 = Figure()
        self.canvas_spectrogram_suspect1 = FigureCanvas(self.figure_spectrogram_suspect1)
        self.figure_spectrogram_suspect1.set_size_inches(10, 6)
        self.gridLayout_23.addWidget(self.canvas_spectrogram_suspect1)

        # ************************************************* CREATING MEDIA PLAYERS***********************************************************************

        self.media_player = QMediaPlayer()
        self.media_player.setVolume(70)  # Set initial volume to 50%

        self.media_player_suspect = QMediaPlayer()
        self.media_player_suspect.setVolume(70)  # Set initial volume to 50%
        # *********************************************** DEFINING FILE NAMES *****************************************************************************
        self.crime_filename = None
        self.suspect_filename = None
        self.enhanced_crime = None
        self.enhanced_suspect = None
        self.GetSimilarity = None

        self.case_number_line6 = None
        self.investigator_name_line5 = None
        self.suspect_name_line8 = None
        self.date_and_time_of_case = None
        self.device_name_line9 = None
        self.crime_scene_location_line11 = None
        self.crime_audio_name_line10 = None
        self.crime_file_format = None
        self.suspect_audio_name_line12 = None
        self.suspect_audio_format_combo2 = None
        self.date_and_time_of_acquisition_Date2 = None
        self.conclusion_word = None

        # THIS ARE THE METADATA VALUES OF CRIME
        self.sample_rate = None
        self.bit_rate = None
        self.file_format = None
        self.audio_channel = None
        self.codec_information = None
        self.hash_value = None
        self.creation_time_stamp = None
        self.modification_time_stamp = None
        self.digital_watermark = None
        self.gps_info = None
        self.device_specific_meta_data = None

        # THIS ARE THE METADATA VALUES OF SUSPECT
        self.sample_rate_suspect = None
        self.bit_rate_suspect = None
        self.file_format_suspect = None
        self.audio_channel_suspect = None
        self.codec_information_suspect = None
        self.hash_value_suspect = None
        self.creation_time_stamp_suspect = None
        self.modification_time_stamp_suspect = None
        self.digital_watermark_suspect = None
        self.gps_info_suspect = None
        self.device_specific_meta_data_suspect = None

        self.title_label = QLabel("<h1>Forensic Voice Comparison Report</h1>")
        self.gridLayout_18.addWidget(self.title_label)
        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.web_view)
        # self.widget_10.setLayout(self.layout)

        self.report_text_edit = QTextEdit()
        self.report_text_edit.setReadOnly(True)
        self.gridLayout_18.addWidget(self.report_text_edit)

        # WAVE FORM TIMER

        self.media_player = QMediaPlayer(self)
        self.media_player.setVolume(50)
        self.media_player.mediaStatusChanged.connect(self.update_waveform)

        self.waveform_plot = pg.PlotWidget()
        self.waveform_plot.showGrid(x=True, y=True)
        self.waveform_plot.setLabel("left", "Amplitude")
        self.waveform_plot.setLabel("bottom", "Time (s)")
        self.layout_waveform = QVBoxLayout()
        self.layout_waveform.addWidget(self.waveform_plot)
        self.widget_16.setLayout(self.layout_waveform)

        self.trim_start = 0
        self.trim_end = 0
        self.playback_line = None
        self.region = pg.LinearRegionItem([0, 0])  # Initialize the region for trimming
        self.region.sigRegionChangeFinished.connect(self.update_trim_region)

        self.selected_audio = None  # Store the selected audio

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_waveform)
        self.timer.start(100)

    def create_canvas_widget(self, canvas):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(canvas)
        return widget

    def single_speaker_selection(self):
        self.pushButton_37.setStyleSheet(u"background-color: #14213d;\n"
                                         "color: rgb(255, 255, 255);")
        self.stackedWidget.setCurrentIndex(2)
    def mult_speaker_selection(self):
        self.stackedWidget.setCurrentIndex(1)
    def upload_audio_trim(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
        if file_path:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))

    def play_audio_trim(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def pause_audio_trim(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()

    def trim_audio(self):
        file_path = self.media_player.media().canonicalUrl().toLocalFile()
        if not file_path:
            QMessageBox.warning(self, "No Audio File", "Please select an audio file to trim.")
            return

        audio = AudioSegment.from_file(file_path)

        start_time = self.region.getRegion()[0] * 1000  # Convert to milliseconds
        end_time = self.region.getRegion()[1] * 1000  # Convert to milliseconds

        trimmed_audio = audio[start_time:end_time]

        output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
        if output_file_path:
            output_format = os.path.splitext(output_file_path)[1][
                            1:].lower()  # Get the file extension for output format
            if output_format in ['mp3', 'wav']:
                trimmed_audio.export(output_file_path, format=output_format)  # Export audio with specified format
            else:
                QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")

    def update_waveform(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            position = self.media_player.position() / 1000  # Convert to seconds
            duration = self.media_player.duration() / 1000  # Convert to seconds
            self.waveform_plot.clear()
            self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))

            # Draw a line indicating the playback position
            if self.playback_line:
                self.waveform_plot.removeItem(self.playback_line)
            self.playback_line = self.waveform_plot.plot([position, position], [-1, 1], pen=pg.mkPen("r", width=2))

            self.waveform_plot.addItem(self.region)  # Add the region item for trimming
            self.region.setRegion([self.trim_start, self.trim_end])  # Set the region based on trim start and end

    def update_trim_region(self):
        region = self.region.getRegion()
        self.trim_start = region[0]
        self.trim_end = region[1]

        if self.selected_audio is not None:
            self.selected_audio.close()

        file_path = self.media_player.media().canonicalUrl().toLocalFile()
        audio = AudioSegment.from_file(file_path)
        start_time = int(region[0] * 1000)  # Convert to milliseconds
        end_time = int(region[1] * 1000)  # Convert to milliseconds
        self.selected_audio = audio[start_time:end_time]

        self.media_player.setPosition(start_time)
        self.media_player.play()

    def upload_crime_voice(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Audio Files (*.mp3 *.wav *.aac *.m4a)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.crime_filename = selected_files[0]
                file_name = os.path.basename(self.crime_filename)  # Get the base name of the file
                self.label_9.setText(file_name)
                # Process the uploaded crime voice file, e.g., save it or perform further actions

    def upload_suspect_voice(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Audio Files (*.mp3 *.wav *.aac *.m4a)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.suspect_filename = selected_files[0]
                file_name = os.path.basename(self.suspect_filename)  # Get the base name of the file
                self.label_10.setText(file_name)  # Update the label with the file name
                # return file_path
                # Process the uploaded suspect voice file, e.g., save it or perform further actions

    def home_page(self):
        self.pushButton_37.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stackedWidget.setCurrentIndex(0)

    def upload_page(self):
        self.pushButton_17.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stop_audio()
        self.stop_audio_suspect()
        self.stackedWidget.setCurrentIndex(2)

    def metadata_page(self):
        # self.pushButton_17.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
        #                                  "color: rgb(255, 255, 255);")
        self.pushButton_38.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stop_audio()
        self.stop_audio_suspect()
        self.stackedWidget.setCurrentIndex(3)


    def filter_page(self):
        self.pushButton_19.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stop_audio_filter()
        self.stop_audio_suspect_filter()
        self.stackedWidget.setCurrentIndex(5)

    def compare_page(self):
        self.pushButton_22.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stackedWidget.setCurrentIndex(6)

    def report_button_page(self):
        self.pushButton_23.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stackedWidget.setCurrentIndex(7)

    def process_and_display_results(self):
        self.case_number_line6 = self.lineEdit_6.text().strip()
        self.investigator_name_line5 = self.lineEdit_5.text().strip()
        self.suspect_name_line8 = self.lineEdit_8.text().strip()
        self.date_and_time_of_case = self.dateTimeEdit.dateTime()
        self.date_and_time_of_case = self.date_and_time_of_case.toString('yyyy-MM-dd HH:mm:ss')
        self.device_name_line9 = self.lineEdit_9.text().strip()
        self.crime_scene_location_line11 = self.lineEdit_11.text().strip()
        self.crime_audio_name_line10 = self.lineEdit_10.text().strip()
        self.crime_file_format = self.comboBox.currentText()
        self.suspect_audio_name_line12 = self.lineEdit_12.text().strip()
        self.suspect_audio_format_combo2 = self.comboBox_2.currentText()
        self.date_and_time_of_acquisition_Date2 = self.dateTimeEdit_2.dateTime()
        self.date_and_time_of_acquisition_Date2 = self.date_and_time_of_acquisition_Date2.toString('yyyy-MM-dd HH:mm:ss')
        print(self.date_and_time_of_case)
        print(self.crime_file_format)
        print(self.case_number_line6)
        if self.crime_filename and self.suspect_filename:
            print(self.crime_filename)
            self.pushButton_17.setStyleSheet(u"background-color: #14213d;\n"
                                             "color: rgb(255, 255, 255);")
            self.stackedWidget.setCurrentIndex(3)  # Switch to page_2 of the stacked widget
            crime_voice_path = self.crime_filename
            suspect_voice_path = self.suspect_filename
            self.get_audio_clips_metadata(crime_voice_path, suspect_voice_path)
            # self.show_uploaded_clips(crime_voice_path, suspect_voice_path)
    def get_audio_clips_metadata(self,crime_file, suspect_file, hash_function='md5'):
        hash_func1 = getattr(hashlib, hash_function)()
        with open(crime_file, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func1.update(chunk)
        stats = os.stat(crime_file)
        self.creation_time_stamp = datetime.fromtimestamp(stats.st_ctime)
        self.modification_time_stamp = datetime.fromtimestamp(stats.st_mtime)
        info = mediainfo(crime_file)
        self.audio_channel = info.get('channels')
        self.sample_rate = info.get('sample_rate')
        self.bit_rate = info.get('bit_rate')
        self.codec_information = info.get('codec_name')
        self.file_format = info.get('format_name')
        self.hash_value = hash_func1.hexdigest()

    #     SUSPECT METADATA
        hash_func2 = getattr(hashlib, hash_function)()
        with open(suspect_file, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func2.update(chunk)
        stats = os.stat(suspect_file)
        self.creation_time_stamp_suspect = datetime.fromtimestamp(stats.st_ctime)
        self.modification_time_stamp_suspect = datetime.fromtimestamp(stats.st_mtime)
        info = mediainfo(suspect_file)
        self.audio_channel_suspect = info.get('channels')
        self.sample_rate_suspect = info.get('sample_rate')
        self.bit_rate_suspect = info.get('bit_rate')
        self.codec_information_suspect = info.get('codec_name')
        self.file_format_suspect = info.get('format_name')
        self.hash_value_suspect = hash_func2.hexdigest()

        self.label_39.setText(str(self.file_format))
        self.label_40.setText(str(self.hash_value))
        self.label_41.setText(str(self.creation_time_stamp))
        self.label_42.setText(str(self.bit_rate)+'bps')
        self.label_43.setText(str(self.sample_rate)+'Hz')
        # for suspect
        self.label_49.setText(str(self.file_format_suspect))
        self.label_51.setText(str(self.hash_value_suspect))
        self.label_53.setText(str(self.creation_time_stamp_suspect))
        self.label_55.setText(str(self.bit_rate_suspect)+"bps")
        self.label_57.setText(str(self.sample_rate_suspect)+'Hz')
    def authenticate_page(self):
        self.pushButton_38.setStyleSheet(u"background-color: #14213d;\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_39.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stackedWidget.setCurrentIndex(4)
    def show_uploaded_clips(self):
        self.pushButton_39.setStyleSheet(u"background-color: #14213d;\n"
                                         "color: rgb(255, 255, 255);")
        self.stackedWidget.setCurrentIndex(5)
        # self.pushButton_17.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
        #                                  "color: rgb(255, 255, 255);")
        crime_voice_path = self.crime_filename  # Replace with actual file path
        suspect_voice_path = self.suspect_filename  # Replace with actual file path
        print("Crime Screen Path", crime_voice_path)
        audio_data_crime, sample_rate_crime = librosa.load(crime_voice_path, sr=None)
        audio_data_suspect, sample_rate_suspect = librosa.load(suspect_voice_path, sr=None)

        # audio_data_crime, sample_rate_crime = wavfile.read(crime_voice_path)
        print("Audio Data Type:", type(audio_data_crime))  # Print data type for debugging
        print("Sample Rate Type:", type(sample_rate_crime))  # Print sample rate type for debugging
        print("Audio Data Length:", len(audio_data_crime))  # Print data length for debugging
        print("Sample Rate:", sample_rate_crime)  # Print sample rate for debugging
        ax_waveform = self.figure_waveform_crime.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
        ax_waveform.clear()
        ax_waveform.set_title('Waveform')
        ax_waveform.plot(np.arange(len(audio_data_crime)) / sample_rate_crime, audio_data_crime)
        ax_waveform.set_xlabel('Time (s)')
        ax_waveform.set_ylabel('Amplitude')

        ax_spectrogram = self.figure_spectrogram_crime.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
        ax_spectrogram.clear()
        ax_spectrogram.set_title('Spectrogram')
        f, t, Sxx = spectrogram(audio_data_crime, sample_rate_crime)
        ax_spectrogram.pcolormesh(t, f, np.log(Sxx))
        ax_spectrogram.set_ylabel('Frequency [Hz]')
        ax_spectrogram.set_xlabel('Time [sec]')

        self.canvas_waveform_crime.draw()
        self.canvas_spectrogram_crime.draw()

        #     PLOTTING THE PLOTS FOR SUPSECT VOICE
        ax_waveform1 = self.figure_waveform_suspect.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
        ax_waveform1.clear()
        ax_waveform1.set_title('Waveform')
        ax_waveform1.plot(np.arange(len(audio_data_suspect)) / sample_rate_suspect, audio_data_suspect)
        ax_waveform1.set_xlabel('Time (s)')
        ax_waveform1.set_ylabel('Amplitude')

        ax_spectrogram1 = self.figure_spectrogram_suspect.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
        ax_spectrogram1.clear()
        ax_spectrogram1.set_title('Spectrogram')
        f, t, Sxx = spectrogram(audio_data_suspect, sample_rate_suspect)
        ax_spectrogram1.pcolormesh(t, f, np.log(Sxx))
        ax_spectrogram1.set_ylabel('Frequency [Hz]')
        ax_spectrogram1.set_xlabel('Time [sec]')

        self.canvas_waveform_suspect.draw()
        self.canvas_spectrogram_suspect.draw()

    # ****************************  BELOW ARE THE BUTTONS FOR PLAYING NON FILTERED DATA ******************************
    def play_audio(self):
        if self.crime_filename:
            wav_filename = os.path.splitext(self.crime_filename)[0] + '.wav'
            audio = AudioSegment.from_file(self.crime_filename)
            audio.export(wav_filename, format='wav')
            media_content = QMediaContent(QUrl.fromLocalFile(wav_filename))
            self.media_player.setMedia(media_content)
            self.media_player.play()

    def stop_audio(self):
        self.media_player.stop()

    def play_audio_supect(self):
        if self.suspect_filename:
            wav_filename = os.path.splitext(self.suspect_filename)[0] + '.wav'
            audio = AudioSegment.from_file(self.suspect_filename)
            audio.export(wav_filename, format='wav')
            media_content = QMediaContent(QUrl.fromLocalFile(wav_filename))
            self.media_player_suspect.setMedia(media_content)
            self.media_player_suspect.play()

    def stop_audio_suspect(self):
        self.media_player_suspect.stop()

    #     ******************************************** BELOW IS FOR PLAYING AND STOPING FILTERED DATA *******************************
    def play_audio_filter(self):
        if self.enhanced_crime:
            # Load the audio file and play it
            media_content = QMediaContent(QUrl.fromLocalFile(self.enhanced_crime))
            self.media_player.setMedia(media_content)
            self.media_player.play()

    def stop_audio_filter(self):
        self.media_player.stop()

    def play_audio_supect_filter(self):
        if self.enhanced_suspect:
            # Load the audio file and play it
            media_content = QMediaContent(QUrl.fromLocalFile(self.enhanced_suspect))
            self.media_player_suspect.setMedia(media_content)
            self.media_player_suspect.play()

    def stop_audio_suspect_filter(self):
        self.media_player_suspect.stop()

    def process_and_filter_voice_clips(self):
        if self.crime_filename and self.suspect_filename:
            # self.progressBar.setValue(100)
            self.pushButton_19.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
                                             "color: rgb(255, 255, 255);")
            self.stop_audio()
            self.stop_audio_suspect()
            self.pushButton_19.setStyleSheet(u"background-color: #14213d;\n"
                                             "color: rgb(255, 255, 255);")
            self.stackedWidget.setCurrentIndex(6)  # Switch to page_2 of the stacked widget
            crime_voice_path = self.crime_filename
            suspect_voice_path = self.suspect_filename
            print("yeaaaaa", crime_voice_path)
            model, df_state, _ = init_df()

            audio_crime, _ = load_audio(crime_voice_path, sr=df_state.sr())
            audio_suspect, _ = load_audio(suspect_voice_path, sr=df_state.sr())
            enhanced_crime_data = enhance(model, df_state, audio_crime)
            enhanced_suspect_data = enhance(model, df_state, audio_suspect)

            enhanced_crime_file = "enhanced_crime.wav"
            enhanced_suspect_file = "enhanced_suspect.wav"

            # Set the enhanced_crime variable to the path of the saved file
            self.enhanced_crime = os.path.abspath(enhanced_crime_file)
            self.enhanced_suspect = os.path.abspath(enhanced_suspect_file)
            # self.enhanced_crime = enhance(model, df_state, audio_crime)
            # self.enhanced_suspect = enhance(model, df_state, audio_suspect)
            save_audio(enhanced_crime_file, enhanced_crime_data, df_state.sr())
            # print("Weeeeeee", self.enhanced_crime)
            save_audio(enhanced_suspect_file, enhanced_suspect_data, df_state.sr())
            audio_data_crime, sample_rate_crime = librosa.load(self.enhanced_crime, sr=None)
            audio_data_suspect, sample_rate_suspect = librosa.load(self.enhanced_suspect, sr=None)

            # audio_data_crime, sample_rate_crime = wavfile.read(crime_voice_path)
            print("Audio Data Type:", type(audio_data_crime))  # Print data type for debugging
            print("Sample Rate Type:", type(sample_rate_crime))  # Print sample rate type for debugging
            print("Audio Data Length:", len(audio_data_crime))  # Print data length for debugging
            print("Sample Rate:", sample_rate_crime)  # Print sample rate for debugging
            ax_waveform = self.figure_waveform_crime1.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
            ax_waveform.clear()
            ax_waveform.set_title('Waveform')
            ax_waveform.plot(np.arange(len(audio_data_crime)) / sample_rate_crime, audio_data_crime)
            ax_waveform.set_xlabel('Time (s)')
            ax_waveform.set_ylabel('Amplitude')

            ax_spectrogram = self.figure_spectrogram_crime1.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
            ax_spectrogram.clear()
            ax_spectrogram.set_title('Spectrogram')
            f, t, Sxx = spectrogram(audio_data_crime, sample_rate_crime)
            ax_spectrogram.pcolormesh(t, f, np.log(Sxx))
            ax_spectrogram.set_ylabel('Frequency [Hz]')
            ax_spectrogram.set_xlabel('Time [sec]')

            self.canvas_waveform_crime1.draw()
            self.canvas_spectrogram_crime1.draw()

            #     PLOTTING THE PLOTS FOR SUPSECT VOICE
            ax_waveform1 = self.figure_waveform_suspect1.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
            ax_waveform1.clear()
            ax_waveform1.set_title('Waveform')
            ax_waveform1.plot(np.arange(len(audio_data_suspect)) / sample_rate_suspect, audio_data_suspect)
            ax_waveform1.set_xlabel('Time (s)')
            ax_waveform1.set_ylabel('Amplitude')

            ax_spectrogram1 = self.figure_spectrogram_suspect1.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
            ax_spectrogram1.clear()
            ax_spectrogram1.set_title('Spectrogram')
            f, t, Sxx = spectrogram(audio_data_suspect, sample_rate_suspect)
            ax_spectrogram1.pcolormesh(t, f, np.log(Sxx))
            ax_spectrogram1.set_ylabel('Frequency [Hz]')
            ax_spectrogram1.set_xlabel('Time [sec]')

            self.canvas_waveform_suspect.draw()
            self.canvas_spectrogram_suspect.draw()

    def send_data_to_compare(self):
        if self.enhanced_crime and self.enhanced_suspect:

            self.compareSounds(self.enhanced_crime, self.enhanced_suspect)

    def compareSounds(self, sound_1_path, sound_2_path):
        self.pushButton_22.setStyleSheet(u"background-color: #14213d;\n"
                                         "color: rgb(255, 255, 255);")
        self.stop_audio_suspect_filter()
        self.stop_audio_filter()
        self.stackedWidget.setCurrentIndex(7)
        sound_encoder = VoiceEncoder(verbose=False)
        file_1 = preprocess_wav(sound_1_path)
        file_2 = preprocess_wav(sound_2_path)

        encoded_sound1 = sound_encoder.embed_utterance(file_1)
        encoded_sound2 = sound_encoder.embed_utterance(file_2)
        print("THis is the sound one", encoded_sound1)
        print("THis is the sound two", encoded_sound2)
        dot_product_size = np.dot(encoded_sound1, encoded_sound2)
        norm_sound1 = np.linalg.norm(encoded_sound1)
        norm_sound2 = np.linalg.norm(encoded_sound2)

        # kosinus benzerliğini hesaplama
        self.GetSimilarity = round(dot_product_size / (norm_sound1 * norm_sound2),2)
        self.label_15.setText(str(self.GetSimilarity))

        if(0<= self.GetSimilarity < 0.3):
            self.conclusion_word =f"Based on the likelihood ratio {round(self.GetSimilarity,2)}The analysis indicates that it is highly unlikely that the speakers are the same person."
            self.label_79.setText(f"Based on the likelihood ratio {round(self.GetSimilarity,2)}The analysis indicates that it is highly unlikely that the speakers are the same person.")
        if (0.3 <= self.GetSimilarity < 0.7):
            self.conclusion_word=f"Based on the likelihood ratio {round(self.GetSimilarity,2)} Evidence suggests the speakers are likely different."
            self.label_79.setText(f"Based on the likelihood ratio {round(self.GetSimilarity,2)} Evidence suggests the speakers are likely different.")
        if (0.7 <= self.GetSimilarity < 0.9):
            self.conclusion_word=f"Based on the likelihood ratio {round(self.GetSimilarity,2)} The current data does not provide a clear answer. Additional information or analysis is required to make a more definitive conclusion."
            self.label_79.setText(f"Based on the likelihood ratio {round(self.GetSimilarity,2)} The current data does not provide a clear answer. Additional information or analysis is required to make a more definitive conclusion.")
        if (0.9 <= self.GetSimilarity < 1.999):
            self.conclusion_word=f"Based on the likelihood ratio  {round(self.GetSimilarity,2) } The analysis strongly suggests that the speakers are the same person."
            self.label_79.setText(f"Based on the likelihood ratio  {round(self.GetSimilarity,2) } The analysis strongly suggests that the speakers are the same person.")
        # GetSimilarity = GetSimilarity * 100
        #
        # GetSimilarity = int(GetSimilarity)

    def open_genarate_reports(self):
        self.label_23.setText(str(self.GetSimilarity))
        self.stackedWidget.setCurrentIndex(0)

    def genarate_report_page(self):
        self.pushButton_23.setStyleSheet(u"background-color: #14213d;\n"
                                         "color: rgb(255, 255, 255);")
        suspect_name = "self.lineEdit.text().strip()"
        About_Case = "self.textEdit_3.toPlainText().strip()"
        CommentOfInvestigator = "self.textEdit_4.toPlainText().strip()"
        ResultShortSummary = "self.textEdit_5.toPlainText().strip()"
        ResultInNumeric = str(self.GetSimilarity)
        date = datetime.now().strftime('%Y-%m-%d')
        header = ["SUSPECT NAME", "ABOUT CASE", "INVESTIGATOR COMMENT", "SHORT SUMMARY", "LIKELIHOOD RATIO", "DATE"]
        data = [ ResultInNumeric, date]

        if not os.path.exists('report'):
            os.makedirs('report')

        file_path = 'report/Voice_Analysis_Reports.csv'
        file_exists = os.path.isfile(file_path)
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(header)  # Write titles only if the file is new
            writer.writerow(data)

        pdf_file_name = f'report_{suspect_name}{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pdf'
        doc = SimpleDocTemplate(pdf_file_name, pagesize=letter)

        # Set up styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(name='TitleStyle', parent=styles['Heading1'], alignment=1, spaceAfter=14)
        subtitle_style = ParagraphStyle(name='SubtitleStyle', parent=styles['Heading2'], alignment=1, spaceAfter=12)
        normal_style = ParagraphStyle(name='NormalStyle', parent=styles['Normal'], spaceAfter=12)
        table_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('FONT', (0, 0), (-1, -1), 'Helvetica'),
                                  ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                  ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        # Elements to be added to the PDF
        elements = []

        # Title
        elements.append(Paragraph("GENERAL REPORT FOR FORENSIC VOICE COMPARISON ANALYSIS TOOL", title_style))

        # Image
        image_path = '/home/shadyai/PycharmProjects/pyqtProject1/ui/images/voiceAnalysis.png'
        img = Image(image_path, width=6 * inch, height=2 * inch)
        elements.append(Spacer(1, 12))
        elements.append(img)
        elements.append(Spacer(1, 24))

        # Subtitle
        elements.append(Paragraph("ANALYSIS RESULTS", subtitle_style))

        # Table
        data = [['SN', 'ATTRIBUTE', 'INFORMATION'],
                ['1', 'Case Number', self.case_number_line6],
                ['2', 'Name of Investigator', self.investigator_name_line5],
                ['3', 'Suspect Name', self.suspect_name_line8],
                ['4', 'Date and Time of Case', self.date_and_time_of_case],
                ['5', 'Device Name', self.device_name_line9],
                ['6', 'Crime Scene Location', self.crime_scene_location_line11],
                ['7', 'Crime Audio File Name', self.crime_audio_name_line10],
                ['8', 'Crime Audio File Format', self.crime_file_format],
                ['9', 'Suspect Audio File Name', self.suspect_audio_name_line12],
                ['10', 'Suspect Audio FIle Format', self.suspect_audio_format_combo2],
                ['11', 'Date And Time Of Acquisition', self.date_and_time_of_acquisition_Date2],
                ['12', 'Crime Audio Hash Value', self.hash_value],
                ['13', 'Suspect Audio Hash Value', self.hash_value_suspect]]
        t = Table(data, colWidths=[30, 200, 200])  # Increase table width

        t.setStyle(table_style)
        elements.append(t)
        elements.append(Spacer(1, 24))

        # Forensic investigator sections
        elements.append(Paragraph("Forensic Investigator Name:", normal_style))
        elements.append(Paragraph("Signature:", normal_style))

        # Build PDF
        doc.build(elements)

        print(f"PDF report generated: {pdf_file_name}")
        file_dialog = QFileDialog()
        file_dialog.setDirectory('')
        self.crime_filename = file_dialog.selectedFiles()
        self.suspect_filename = file_dialog.selectedFiles()

        # self.view_report(pdf_file_name)
        report_text = f"""
                        Forensic Voice Comparison Report

                        Introduction

                        Case ID: {self.case_number_line6}  
                        Date: {self.date_and_time_of_acquisition_Date2}  
                        Suspect Name : {self.suspect_name_line8}
                        Analyst: {self.investigator_name_line5}

                        Methodology

                        1. Data Collection:
                           Two voice samples were provided for analysis:
                           - Suspect Voice Sample: {self.suspect_audio_name_line12}
                           - Crime Scene Voice Sample: {self.crime_audio_name_line10}

                        2. Pre-processing: 
                           The audio files were converted to a consistent format (WAV) and sampled at 16 kHz. Noise reduction techniques were applied to enhance the quality of the recordings.

                        4. Comparison: 
                           A Machine learning model was used to genarate encodings of each Audio where this encodings contain the uniqueness of each voice by considereing features like frequency, pitch , Mel Spectogram , Amplitude etc

                        Analysis

                        Feature Extraction

                        Suspect Voice Sample:
                        - Duration: {10} seconds
                        - Sampling Rate: {self.sample_rate_suspect} Hz
                        - Bit Rate: {self.bit_rate_suspect} bps

                        Crime Scene Voice Sample: 
                        - Duration: {10} seconds
                        - Sampling Rate: {self.sample_rate} Hz
                        - Bit Rate: {self.bit_rate} bps

                        Results:
                        - Overall Likelihood Ratio (LR): {self.GetSimilarity}

                        Results
                        The likelihood ratio of {self.GetSimilarity} suggests that the probability of the two voice samples being from the same individual is significantly higher than being from different individuals. This indicates a strong similarity between the suspect's voice sample and the crime scene voice sample.

                        Conclusion

                        Based on the analysis conducted, there is strong evidence to suggest that the suspect's voice is likely the same as the voice recorded at the crime scene. The high likelihood ratio supports the hypothesis that the two voice samples originate from the same speaker.

                        Recommendations:
                        - Further forensic examination and corroboration with additional evidence are advised to strengthen the findings.
                        - Consideration of context and other case-specific factors should be taken into account when interpreting the results.

                        ---

                        {self.investigator_name_line5} 
                        Forensic Analyst
                        """
        self.report_text_edit.setPlainText(report_text)
        self.stackedWidget.setCurrentIndex(8)

    def view_report(self):
        self.pushButton_36.setStyleSheet(u"background-color: #14213d;\n"
                                         "color: rgb(255, 255, 255);")
        filename = f'{self.suspect_name_line8}_{self.hash_value_suspect}_Forensic_Voice_Comparison_Report.pdf'

        # Create a PDF document
        doc = SimpleDocTemplate(filename, pagesize=letter)
        story = []

        # Define the styles for the document
        styles = getSampleStyleSheet()
        normal_style = styles['Normal']
        title_style = styles['Title']

        # Add title to the first page
        title = Paragraph('Forensic Voice Comparison Report', title_style)
        story.append(title)

        # Add content to the report
        content = f"""
                        <b>Introduction</b>
                        <b>Case ID:</b> {self.case_number_line6}  
                        <b>Date:</b> {self.date_and_time_of_acquisition_Date2}  
                        <b>Suspect Name :</b> {self.suspect_name_line8}
                        <b>Analyst:</b> {self.investigator_name_line5}

                        <b>Methodology</b>
                        1. Data Collection:
                           Two voice samples were provided for analysis:
                           - <b>Suspect Voice Sample:</b> {self.suspect_audio_name_line12}
                           - <b>Crime Scene Voice Sample:</b> {self.crime_audio_name_line10}
                        2. Pre-processing: 
                           The audio files were converted to a consistent format (WAV) and sampled at 16 kHz. Noise reduction techniques were applied to enhance the quality of the recordings.
                        4. Comparison: 
                           A Machine learning model was used to genarate encodings of each Audio where this encodings contain the uniqueness of each voice by considereing features like frequency, pitch , Mel Spectogram , Amplitude etc

                        <b>Analysis</b>
                        Suspect Voice Sample:
                        - <b>Duration:</b> {10} seconds
                        - <b>Sampling Rate:</b> {self.sample_rate_suspect} Hz
                        Crime Scene Voice Sample: 
                        - <b>Duration:</b> {10} seconds
                        - <b>Sampling Rate:</b> {self.sample_rate} Hz

                        <b>Results:</b>
                        - Overall Likelihood Ratio (LR): {self.GetSimilarity}
                        {self.conclusion_word}

                        <b>Conclusion</b>
                        {self.conclusion_word}

                        <b>Recommendations:</b>
                        - Further forensic examination and corroboration with additional evidence are advised to strengthen the findings.
                        - Consideration of context and other case-specific factors should be taken into account when interpreting the results.
                        <b>{self.investigator_name_line5} </b>
                        Forensic Analyst
                """

        # Split the content into paragraphs and add to the story
        paragraphs = content.split('\n')
        for paragraph in paragraphs:
            para = Paragraph(paragraph, normal_style)
            story.append(para)
            story.append(Spacer(1, 12))  # Add space between paragraphs
            # Add watermark to every page
        doc.build(story, onFirstPage=self.addWatermark, onLaterPages=self.addWatermark)

        # Build the PDF document
        # doc.build(story)
        print(f'Report saved as {filename}')
        self.crime_filename = None
        self.suspect_filename = None
        self.enhanced_crime = None
        self.enhanced_suspect = None
        self.GetSimilarity = None

        self.case_number_line6 = None
        self.investigator_name_line5 = None
        self.suspect_name_line8 = None
        self.date_and_time_of_case = None
        self.device_name_line9 = None
        self.crime_scene_location_line11 = None
        self.crime_audio_name_line10 = None
        self.crime_file_format = None
        self.suspect_audio_name_line12 = None
        self.suspect_audio_format_combo2 = None
        self.date_and_time_of_acquisition_Date2 = None
        self.conclusion_word = None
        # THIS ARE THE METADATA VALUES OF CRIME
        self.sample_rate = None
        self.bit_rate = None
        self.file_format = None
        self.audio_channel = None
        self.codec_information = None
        self.hash_value = None
        self.creation_time_stamp = None
        self.modification_time_stamp = None
        self.digital_watermark = None
        self.gps_info = None
        self.device_specific_meta_data = None

        # THIS ARE THE METADATA VALUES OF SUSPECT
        self.sample_rate_suspect = None
        self.bit_rate_suspect = None
        self.file_format_suspect = None
        self.audio_channel_suspect = None
        self.codec_information_suspect = None
        self.hash_value_suspect = None
        self.creation_time_stamp_suspect = None
        self.modification_time_stamp_suspect = None
        self.digital_watermark_suspect = None
        self.gps_info_suspect = None
        self.device_specific_meta_data_suspect = None
        self.label_9.setText("Crime Voice")
        self.label_10.setText("Suspect Voice")

        self.pushButton_17.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_19.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_22.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_23.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_37.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_38.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_39.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_36.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stackedWidget.setCurrentIndex(0)

    def addWatermark(self, canvas, doc):
        # Add watermark text to every page
        # canvas.saveState()
        # canvas.setFont('Helvetica', 120)
        # canvas.setFillGray(0.8)  # Set the color of the watermark
        # canvas.rotate(45)
        # canvas.drawString(100, -40, "Confidential")
        # canvas.restoreState()
        # Load the logo image
        logo_path = '/home/shadyai/PycharmProjects/pyqtProject1/ui/images/emblem1.png'
        logo = ImageReader(logo_path)

        # Calculate position to center the logo on each page
        width, height = letter
        logo_width, logo_height = logo.getSize()
        x = (width - logo_width) / 2
        y = (height - logo_height) / 2

        # Add logo as watermark at the center of the page
        canvas.saveState()
        canvas.setFillAlpha(0.2)
        canvas.drawImage(logo, x, y, width=logo_width, height=logo_height)
        canvas.restoreState()


# *************************************************** WELCOME WINDOW PART

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(55)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO FORENSIC VOICE COMPARISON TOOL")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText(
            "<strong>INITIALIZING</strong> THE APPLICATION"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.ui.label_description.setText("<strong>INITILIZATION COMPLETE</strong>"))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainHome()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == '__main__':
    loader = QUiLoader()
    app = QApplication()

    # loader.show()
    window = SplashScreen()
    # loader_ui = Loader()
    app.exec_()
