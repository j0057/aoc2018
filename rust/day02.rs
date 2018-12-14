use std::collections::HashMap;

fn letter_count(word: &String) -> HashMap<char, u64> {
    let mut letters = HashMap::<char, u64>::new();
    for ch in word.chars() {
        *letters.entry(ch).or_insert(0) += 1;
    }
    return letters;
}

pub fn day02a(ids: &[String]) -> u64 {
    let counts = ids.iter().map(letter_count).collect::<Vec<_>>();
    return counts.iter().filter(|c| c.values().any(|&v| v == 2)).count();
}
