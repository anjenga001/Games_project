create table raw_game_data(
    id INTEGER,
    name VARCHAR(20),
    rating_mean FLOAT,
    rating_count INT,
    genre VARCHAR(20),
    adult_only BOOLEAN
);
alter table raw_game_data
add column year int;





