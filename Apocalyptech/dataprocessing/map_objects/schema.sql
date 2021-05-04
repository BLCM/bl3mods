drop table if exists object;
drop table if exists datatype;
drop table if exists submap;
drop table if exists map;

create table map
(
    id integer not null primary key autoincrement,
    name text not null,
    base_path text not null
);

create table submap
(
    id integer not null primary key autoincrement,
    mapid integer not null,
    name text not null,
    foreign key (mapid) references map (id)
);

create table datatype
(
    id integer not null primary key autoincrement,
    name text not null
);

create table object
(
    id integer not null primary key autoincrement,
    submapid integer not null,
    typeid integer not null,
    name text not null,
    foreign key (submapid) references submap (id),
    foreign key (typeid) references datatype (id)
);
