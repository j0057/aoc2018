mod day01;

fn main() -> std::io::Result<()> {
    let day01 = day01::util::get_numbers("../input/day01.txt")?;

    println!("Day 01A: {}", day01::day01a(&day01));
    println!("Day 01B: {}", day01::day01b(&day01));

    Ok(())
}
