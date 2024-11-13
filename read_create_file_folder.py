import os

def read_system_value(file_path='system_information.txt'):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


system_info_file_path = 'system_information.txt'

def create_main_folder(topic_name):
    # Get first alphabet
    # first_alphabet = var[0].upper()
    first_alphabet_of_topic = topic_name[0].upper()

    # Create folder
    folder_name = f"{first_alphabet_of_topic}"
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")


def create_genai_summary_file(topic_name, document):
    # Base filename
    first_alphabet =  topic_name[0].upper()
    # filename = topic_name

    # Extension
    extension = ".docx"

    # Initialize counter
    counter = 1

    # Check existing files
    while True:
        # Construct filename
        file_name = f"{topic_name}_{counter}{extension}"
        full_file_path = f"{first_alphabet}/{file_name}"

        # Check if file exists
        if not os.path.exists(full_file_path):
            # Create file
            # open(file_name, 'w').close()
            document.save(full_file_path)
            print(f"File '{full_file_path}' created successfully.")
            break
        counter += 1

