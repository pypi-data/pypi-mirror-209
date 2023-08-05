__author__ = "Simon Nilsson"

from tkinter import *
from PIL import ImageTk
import PIL.Image
from tkinter import messagebox
import os
from simba.pose_importers import trk_importer
from typing import Tuple, Optional, List, Dict


from simba.utils.checks import (check_int,
                                check_str,
                                check_float,
                                check_if_dir_exists)
from simba.pose_importers.read_DANNCE_mat import import_DANNCE_file, import_DANNCE_folder
from simba.pose_importers.import_mars import MarsImporter
from simba.pose_importers.madlc_importer import MADLCImporterH5
from simba.pose_importers.sleap_csv_importer import SLEAPImporterCSV
from simba.pose_importers.sleap_h5_importer import SLEAPImporterH5
from simba.pose_importers.sleap_slp_importer import SLEAPImporterSLP


from simba.pose_importers.dlc_importer_csv import (import_multiple_dlc_tracking_csv_file, import_single_dlc_tracking_csv_file)
from simba.utils.enums import ConfigKey, Options, Formats
from simba.utils.read_write import find_core_cnt, copy_single_video_to_project, copy_multiple_videos_to_project, read_config_file, read_config_entry
from simba.ui.tkinter_functions import (hxtScrollbar,
                                        DropDownMenu,
                                        Entry_Box,
                                        FileSelect,
                                        FolderSelect)
from simba.utils.checks import check_file_exist_and_readable
from simba.mixins.config_reader import ConfigReader
from simba.utils.errors import CountError
from simba.utils.lookups import (get_icons_paths,
                                 get_color_dict,
                                 get_named_colors)

