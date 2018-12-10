use std::fs::File;
use std::io;
use std::io::BufRead;

pub fn get_lines(filename: &str) -> io::Result<Vec<String>> {
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);
    return reader.lines().collect::<io::Result<Vec<String>>>();
}

pub fn get_numbers(filename: &str) -> io::Result<Vec<i64>> {
    get_lines(filename)?
        .iter()
        .map(|s| s.parse::<i64>())
        .collect::<Result<Vec<i64>, std::num::ParseIntError>>()
        .map_err(|e| io::Error::new(io::ErrorKind::Other, e))
}
