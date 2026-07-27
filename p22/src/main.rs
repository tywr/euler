use std::collections::HashMap;
use std::fs;

fn score(rank: u32, name: &str) -> u32 {
    let ls: u32 = name.chars().map(|c| (c as u32) - ('A' as u32) + 1).sum();
    rank * ls
}

fn main() {
    let text = fs::read_to_string("p22/names.txt")
        .expect("There should have been a file.")
        .trim_end()
        .to_string();

    let mut sorted_names: Vec<&str> = text.split(',').map(|name| name.trim_matches('"')).collect();
    sorted_names.sort_unstable();

    let total: u32 = sorted_names
        .iter()
        .enumerate()
        .map(|(rank, name)| score((rank + 1) as u32, name))
        .sum();

    println!("{total}");
}
