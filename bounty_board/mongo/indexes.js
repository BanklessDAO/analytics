db.bounties.createIndex(
  {
    customerId: 1,
    createdAt: 1
  },
  {
    background: true
  }
);