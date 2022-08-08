{{ config(materialized='table') }}

with source_camp as (
    select * from {{source("source_table", "source_campaign")}}
),
source_brief as (
    select * from {{source("source_table", "source_briefing")}}
),
source_global as (
    select * from {{source("source_table", "source_global_design")}}
),
joins as (
    SELECT 
    c.campaign_id,
    c.types, 
    c.width, 
    c.height,  
    c.creative_id, 
    c.auction_id,
    c.browser_ts, 
    c.game_key,
    c.geo_country, 
    c.site_name, 
    c.platform_os,
    c.device_type, 
    c.browser,
    b.campaign_name, 
    b.Submission_Date, 
    b.Descriptions,
    b.Campaign_Objectives, 
    b.KPIs, 
    b.Placement, 
    b.StartDate, 
    b.EndDate,
    b.Serving_Location, 
    b.Black_white_audience,
    b.Delivery_Requirements, 
    b.Cost_Centre,
    b.Currency, 
    b.Buy_Rate_CPE, 
    b.Volume_Agreed, 
    b.Gross_Cost_or_Budget,
    b.Agency_Fee, 
    b.Percentages, 
    b.Flat_Fee, 
    b.Net_Cost
    FROM source_camp as c
    INNER JOIN source_brief as b ON c.campaign_id = b.campaign_id
),

joins2 as (
    SELECT 
    j.campaign_id,
    j.types, 
    j.width, 
    j.height,  
    j.creative_id, 
    j.auction_id,
    j.browser_ts, 
    j.game_key,
    j.geo_country, 
    j.site_name, 
    j.platform_os,
    j.device_type, 
    j.browser,
    j.campaign_name, 
    j.Submission_Date, 
    j.Descriptions,
    j.Campaign_Objectives, 
    j.KPIs, 
    j.Placement, 
    j.StartDate, 
    j.EndDate,
    j.Serving_Location, 
    j.Black_white_audience,
    j.Delivery_Requirements, 
    j.Cost_Centre,
    j.Currency, 
    j.Buy_Rate_CPE, 
    j.Volume_Agreed, 
    j.Gross_Cost_or_Budget,
    j.Agency_Fee, 
    j.Percentages, 
    j.Flat_Fee, 
    j.Net_Cost,
    g.design_feature, 
    g.feature_type, 
    g.feature_variety,
    g.sub_feature, 
    g.feature_value
    FROM joins as j
    INNER JOIN source_global as g ON g.game_key = j.game_key
),

final as (
    select * from joins2
)

select * from final