# Video_game ETL Pipeline
## Overview
This is an end to end pipeline that gets data from an API, transforms it using python and loads it for further analysis using SQL

## Tech stack
- Python(pandas, requests, json)
- PostgreSQL
- SQL
- DataGrip
- VScode
- Git

## ETL Process
###Extract
Pulled data from gameBrain API (https://gamebrain.co/). Pulled all pc game data from past year and    used 'time.sleep' to limit time between requests(API constraint). Data stored as JSON. API requires access key so made use of '.env' file.

### Transform
Imported Pandas to clean. Removed unnecessary columns such as 'images'. Removed entries with important missing values.

### Load
Stored cleaned data into CSV file
Used SQL for normalization

### Database structure
- **game_data**
Contains all game info from csv: Id, name, genre, etc.

- **normalized tables**
Made use of 'primary' and 'foreign' keys to create a 'games' table and 'rating' table.

## Project Structure
```text
GAMES/
--datascripts/
--game_scripts/
--games_last_year.csv
--pc_games_last_year.json
--.gitignore
--README.md




