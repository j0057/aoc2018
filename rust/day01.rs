use std::collections::HashSet;

pub fn day01a(m: &[i32]) -> i32 {
    m.iter().sum()
}

pub fn day01b(deltas: &[i32]) -> i32 {
    let mut seen = HashSet::new();
    let mut freq: i32 = 0;
    seen.insert(0);
    loop {
        for delta in deltas.iter() {
            freq += delta;
            if seen.contains(&freq) {
                return freq;
            }
            seen.insert(freq);
        }
    }
}

#[cfg(test)]
mod test {
    use std::error::Error;

    use util;

    #[test]
    fn test01a0() {
        assert_eq!(super::day01a(&[1, -2, 3, 1]), 3);
    }

    #[test]
    fn test01a1() {
        assert_eq!(super::day01a(&[1, 1, 1]), 3);
    }

    #[test]
    fn test01a2() {
        assert_eq!(super::day01a(&[ 1, 1, -2]), 0);
    }

    #[test]
    fn test01a3() {
        assert_eq!(super::day01a(&[-1, -2, -3]), -6);
    }

    #[test]
    fn test01a() -> Result<(), Box<Error>> {
        let n = util::get_numbers("input/day01.txt")?;
        let r = super::day01a(&n);
        assert_eq!(r, 508);
        Ok(())
    }

    #[test]
    fn test01b0() {
        assert_eq!(super::day01b(&[1, -2, 3, 1]), 2);
    }

    #[test]
    fn test01b1() {
        assert_eq!(super::day01b(&[1, -1]), 0);
    }

    #[test]
    fn test01b2() {
        assert_eq!(super::day01b(&[3, 3, 4, -2, -4]), 10);
    }

    #[test]
    fn test01b3() {
        assert_eq!(super::day01b(&[-6, 3, 8, 5, -6]), 5);
    }

    #[test]
    fn test01b4() {
        assert_eq!(super::day01b(&[7, 7, -2, -7, -4]), 14);
    }

    #[test]
    fn test01b() -> Result<(), Box<Error>> {
        let n = util::get_numbers("input/day01.txt")?;
        let r = super::day01b(&n);
        assert_eq!(r, 549);
        Ok(())
    }
}
