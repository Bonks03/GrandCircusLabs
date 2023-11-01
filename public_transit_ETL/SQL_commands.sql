ALTER TABLE monthly_totals
ALTER COLUMN "Month" TYPE date;

CREATE TABLE bus_monthly_totals AS
SELECT * FROM monthly_totals WHERE ridership_type = 'bus';

CREATE TABLE metro_monthly_totals AS
SELECT * FROM monthly_totals WHERE ridership_type = 'metro';

ALTER TABLE bus_monthly_totals
DROP COLUMN ridership_type;

ALTER TABLE metro_monthly_totals
DROP COLUMN ridership_type;