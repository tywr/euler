fn factorial_digit_sum(n: i32) -> i32 {
    let mut v = vec![1];
    let mut carry = 0;
    for n in 1..=n {
        let l = v.len();
        for i in 0..l {
            let cur = v[i] * n + carry;
            v[i] = cur % 10;
            carry = cur / 10;
        }
        while carry != 0 {
            v.push(carry % 10);
            carry /= 10;
        }
    }
    v.iter().sum()
}

fn main() {
    let c = factorial_digit_sum(100);
    println!("Result is {c:?}");
}
