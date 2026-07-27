use chrono::{Datelike, Duration, NaiveDate, Weekday};

fn count_sundays(start_year: i32, end_year: i32) -> i32 {
    let mut count = 0;
    let start_date = NaiveDate::from_ymd_opt(start_year, 1, 1).unwrap();
    let end_date = NaiveDate::from_ymd_opt(end_year, 12, 31).unwrap();
    let mut current_date = start_date;
    while current_date <= end_date {
        if (current_date.day() == 1) & (current_date.weekday() == Weekday::Sun) {
            count += 1;
        }
        current_date += Duration::days(1);
    }
    count
}

fn main() {
    let c = count_sundays(1901, 2000);
    println!("Result is {c:?}");
}
