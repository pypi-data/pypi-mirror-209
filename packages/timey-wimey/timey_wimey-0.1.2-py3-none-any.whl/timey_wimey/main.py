import sys
from typing import Optional, List
import sentinel

import dateparser
import pendulum
import typer
import tzlocal

app = typer.Typer()

valid_interval_types = [
    "years",
    "months",
    "weeks",
    "days",
    "hours",
    "minutes",
    "seconds"
]

def parse_range(range_str: str):
    split_range = range_str.split(" ")

    if len(split_range) > 2:
        raise ValueError(f"Range string must be a max of two words. It is {len(split_range)}")

    try:
        number = int(split_range[0])
    except ValueError:
        raise ValueError(f"{split_range[0]} is not a valid integer.")

    interval_type = split_range[1]

    if interval_type[-1] != 's':
        interval_type = interval_type + 's'

    if interval_type not in valid_interval_types:
        raise ValueError(f"{interval_type} not in {','.join(valid_interval_types)}")

    return number,interval_type


def print_date(date_obj: pendulum.DateTime,format: Optional[str] = None):

    if format:
        typer.echo(date_obj.strftime(format))
    else:
        typer.echo(date_obj)


@app.command()
def date(
    date_string: str,
    to: Optional[str] = typer.Option(None, help="An optional end time to go to."),
    time_zone: Optional[str] = typer.Option(None,help="Optional timezone to use."),
    format: Optional[str] = typer.Option(None,help="Stftime format to use."),
    interval: Optional[str] = typer.Option(
        "1 hours", help="Interval to use if a range. Should be like `2 days` or `37 minutes`"
    ),
):

    if time_zone is None:
        time_zone = tzlocal.get_localzone_name()

    parsed_start = dateparser.parse(date_string)

    start_date = pendulum.parse(str(parsed_start))

    if not parsed_start.tzinfo:
        local_tz = pendulum.timezone(time_zone)
        start_date = local_tz.convert(start_date)

    print_date(start_date,format)
    if to is None:
        exit(0)

    end_date = pendulum.parse(str(dateparser.parse(to)))

    period = pendulum.period(start_date,end_date)

    amount,unit = parse_range(interval)

    for dt in period.range(unit,amount):
        print_date(dt,format)

if __name__ == "__main__":
    app()
