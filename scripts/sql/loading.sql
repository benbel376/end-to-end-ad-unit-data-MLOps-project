CREATE EXTENSION IF NOT EXISTS dblink;
DROP TABLE IF EXISTS warehouse;
CREATE TABLE warehouse
AS
SELECT *
FROM dblink('host=postgres
            user=staging
            password=staging
            dbname=staging',
            'select *
            from trans_join') 
            as linktable (
                            campaign_id TEXT,
                            types TEXT, 
                            width TEXT, 
                            height TEXT,  
                            creative_id TEXT, 
                            auction_id TEXT,
                            browser_ts TEXT, 
                            game_key TEXT,
                            geo_country TEXT, 
                            site_name TEXT, 
                            platform_os TEXT,
                            device_type TEXT, 
                            browser TEXT, 
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
                            Net_Cost TEXT, 
                            design_feature TEXT, 
                            feature_type TEXT, 
                            feature_variety TEXT,
                            sub_feature TEXT, 
                            feature_value TEXT);