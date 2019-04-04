CREATE TABLE emails (
  id VARCHAR NOT NULL,
  data json
);

CREATE TABLE email_events (
  id VARCHAR NOT NULL,
  data json
);

CREATE TABLE emails_with_events (
  id VARCHAR not null,
  data json
);

\set input `cat "/tmp/emails_with_events.json"`

with content as (select * from json_array_elements(:'input'))

insert into emails_with_events(id,data) select (to_json(c.value)->>'id')::VARCHAR, (to_json(c.value)) from content c
