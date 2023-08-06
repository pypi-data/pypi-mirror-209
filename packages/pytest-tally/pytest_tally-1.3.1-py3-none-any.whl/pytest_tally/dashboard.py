import pickle
import time
from pathlib import Path

from rich.live import Live
from rich.progress import Progress
from rich.table import Table

FILE = Path("/Users/jwr003/coding/pytest-tally/data.pickle")

import pickle

from conftest import TestReportDistilled, TestSessionData

def get_data():
    try:
        with open("data.pickle", "rb") as pfile:
            return pickle.load(pfile)
    except (FileNotFoundError, EOFError):
        return TestSessionData(
            num_collected_tests=0,
            total_duration=0,
            reports={},
            session_started=False,
            session_finished=False,
        )


def generate_table() -> Table:
    table = Table()
    table.add_column("Test NodeId")
    table.add_column("Duration")
    table.add_column("Outcome")

    data = get_data()
    for report in data.reports:
        table.add_row(f"{report.node_id}", 0, f"{report.modified_outcome}")
    return table


def main():
    table = generate_table()
    while True:
        print("True loop 1")
        data = get_data()
        with Live(generate_table(), refresh_per_second=4) as live:
            while not data.session_finished:
                print("True loop 2")
                time.sleep(0.4)
                live.update(generate_table())
                data = get_data()

        while True:
            print("True loop 3")
            data = get_data()
            if not data.session_finished:
                break
            time.sleep(2)

if __name__ == "__main__":
    main()
