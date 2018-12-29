use std::collections::HashMap;

fn letter_count(word: &str) -> HashMap<char, u64> {
    let mut letters = HashMap::<char, u64>::new();
    for ch in word.chars() {
        *letters.entry(ch).or_insert(0) += 1;
    }
    return letters;
}

pub fn day02a<T: AsRef<str>>(ids: &[T]) -> u64 {
    let counts = ids.iter().map(|s| letter_count(s.as_ref())).collect::<Vec<_>>();
    return counts.iter().filter(|c| c.values().any(|&v| v == 2)).count() as u64
         * counts.iter().filter(|c| c.values().any(|&v| v == 3)).count() as u64;
}

#[cfg(test)]
mod test {
    use std::error::Error;

    use util;

    #[test]
    fn test02a1() {
        assert_eq!(super::day02a(&["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]), 12);
    }

    #[test]
    fn test02a() -> Result<(), Box<Error>> {
        let s = util::get_lines("input/day02.txt")?;
        let r = super::day02a(&s);
        assert_eq!(r, 8892);
        Ok(())
    }
}
