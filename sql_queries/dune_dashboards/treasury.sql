/* Bankless DAO Treasury Dashboard SQL Queries */
/* Dune Analytics */


/* Transactions: Bankless DAO Treasury */
/* mirrors txns in etherscan.io */
/* Dashboard link: https://duneanalytics.com/paulapivat/WIP-Bankless-DAO-Treasury */
/* Query link: https://duneanalytics.com/queries/51047/100737 */

WITH txn_hash_table AS (
SELECT
    hash,
    block_number,
    block_time,
    "from",
    "to",
    value / 1e18 AS ether,               /* 18 decimals for ether values */
    gas_used,
    gas_price / 1e9 AS gas_price_gwei    /* 9 decimals for gwei values */
FROM ethereum."transactions"
WHERE "to" = '\xf26d1Bb347a59F6C283C53156519cC1B1ABacA51' /* Bankless DAO Treasury address */
ORDER BY block_time DESC
)
SELECT
    block_time,
    "from",
    "to",
    ether,
    (gas_used * gas_price_gwei) / 1e9 AS txn_fee,
    hash,
    block_number
FROM txn_hash_table

/* Number of Transactions */
/* mirrors txns in etherscan.io */
/* Dashboard link: https://duneanalytics.com/paulapivat/WIP-Bankless-DAO-Treasury */

WITH num_txn_table AS (
SELECT
    hash,
    block_number,
    block_time,
    "from",
    "to",
    value / 1e18 AS ether,
    gas_used,
    gas_price / 1e9 AS gas_price_gwei
FROM ethereum."transactions"
WHERE "to" = '\xf26d1Bb347a59F6C283C53156519cC1B1ABacA51'
ORDER BY block_time DESC
), calc_txn_fee AS (
SELECT
    hash,
    block_number,
    block_time,
    "from",
    "to",
    ether,
    (gas_used * gas_price_gwei) / 1e9 AS txn_fee
FROM num_txn_table
)
SELECT
    COUNT(*)
FROM calc_txn_fee


/* */

/* */

/* */