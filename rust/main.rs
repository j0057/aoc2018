mod util;
mod day01;
mod day02;

use std::error::Error;
use std::time;

fn get_puzzles() -> Result<Vec<(u8, char, Box<Fn() -> String>)>, Box<Error>> {
    let day01a = util::get_numbers("input/day01.txt")?;
    let day01b = day01a.clone();

    let day02a = util::get_lines("input/day02.txt")?;

    let result: Vec<(u8, char, Box<Fn() -> String>)> = vec![
        (1, 'A', Box::new(move || day01::day01a(&day01a).to_string())),
        (1, 'B', Box::new(move || day01::day01b(&day01b).to_string())),
        (2, 'A', Box::new(move || day02::day02a(&day02a).to_string())),
    ];
    Ok(result)
}

fn main() -> Result<(), Box<Error>> {
    let puzzles = get_puzzles()?;

    for (problem, part, solution) in puzzles.iter() {
        let start = time::SystemTime::now();
        let answer = solution();
        let elapsed = start.elapsed()?;
        let micros = elapsed.as_secs() * 1_000_000 + (elapsed.subsec_micros() as u64);
        println!("problem: {:>2}{}; time: {:9} μs, answer: {}", problem, part, micros, answer);
    }

    Ok(())
}
