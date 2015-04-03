create table people (
    id          integer primary key autoincrement not null,
    first_name  text,
    last_name   text,
    birth_date  date,
    created_at  date,
    updated_at  date
);
insert into people (id, first_name, last_name, birth_date, created_at) values
                   (1, "John", "Doe", "1985-06-17", date('now')),
                   (2, "Jane", "Doe", "1994-09-02", date('now')),
                   (3, "Kathy", "Holloway", "1994-09-02", date('now')),
                   (4, "Doug", "Robertson", "1994-09-02", date('now')),
                   (5, "Dylan", "MacFerson", "1994-09-02", date('now'));

create table stimuli_configurations (
    id                          integer primary key autoincrement not null,
    name                        text,
    consigne                    text,
    number_of_stimuli           integer,
    average_interval_time       double,
    random_interval_time_delta  double,
    display_duration            double,
    created_at                  date,
    updated_at                  date
);

insert into stimuli_configurations (id, name, consigne, number_of_stimuli, average_interval_time, random_interval_time_delta, display_duration, created_at) values
                                        (1, "Nombres impairs", "Cliquer lorsqu'un nombre impair apparait à l'écran", 50, 5.0, 1.5, 1.0, date('now')),
                                        (2, "Couleurs", "Cliquer lorsqu'un nom de couleur apparait à l'écran", 30, 3.0, 0.5, 1.0, date('now'));


create table stimuli_values (
    id                          integer primary key autoincrement not null,
    string_value                text,
    configuration_id            integer,
    authorized                  boolean,
    FOREIGN KEY(configuration_id) REFERENCES stimuli_testing_configurations(id)
);

insert into stimuli_values (id, string_value, configuration_id, authorized) values
                           (1, "1", 1, 1),
                           (2, "2", 1, 0),
                           (3, "3", 1, 1),
                           (4, "4", 1, 0),
                           (5, "5", 1, 1),
                           (6, "6", 1, 0),
                           (7, "7", 1, 1),
                           (8, "8", 1, 0),
                           (9, "9", 1, 1),
                           (100, "bleu", 2, 1),
                           (101, "rouge", 2, 1),
                           (102, "jaune", 2, 1),
                           (103, "vert", 2, 1),
                           (104, "maison", 2, 0),
                           (105, "chien", 2, 0),
                           (106, "chat", 2, 0),
                           (107, "voiture", 2, 0),
                           (108, "lettre", 2, 0),
                           (109, "feuille", 2, 0),
                           (110, "camion", 2, 0),
                           (111, "couteau", 2, 0),
                           (112, "table", 2, 0),
                           (113, "arbre", 2, 0),
                           (114, "plante", 2, 0),
                           (115, "rose", 2, 1),
                           (116, "banc", 2, 0);

create table stimuli_testing_sessions (
    id                          integer primary key autoincrement not null,
    person_id                   integer,
    configuration_name          text,
    started_at                  timestamp,
    FOREIGN KEY(person_id) REFERENCES people(id)
);

create table stimuli (
    id                          integer primary key autoincrement not null,
    session_id                  integer,
    string_value                text,
    valid                       boolean,
    correct                     boolean,
    display_time                time,
    action_time                 time,
    action_count                integer,
    FOREIGN KEY(session_id) REFERENCES stimuli_testing_sessions(id)
);