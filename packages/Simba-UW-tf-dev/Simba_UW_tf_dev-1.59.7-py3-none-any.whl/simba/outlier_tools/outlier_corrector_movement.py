__author__ = "Simon Nilsson"

import os, glob
import pandas as pd
import numpy as np
from simba.mixins.config_reader import ConfigReader
from simba.utils.read_write import read_df, write_df, get_fn_ext, read_config_entry
from simba.utils.printing import stdout_success, SimbaTimer
from simba.utils.enums import ConfigKey, Dtypes

class OutlierCorrecterMovement(ConfigReader):
    """
    Detect and ammend outliers in pose-estimation data based on movement lenghth (Euclidean) of the body-parts
    in the current frame from preceeding frame. Uses critera stored in the SimBA project project_config.ini
    under the [Outlier settings] header.

    :parameter str config_path: path to SimBA project config file in Configparser format

    .. note::
       `Outlier correction documentation <https://github.com/sgoldenlab/simba/blob/master/misc/Outlier_settings.pdf>`__.

    Examples
    ----------
    >>> outlier_correcter_movement = OutlierCorrecterMovement(config_path='MyProjectConfig')
    >>> outlier_correcter_movement.run()

    """

    def __init__(self,
                 config_path: str):

        super().__init__(config_path=config_path)
        if not os.path.exists(self.outlier_corrected_movement_dir): os.makedirs(self.outlier_corrected_movement_dir)
        if self.animal_cnt == 1:
            self.animal_id = read_config_entry(self.config, ConfigKey.MULTI_ANIMAL_ID_SETTING.value, ConfigKey.MULTI_ANIMAL_IDS.value, Dtypes.STR.value)
            if self.animal_id != 'None':
                self.animal_bp_dict[self.animal_id] = self.animal_bp_dict.pop('Animal_1')
        self.above_criterion_dict_dict = {}
        self.criterion = read_config_entry(self.config, ConfigKey.OUTLIER_SETTINGS.value, ConfigKey.MOVEMENT_CRITERION.value, Dtypes.FLOAT.value)
        self.outlier_bp_dict = {}
        for animal_name in self.animal_bp_dict.keys():
            self.outlier_bp_dict[animal_name] = {}
            self.outlier_bp_dict[animal_name]['bp_1'] = read_config_entry(self.config, 'Outlier settings', 'movement_bodypart1_{}'.format(animal_name.lower()), 'str')
            self.outlier_bp_dict[animal_name]['bp_2'] = read_config_entry(self.config, 'Outlier settings', 'movement_bodypart2_{}'.format(animal_name.lower()), 'str')


    def __outlier_replacer(self, bp_lst=None, animal_name=None):
        self.above_criterion_dict = {}
        self.below_criterion_dict = {}
        self.above_criterion_dict_dict[self.video_name][animal_name] = {}
        for c in self.body_parts_lst:
            self.data_df_combined[c + '_movement'] = np.sqrt((self.data_df_combined[c + '_x'] - self.data_df_combined[c + '_x_shifted']) ** 2 + (self.data_df_combined[c + '_y'] - self.data_df_combined[c + '_y_shifted']) ** 2)
            self.above_criterion_dict[c] = list(self.data_df_combined.index[self.data_df_combined[c + '_movement'] > self.animal_criteria[animal_name]])
            self.below_criterion_dict[c] = list(self.data_df_combined.index[self.data_df_combined[c + '_movement'] <= self.animal_criteria[animal_name]])
            self.above_criterion_dict_dict[self.video_name][animal_name][c] = self.above_criterion_dict[c]
        for body_part, body_part_idx in self.above_criterion_dict.items():
            body_part_x, body_part_y = body_part + '_x', body_part + '_y'
            for idx in body_part_idx:
                try:
                    closest_idx = max([i for i in self.below_criterion_dict[body_part] if idx > i])
                except ValueError:
                    closest_idx = idx
                self.data_df.loc[[idx], body_part_x] = self.data_df.loc[[closest_idx], body_part_x].values[0]
                self.data_df.loc[[idx], body_part_y] = self.data_df.loc[[closest_idx], body_part_y].values[0]

    def run(self):
        """
        Runs outlier detection and correction. Results are stored in the
        ``project_folder/csv/outlier_corrected_movement`` directory of the SimBA project.
        """
        for file_cnt, file_path in enumerate(self.input_csv_paths):
            video_timer = SimbaTimer(start=True)
            _, self.video_name, _ = get_fn_ext(file_path)
            print('Processing video {}. Video {}/{}...'.format(self.video_name, str(file_cnt+1), str(len(self.input_csv_paths))))
            self.above_criterion_dict_dict[self.video_name] = {}
            save_path = os.path.join(self.outlier_corrected_movement_dir, self.video_name + '.' + self.file_type)
            self.data_df = read_df(file_path, self.file_type, check_multiindex=True)
            self.data_df = self.insert_column_headers_for_outlier_correction(data_df=self.data_df, new_headers=self.bp_headers, filepath=file_path)
            self.data_df_shifted = self.data_df.shift(periods=1).add_suffix('_shifted').fillna(0)
            self.data_df_combined = pd.concat([self.data_df, self.data_df_shifted], axis=1, join='inner').fillna(0)
            self.animal_criteria = {}
            for animal_name, animal_bps in self.outlier_bp_dict.items():
                animal_bp_distances = np.sqrt((self.data_df[animal_bps['bp_1'] + '_x'] - self.data_df[animal_bps['bp_2'] + '_x']) ** 2 + (self.data_df[animal_bps['bp_1'] + '_y'] - self.data_df[animal_bps['bp_2'] + '_y']) ** 2)
                self.animal_criteria[animal_name] = animal_bp_distances.mean() * self.criterion
            for animal_name in self.outlier_bp_dict.keys():
                animal_bps = [x for x in self.bp_headers if x.startswith(animal_name + '_')]
                self.__outlier_replacer(bp_lst=animal_bps, animal_name=animal_name)
            write_df(df=self.data_df, file_type=self.file_type, save_path=save_path)
            video_timer.stop_timer()
            print(f'Corrected movement outliers for file {self.video_name} (elapsed time: {video_timer.elapsed_time_str}s)...')
        self.__save_log_file()

    def __save_log_file(self):
        out_df_lst = []
        for video_name, video_data in self.above_criterion_dict_dict.items():
            for animal_name, animal_data in video_data.items():
                for bp_name, vid_idx_lst in animal_data.items():
                    correction_ratio = round(len(vid_idx_lst) / len(self.data_df), 6)
                    out_df_lst.append(pd.DataFrame([[video_name, animal_name, bp_name, len(vid_idx_lst), correction_ratio]], columns=['Video', 'Animal', 'Body-part', 'Corrections', 'Correction ratio (%)']))
        out_df = pd.concat(out_df_lst, axis=0).reset_index(drop=True)
        log_fn = os.path.join(self.logs_path, 'Outliers_movement_{}.csv'.format(self.datetime))
        out_df.to_csv(log_fn)
        self.timer.stop_timer()
        stdout_success(msg='Log for corrected "movement outliers" saved in project_folder/logs', elapsed_time=self.timer.elapsed_time_str)

# test = OutlierCorrecterMovement(config_path='/Users/simon/Desktop/envs/troubleshooting/two_animals_16bp_032023/project_folder/project_config.ini')
# test.correct_movement_outliers()

# test = OutlierCorrecterMovement(config_path='/Users/simon/Desktop/envs/troubleshooting/naresh/project_folder/project_config.ini')
# test.run()

# test = OutlierCorrecterMovement(config_path='/Users/simon/Desktop/envs/troubleshooting/two_black_animals_14bp/project_folder/project_config.ini')
# test.correct_movement_outliers()
#
# test = OutlierCorrecterMovement(config_path='/Users/simon/Desktop/envs/troubleshooting/two_animals_16bp_032023/project_folder/project_config.ini')
# test.correct_movement_outliers()

