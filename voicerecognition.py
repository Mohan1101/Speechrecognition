import pandas as pd
import matplotlib.pyplot as plt
import deepspeech

# Load the dataset
dataset = pd.read_csv("../../Desktop/PANTECH NM PYTHON/example_dataset.csv")


# Function to retrieve column names
def get_column_names():
    return dataset.columns


# Function to check for null values
def check_null_values():
    return dataset.isnull().sum()


# Function to get dataset shape
def get_dataset_shape():
    return dataset.shape


# Function to display the first few rows of the dataset
def display_first_few_rows():
    return dataset.head()


# Function to calculate summary statistics
def calculate_summary_statistics():
    return dataset.describe()


# Function to generate a scatter plot
def generate_scatter_plot(x_column, y_column):
    plt.scatter(dataset[x_column], dataset[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()


# Create a DeepSpeech recognizer
model_path = "path/to/deepspeech/model.pb"
model = deepspeech.Model(model_path)

# Initialize the microphone
r = deepspeech.Recognizer(model)


# Function for speech recognition
def recognize_speech():
    with deepspeech.Microphone() as source:
        print("Say something!")
        audio = r.record(source)

    text = r.recognize(audio)
    return text


# Convert audio to text
retry_count = 3
while retry_count > 0:
    try:
        text = recognize_speech()
        print("You said: " + text)

        # Perform task based on user input
        if "column names" in text:
            print(get_column_names())
        elif "null values" in text:
            print(check_null_values())
        elif "dataset shape" in text:
            print(get_dataset_shape())
        elif "first few rows" in text:
            print(display_first_few_rows())
        elif "summary statistics" in text:
            print(calculate_summary_statistics())
        elif "scatter plot" in text:
            # Prompt the user for the x and y column names
            print("Enter the x-axis column name:")
            x_column = input()
            print("Enter the y-axis column name:")
            y_column = input()
            generate_scatter_plot(x_column, y_column)
        else:
            print("Sorry, I didn't understand what you said.")
        break
    except deepspeech.UnknownValueError:
        print("Speech recognition could not understand audio. Please try again.")
        retry_count -= 1
    except deepspeech.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
        break
