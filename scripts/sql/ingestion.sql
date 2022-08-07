DROP TABLE IF EXISTS campaign_inventory;
DROP TABLE IF EXISTS briefing;
CREATE TABLE IF NOT EXISTS campaign_inventory (
    id  SERIAL PRIMARY KEY,
    types TEXT, 
    width TEXT, 
    height TEXT, 
    campaign_id TEXT, 
    creative_id TEXT, 
    auction_id TEXT,
    browser_ts TEXT, 
    game_key TEXT,
    geo_country TEXT, 
    site_name TEXT, 
    platform_os TEXT,
    device_type TEXT, 
    browser TEXT);
CREATE TABLE IF NOT EXISTS briefing (
    campaign_id TEXT, 
    campaign_name TEXT, 
    Submission_Date TEXT, 
    Descriptions TEXT,
    Campaign_Objectives TEXT, 
    KPIs TEXT, 
    Placement TEXT, 
    StartDate TEXT, 
    EndDate TEXT,
    Serving_Location TEXT, 
    Black_white_audience TEXT,
    Delivery_Requirements TEXT, 
    Cost_Centre TEXT,
    Currency TEXT, 
    Buy_Rate_CPE TEXT, 
    Volume_Agreed TEXT, 
    Gross_Cost_or_Budget TEXT,
    Agency_Fee TEXT, 
    Percentages TEXT, 
    Flat_Fee TEXT, 
    Net_Cost TEXT);

COPY campaign_inventory (
    types, 
    width, 
    height, 
    campaign_id, 
    creative_id, 
    auction_id,
    browser_ts, 
    game_key,
    geo_country, 
    site_name, 
    platform_os,
    device_type, 
    browser
)
FROM '/usr/local/postgres/data/campaigns_inventory_updated.csv'
DELIMITER ','
CSV HEADER;