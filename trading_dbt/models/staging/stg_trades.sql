with source_data as (
    select * 
    from {{ source('trading_bronze', 'trading_events') }}
),
renamed_and_casted as (
    select
        cast(ticker as string) as ticker,
        cast(price as numeric) as trade_price,
        safe_cast(timestamp as timestamp) as traded_at,
        current_timestamp() as _ingested_at
    from source_data
    where ticker is not null 
      and price is not null
)
select * from renamed_and_casted