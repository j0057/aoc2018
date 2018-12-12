use std::error;
use std::fs::File;
use std::io;
use std::io::BufRead;

pub fn get_lines(filename: &str) -> Result<Vec<String>, Box<error::Error>> {
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);
    let result = reader.lines().collect::<Result<Vec<String>, io::Error>>()?;
    Ok(result)
}

pub fn get_numbers(filename: &str) -> Result<Vec<i64>, Box<error::Error>> {
    let result = get_lines(filename)?
        .iter()
        .map(|s| s.parse::<i64>())
        .collect::<Result<Vec<i64>, std::num::ParseIntError>>()?;
    Ok(result)
}
