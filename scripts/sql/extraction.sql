CREATE EXTENSION IF NOT EXISTS dblink; -- used to transfer data between databases
DROP TABLE IF EXISTS source_campaign;  -- added becasuse the data in staging shouldn't be stored permanently
CREATE TABLE source_campaign           -- Create the table that temporarily holds the campaign inventory data
AS
SELECT *
FROM dblink('host=postgres
            user=data_lake
            password=data_lake
            dbname=data_lake',
            'select *
            from campaign_inventory') 
            as linktable (types TEXT, 
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
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
DROP TABLE IF EXISTS source_briefing;       -- added becasuse the data in staging shouldn't be stored permanently 
CREATE TABLE source_briefing                -- Create the table that temporarily holds the briefing data
AS
SELECT *
FROM dblink('host=postgres
            user=data_lake
            password=data_lake
            dbname=data_lake',
            'select *
            from briefing') 
            as linktable (campaign_id TEXT, 
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

--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------

DROP TABLE IF EXISTS source_global_design;  -- added becasuse the data in staging shouldn't be stored permanently
CREATE TABLE source_global_design           -- Create the table that temporarily holds the design features data
AS
SELECT *
FROM dblink('host=postgres
            user=data_lake
            password=data_lake
            dbname=data_lake',
            'select *
            from global_design') 
            as linktable (game_key TEXT, 
                            design_feature TEXT, 
                            feature_type TEXT, 
                            feature_variety TEXT,
                            sub_feature TEXT, 
                            feature_value TEXT);