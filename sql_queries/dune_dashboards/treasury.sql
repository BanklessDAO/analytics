/* Bankless DAO Treasury Dashboard SQL Queries */
/* Dune Analytics */


/************************* Transactions: Bankless DAO Treasury *************************/
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

/************************* Number of Transactions *************************/
/* Query link: https://duneanalytics.com/queries/54273/107626 */

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
), 

calc_txn_fee AS (
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


/************************ Treasury Token Holdings (including Ether) *************************/
/* Query link: https://duneanalytics.com/queries/58504/116328 */

-- ERC20 Token Holdings
WITH erc20_evt AS (   
    SELECT -- outbound transfer erc20 txns
        evt_tx_hash,
        evt_block_time,
        tr."from" AS address,
        -tr.value AS amount,
        contract_address
    FROM erc20."ERC20_evt_Transfer" tr

    UNION ALL

    SELECT -- inbound transfer erc20 txns
        evt_tx_hash,
        evt_block_time,
        tr."to" AS address,
        tr.value AS amount,
        contract_address
    FROM erc20."ERC20_evt_Transfer" tr
),

banklessvault_erc20_holding AS (
SELECT
        evt_tx_hash,
        evt_block_time,
        address,
        amount as balance,
        contract_address
FROM erc20_evt
WHERE address = '\xf26d1Bb347a59F6C283C53156519cC1B1ABacA51'
ORDER BY evt_block_time DESC
),

erc20_token_quant AS (
SELECT 
        beh.contract_address AS contract_addr,
        CASE 
            WHEN beh.contract_address = '\x2d94aa3e47d9d5024503ca8491fce9a2fb4da198' THEN 'BANK' -- BANK currently not listed in Dune erc20 abstractions
            ELSE tok.symbol
        END AS token,
        CASE 
            WHEN beh.contract_address = '\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48' -- USDC token has 6 decimals (instead of 18)
            THEN balance/1e6 
        ELSE balance/1e18
        END AS quantity
FROM banklessvault_erc20_holding beh
LEFT JOIN erc20.tokens tok ON beh.contract_address = tok.contract_address
),

sum_erc20_token AS (
SELECT
    contract_addr,
    token,
    SUM(quantity) AS sum_quantity
FROM erc20_token_quant
GROUP BY 1,2
),

erc20_latest_price AS (
SELECT 
    minute,
    price,
    symbol
FROM prices."usd" 
WHERE symbol = 'USDC' OR (symbol = 'WETH')
ORDER BY minute DESC
LIMIT 2
),

erc20_table AS (
SELECT
    minute,
    token,
    sum_quantity,
    price
FROM sum_erc20_token st FULL JOIN erc20_latest_price ep ON st.token = ep.symbol
),

-- Ether Holdings

eth_holding AS (
--outbound transfers
SELECT
    "from" AS address,
    -tr.value AS amount
FROM ethereum.traces tr                                         -- Ether balance requires querying traces
WHERE "from" = '\xf26d1Bb347a59F6C283C53156519cC1B1ABacA51'
AND success
AND (call_type NOT IN ('delegatecall', 'callcode', 'staticcall') OR call_type IS null) -- only want call_type 'call'

UNION ALL

--inbound transfer
SELECT
    "to" AS address,
    tr.value AS amount
FROM ethereum.traces tr
WHERE "to" = '\xf26d1Bb347a59F6C283C53156519cC1B1ABacA51'
AND success
AND (call_type NOT IN ('delegatecall', 'callcode', 'staticcall') OR call_type IS null)

UNION ALL

--gas costs
SELECT 
    "from" AS address,
    -gas_used * gas_price AS amount
FROM ethereum.transactions
WHERE "from" = '\xf26d1Bb347a59F6C283C53156519cC1B1ABacA51'
), 

eth_quant AS (
SELECT
    sum(amount) / 1e18 AS sum_quantity,
    'ETH' AS token
FROM eth_holding h
GROUP BY 2
),

eth_price AS (
SELECT 
    minute, 
    price,
    SYMBOL
FROM prices."layer1_usd"
WHERE SYMBOL = 'ETH'
ORDER BY 1 desc
LIMIT 1
),

eth_table AS (
SELECT
    minute,
    eq.token,
    eq.sum_quantity,
    ep.price
FROM eth_quant eq
LEFT JOIN eth_price ep ON ep.symbol = eq.token
)

-- Union Both erc20_table and eth_table
SELECT * FROM erc20_table
UNION ALL
SELECT * FROM eth_table

/*************************  ERC20 Token Txns *************************/
/* Query Link: https://duneanalytics.com/queries/50995/100608 */

WITH erc20_transfer AS (
    SELECT 
    evt_tx_hash,
    evt_block_time,
    tr."from" AS address,
    -tr.value AS amount,
    contract_address
    FROM erc20."ERC20_evt_Transfer" tr

    UNION ALL

    SELECT 
    evt_tx_hash,
    evt_block_time,
    tr."to" AS address,
    tr.value AS amount,
    contract_address
    FROM erc20."ERC20_evt_Transfer" tr
), 

treasury_erc20_holding AS (
    SELECT
        evt_tx_hash,
        evt_block_time,
        address,
        amount as balance,
        contract_address
    FROM erc20_transfer
    WHERE address = '\xf26d1Bb347a59F6C283C53156519cC1B1ABacA51'
    ORDER BY evt_block_time DESC
)

SELECT 
    evt_block_time,
    address,
    CASE 
        WHEN tr.contract_address = '\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
        THEN balance/1e6 
        ELSE balance/1e18
    END AS balance,
    CASE 
        WHEN tr.contract_address = '\x2d94aa3e47d9d5024503ca8491fce9a2fb4da198' THEN 'BANK'
        ELSE tok.symbol
    END AS token,
    evt_tx_hash
FROM treasury_erc20_holding tr
LEFT JOIN erc20.tokens tok ON tr.contract_address = tok.contract_address

/* */