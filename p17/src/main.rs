enum NumberWord {
    One,
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Eleven,
    Twelve,
    Thirteen,
    Fourteen,
    Fifteen,
    Sixteen,
    Seventeen,
    Eighteen,
    Nineteen,
    Twenty,
    Thirty,
    Forty,
    Fifty,
    Sixty,
    Seventy,
    Eighty,
    Ninety,
    OneHundred,
    OneThousand,
}

impl NumberWord {
    fn as_str(&self) -> &'static str {
        match self {
            NumberWord::One => "one",
            NumberWord::Two => "two",
            NumberWord::Three => "three",
            NumberWord::Four => "four",
            NumberWord::Five => "five",
            NumberWord::Six => "six",
            NumberWord::Seven => "seven",
            NumberWord::Eight => "eight",
            NumberWord::Nine => "nine",
            NumberWord::Ten => "ten",
            NumberWord::Eleven => "eleven",
            NumberWord::Twelve => "twelve",
            NumberWord::Thirteen => "thirteen",
            NumberWord::Fourteen => "fourteen",
            NumberWord::Fifteen => "fifteen",
            NumberWord::Sixteen => "sixteen",
            NumberWord::Seventeen => "seventeen",
            NumberWord::Eighteen => "eighteen",
            NumberWord::Nineteen => "nineteen",
            NumberWord::Twenty => "twenty",
            NumberWord::Thirty => "thirty",
            NumberWord::Forty => "forty",
            NumberWord::Fifty => "fifty",
            NumberWord::Sixty => "sixty",
            NumberWord::Seventy => "seventy",
            NumberWord::Eighty => "eighty",
            NumberWord::Ninety => "ninety",
            NumberWord::OneHundred => "one hundred",
            NumberWord::OneThousand => "one thousand",
        }
    }
}

fn number_to_word(n: u64) -> Option<NumberWord> {
    match n {
        1 => Some(NumberWord::One),
        2 => Some(NumberWord::Two),
        3 => Some(NumberWord::Three),
        4 => Some(NumberWord::Four),
        5 => Some(NumberWord::Five),
        6 => Some(NumberWord::Six),
        7 => Some(NumberWord::Seven),
        8 => Some(NumberWord::Eight),
        9 => Some(NumberWord::Nine),
        10 => Some(NumberWord::Ten),
        11 => Some(NumberWord::Eleven),
        12 => Some(NumberWord::Twelve),
        13 => Some(NumberWord::Thirteen),
        14 => Some(NumberWord::Fourteen),
        15 => Some(NumberWord::Fifteen),
        16 => Some(NumberWord::Sixteen),
        17 => Some(NumberWord::Seventeen),
        18 => Some(NumberWord::Eighteen),
        19 => Some(NumberWord::Nineteen),
        20 => Some(NumberWord::Twenty),
        30 => Some(NumberWord::Thirty),
        40 => Some(NumberWord::Forty),
        50 => Some(NumberWord::Fifty),
        60 => Some(NumberWord::Sixty),
        70 => Some(NumberWord::Seventy),
        80 => Some(NumberWord::Eighty),
        90 => Some(NumberWord::Ninety),
        100 => Some(NumberWord::OneHundred),
        1000 => Some(NumberWord::OneThousand),
        _ => None,
    }
}

fn push_word(s: &mut String, n: u64) {
    if let Some(word) = number_to_word(n) {
        s.push_str(word.as_str());
    }
}

fn map_integer_to_str(n: u64) -> String {
    match number_to_word(n) {
        Some(word) => String::from(word.as_str()),
        None => {
            let mut s = String::from("");
            let hundreds = n / 100;
            let remainder = n % 100;
            let dozens = remainder / 10;
            let units = remainder % 10;

            if hundreds > 0 {
                push_word(&mut s, hundreds);
                if (dozens == 0) && (units == 0) {
                    s.push_str(" hundred");
                } else {
                    s.push_str(" hundred and ");
                }
            }
            if dozens == 1 {
                s.push_str(number_to_word(dozens * 10 + units).unwrap().as_str())
            } else if dozens > 0 {
                if units == 0 {
                    s.push_str(number_to_word(dozens * 10).unwrap().as_str())
                } else if units > 0 {
                    s.push_str(number_to_word(dozens * 10).unwrap().as_str());
                    s.push_str(" ");
                    s.push_str(number_to_word(units).unwrap().as_str())
                }
            } else if units > 0 {
                s.push_str(number_to_word(units).unwrap().as_str())
            }
            return s;
        }
    }
}

fn main() {
    let mut total: u64 = 0;
    for i in 1..=1000 {
        let s = map_integer_to_str(i);
        total += s.replace(" ", "").len() as u64;
    }
    dbg!(total);
}
