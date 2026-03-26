create table games(
    id integer primary key,
    name varchar(20),
    genre varchar(20),
    year int,
    adult_only boolean
);

create table ratings(
    id integer primary key,
    foreign key(id) references games(id),
    rating_count int,
    rating_mean float
);

insert into games (id, name, genre, year, adult_only)
select id, name, genre, year, adult_only
from raw_game_data;

insert into ratings (id, rating_mean, rating_count)
select id, rating_mean, rating_count
from raw_game_data;
