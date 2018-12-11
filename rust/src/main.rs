mod util;
mod day01;
mod day02;

use std::collections;
use std::error::Error;
use std::time;

type Solution = fn() -> Result<String, Box<Error>>;

fn main() -> Result<(), Box<Error>> {
    let mut problems: collections::HashMap<&str, Solution> = collections::HashMap::new();

    problems.insert("1A", || {
        let day01 = util::get_numbers("../input/day01.txt")?;
        Ok(day01::day01a(&day01).to_string())
    });

    problems.insert("1B", || {
        let day01 = util::get_numbers("../input/day01.txt")?;
        Ok(day01::day01b(&day01).to_string())
    });

    problems.insert("2A", || {
        let day02 = [String::from("Hello, world!")];
        Ok(day02::day02a(&day02).to_string())
    });

    for &problem in problems.keys() {
        let start = time::SystemTime::now();
        let answer = problems[problem]()?;
        let elapsed = start.elapsed()?;
        let micros = elapsed.as_secs() * 1_000_000 + (elapsed.subsec_micros() as u64);
        println!("problem: {:>3}; time: {:9} μs, answer: {}", problem, micros, answer);
    }

    Ok(())
}
