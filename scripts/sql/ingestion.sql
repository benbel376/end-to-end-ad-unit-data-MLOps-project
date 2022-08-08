CREATE EXTENSION IF NOT EXISTS dblink;

DROP TABLE IF EXISTS campaign_inventory;
CREATE TABLE IF NOT EXISTS campaign_inventory (
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

DROP TABLE IF EXISTS briefing;
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

DROP TABLE IF EXISTS global_design;
CREATE TABLE IF NOT EXISTS global_design (
    game_key TEXT, 
    design_feature TEXT, 
    feature_type TEXT, 
    feature_variety TEXT,
    sub_feature TEXT, 
    feature_value TEXT);

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

COPY briefing (
    campaign_id, 
    campaign_name, 
    Submission_Date, 
    Descriptions,
    Campaign_Objectives, 
    KPIs, 
    Placement, 
    StartDate, 
    EndDate,
    Serving_Location, 
    Black_white_audience,
    Delivery_Requirements, 
    Cost_Centre,
    Currency, 
    Buy_Rate_CPE, 
    Volume_Agreed, 
    Gross_Cost_or_Budget,
    Agency_Fee, 
    Percentages, 
    Flat_Fee, 
    Net_Cost
)
FROM '/usr/local/postgres/data/briefing.csv'
DELIMITER ','
CSV HEADER;


COPY global_design (
    game_key, 
    design_feature, 
    feature_type, 
    feature_variety,
    sub_feature, 
    feature_value
)
FROM '/usr/local/postgres/data/global_design_data.csv'
DELIMITER ','
CSV HEADER;
