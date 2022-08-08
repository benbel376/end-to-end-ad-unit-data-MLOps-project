{{ config(materialized='table') }}

with source_camp as (
    select * from {{source("source_table", "source_campaign")}}
),
source_brief as (
    select * from {{source("source_table", "source_briefing")}}
),
joins as (
    SELECT 
    c.id,
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

final as (
    select * from joins
)

select * from final