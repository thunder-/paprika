CREATE TABLE actions
(
  id           int not null auto_increment primary key,
  name         varchar(100) not null unique,
  value        varchar(4000) not null,
  description  varchar(255),
  type         varchar(255),
  properties   mediumtext,
  created_at   datetime not null,
  created_by   varchar(45) not null,
  updated_at   datetime not null,
  updated_by   varchar(45) not null
);

