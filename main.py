import pywhatkit
import datetime
import os

# Phone Number of the Contact
RECIPIENT_NUMBER = "+xxxxxxxxxxxxx"

# main function
def main():
    # Foreach .txt file in the directory
    directory = os.getcwd()
    message = ""
        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"): 
            message += handle_txt_files(os.path.join(directory, filename))
        else:
            continue

    message += "Viel Erfolg beim Lernen! (^-^)"
    print(message)

    # Send a WhatsApp Message to a Contact at 9:30 AM
    try:
        pywhatkit.sendwhatmsg(RECIPIENT_NUMBER, message, 9, 30)
    except:
        print("An Error Occurred!")


# Function handle the .txt files to get the message
def handle_txt_files(file):
    message = ""

    # Days until the Exam
    date_of_exam = read_first_line(file)
    filename = os.fsdecode(file)
    name_of_exam = os.path.splitext(os.path.basename(filename))[0]
    days = (datetime.datetime.strptime(date_of_exam, "%Y-%m-%d") - datetime.datetime.now()).days

    # Message to be Sent
    if days > 1:
        message += "Noch " + str(days) + " Tage bis zur " + name_of_exam + " Klausur!\n"
    elif days == 1:
        message += "Morgen ist die " + name_of_exam + " Klausur!\n"

    return message

# Function to Read First Line of File
def read_first_line(file):
    with open(file, 'r') as f:
        first_line = f.readline()
        return first_line

if __name__ == "__main__":
    main()
