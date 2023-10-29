CREATE TABLE spot_entry (
    spot_id integer primary key autoincrement,
    symbol varchar(255),
    ticker_time integer,
    open_price double,
    close_price double,
    min_price double,
    max_price double,
    volume double
);