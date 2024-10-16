# view_parquet - view parquet files
# Joe Zirilli @2024 jszirilli@gmail.com

import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pandasgui import show


def select_parquet_file():
    
    root = tk.Tk()  # Create a Tkinter root window
    root.withdraw()  # Hide the root window

    # Open a file dialog and return the selected file path
    file_path = filedialog.askopenfilename(
        title='Select a parquet file or Cancel to quit',
        filetypes=(('Parquet files', '*.parquet'), ('All files', '*.*'))
    )
    
    return file_path


if __name__ == '__main__':
    parquet_file = select_parquet_file()
    while parquet_file:
        try:
            print('Processing - please wait')
            data = pd.read_parquet(parquet_file)
            show(data)
        except Exception as e:
            print(f'ERROR: {e}')
        parquet_file = select_parquet_file()
