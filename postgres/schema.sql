CREATE TABLE emails (
  id serial NOT NULL,
  data json
);

CREATE TABLE email_events (
  id serial NOT NULL,
  data json
);

CREATE TABLE emails_with_events (
  id serial not null,
  data json
);

\set content `cat "/data/postgres/emails_with_events.json"`

insert into emails_with_events(data) values (json_array_elements(:'content')::json);


\set content `cat "/data/postgres/emails_with_events2.json"`

insert into emails_with_events(data) values (json_array_elements(:'content')::json)