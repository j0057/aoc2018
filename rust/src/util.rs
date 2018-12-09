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
