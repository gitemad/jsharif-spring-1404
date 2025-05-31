-- SQLite
-- .timer ON
-- SELECT *
-- FROM "movies"
-- WHERE "title" = 'Cars';

-- EXPLAIN QUERY PLAN
-- SELECT *
-- FROM "movies"
-- WHERE "title" = 'Cars';

-- CREATE INDEX "title_index"
-- ON "movies" ("title")

-- EXPLAIN QUERY PLAN
-- SELECT "title"
-- FROM "movies"
-- WHERE "id" IN (
--     SELECT "movie_id"
--     FROM "stars"
--     WHERE "person_id" = (
--         SELECT "id"
--         FROM "people"
--         WHERE "name" = 'Tom Hanks'
--     )
-- );

-- CREATE INDEX "person_index" ON "stars" ("person_id", "movie_id");
-- CREATE INDEX "name_index" ON "people" ("name");

-- CREATE INDEX "recents" ON "movies" ("title")
-- WHERE "year" = 2023

-- EXPLAIN QUERY PLAN
-- SELECT "title"
-- FROM "movies"
-- WHERE "title" LIKE '%a'

-- DROP INDEX "person_index";

VACUUM;