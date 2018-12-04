fn day01a(m: &[i64]) -> i64 {
    m.iter().sum()
}

mod util {
    use std::io::BufRead;

    pub fn get_numbers(filename: &str) -> std::io::Result<Vec<i64>> {
        let f = std::fs::File::open(filename)?;
        let f = std::io::BufReader::new(f);
        let n = f.lines().map(|s| s.unwrap().parse::<i64>().unwrap()).collect();
        Ok(n)
    }
}

#[cfg(test)]
mod test {
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
    fn test01a() -> std::io::Result<()> {
        let n = super::util::get_numbers("../input/day01.txt")?;
        let r = super::day01a(&n);
        assert_eq!(r, 508);
        Ok(())
    }
}
