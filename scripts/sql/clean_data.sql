
-- replacing string parts for eaither conversion and comparison
UPDATE 
source_campaign
SET 
auction_id = REPLACE (
    auction_id,
    '-',
    ''
),
width = REPLACE (
    height,
    '%',
    '0'
),
height = REPLACE (
    height,
    '%',
    '0'
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
ALTER COLUMN browser_ts 
   TYPE TIMESTAMP WITH TIME ZONE 
     USING to_timestamp(browser_ts, 'YYYY-MM-DD"T"HH24:MI:SS"Z"');

ALTER TABLE source_briefing
ALTER COLUMN buy_rate_cpe TYPE FLOAT USING buy_rate_cpe::float,
ALTER COLUMN volume_agreed TYPE FLOAT USING volume_agreed::float,
ALTER COLUMN gross_cost_or_budget TYPE FLOAT USING gross_cost_or_budget::float,
ALTER COLUMN percentages TYPE FLOAT USING percentages::float,
ALTER COLUMN startdate TYPE DATE using to_date(startdate, 'DD-MM-YYYY'),
ALTER COLUMN enddate TYPE DATE using to_date(enddate, 'DD-MM-YYYY');


-- droping some empty columns
ALTER TABLE source_briefing
  DROP COLUMN delivery_requirements,
  DROP COLUMN flat_fee;

