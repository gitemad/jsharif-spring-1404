-- SQLite
-- SELECT *
-- FROM "longlist";
-- SELECT *
-- FROM longlist;

-- SELECT "title", "author"
-- FROM "longlist";

-- SELECT *
-- FROM "longlist"
-- LIMIT 10;

-- SELECT *
-- FROM "longlist"
-- LIMIT 10, 5;

-- SELECT "title", "author", "year"
-- FROM "longlist"
-- WHERE "year" = 2023;

-- SELECT "title", "format"
-- FROM "longlist"
-- WHERE "format" != 'hardcover';

-- SELECT "title", "format"
-- FROM "longlist"
-- WHERE "format" <> 'hardcover';

-- SELECT "title", "format"
-- FROM "longlist"
-- WHERE NOT "format" = 'hardcover';

-- SELECT "title", "author", "year"
-- FROM "longlist"
-- WHERE "year" = 2023 OR "year" = 2022;

-- SELECT "title", "author", "year"
-- FROM "longlist"
-- WHERE ("year" = 2023 OR "year" = 2022) AND "format" != 'hardcover';

-- SELECT "title", "translator"
-- FROM "longlist"
-- WHERE "translator" IS NULL;

-- SELECT "title", "translator"
-- FROM "longlist"
-- WHERE "translator" IS NOT NULL;

-- SELECT "title"
-- FROM "longlist"
-- WHERE "title" LIKE '%love%';

-- SELECT "title"
-- FROM "longlist"
-- WHERE "title" LIKE 'The%';

-- SELECT "title"
-- FROM "longlist"
-- WHERE "title" LIKE 'The %';

-- SELECT "title"
-- FROM "longlist"
-- WHERE "title" LIKE 'p_re';

-- SELECT "title"
-- FROM "longlist"
-- WHERE "title" LIKE '____';

-- SELECT "title", "author", "year"
-- FROM "longlist"
-- WHERE 2019 <= "year" AND "year" <= 2022;

-- SELECT "title", "author", "year"
-- FROM "longlist"
-- WHERE "year" BETWEEN 2019 AND 2022;

-- SELECT "title", "rating"
-- FROM "longlist"
-- WHERE "rating" > 4.0;

-- SELECT "title", "rating", "votes"
-- FROM "longlist"
-- WHERE "rating" > 4.0 AND "votes" > 10000;

-- SELECT "title", "pages"
-- FROM "longlist"
-- WHERE "pages" < 300;

-- SELECT "title", "pages"
-- FROM "longlist"
-- ORDER BY "pages";

-- SELECT "title", "pages"
-- FROM "longlist"
-- ORDER BY "pages" ASC;

-- SELECT "title", "pages"
-- FROM "longlist"
-- ORDER BY "pages" DESC;

-- SELECT "title", "rating", "votes"
-- FROM "longlist"
-- ORDER BY "rating" DESC, "votes" DESC
-- LIMIT 20;

-- SELECT "title"
-- FROM "longlist"
-- ORDER BY "title";

-- SELECT ROUND(AVG("rating"), 2) AS "average rating"
-- FROM "longlist";

-- SELECT MAX("rating")
-- FROM "longlist";

-- SELECT MIN("rating")
-- FROM "longlist";

-- SELECT "title", MIN("votes")
-- FROM "longlist";

-- SELECT SUM("votes")
-- FROM "longlist";

-- SELECT COUNT(*)
-- FROM "longlist";

-- SELECT COUNT(DISTINCT "format")
-- FROM "longlist";

-- SELECT COUNT("translator")
-- FROM "longlist";

-- SELECT COUNT(DISTINCT "publisher")
-- FROM "longlist";

-- SELECT "title", "rating", (SELECT AVG("rating") FROM "longlist") AS avg
-- FROM "longlist"
-- WHERE "rating" > "avg";