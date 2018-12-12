mod util;
mod day01;
mod day02;

use std::error::Error;
use std::time;

type Solution = fn() -> Result<String, Box<Error>>;

fn get_puzzles() -> Vec<(u8, char, Solution)> {
    vec![
        (1, 'A', || {
            let day01 = util::get_numbers("../input/day01.txt")?;
            Ok(day01::day01a(&day01).to_string())
        }),
        (1, 'B', || {
            let day01 = util::get_numbers("../input/day01.txt")?;
            Ok(day01::day01b(&day01).to_string())
        }),
        (2, 'A', || {
            let day02 = [String::from("Hello, world!")];
            Ok(day02::day02a(&day02).to_string())
        }),
    ]
}

fn main() -> Result<(), Box<Error>> {
    let puzzles = get_puzzles();

    for (problem, part, solution) in puzzles.iter() {
        let start = time::SystemTime::now();
        let answer = solution()?;
        let elapsed = start.elapsed()?;
        let micros = elapsed.as_secs() * 1_000_000 + (elapsed.subsec_micros() as u64);
        println!("problem: {:>2}{}; time: {:9} μs, answer: {}", problem, part, micros, answer);
    }

    Ok(())
}
