drop table if exists bl3refs;
drop table if exists bl3object;

create table bl3object
(
    id int not null auto_increment,
    name varchar(512) character set latin1 not null,
    primary key (id),
    unique index idx_name (name)
) engine=innodb;

create table bl3refs
(
    from_obj int not null,
    to_obj int not null,
    unique index idx_from (from_obj, to_obj),
    index idx_to (to_obj, from_obj)
) engine=innodb;

