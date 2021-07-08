
WITH total_lp AS (
SELECT 
    evt_block_time,
    tr."from" AS address,
    -tr.value AS amount,
    contract_address
FROM erc20."ERC20_evt_Transfer" tr
WHERE contract_address = '\x2c51eaa1bcc7b013c3f1d5985cdcb3c56dc3fbc1' -- SushiSwap  BANK-WETH SLP Token

UNION ALL

SELECT
    evt_block_time,
    tr."to" AS address,
    tr.value AS amount,
    contract_address
FROM erc20."ERC20_evt_Transfer" tr
WHERE contract_address = '\x2c51eaa1bcc7b013c3f1d5985cdcb3c56dc3fbc1' -- SushiSwap BANK-WETH SLP Token
), total_lp2 AS (
SELECT
    address,
    SUM(amount/10^18) AS balance
FROM total_lp tl
LEFT JOIN erc20.tokens tok ON tl.contract_address = tok.contract_address
GROUP BY 1
ORDER BY 2 DESC
)
SELECT
    address,
    balance,
    (balance / SUM(balance) OVER ()) * 100 AS percentage --
FROM total_lp2
WHERE balance > 0
