-- SQLite
-- CREATE TABLE riders (
--     "id",
--     "name"
-- );

-- CREATE TABLE stations (
--     "id",
--     "name",
--     "line"
-- );

-- CREATE TABLE riders_stations (
--     "rider_id",
--     "station_id"
-- );

-- DROP TABLE "riders";
-- DROP TABLE "riders_stations";
-- DROP TABLE "stations";

-- CREATE TABLE riders (
--     "id" INTEGER,
--     "name" TEXT
-- );

-- CREATE TABLE stations (
--     "id" INTEGER,
--     "name" TEXT,
--     "line" INTEGER
-- );

-- CREATE TABLE riders_stations (
--     "rider_id" INTEGER,
--     "station_id" INTEGER
-- );


-- DROP TABLE "riders";
-- DROP TABLE "riders_stations";
-- DROP TABLE "stations";

-- CREATE TABLE riders (
--     "id" INTEGER,
--     "name" TEXT,
--     PRIMARY KEY("id")
-- );

-- CREATE TABLE stations (
--     "id" INTEGER,
--     "name" TEXT,
--     "line" INTEGER,
--     PRIMARY KEY("id")
-- );

-- CREATE TABLE riders_stations (
--     "rider_id" INTEGER,
--     "station_id" INTEGER,
--     FOREIGN KEY("rider_id") REFERENCES "riders"("id"),
--     FOREIGN KEY("station_id") REFERENCES "stations"("id")
-- );

-- CREATE TABLE riders (
--     "id" INTEGER,
--     "name" TEXT,
--     PRIMARY KEY("id")
-- );

-- CREATE TABLE stations (
--     "id" INTEGER,
--     "name" TEXT NOT NULL UNIQUE,
--     "line" INTEGER NOT NULL,
--     PRIMARY KEY("id")
-- );

-- CREATE TABLE riders_stations (
--     "rider_id" INTEGER,
--     "station_id" INTEGER,
--     FOREIGN KEY("rider_id") REFERENCES "riders"("id"),
--     FOREIGN KEY("station_id") REFERENCES "stations"("id")
-- );

-- DROP TABLE "riders";

-- CREATE TABLE "cards" (
--     "id" INTEGER,
--     PRIMARY KEY("id")
-- );

-- ALTER TABLE "riders_stations"
-- RENAME TO "cards_stations";

-- ALTER TABLE "cards_stations"
-- RENAME COLUMN "rider_id" TO "card_id";

-- ALTER TABLE "cards_stations"
-- ADD COLUMN "type" TEXT;

-- ALTER TABLE "cards_stations"
-- DROP COLUMN "type";

-- CREATE TABLE "cards_stations" (
--     "id" INTEGER,
--     "card_id" INTEGER,
--     "station_id" INTEGER,
--     "type" TEXT NOT NULL CHECK("type" IN ('Enter', 'Exit')),
--     "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     "amount" NUMERIC NOT NULL CHECK("amount" > 0),
--     PRIMARY KEY ("id"),
--     FOREIGN KEY ("card_id") REFERENCES "cards"("id") ON DELETE CASCADE,
--     FOREIGN KEY ("station_id") REFERENCES "stations"("id") ON DELETE CASCADE
-- );

-- INSERT INTO "stations"
--     ("id", "name", "line")
-- VALUES
--     (1, 'Tajrish', 1);

-- INSERT INTO "stations"
--     ("name", "line")
-- VALUES
--     ('Qolhak', 1)

-- INSERT INTO "stations"
--     ("name", "line")
-- VALUES
--     (NULL, 2)

-- INSERT INTO "stations"
--     ("name", "line")
-- VALUES
--     ('Kahrizak', 1),
--     ('Azadi', 4),
--     ('Sharif', 2);

-- CREATE TABLE "stations_copy" (
--     "id" INTEGER,
--     "name" TEXT NOT NULL UNIQUE,
--     "line" INTEGER NOT NULL,
--     PRIMARY KEY ("id")
-- );

-- INSERT INTO "stations_copy"
--     ("name", "line")
-- SELECT "name", "line" FROM "stations";

-- DELETE FROM "stations_copy"
-- WHERE "name" = 'Azadi';

-- DELETE FROM "stations_copy"

-- INSERT INTO "cards"
--     ("id")
-- VALUES
--     (1),
--     (2),
--     (3)

-- INSERT INTO "cards_stations"
--     ("card_id", "station_id", "type", "amount")
-- VALUES
--     (1, 1, 'Enter', 4000),
--     (1, 3, 'Exit', 4000),
--     (2, 2, 'Enter', 4500),
--     (3, 4, 'Exit', 3500)

-- DELETE FROM "stations"
-- WHERE "name" = 'Azadi';

-- UPDATE "stations"
-- SET "name" = LOWER("name");

-- UPDATE "stations"
-- SET "name" = 'sharif university'
-- WHERE "name" = 'sharif';
