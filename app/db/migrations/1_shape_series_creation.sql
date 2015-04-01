create table shape_configurations (
    id                  integer primary key autoincrement not null,
    name                text,
    display_duration    double,
    show_delay          double
);

create table shape_series (
    id                          integer primary key autoincrement not null,
    configuration_id            integer,
    FOREIGN KEY(configuration_id) REFERENCES shape_configurations(id)
);

create table shapes (
    id                          integer primary key autoincrement not null,
    serie_id                   integer,
    filename                    text,
    FOREIGN KEY(serie_id) REFERENCES shape_series(id)
);

INSERT INTO shape_configurations (id, name) VALUES (1, "Puzzle");
INSERT INTO shape_series (id, configuration_id) VALUES (1, 1),(2, 1),(3, 1);
INSERT INTO shapes (id, serie_id, filename) VALUES (1, 1, 'assets/images/shapes/jigsaw_1_1.svg'),
                                                   (2, 1, 'assets/images/shapes/jigsaw_1_2.svg'),
                                                   (3, 1, 'assets/images/shapes/jigsaw_1_3.svg'),
                                                   (4, 1, 'assets/images/shapes/jigsaw_1_4.svg'),
                                                   (5, 2, 'assets/images/shapes/jigsaw_2_1.svg'),
                                                   (6, 2, 'assets/images/shapes/jigsaw_2_2.svg'),
                                                   (7, 2, 'assets/images/shapes/jigsaw_2_3.svg'),
                                                   (8, 2, 'assets/images/shapes/jigsaw_2_4.svg'),
                                                   (9, 3, 'assets/images/shapes/jigsaw_3_1.svg'),
                                                   (10, 3, 'assets/images/shapes/jigsaw_3_2.svg'),
                                                   (11, 3, 'assets/images/shapes/jigsaw_3_3.svg'),
                                                   (12, 3, 'assets/images/shapes/jigsaw_3_4.svg');

create table shape_sessions (
    id                  integer primary key autoincrement not null,
    person_id           integer,
    configuration_id    integer,
    date                date,
    FOREIGN KEY(person_id) REFERENCES people(id),
    FOREIGN KEY(configuration_id) REFERENCES shape_configurations(id)
);

create table shape_session_series (
    id                  integer primary key autoincrement not null,
    session_id          integer,
    serie_id            integer,
    expected_shape_id   integer,
    selected_shape_id   integer,
    display_time        time,
    action_time         time,
    FOREIGN KEY(session_id)         REFERENCES shape_sessions(id),
    FOREIGN KEY(serie_id)           REFERENCES shape_series(id),
    FOREIGN KEY(expected_shape_id)  REFERENCES shapes(id),
    FOREIGN KEY(selected_shape_id)  REFERENCES shapes(id)
);