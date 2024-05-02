import csv
import os

import librosa
import numpy as np
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QTimer, Qt, QUrl
from PySide2.QtGui import QColor
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QVBoxLayout, QWidget, QFileDialog, QMainWindow, QApplication, QGraphicsDropShadowEffect, \
    QMessageBox
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from scipy.io import wavfile
from scipy.signal import spectrogram
from df.enhance import enhance, init_df, load_audio, save_audio
from df.utils import download_file
from datetime import datetime
import pyqtgraph as pg
from pydub import AudioSegment

import new

import main

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
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
        self.pushButton_9.clicked.connect(self.upload_page)
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
        self.pushButton_16.clicked.connect(self.open_genarate_reports)
        self.pushButton_18.clicked.connect(self.genarate_report_page)
        self.pushButton_20.clicked.connect(self.report_button_page)

        self.pushButton_24.clicked.connect(self.single_speaker_selection)
        self.pushButton_25.clicked.connect(self.mult_speaker_selection)
        self.pushButton_26.clicked.connect(self.upload_audio_trim)
        self.pushButton_27.clicked.connect(self.play_audio_trim)
        self.pushButton_28.clicked.connect(self.pause_audio_trim)
        self.pushButton_29.clicked.connect(self.trim_audio)
        self.pushButton_30.clicked.connect(self.single_speaker_selection)

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

    def upload_page(self):
        self.pushButton_17.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stop_audio()
        self.stop_audio_suspect()
        self.stackedWidget.setCurrentIndex(2)

    def filter_page(self):
        self.pushButton_19.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stop_audio_filter()
        self.stop_audio_suspect_filter()
        self.stackedWidget.setCurrentIndex(3)

    def compare_page(self):
        self.pushButton_22.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stackedWidget.setCurrentIndex(4)

    def report_button_page(self):
        self.pushButton_23.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.stackedWidget.setCurrentIndex(5)

    def process_and_display_results(self):
        if self.crime_filename and self.suspect_filename:
            self.stackedWidget.setCurrentIndex(3)  # Switch to page_2 of the stacked widget
            crime_voice_path = self.crime_filename
            suspect_voice_path = self.suspect_filename
            self.show_uploaded_clips(crime_voice_path, suspect_voice_path)

    def show_uploaded_clips(self, crime_filename, suspect_filename):
        self.pushButton_17.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
                                         "color: rgb(255, 255, 255);")
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
            self.stackedWidget.setCurrentIndex(4)  # Switch to page_2 of the stacked widget
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
        self.pushButton_22.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
                                         "color: rgb(255, 255, 255);")
        self.stop_audio_suspect_filter()
        self.stop_audio_filter()
        self.stackedWidget.setCurrentIndex(5)
        sound_encoder = VoiceEncoder(verbose=False)
        file_1 = preprocess_wav(sound_1_path)
        file_2 = preprocess_wav(sound_2_path)

        encoded_sound1 = sound_encoder.embed_utterance(file_1)
        encoded_sound2 = sound_encoder.embed_utterance(file_2)

        dot_product_size = np.dot(encoded_sound1, encoded_sound2)
        norm_sound1 = np.linalg.norm(encoded_sound1)
        norm_sound2 = np.linalg.norm(encoded_sound2)

        # kosinus benzerliğini hesaplama
        self.GetSimilarity = dot_product_size / (norm_sound1 * norm_sound2)
        self.label_15.setText(str(self.GetSimilarity))
        # GetSimilarity = GetSimilarity * 100
        #
        # GetSimilarity = int(GetSimilarity)

    def open_genarate_reports(self):
        self.label_23.setText(str(self.GetSimilarity))
        self.stackedWidget.setCurrentIndex(6)

    def genarate_report_page(self):
        self.pushButton_23.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
                                         "color: rgb(255, 255, 255);")
        suspect_name = self.lineEdit.text().strip()
        About_Case = self.textEdit_3.toPlainText().strip()
        CommentOfInvestigator = self.textEdit_4.toPlainText().strip()
        ResultShortSummary = self.textEdit_5.toPlainText().strip()
        ResultInNumeric = str(self.GetSimilarity)
        date = datetime.now().strftime('%Y-%m-%d')
        header = ["SUSPECT NAME", "ABOUT CASE", "INVESTIGATOR COMMENT", "SHORT SUMMARY", "LIKELIHOOD RATIO", "DATE"]
        data = [suspect_name, About_Case, CommentOfInvestigator, ResultShortSummary, ResultInNumeric, date]

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
        c = canvas.Canvas(pdf_file_name, pagesize=letter)

        image_path = '/home/shadyai/PycharmProjects/pyqtProject1/ui/images/voiceAnalysis.png'
        img = ImageReader(image_path)
        img_width, img_height = img.getSize()
        aspect_ratio = img_height / img_width
        desired_height = 200
        desired_width = 800

        c.drawImage(img, x=0, y=letter[1] - desired_height, width=desired_width, height=desired_height, mask='auto')

        # Set font styles
        title_style = ParagraphStyle(name='TitleStyle', fontName='Helvetica-Bold', fontSize=12, alignment=1)
        subtitle_style = ParagraphStyle(name='SubtitleStyle', fontName='Helvetica', fontSize=12, alignment=1)
        table_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('FONT', (0, 0), (-1, -1), 'Helvetica'),
                                  ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                  ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        # Title
        title = Paragraph("<u>GENERAL REPORT FOR FORENSIC VOICE COMPARISON ANALYSIS TOOL</u>", title_style)
        title.wrapOn(c, 400, 100)
        title.drawOn(c, 100, 550)

        # Subtitle
        subtitle = Paragraph("<u>ANALYSIS RESULTS</u>", subtitle_style)
        subtitle.wrapOn(c, 400, 100)
        subtitle.drawOn(c, 100, 530)

        # Table
        data = [['SN', 'ATTRIBUTE', 'INFORMATION'],
                ['1', 'Name Of Suspect', suspect_name],
                ['2', 'About Case', About_Case],
                ['3', 'Comment Of Investigator', CommentOfInvestigator],
                ['4', 'Short Summary Of Result', ResultShortSummary],
                ['4', 'Likelihood Ration', ResultInNumeric],
                ['4', 'Date', date]]
        t = Table(data, colWidths=[30, 200, 200])  # Increase table width

        t.setStyle(table_style)
        t.wrapOn(c, 400, 400)
        t.drawOn(c, 100, 410)

        # Forensic investigator sections
        c.drawString(100, 390, "Forensic Investigator Name:")
        c.drawString(100, 375, "Signature:")

        c.save()

        print(f"PDF report generated: {pdf_file_name}")
        file_dialog = QFileDialog()
        file_dialog.setDirectory('')
        self.crime_filename = file_dialog.selectedFiles()
        self.suspect_filename = file_dialog.selectedFiles()
        self.pushButton_17.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_19.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_22.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_23.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
                                         "color: rgb(255, 255, 255);")
        self.crime_filename = None
        self.suspect_filename = None
        self.stackedWidget.setCurrentIndex(0)



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
