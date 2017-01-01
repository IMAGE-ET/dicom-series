import dicom
import os
import shutil


class SeriesSet:
    def __init__(self, dic_input_path, dic_output_path):
        self.dic_input = dic_input_path
        self.dic_output = dic_output_path

    def sort_dicoms(self):
        all_dicoms = [dic for dic in os.listdir(self.dic_input)]

        for dicom_file in all_dicoms:
            file_path = self.dic_input + dicom_file
            dicom_file = dicom.read_file(file_path)
            study_dir = self.dic_output + dicom_file.StudyID
            series_dir = study_dir + '/' + dicom_file.SeriesInstanceUID
            if not os.path.isdir(study_dir):
                os.makedirs(study_dir)
            if not os.path.isdir(series_dir):
                os.makedirs(series_dir)
            shutil.copy2(file_path, series_dir)


data = SeriesSet('studies/', 'dicoms/')
data.sort_dicoms()