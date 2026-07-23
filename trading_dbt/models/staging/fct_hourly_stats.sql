{{ config(materialized='table') }}

with trades as (
    select * 
    from {{ ref('stg_trades') }}
),

daily_summary as (
    select
        ticker,
        date(traded_at) as trade_date,
        count(*) as total_trades,
        round(avg(trade_price), 4) as avg_price,
        min(trade_price) as min_price,
        max(trade_price) as max_price,
        max(_ingested_at) as last_updated_at

    from trades
    group by 1, 2
)

select * from daily_summary
order by trade_date desc, ticker

