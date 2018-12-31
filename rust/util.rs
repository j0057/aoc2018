use std::error;
use std::fs::File;
use std::io;
use std::io::BufRead;
use std::num::ParseIntError;

pub fn get_lines(filename: &str) -> Result<Vec<String>, Box<error::Error>> {
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);
    let result = reader.lines().collect::<Result<Vec<String>, io::Error>>()?;
    Ok(result)
}

pub fn get_numbers<T>(filename: &str) -> Result<Vec<T>, Box<error::Error>>
where T: std::str::FromStr<Err=ParseIntError> {
    let result = get_lines(filename)?
        .iter()
        .map(|s| s.parse::<T>())
        .collect::<Result<Vec<T>, ParseIntError>>()?;
    Ok(result)
}
