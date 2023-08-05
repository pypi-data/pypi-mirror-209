import argparse
import os
from typing import Callable

from race_report.report import abbr_decoder, drivers_best_lap, build_report, print_report


AVAILABLE_FILE_NAMES = ['abbreviations.txt', 'end.log', 'start.log']


def parse_arguments():
    """Parse command line arguments. """
    parser = argparse.ArgumentParser(
        description="""Read data from two files, order racers by time and 
                       print 2 reports that shows the top 15 racers and others""")
    parser.add_argument("--files", "-f", type=str, metavar="", required=True, help="Path to folder with files")
    parser.add_argument("--driver", "-d", type=str, metavar="", help="Detail info about driver")
    parser.add_argument("--desc", action="store_true", help="Shows the list of drivers in reverse order")

    parse_args = parser.parse_args()
    return parse_args


def drivers_report_cli(args: Callable) -> None:
    """Prints the report of the drivers with their team and best lap time. """
    actual_file_names = os.listdir(args.files)
    if AVAILABLE_FILE_NAMES != actual_file_names:
        error_text = f"Folder {args.files} should contain 'abbreviations.txt', 'end.log', 'start.log'"
        print(error_text)
        return

    abbreviations_path = os.path.join(args.files, "abbreviations.txt")
    start_path = os.path.join(args.files, "start.log")
    end_path = os.path.join(args.files, "end.log")

    drivers_abbreviations = abbr_decoder(abbreviations_path)
    drivers_best_time = drivers_best_lap(start_path, end_path)
    report = build_report(drivers_abbreviations, drivers_best_time)

    try:
        if args.driver:
            driver = args.driver
            print(
                f"{report[driver]['place']}. {driver.title()} | {report[driver]['team']} | {report[driver]['best_lap']}")
        elif args.desc:
            print_report(report, desc=True)
        elif args.files:
            print_report(report)
    except KeyError:
        error_text = f"Driver '{args.driver}' is not found."
        raise KeyError(error_text)


if __name__ == "__main__":
    args = parse_arguments()
    drivers_report_cli(args)