class PopUpMixin(object):
    """
    Methods for pop-up windows in SimBA.

    :param str title: Pop-up window title
    :param Optional[configparser.Configparser] config_path: path to SimBA project_config.ini
    :param tuple size: HxW of the pop-up window.
    """


    def __init__(self,
                 title: str,
                 config_path: Optional[str] = None,
                 size: Tuple[int, int] = (400, 400)):

        self.main_frm = Toplevel()
        self.main_frm.minsize(size[0], size[1])
        self.main_frm.wm_title(title)
        self.main_frm.lift()
        self.main_frm = Canvas(hxtScrollbar(self.main_frm))
        self.main_frm.pack(fill="both", expand=True)

        self.palette_options = Options.PALETTE_OPTIONS.value
        self.resolutions = Options.RESOLUTION_OPTIONS.value
        self.shading_options = Options.HEATMAP_SHADING_OPTIONS.value
        self.heatmap_bin_size_options = Options.HEATMAP_BIN_SIZE_OPTIONS.value
        self.dpi_options = Options.DPI_OPTIONS.value
        self.colors = get_named_colors()
        self.colors_dict = get_color_dict()
        self.cpu_cnt, _ = find_core_cnt()
        self.menu_icons = get_icons_paths()
        for k in self.menu_icons.keys():
            self.menu_icons[k]['img'] = ImageTk.PhotoImage(image=PIL.Image.open(os.path.join(os.path.dirname(__file__), self.menu_icons[k]['icon_path'])))
        if config_path:
            print(config_path)
            ConfigReader.__init__(self, config_path=config_path, read_video_info=False)

    def create_clf_checkboxes(self,
                              main_frm: Frame,
                              clfs: List[str]):
        self.choose_clf_frm = LabelFrame(self.main_frm, text='SELECT CLASSIFIER ANNOTATIONS', font=Formats.LABELFRAME_HEADER_FORMAT.value)
        self.clf_selections = {}
        for clf_cnt, clf in enumerate(clfs):
            self.clf_selections[clf] = BooleanVar(value=False)
            self.calculate_distance_moved_cb = Checkbutton(self.choose_clf_frm, text=clf, variable=self.clf_selections[clf])
            self.calculate_distance_moved_cb.grid(row=clf_cnt, column=0, sticky=NW)
        self.choose_clf_frm.grid(row=self.children_cnt_main(), column=0, sticky=NW)

    def create_cb_frame(self,
                        main_frm: Frame,
                        cb_titles: List[str],
                        frm_title: str) -> Dict[str, BooleanVar]:

        cb_frm = LabelFrame(main_frm, text=frm_title, font=Formats.LABELFRAME_HEADER_FORMAT.value)
        cb_dict = {}
        for cnt, title in enumerate(cb_titles):
            cb_dict[title] = BooleanVar(value=False)
            cb = Checkbutton(cb_frm, text=title, variable=cb_dict[title])
            cb.grid(row=cnt, column=0, sticky=NW)
        cb_frm.grid(row=self.children_cnt_main(), column=0, sticky=NW)
        return cb_dict

    def create_dropdown_frame(self,
                              main_frm: Frame,
                              drop_down_titles: List[str],
                              drop_down_options: List[str],
                              frm_title: str):

        dropdown_frm = LabelFrame(main_frm, text=frm_title, font=Formats.LABELFRAME_HEADER_FORMAT.value)
        dropdown_dict = {}
        for cnt, title in enumerate(drop_down_titles):
            dropdown_dict[title] = DropDownMenu(dropdown_frm, title, drop_down_options, '35')
            dropdown_dict[title].setChoices(drop_down_options[0])
            dropdown_dict[title].grid(row=cnt, column=0, sticky=NW)
        dropdown_frm.grid(row=self.children_cnt_main(), column=0, sticky=NW)
        return dropdown_dict

    def create_choose_animal_cnt_dropdown(self):
        if hasattr(self, 'animal_cnt_frm'):
            self.animal_cnt_frm.destroy()
        animal_cnt_options = set(range(1, self.project_animal_cnt + 1))
        self.animal_cnt_frm = LabelFrame(self.main_frm, text='SELECT NUMBER OF ANIMALS', font=Formats.LABELFRAME_HEADER_FORMAT.value)
        self.animal_cnt_dropdown = DropDownMenu(self.animal_cnt_frm, '# of animals', animal_cnt_options, '12')
        self.animal_cnt_dropdown.setChoices(max(animal_cnt_options))
        self.animal_cnt_confirm_btn = Button(self.animal_cnt_frm, text="Confirm", command=lambda: self.update_body_parts())
        self.animal_cnt_frm.grid(row=self.children_cnt_main(), sticky=NW)
        self.animal_cnt_dropdown.grid(row=self.children_cnt_main(), column=1, sticky=NW)
        self.animal_cnt_confirm_btn.grid(row=self.children_cnt_main(), column=2, sticky=NW)
        self.create_choose_body_parts_frm()
        self.update_body_parts()

    def create_choose_body_parts_frm(self):
        if hasattr(self, 'body_part_frm'):
            self.body_part_frm.destroy()
        self.body_parts_dropdown_dict = {}
        self.body_part_frm = LabelFrame(self.main_frm, text="CHOOSE ANIMAL BODY-PARTS", font=Formats.LABELFRAME_HEADER_FORMAT.value, name='choose animal body-parts')
        self.body_part_frm.grid(row=self.children_cnt_main(), sticky=NW)

    def update_body_parts(self):
        for child in self.body_part_frm.winfo_children():
            child.destroy()
        for animal_cnt in range(int(self.animal_cnt_dropdown.getChoices())):
            animal_name = list(self.animal_bp_dict.keys())[animal_cnt]
            self.body_parts_dropdown_dict[animal_name] = DropDownMenu(self.body_part_frm, f'{animal_name} body-part:', self.body_parts_lst, '25')
            self.body_parts_dropdown_dict[animal_name].grid(row=animal_cnt, column=1, sticky=NW)
            self.body_parts_dropdown_dict[animal_name].setChoices(self.body_parts_lst[animal_cnt])

    def create_time_bin_entry(self):
        if hasattr(self, 'time_bin_frm'):
            self.time_bin_frm.destroy()
        self.time_bin_frm = LabelFrame(self.main_frm, text="TIME BIN", font=Formats.LABELFRAME_HEADER_FORMAT.value)
        self.time_bin_entrybox = Entry_Box(self.time_bin_frm, 'Time-bin size (s): ', '12', validation='numeric')
        self.time_bin_entrybox.grid(row=0, column=0, sticky=NW)
        self.time_bin_frm.grid(row=self.children_cnt_main(), column=0, sticky=NW)

    def create_run_frm(self,
                       run_function: object,
                       title: str = 'RUN'):
        if hasattr(self, 'run_frm'):
            self.run_frm.destroy()
            self.run_btn.destroy()
        self.run_frm = LabelFrame(self.main_frm, text='RUN', font=Formats.LABELFRAME_HEADER_FORMAT.value, fg='black')
        self.run_btn = Button(self.run_frm, text=title, fg='blue', command=lambda: run_function())
        self.run_frm.grid(row=self.children_cnt_main()+1, column=0, sticky=NW)
        self.run_btn.grid(row=0, column=0, sticky=NW)

    def create_choose_number_of_body_parts_frm(self,
                                               project_body_parts: List[str],
                                               run_function: object):
        self.bp_cnt_frm = LabelFrame(self.main_frm, text='SELECT NUMBER OF BODY-PARTS',  font=Formats.LABELFRAME_HEADER_FORMAT.value)
        self.bp_cnt_dropdown = DropDownMenu(self.bp_cnt_frm, '# of body-parts', list(range(1, len(project_body_parts))), '12')
        self.bp_cnt_dropdown.setChoices(1)
        self.bp_cnt_confirm_btn = Button(self.bp_cnt_frm, text="Confirm", command=lambda: self.create_choose_bp_frm(project_body_parts, run_function))
        self.bp_cnt_frm.grid(row=0, sticky=NW)
        self.bp_cnt_dropdown.grid(row=0, column=0, sticky=NW)
        self.bp_cnt_confirm_btn.grid(row=0, column=1, sticky=NW)

    def add_to_listbox_from_entrybox(self,
                                     list_box: Listbox,
                                     entry_box: Entry_Box):
        value = entry_box.entry_get
        check_float(name='VALUE', value=value)
        list_box_content = [float(x) for x in list_box.get(0, END)]
        if float(value) not in list_box_content:
            list_box.insert(0, value)

    def add_value_to_listbox(self,
                             list_box: Listbox,
                             value: float):
        list_box.insert(0, value)

    def add_values_to_several_listboxes(self,
                                        list_boxes: List[Listbox],
                                        values: List[float]):
        if len(list_boxes) != len(values):
            raise CountError(msg='Value count and listboxes count are not equal')
        for i in range(len(list_boxes)):
            list_boxes[i].insert(0, values[i])

    def remove_from_listbox(self,
                            list_box: Listbox):
        selection = list_box.curselection()
        if selection:
            list_box.delete(selection[0])


    def create_choose_bp_frm(self, project_body_parts, run_function):
        if hasattr(self, 'body_part_frm'):
            self.body_part_frm.destroy()
        self.body_parts_dropdowns = {}
        self.body_part_frm = LabelFrame(self.main_frm, text="CHOOSE ANIMAL BODY-PARTS", font=Formats.LABELFRAME_HEADER_FORMAT.value, name='choose animal body-parts')
        self.body_part_frm.grid(row=self.children_cnt_main(), sticky=NW)
        for bp_cnt in range(int(self.bp_cnt_dropdown.getChoices())):
            self.body_parts_dropdowns[bp_cnt] = DropDownMenu(self.body_part_frm, f'Body-part {str(bp_cnt+1)}:', project_body_parts, '25')
            self.body_parts_dropdowns[bp_cnt].grid(row=bp_cnt, column=0, sticky=NW)
            self.body_parts_dropdowns[bp_cnt].setChoices(project_body_parts[bp_cnt])
        self.create_run_frm(run_function=run_function)

    def choose_bp_frm(self, parent: LabelFrame, bp_options: list):
        self.body_parts_dropdowns = {}
        self.body_part_frm = LabelFrame(parent, text="CHOOSE ANIMAL BODY-PARTS",
                                        font=Formats.LABELFRAME_HEADER_FORMAT.value, name='choose animal body-parts')
        self.body_part_frm.grid(row=self.frame_children(frame=parent), sticky=NW)
        for bp_cnt in range(int(self.animal_cnt_dropdown.getChoices())):
            self.body_parts_dropdowns[bp_cnt] = DropDownMenu(self.body_part_frm, f'Body-part {str(bp_cnt + 1)}:', bp_options, '20')
            self.body_parts_dropdowns[bp_cnt].grid(row=bp_cnt, column=0, sticky=NW)
            self.body_parts_dropdowns[bp_cnt].setChoices(bp_options[bp_cnt])


    def children_cnt_main(self) -> int:
        return int(len(list(self.main_frm.children.keys())))

    def frame_children(self, frame: Frame) -> int:
        return int(len(list(frame.children.keys())))

    def update_config(self) -> None:
        with open(self.config_path, 'w') as f:
            self.config.write(f)

    def show_smoothing_entry_box_from_dropdown(self, choice: str):
        if choice == 'None':
            self.smoothing_time_eb.grid_forget()
        if (choice == 'Gaussian') or (choice == 'Savitzky Golay'):
            self.smoothing_time_eb.grid(row=0, column=1, sticky=E)

    def choose_bp_threshold_frm(self, parent: LabelFrame):
        self.probability_frm = LabelFrame(parent, text="PROBABILITY THRESHOLD", font=Formats.LABELFRAME_HEADER_FORMAT.value)
        self.probability_frm.grid(row=self.frame_children(frame=parent), column=0, sticky=NW)
        self.probability_entry = Entry_Box(self.probability_frm, "Probability threshold: ", labelwidth=20)
        self.probability_entry.entry_set('0.00')
        self.probability_entry.grid(row=0, column=0, sticky=NW)


    def enable_dropdown_from_checkbox(self,
                                      check_box_var: BooleanVar,
                                      dropdown_menus: List[DropDownMenu]):
        if check_box_var.get():
            for menu in dropdown_menus:
                menu.enable()
        else:
            for menu in dropdown_menus:
                menu.disable()

    def create_entry_boxes_from_entrybox(self, count: int, parent: Frame, current_entries: list):
        check_int(name='CLASSIFIER COUNT', value=count, min_value=1)
        for entry in current_entries:
            entry.destroy()
        for clf_cnt in range(int(count)):
            entry = Entry_Box(parent, f'Classifier {str(clf_cnt+1)}:', labelwidth=15)
            current_entries.append(entry)
            entry.grid(row=clf_cnt + 2, column=0, sticky=NW)

    def create_animal_names_entry_boxes(self, animal_cnt: str):
        check_int(name='NUMBER OF ANIMALS', value=animal_cnt, min_value=0)
        if hasattr(self, 'animal_names_frm'):
            self.animal_names_frm.destroy()
        if not hasattr(self, 'multi_animal_id_list'):
            self.multi_animal_id_list = []
            for i in range(int(animal_cnt)):
                self.multi_animal_id_list.append(f'Animal {i+1}')
        self.animal_names_frm = Frame(self.animal_settings_frm, pady=5, padx=5)
        self.animal_name_entry_boxes = {}
        for i in range(int(animal_cnt)):
            self.animal_name_entry_boxes[i+1] = Entry_Box(self.animal_names_frm, f'Animal {str(i+1)} name: ', '25')
            if i <= len(self.multi_animal_id_list)-1:
                self.animal_name_entry_boxes[i+1].entry_set(self.multi_animal_id_list[i])
            self.animal_name_entry_boxes[i+1].grid(row=i, column=0, sticky=NW)

        self.animal_names_frm.grid(row=1, column=0, sticky=NW)

    def enable_entrybox_from_checkbox(self,
                                      check_box_var: BooleanVar,
                                      entry_boxes: List[Entry_Box],
                                      reverse: bool = False):
        if reverse:
            if check_box_var.get():
                for box in entry_boxes:
                    box.set_state('disable')
            else:
                for box in entry_boxes:
                    box.set_state('normal')
        else:
            if check_box_var.get():
                for box in entry_boxes:
                    box.set_state('normal')
            else:
                for box in entry_boxes:
                    box.set_state('disable')

    def create_import_pose_menu(self,
                                parent_frm: Frame,
                                idx_row: int = 0,
                                idx_column: int = 0):

        def run_call(data_type: str,
                     interpolation: str,
                     smoothing: str,
                     smoothing_window: str,
                     animal_names: dict,
                     data_path: str,
                     tracking_data_type: str or None=None):

            smooth_settings = {}
            smooth_settings['Method'] = smoothing
            smooth_settings['Parameters'] = {}
            smooth_settings['Parameters']['Time_window'] = smoothing_window

            if smooth_settings['Method'] != 'None':
                check_int(name='SMOOTHING TIME WINDOW', value=smoothing_window, min_value=1)

            if self.animal_name_entry_boxes is None:
                raise CountError(msg='Select animal number and animal names BEFORE importing data.')

            animal_ids = []
            for animal_cnt, animal_entry_box in animal_names.items():
                check_str(name=f'ANIMAL {str(animal_cnt)} NAME', value=animal_entry_box.entry_get, allow_blank=False)
                animal_ids.append(animal_entry_box.entry_get)


            self.config = read_config_file(config_path=self.config_path)
            self.config.set(ConfigKey.MULTI_ANIMAL_ID_SETTING.value, ConfigKey.MULTI_ANIMAL_IDS.value, ",".join(animal_ids))
            self.update_config()

            if data_type == 'H5 (multi-animal DLC)':
                dlc_multi_animal_importer = MADLCImporterH5(config_path=self.config_path,
                                                           data_folder=data_path,
                                                           file_type=tracking_data_type,
                                                           id_lst=animal_ids,
                                                           interpolation_settings=interpolation,
                                                           smoothing_settings=smooth_settings)
                dlc_multi_animal_importer.run()

            if data_type == 'SLP (SLEAP)':
                sleap_importer = SLEAPImporterSLP(project_path=self.config_path,
                                                  data_folder=data_path,
                                                  id_lst=animal_ids,
                                                  interpolation_settings=interpolation,
                                                  smoothing_settings=smooth_settings)
                sleap_importer.run()

            if data_type == 'TRK (multi-animal APT)':
                try:
                    trk_importer(self.config_path, data_path, animal_ids, interpolation, smooth_settings)
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            if data_type == 'CSV (SLEAP)':
                sleap_csv_importer = SLEAPImporterCSV(config_path=self.config_path,
                                                      data_folder=data_path,
                                                      id_lst=animal_ids,
                                                      interpolation_settings=interpolation,
                                                      smoothing_settings=smooth_settings)
                sleap_csv_importer.run()

            if data_type == 'H5 (SLEAP)':
                sleap_h5_importer = SLEAPImporterH5(config_path=self.config_path,
                                                    data_folder=data_path,
                                                    id_lst=animal_ids,
                                                    interpolation_settings=interpolation,
                                                    smoothing_settings=smooth_settings)
                sleap_h5_importer.run()


        def import_menu(data_type_choice: str):
            if hasattr(self, 'choice_frm'):
                self.choice_frm.destroy()
            self.choice_frm = Frame(self.import_tracking_frm)
            self.animal_name_entry_boxes = None

            self.interpolation_frm = LabelFrame(self.choice_frm, text='INTERPOLATION METHOD', pady=5, padx=5)
            self.interpolation_dropdown = DropDownMenu(self.interpolation_frm, 'Interpolation method: ', Options.INTERPOLATION_OPTIONS_W_NONE.value, '25')
            self.interpolation_dropdown.setChoices('None')
            self.interpolation_frm.grid(row=0, column=0, sticky=NW)
            self.interpolation_dropdown.grid(row=0, column=0, sticky=NW)

            self.smoothing_frm = LabelFrame(self.choice_frm, text='SMOOTHING METHOD', pady=5, padx=5)
            self.smoothing_dropdown = DropDownMenu(self.smoothing_frm, 'Smoothing', Options.SMOOTHING_OPTIONS_W_NONE.value, '25', com=self.show_smoothing_entry_box_from_dropdown)
            self.smoothing_dropdown.setChoices('None')
            self.smoothing_time_eb = Entry_Box(self.smoothing_frm, 'Period (ms):', labelwidth='12', width=10, validation='numeric')
            self.smoothing_frm.grid(row=1, column=0, sticky=NW)
            self.smoothing_dropdown.grid(row=0, column=0, sticky=NW)

            if data_type_choice in ['CSV (DLC/DeepPoseKit)', 'MAT (DANNCE 3D)', 'JSON (BENTO)']:
                if data_type_choice == 'CSV (DLC/DeepPoseKit)':
                    self.import_directory_frm = LabelFrame(self.choice_frm, text='IMPORT DLC CSV DIRECTORY', pady=5, padx=5)
                    self.import_directory_select = FolderSelect(self.import_directory_frm, 'Input DIRECTORY:', lblwidth=25)
                    self.import_dir_btn = Button(self.import_directory_frm, fg='blue', text='Import DIRECTORY to SimBA project', command= lambda: import_multiple_dlc_tracking_csv_file(config_path=self.config_path,
                                                                                                                                                                               interpolation_setting=self.interpolation_dropdown.getChoices(),
                                                                                                                                                                               smoothing_setting=self.smoothing_dropdown.getChoices(),
                                                                                                                                                                               smoothing_time=self.smoothing_time_eb.entry_get,
                                                                                                                                                                               data_dir=self.import_directory_select.folder_path))

                    self.import_single_frm = LabelFrame(self.choice_frm, text='IMPORT DLC CSV FILE', pady=5, padx=5)
                    self.import_file_select = FileSelect(self.import_single_frm, 'Input FILE:', lblwidth=25)
                    self.import_file_btn = Button(self.import_single_frm, fg='blue', text='Import FILE to SimBA project', command= lambda: import_single_dlc_tracking_csv_file(config_path=self.config_path,
                                                                                                                                                                               interpolation_setting=self.interpolation_dropdown.getChoices(),
                                                                                                                                                                               smoothing_setting=self.smoothing_dropdown.getChoices(),
                                                                                                                                                                               smoothing_time=self.smoothing_time_eb.entry_get,
                                                                                                                                                                               file_path=self.import_file_select.file_path))

                elif data_type_choice == 'MAT (DANNCE 3D)':
                    self.import_directory_frm = LabelFrame(self.choice_frm, text='IMPORT DANNCE MAT DIRECTORY', pady=5, padx=5)
                    self.import_directory_select = FolderSelect(self.import_directory_frm, 'Input DIRECTORY:', lblwidth=25)
                    self.import_dir_btn = Button(self.import_directory_frm, fg='blue', text='Import directory to SimBA project', command= lambda: import_DANNCE_folder(config_path=self.config_path,
                                                                                                                                                              folder_path=self.import_directory_select.folder_path,
                                                                                                                                                              interpolation_method=self.interpolation_dropdown.getChoices()))

                    self.import_single_frm = LabelFrame(self.choice_frm, text='IMPORT DANNCE CSV FILE', pady=5, padx=5)
                    self.import_file_select = FileSelect(self.import_single_frm, 'Input FILE:', lblwidth=25)
                    self.import_file_btn = Button(self.import_single_frm, fg='blue', text='Import file to SimBA project', command=lambda: import_DANNCE_file(config_path=self.config_path,
                                                                                                                                                     file_path=self.import_file_select.file_path,
                                                                                                                                                     interpolation_method=self.interpolation_dropdown.getChoices()))

                elif data_type_choice == 'JSON (BENTO)':
                    self.import_directory_frm = LabelFrame(self.choice_frm, text='IMPORT MARS JSON DIRECTORY', pady=5, padx=5)
                    self.import_directory_select = FolderSelect(self.import_directory_frm, 'Input DIRECTORY:', lblwidth=25)
                    self.import_dir_btn = Button(self.import_directory_frm, fg='blue', text='Import directory to SimBA project', command= lambda: MarsImporter(config_path=self.config_path,
                                                                                                                                                      data_path=self.import_directory_select.folder_path,
                                                                                                                                                      interpolation_method=self.interpolation_dropdown.getChoices(),
                                                                                                                                                      smoothing_method={'Method': self.smoothing_dropdown.getChoices(), 'Parameters': {'Time_window': self.smoothing_time_eb.entry_get}}))

                    self.import_single_frm = LabelFrame(self.choice_frm, text='IMPORT MARS JSON FILE', pady=5, padx=5)
                    self.import_file_select = FileSelect(self.import_single_frm, 'Input FILE:', lblwidth=25)
                    self.import_file_btn = Button(self.import_single_frm, fg='blue', text='Import file to SimBA project', command= lambda: MarsImporter(config_path=self.config_path,
                                                                                                                                                      data_path=self.import_directory_select.folder_path,
                                                                                                                                                      interpolation_method=self.interpolation_dropdown.getChoices(),
                                                                                                                                                      smoothing_method={'Method': self.smoothing_dropdown.getChoices(),
                                                                                                                                                                        'Parameters': {'Time_window': self.smoothing_time_eb.entry_get}}))
                self.import_directory_frm.grid(row=2, column=0, sticky=NW)
                self.import_directory_select.grid(row=0, column=0, sticky=NW)
                self.import_dir_btn.grid(row=1, column=0, sticky=NW)

                self.import_single_frm.grid(row=3, column=0, sticky=NW)
                self.import_file_select.grid(row=0, column=0, sticky=NW)
                self.import_file_btn.grid(row=1, column=0, sticky=NW)

            elif data_type_choice in ['SLP (SLEAP)', 'H5 (multi-animal DLC)', 'TRK (multi-animal APT)', 'CSV (SLEAP)', 'H5 (SLEAP)']:
                self.animal_settings_frm = LabelFrame(self.choice_frm, text='ANIMAL SETTINGS', pady=5, padx=5)
                animal_cnt_entry_box = Entry_Box(self.animal_settings_frm, 'ANIMAL COUNT:', '25', validation='numeric')
                animal_cnt_entry_box.entry_set(val=self.project_animal_cnt)
                animal_cnt_confirm = Button(self.animal_settings_frm, text='CONFIRM', fg='blue', command=lambda: self.create_animal_names_entry_boxes(animal_cnt=animal_cnt_entry_box.entry_get))
                self.create_animal_names_entry_boxes(animal_cnt=animal_cnt_entry_box.entry_get)
                self.animal_settings_frm.grid(row=4, column=0, sticky=NW)
                animal_cnt_entry_box.grid(row=0, column=0, sticky=NW)
                animal_cnt_confirm.grid(row=0, column=1, sticky=NW)

                self.data_dir_frm = LabelFrame(self.choice_frm, text='DATA DIRECTORY', pady=5, padx=5)
                self.import_frm = LabelFrame(self.choice_frm, text='IMPORT', pady=5, padx=5)

                if data_type_choice == 'H5 (multi-animal DLC)':
                    self.tracking_type_frm = LabelFrame(self.choice_frm, text='TRACKING DATA TYPE', pady=5, padx=5)
                    self.dlc_data_type_option_dropdown = DropDownMenu(self.tracking_type_frm, 'Tracking type', Options.MULTI_DLC_TYPE_IMPORT_OPTION.value, labelwidth=25)
                    self.dlc_data_type_option_dropdown.setChoices(Options.MULTI_DLC_TYPE_IMPORT_OPTION.value[1])
                    self.tracking_type_frm.grid(row=5, column=0, sticky=NW)
                    self.dlc_data_type_option_dropdown.grid(row=0, column=0, sticky=NW)

                    self.data_dir_select = FolderSelect(self.data_dir_frm, 'H5 DLC DIRECTORY: ', lblwidth=25)
                    self.instructions_lbl = Label(self.data_dir_frm, text='Please import videos before importing the \n multi animal DLC tracking data')
                    self.run_btn = Button(self.import_frm, text='IMPORT DLC .H5', fg='blue', command= lambda: run_call(data_type=data_type_choice,
                                                                                                            interpolation=self.interpolation_dropdown.getChoices(),
                                                                                                            smoothing=self.smoothing_dropdown.getChoices(),
                                                                                                            smoothing_window=self.smoothing_time_eb.entry_get,
                                                                                                            animal_names=self.animal_name_entry_boxes,
                                                                                                            data_path=self.data_dir_select.folder_path,
                                                                                                            tracking_data_type=self.dlc_data_type_option_dropdown.getChoices()))

                elif data_type_choice == 'SLP (SLEAP)':
                    self.data_dir_select = FolderSelect(self.data_dir_frm, 'SLP SLEAP DIRECTORY: ', lblwidth=25)
                    self.instructions_lbl = Label(self.data_dir_frm, text='Please import videos before importing the \n multi animal SLEAP tracking data if you are tracking more than ONE animal')
                    self.run_btn = Button(self.import_frm, text='IMPORT SLEAP .SLP', fg='blue', command= lambda: run_call(data_type=data_type_choice,
                                                                                                               interpolation=self.interpolation_dropdown.getChoices(),
                                                                                                               smoothing=self.smoothing_dropdown.getChoices(),
                                                                                                               smoothing_window=self.smoothing_time_eb.entry_get,
                                                                                                               animal_names=self.animal_name_entry_boxes,
                                                                                                               data_path=self.data_dir_select.folder_path))

                elif data_type_choice == 'TRK (multi-animal APT)':
                    self.data_dir_select = FolderSelect(self.data_dir_frm, 'TRK APT DIRECTORY: ', lblwidth=25)
                    self.instructions_lbl = Label(self.data_dir_frm, text='Please import videos before importing the \n multi animal TRK tracking data')
                    self.run_btn = Button(self.import_frm, text='IMPORT APT .TRK', fg='blue', command= lambda: run_call(data_type=data_type_choice,
                                                                                                    interpolation=self.interpolation_dropdown.getChoices(),
                                                                                                    smoothing=self.smoothing_dropdown.getChoices(),
                                                                                                    smoothing_window=self.smoothing_time_eb.entry_get,
                                                                                                    animal_names=self.animal_name_entry_boxes,
                                                                                                    data_path=self.data_dir_select.folder_path))

                elif data_type_choice == 'CSV (SLEAP)':
                    self.data_dir_select = FolderSelect(self.data_dir_frm, 'CSV SLEAP DIRECTORY:', lblwidth=25)
                    self.instructions_lbl = Label(self.data_dir_frm, text='Please import videos before importing the sleap csv tracking data \n if you are tracking more than ONE animal')
                    self.run_btn = Button(self.import_frm, text='IMPORT SLEAP .CSV', fg='blue', command= lambda: run_call(data_type=data_type_choice,
                                                                                                               interpolation=self.interpolation_dropdown.getChoices(),
                                                                                                               smoothing=self.smoothing_dropdown.getChoices(),
                                                                                                               smoothing_window=self.smoothing_time_eb.entry_get,
                                                                                                               animal_names=self.animal_name_entry_boxes,
                                                                                                               data_path=self.data_dir_select.folder_path))

                elif data_type_choice == 'H5 (SLEAP)':
                    self.data_dir_select = FolderSelect(self.data_dir_frm, 'H5 SLEAP DIRECTORY', lblwidth=25)
                    self.instructions_lbl = Label(self.data_dir_frm, text='Please import videos before importing the sleap h5 tracking data \n if you are tracking more than ONE animal')
                    self.run_btn = Button(self.import_frm, text='IMPORT SLEAP H5', fg='blue', command= lambda: run_call(data_type=data_type_choice,
                                                                                                             interpolation=self.interpolation_dropdown.getChoices(),
                                                                                                             smoothing=self.smoothing_dropdown.getChoices(),
                                                                                                             smoothing_window=self.smoothing_time_eb.entry_get,
                                                                                                             animal_names=self.animal_name_entry_boxes,
                                                                                                             data_path=self.data_dir_select.folder_path))

                self.data_dir_frm.grid(row=self.frame_children(frame=self.choice_frm), column=0, sticky=NW)
                self.data_dir_select.grid(row=0, column=0, sticky=NW)
                self.instructions_lbl.grid(row=1, column=0, sticky=NW)
                self.import_frm.grid(row=self.frame_children(frame=self.choice_frm)+1, column=0, sticky=NW)
                self.run_btn.grid(row=0, column=0, sticky=NW)
            self.choice_frm.grid(row=1, column=0, sticky=NW)

        self.import_tracking_frm = LabelFrame(parent_frm, text='IMPORT TRACKING DATA', font=Formats.LABELFRAME_HEADER_FORMAT.value, fg='black')
        if not hasattr(self, 'config_path'):
            self.instructions_lbl = Label(self.import_tracking_frm, text='Please CREATE PROJECT CONFIG before importing tracking data \n')
            self.import_tracking_frm.grid(row=0, column=0, sticky=NW)
            self.instructions_lbl.grid(row=0, column=0, sticky=NW)
        else:
            self.config = read_config_file(config_path=self.config_path)
            self.project_animal_cnt = read_config_entry(config=self.config, section=ConfigKey.GENERAL_SETTINGS.value, option=ConfigKey.ANIMAL_CNT.value, data_type='int')
            self.data_type_dropdown = DropDownMenu(self.import_tracking_frm,'DATA TYPE:', Options.IMPORT_TYPE_OPTIONS.value, labelwidth=25, com=import_menu)
            self.data_type_dropdown.setChoices(Options.IMPORT_TYPE_OPTIONS.value[0])
            import_menu(data_type_choice=Options.IMPORT_TYPE_OPTIONS.value[0])
            self.import_tracking_frm.grid(row=idx_row, column=idx_column, sticky=NW)
            self.data_type_dropdown.grid(row=0, column=0, sticky=NW)


    def create_import_videos_menu(self,
                                  parent_frm: Frame,
                                  idx_row: int=0,
                                  idx_column: int=0):

        def run_import(multiple_videos: bool):
            if multiple_videos:
                check_if_dir_exists(in_dir=self.video_directory_select.folder_path)
                copy_multiple_videos_to_project(config_path=self.config_path,
                                                source=self.video_directory_select.folder_path,
                                                file_type=self.video_type.getChoices())
            else:
                check_file_exist_and_readable(file_path=self.video_file_select.file_path)
                copy_single_video_to_project(simba_ini_path=self.config_path, source_path=self.video_file_select.file_path)

        import_videos_frm = LabelFrame(parent_frm, text='IMPORT VIDEOS', fg='black', font=Formats.LABELFRAME_HEADER_FORMAT.value)
        if not hasattr(self, 'config_path'):
            self.instructions_lbl = Label(import_videos_frm, text='Please CREATE PROJECT CONFIG before importing VIDEOS \n')
            import_videos_frm.grid(row=0, column=0, sticky=NW)
            self.instructions_lbl.grid(row=0, column=0, sticky=NW)

        else:
            import_multiple_videos_frm = LabelFrame(import_videos_frm, text='IMPORT MULTIPLE VIDEOS')
            self.video_directory_select = FolderSelect(import_multiple_videos_frm, 'VIDEO DIRECTORY: ', lblwidth=25)
            self.video_type = DropDownMenu(import_multiple_videos_frm, 'VIDEO FILE FORMAT: ', Options.VIDEO_FORMAT_OPTIONS.value, '25')
            self.video_type.setChoices(Options.VIDEO_FORMAT_OPTIONS.value[0])
            import_multiple_btn = Button(import_multiple_videos_frm, text='Import MULTIPLE videos', fg='blue', command= lambda: run_import(multiple_videos=True))

            import_single_frm = LabelFrame(import_videos_frm, text='IMPORT SINGLE VIDEO', pady=5, padx=5)
            self.video_file_select = FileSelect(import_single_frm, "VIDEO PATH: ", title='Select a video file', lblwidth=25)
            import_single_btn = Button(import_single_frm, text='Import SINGLE video', fg='blue', command= lambda: run_import(multiple_videos=False))

            import_videos_frm.grid(row=0, column=0, sticky=NW)
            import_multiple_videos_frm.grid(row=0, sticky=W)
            self.video_directory_select.grid(row=1, sticky=W)
            self.video_type.grid(row=2, sticky=W)
            import_multiple_btn.grid(row=3, sticky=W)

            import_single_frm.grid(row=1, column=0, sticky=NW)
            self.video_file_select.grid(row=0, sticky=W)
            import_single_btn.grid(row=1, sticky=W)

            import_videos_frm.grid(row=idx_row, column=idx_column, sticky=NW)

    # def quit(self, e):
    #     self.main_frm.quit()
    #     self.main_frm.destroy()
    #
    # def callback(self, url):
    #     webbrowser.open_new(url)
    #
    # def move_app(self, e):
    #     print(f'+{e.x_root}+{e.y_root}')
    #     self.main_frm.geometry(f'+{e.x_root}+{e.y_root}')
    #     #print(f'+{e.x_root}x{e.y_root}')
    #     #self.main_frm.config(width=e.x_root, height=e.y_root)
    #     #self.main_frm.update()



# test = PopUpMixin(config_path='/Users/simon/Desktop/envs/troubleshooting/two_animals_16bp_032023/project_folder/project_config.ini',
#                   title='ss')
# test.create_import_pose_menu(parent_frm=test.main_frm)

# test = PopUpMixin(config_path='/Users/simon/Desktop/envs/troubleshooting/two_animals_16bp_032023/project_folder/project_config.ini',
#                   title='ss')
# test.create_import_videos_menu(parent_frm=test.main_frm)