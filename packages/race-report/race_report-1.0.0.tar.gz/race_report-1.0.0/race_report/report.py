from datetime import datetime, timedelta

from prettytable import PrettyTable
from termcolor import colored


TABLE_FIELD_NAMES = ["Place", "Driver name", "Team", "Best lap"]
TIME_FORMAT = "%Y-%m-%d_%H:%M:%S.%f"
NUMBER_TOP_DRIVERS = 15  # The number of drivers who will be in the TOP table


def abbr_decoder(path_to_file: str) -> dict:
    """Decrypts abbreviations from a file.

    Returns:
        dict: A dictionary where the keys are driver abbreviations and the values are
              dictionaries with the driver's name and team information.

    The file should have lines in the format "DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER",
    where the underscore character (_) is used as a delimiter. Each line represents a driver,
    with the abbreviation, name, and team information separated by underscores.

    The driver abbreviation is used as the key in the resulting dictionary, and the corresponding
    value is a dictionary with the keys "name" and "team" mapping to the driver's name and team, respectively.
    """
    drivers_abbr = {}
    try:
        with open(path_to_file, "r") as file:
            for line in file:
                driver_data = line.strip().split("_")
                driver_abbr, driver_name, driver_team = driver_data[:3]
                drivers_abbr[driver_abbr] = {"name": driver_name, "team": driver_team}
            return drivers_abbr

    except FileNotFoundError as error:
        error_text = f"No such file or directory '{path_to_file}'"
        raise FileNotFoundError(error_text)
    except (PermissionError, IsADirectoryError, UnicodeDecodeError, IOError) as error:
        error_text = f"Failed to access or read the file - {error}"
        raise OSError(error_text)
    except Exception as error:
        error_text = f"An unexpected error occurred - {error}"
        raise Exception(error_text)


def read_race_data(path_to_file: str) -> dict:
    """Reads the race data from the specified file.

    Returns:
        dict: A dictionary with race data.

    Each line in the file should be in the format "SVF2018-05-24_12:02:58.917", where:
        SVF - racer abbreviation;
        2018-05-24 - date;
        12:02:58.917 - time;
    """
    drivers_lap_time = {}

    try:
        with open(path_to_file, "r") as file:
            for data in file:
                driver_data = data.strip()
                driver_abbr_start = driver_data[:3]
                lap_time = driver_data[3:]

                if driver_abbr_start not in drivers_lap_time:
                    drivers_lap_time[driver_abbr_start] = {}

                drivers_lap_time[driver_abbr_start] = lap_time
        return drivers_lap_time
    except FileNotFoundError as error:
        error_text = f"No such file or directory '{path_to_file}'"
        raise FileNotFoundError(error_text)
    except (PermissionError, IsADirectoryError, UnicodeDecodeError, IOError) as error:
        error_text = f"Failed to access or read the file - {error}"
        raise OSError(error_text)
    except Exception as error:
        error_text = f"An unexpected error occurred - {error}"
        raise Exception(error_text)


def drivers_best_lap(path_to_start_file: str, path_to_end_file: str) -> dict:
    """Retrieve the drivers with the best lap times.

    Returns:
        dict: A dictionary with drivers' best lap times.
    """
    drivers_best_lap = {}

    start_data = read_race_data(path_to_start_file)
    end_data = read_race_data(path_to_end_file)

    for driver_abbr in start_data:
        if driver_abbr not in end_data:
            error_text = f"Can't find {driver_abbr} in end.log"
            raise ValueError(error_text)

        start_time = start_data[driver_abbr]
        finish_time = end_data[driver_abbr]
        time_format = TIME_FORMAT

        driver_start_time = datetime.strptime(start_time, time_format)
        driver_finish_time = datetime.strptime(finish_time, time_format)
        result = driver_finish_time - driver_start_time
        if result < timedelta(0):
            warning_text = f"WARNING: Invalid time for {driver_abbr}. The result is not added to the overall rating."
            print(colored(warning_text, "red"))
            continue

        drivers_best_lap[driver_abbr] = str(result)[:-3]

    drivers_best_lap = dict(sorted(drivers_best_lap.items(), key=lambda item: item[1]))
    return drivers_best_lap


def build_report(drivers_abbr: dict, drivers_best_lap: dict) -> dict:
    """Builds a report of the drivers with their team and best lap time.

    Args:
        drivers_abbr (dict): A dictionary containing driver abbreviations and their corresponding information.
        drivers_best_lap (dict): A dictionary containing the drivers and their best lap times.

    Returns:
        dict: A dictionary with the drivers' names, teams, and best lap times.

    The function takes the driver abbreviations, looks up their information in the drivers_abbr dictionary,
    and constructs a report containing the driver's name, team, and best lap time for the drivers.
    """
    drivers_best_lap_report = {}
    try:
        for place, driver_abbr in enumerate(drivers_best_lap, 1):
            driver_name = drivers_abbr[driver_abbr]["name"]
            driver_team = drivers_abbr[driver_abbr]["team"]
            driver_time = drivers_best_lap[driver_abbr]

            drivers_best_lap_report[driver_name] = {"team": driver_team,
                                                    "best_lap": driver_time,
                                                    "place": place}
        return drivers_best_lap_report
    except KeyError as error:
        error_text = f"Invalid data at some driver abbreviation: {error}"
        raise KeyError(error_text)


def print_report(drivers_best_lap: dict, desc: bool = False) -> bool:
    """Prints the report of the drivers with their team and best lap time.

    Args:
        drivers_best_lap (dict): A dictionary containing the top 15 drivers' names, teams, and best lap times.
        desc (bool, optional): Flag indicating whether to print the report in descending order. Defaults to False.
    Returns:
        bool: True if the report is printed successfully.

    The function prints the two reports:
        1. Top 15 drivers with their corresponding team and best lap time.
        2. Another drivers with their corresponding team and best lap time.
    The report is displayed in a tabular format using the PrettyTable library.
    """
    if desc:
        drivers_best_lap = {key: value for key, value in reversed(drivers_best_lap.items())}

    try:
        ptable = PrettyTable()
        ptable.field_names = TABLE_FIELD_NAMES
        for driver in drivers_best_lap:
            driver_team = drivers_best_lap[driver]["team"]
            driver_time = drivers_best_lap[driver]["best_lap"]
            driver_place = drivers_best_lap[driver]["place"]

            ptable.add_row([str(driver_place) + ".", driver, driver_team, driver_time])
            # If the value of the variable desc is False, print the first table when the driver's place is equal to the constant NUMBER_TOP_DRIVERS
            # to create the second table with other drivers.
            # If the value of the variable desc is True, print the first table until NUMBER_TOP_DRIVERS to create the second table with the top drivers.
            if driver_place == NUMBER_TOP_DRIVERS and not desc or driver_place == NUMBER_TOP_DRIVERS + 1 and desc:
                print(ptable)
                ptable.clear_rows()
        if len(ptable._rows) > 0:  # If there are drivers for the second table
            print(ptable)
    except KeyError as error:
        error_text = f"Invalid data at some driver: {error}"
        raise KeyError(error_text)
