-- SQLite
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

-- CREATE VIEW "longlist" AS
-- SELECT "name", "title"
-- FROM "books"
-- JOIN "authored" ON "authored"."book_id" = "books"."id"
-- JOIN "authors" ON "authored"."author_id" = "authors"."id";

-- SELECT "title"
-- FROM "longlist"
-- WHERE "name" = 'Fernanda Melchor'

-- CREATE VIEW "average_book_ratings" AS
-- SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating"
-- FROM "ratings"
-- JOIN "books" ON "ratings"."book_id" = "books"."id"
-- GROUP BY "book_id"

-- SELECT "year", ROUND(AVG("rating"), 2) AS "rating"
-- FROM "average_book_ratings"
-- GROUP BY "year"

-- DROP VIEW "average_book_ratings"

-- WITH "average_book_ratings" AS (
--     SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating"
--     FROM "ratings"
--     JOIN "books" ON "books"."id" = "ratings"."book_id"
--     GROUP BY "book_id"
-- )
-- SELECT "year", ROUND(AVG("rating"), 2) AS "rating"
-- FROM "average_book_ratings"
-- GROUP BY "year"

-- CREATE VIEW "2022" AS
-- SELECT "id", "title"
-- FROM "books"
-- WHERE "year" = 2022

-- SELECT *
-- FROM "2022"

-- ALTER TABLE "books"
-- ADD COLUMN "deleted" INTEGER DEFAULT 0

-- UPDATE "books"
-- SET "deleted" = 1
-- WHERE "title" = 'Whale'

-- CREATE VIEW "current_books" AS
-- SELECT *
-- FROM "books"
-- WHERE "deleted" = 0

-- CREATE TRIGGER "delete_current_book"
-- INSTEAD OF DELETE ON "current_books"
-- FOR EACH ROW
-- BEGIN
--     UPDATE "books"
--     SET "deleted" = 1
--     WHERE "id" = OLD."id";
-- END;

-- SELECT *
-- FROM "sqlite_master"
-- WHERE "type"='trigger'

-- DELETE FROM "current_books"
-- WHERE "title" = 'Pyre';

-- CREATE TRIGGER "insert_book_when_exists"
-- INSTEAD OF INSERT ON "current_books"
-- FOR EACH ROW
-- WHEN NEW."isbn" IN (
--     SELECT "isbn"
--     FROM "books"
-- )
-- BEGIN
--     UPDATE "books"
--     SET "deleted" = 0
--     WHERE "isbn" = NEW."isbn";
-- END;

-- INSERT INTO "current_books"
--     ("isbn", "title", "publisher_id", "format", "pages", "published", "year")
--     VALUES
--     (9781628971538, 'Whale', 3, 'paperback', 368, '2023-01-19', 2023)

-- CREATE TRIGGER "insert_book_when_new"
-- INSTEAD OF INSERT ON "current_books"
-- FOR EACH ROW
-- WHEN NEW."isbn" NOT IN (
--     SELECT "isbn"
--     FROM "books"
-- )
-- BEGIN
--     INSERT INTO "books" (
--         "isbn",
--         "title",
--         "publisher_id",
--         "format",
--         "pages",
--         "published",
--         "year"
--     )
--     VALUES (
--         NEW."isbn",
--         NEW."title",
--         NEW."publisher_id",
--         NEW."format",
--         NEW."pages",
--         NEW."published",
--         NEW."year"
--     );
-- END;

-- INSERT INTO "current_books"
--     ("isbn", "title", "publisher_id", "format", "pages", "published", "year")
--     VALUES
--     (9781628971588, 'asdasd', 3, 'paperback', 368, '2023-01-19', 2023)

