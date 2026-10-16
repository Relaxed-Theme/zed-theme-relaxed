//! A calm little module to showcase the Relaxed theme.

use std::collections::HashMap;
use std::fmt;

const API_URL: &str = "https://api.example.com/hammocks";
const MAX_SWING: f32 = 0.75;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum Mood {
    Chill,
    Sleepy,
    Focused,
}

#[derive(Debug, Clone)]
pub struct Hammock<'a> {
    pub id: u32,
    pub label: &'a str,
    pub mood: Mood,
    pub swing: Option<f32>,
}

pub trait Describe {
    fn describe(&self) -> String;
}

impl Describe for Mood {
    fn describe(&self) -> String {
        match self {
            Mood::Chill => "Taking it easy".into(),
            Mood::Sleepy => "Almost asleep".into(),
            Mood::Focused => String::from("In the zone"),
        }
    }
}

impl fmt::Display for Hammock<'_> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "#{:03} {:<12} ({:?})", self.id, self.label, self.mood)
    }
}

impl<'a> Hammock<'a> {
    pub fn is_swinging(&self) -> bool {
        self.swing.is_some_and(|s| s > 0.0 && s <= MAX_SWING)
    }
}

fn fetch_hammocks(limit: u32) -> Result<Vec<Hammock<'static>>, String> {
    if limit == 0 {
        return Err(format!("nothing to fetch from {API_URL}"));
    }
    let moods = [Mood::Chill, Mood::Sleepy, Mood::Focused];
    Ok((1..=limit)
        .map(|i| Hammock {
            id: i,
            label: "hammock",
            mood: moods[(i as usize) % moods.len()],
            swing: if i % 2 == 0 { Some(0.5) } else { None },
        })
        .collect())
}

fn main() -> Result<(), String> {
    let hammocks = fetch_hammocks(5)?;
    let mut by_mood: HashMap<Mood, usize> = HashMap::new();

    for hammock in hammocks.iter().filter(|h| h.is_swinging()) {
        *by_mood.entry(hammock.mood).or_default() += 1;
        println!("{hammock} {}", hammock.mood.describe());
    }

    println!("{} moods swinging", by_mood.len());
    Ok(())
}
