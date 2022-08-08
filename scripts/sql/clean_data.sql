UPDATE 
source_campaign
SET 
auction_id = REPLACE (
    auction_id,
    '-',
    ''
);
-- removing duplicates
WITH
cte
AS
(
SELECT ctid,
       row_number() OVER (PARTITION BY auction_id
                          ORDER BY auction_id) rn
       FROM source_campaign
)
DELETE FROM source_campaign
       USING cte
       WHERE cte.rn > 1
             AND cte.ctid = source_campaign.ctid;

-- trimming some columns
UPDATE source_campaign
SET game_key = TRIM (game_key),
    auction_id = TRIM (auction_id);

UPDATE source_global_design
SET game_key = TRIM (game_key);

--type casting
ALTER TABLE source_campaign
ALTER COLUMN width TYPE INT USING width::integer,
ALTER COLUMN height TYPE INT USING height::integer,
ALTER COLUMN platform_os TYPE INT USING platform_os::integer,
ALTER COLUMN browser_ts 
   TYPE TIMESTAMP WITH TIME ZONE 
     USING to_timestamp(browser_ts, 'YYYY-MM-DD"T"HH24:MI:SS"Z"');

