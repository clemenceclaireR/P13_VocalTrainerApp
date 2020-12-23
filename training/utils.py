import random
from tkinter import messagebox
# import simpleaudio as sa


# def play_given_sound(given_sound):
#     """
#     Find and play sound according to its name
#     """
#     son = sa.WaveObject.from_wave_file('resources/sounds/{}.wav'.format(given_sound))
#     son.play()


def read_sound_list(filename):
    """
    Iter through file containing sounds information
    store and return it
    """
    # Step 1 : file content read
    sound_list_file = open(filename, "r")
    file_content = sound_list_file.read()
    sound_list_file.close()

    # Step 2 : Mac/Windows line separator replacement :
    file_content.replace("\r\n", "\n")
    file_content.replace("\r", "\n")

    # Step 3 :
    lines = file_content.split("\n")

    # For each line :
    sound_list = []
    for line in lines:
        if len(line) > 0:
            current_line_info = line.split("\t")

            if len(current_line_info) != 4:
                print(line)
                messagebox.showerror("Error", "Error in line {}: Each line should contain 4 columns.".format(line))
                return

            sound_id = (current_line_info[0])
            sound_file_name = current_line_info[1]
            sound_name = current_line_info[2]
            associated_number = (current_line_info[3])

            current_sound = sound_id, sound_file_name, sound_name, associated_number

            sound_list.append(current_sound)

    return sound_list


def get_sound_by_id(sound_id, sound_list):
    """
    Play sounds by its id in given sound list
    """
    for sound in sound_list:
        if sound[0] == sound_id:
            return sound

    messagebox.showerror("Error", "Unable to find the given ID")


def get_sound_by_name(sound_name, sound_list):
    """
    Play sounds by its name in given sound list
    """
    for sound in sound_list:
        if sound[2] == sound_name:
            return sound

    messagebox.showerror("Unable to find the given name")


def sound_random_choice(sound_list):
    """
    Selects a random sound and its associated information
    and returns it:
    """
    random_selection = random.choice(sound_list)
    print(random_selection)
    return random_selection


# def play_sound(sound):
#     """
#     Play given sound
#     """
#     son = sa.WaveObject.from_wave_file(sound)
#     son.play()