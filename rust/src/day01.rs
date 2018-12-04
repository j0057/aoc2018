fn day01a(m: &[i64]) -> i64 {
    m.iter().sum()
}

mod util {
    use std::fs::File;
    use std::io;
    use std::io::BufRead;

    pub fn get_numbers(filename: &str) -> io::Result<Vec<i64>> {
        let file = File::open(filename)?;
        let reader = io::BufReader::new(file);
        let lines = reader.lines().collect::<io::Result<Vec<String>>>()?;
        lines
            .iter()
            .map(|s| s.parse::<i64>())
            .collect::<Result<Vec<i64>, std::num::ParseIntError>>()
            .map_err(|e| io::Error::new(io::ErrorKind::Other, e))
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
