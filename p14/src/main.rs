// Longest Collatz sequence solving

fn count_sequence(n_start: usize, lookup: &mut Vec<u64>) -> u64 {
    let mut x = n_start;
    let mut seq = Vec::new();
    let mut length = 0;

    while x > 1 {
        if let Some(&l) = lookup.get(x) {
            if l > 0 {
                length = l;
                break;
            }
        }

        seq.push(x);

        if x % 2 != 0 {
            x = 3 * x + 1;
        } else {
            x = x / 2;
        }
    }

    for &value in seq.iter().rev() {
        length += 1;
        if let Some(slot) = lookup.get_mut(value) {
            *slot = length;
        }
    }

    length
}

fn main() {
    let nmax: usize = 1_000_000;
    let mut lookup = vec![0u64; nmax];
    let mut cur: u64 = 0;

    for i in 1..nmax {
        let a = count_sequence(i, &mut lookup);
        if a > cur {
            cur = a;
        }
    }
    println!("{:?}", cur)
}
