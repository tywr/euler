use std::cmp;

fn binomial(k: u64, n: u64) -> u64 {
    if k > n {
        return 0;
    }

    let k = cmp::min(k, n - k);
    let mut res = 1;
    for i in 1..k + 1 {
        res = res * (n - k + i) / i;
    }
    return res;
}

fn main() {
    dbg!(binomial(20, 40));
}
