from datetime import date, timedelta


def count_sundays_1st_of_month(start_year: int, end_year: int) -> int:
    count = 0
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)
    current_date = start_date
    while current_date <= end_date:
        if current_date.day == 1 and current_date.weekday() == 6:
            count += 1
        current_date = current_date + timedelta(days=1)
    return count


if __name__ == "__main__":
    print(count_sundays_1st_of_month(1901, 2000))

