-- Tasks are steps that can be taken to complete a project
create table people (
    id          integer primary key autoincrement not null,
    first_name  text,
    last_name   text,
    birth_date  date
);