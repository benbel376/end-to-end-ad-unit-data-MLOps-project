-- checking trend
select volume_agreed, gross_cost_or_budget 
from warehouse 
limit 1000;

-- top websites
select site_name, count(site_name) as counts
from warehouse 
group by site_name 
order by counts 
desc
limit 5;

-- Top browsers: top browsers are chrome and safari
select distinct browser, count(browser) as counts
from warehouse
group by browser
order by counts 
desc
limit 5;

-- Budget trend : result is that budget is increasing rapidly
select browser_ts, gross_cost_or_budget as cost 
from warehouse 
where browser_ts between '2021/06/27 23:59:59.999' and '2022/01/27 23:59:59.999';

-- Campaign count per types
select distinct types, count(campaign_id) as campaign_count
from warehouse 
group by types;

-- gross budget per type: the cost for click_through event is greater than all
select distinct types, avg(gross_cost_or_budget) 
from warehouse 
group by types;