-- SQLite
-- BEGIN TRANSACTION;
-- UPDATE "accounts"
-- SET "balance" = "balance" + 10
-- WHERE "id" = 2;
-- UPDATE "accounts"
-- SET "balance" = "balance" - 10
-- WHERE "id" = 1;
-- COMMIT;

SELECT *
FROM "users"
WHERE "user" = '<>' AND "password" = '<>'

SELECT *
FROM "users"
WHERE "user" = 'abc' AND "password" = '<p' OR '1' = '1>';

SELECT *
FROM "users"
WHERE "user" = ':username' AND "password" = ':password';