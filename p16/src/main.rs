fn solve(n: u32) -> u32 {
    let mut digits = vec![1u8];

    for _ in 0..n {
        let mut carry = 0;

        for d in digits.iter_mut() {
            let x = *d * 2 + carry;
            *d = x % 10;
            carry = x / 10;
        }

        while carry > 0 {
            digits.push(carry % 10);
            carry /= 10;
        }
    }

    digits.iter().map(|&d| d as u32).sum()
}

fn main() {
    dbg!(solve(1000));
}
