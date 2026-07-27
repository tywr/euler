use std::collections::{BTreeSet, HashMap};

fn get_divisors(n: u32) -> BTreeSet<u32> {
    let mut divs = BTreeSet::new();
    let nmax = (n as f64).sqrt() as u32;
    for i in 1..=nmax {
        if n % i == 0 {
            divs.insert(i);
            divs.insert(n / i);
        }
    }
    divs
}

fn sum_proper_divisors(n: u32) -> u32 {
    let divs = get_divisors(n);
    let s: u32 = divs.iter().sum();
    s - n
}

fn get_amicable_pairs(n: u32) -> BTreeSet<(u32, u32)> {
    let mut d: HashMap<u32, u32> = HashMap::new();
    for i in 0..n {
        d.insert(i, sum_proper_divisors(i));
    }

    let mut pairs = BTreeSet::new();
    for (n, v) in &d {
        if let Some(sd) = d.get(v) {
            if (sd == n) & (n != v) {
                pairs.insert((*n.min(v), *n.max(v)));
            }
        }
    }
    pairs
}

fn main() {
    let s: u32 = get_amicable_pairs(10_000).iter().map(|(x, y)| x + y).sum();
    dbg!(s);
}
