/* Explore poap on xDai network with Dune Analytics */
/* Supplement to GraphQL queries */

/* */

/* POAP GraphQL Schema: */
/* Token */
/* Account */
/* Event */
/* Transfer */
/* _Meta_     (access to subgraph metadata)  */

/* The Graph events id: 2655, accessible on The Graph, not on dune analytics */
/* The Graph tokens id: 317221, is tokenId on dune */
/* The Graph tokens owner id == transfers to id on The Graph == "to" on erc721."ERC721_evt_Transfer" on Dune */
/* The Graph events transfers from id == "from" on erc721."ERC721_evt_Transfer" on Dune */
/* The Graph events transfers id == evt_block_number on erc721."ERC721_evt_Transfer" on Dune */


SELECT *
FROM erc721."ERC721_evt_Transfer"
WHERE contract_address = '\x22C1f6050E56d2876009903609a2cC3fEf83B415'    /* POAP contract_address on xDai */
AND "to" = '\xdfDf2D882D9ebce6c7EAc3DA9AB66cbfDa263781'
ORDER BY evt_block_time DESC
LIMIT 1000