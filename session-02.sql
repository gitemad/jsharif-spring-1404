-- SQLite
-- SELECT "title"
-- FROM "books"
-- WHERE "publisher_id" = (
--     SELECT "id"
--     FROM "publishers"
--     WHERE "publisher" = 'Fitzcarraldo Editions'
-- )

-- SELECT ROUND(AVG("rating"), 2) AS "average rating", COUNT(*) AS "count"
-- FROM "ratings"
-- WHERE "book_id" = (
--     SELECT "id"
--     FROM "books"
--     WHERE "title" = 'In Memory of Memory'
-- )

-- SELECT "name"
-- FROM "authors"
-- WHERE"id" = (
--     SELECT "author_id"
--     FROM "authored"
--     WHERE "book_id" = (
--         SELECT "id"
--         FROM "books"
--         WHERE "title" = 'Flights'
--     )
-- )

-- SELECT "title"
-- FROM "books"
-- WHERE "id" IN (
--     SELECT "book_id"
--     FROM "authored"
--     WHERE "author_id" = (
--         SELECT "id"
--         FROM "authors"
--         WHERE "name" = 'Fernanda Melchor'
--     )
-- )

-- SELECT "books"."title", "authors"."name"
-- FROM "books"
-- JOIN "authored" ON "books".id = "authored"."book_id"
-- JOIN "authors" ON "authored"."author_id" = "authors"."id";

-- SELECT "books"."title", "publishers"."publisher"
-- FROM "books"
-- JOIN "publishers" ON "books"."publisher_id" = "publishers".id;

-- SELECT "name"
-- FROM "authors"
-- INTERSECT
-- SELECT "name"
-- FROM "translators"

-- SELECT "name"
-- FROM "translators"
-- UNION
-- SELECT "name"
-- FROM "authors"

-- SELECT "name"
-- FROM "authors"
-- EXCEPT
-- SELECT "name"
-- FROM "translators"

-- SELECT "title", AVG("rating") AS "average rating"
-- FROM "books"
-- JOIN "ratings" ON "books"."id" = "ratings"."book_id"
-- GROUP BY "book_id"
-- HAVING "average rating" > 4
-- ORDER BY "average rating" DESC

-- SELECT "title", COUNT("rating") AS "count"
-- FROM "books"
-- JOIN "ratings" ON "books"."id" = "ratings"."book_id"
-- GROUP BY "book_id"

SELECT "title", AVG("rating") AS "average rating", COUNT("rating") AS "count"
FROM "books"
JOIN "ratings" ON "books"."id" = "ratings"."book_id"
GROUP BY "book_id"
HAVING "average rating" > 4 AND "count" > 5000
ORDER BY "average rating" DESC