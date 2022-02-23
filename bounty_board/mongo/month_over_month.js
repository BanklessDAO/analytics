// Number of bounties created in past 30-days
// Count
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _claimedAt: "$claimedAt",
      _submittedAt: "$submittedAt",
      _reviewedAt: "$reviewedAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      claimedAt: { $toDate: "$_claimedAt" },
      submittedAt: { $toDate: "$_submittedAt" },
      reviewedAt: { $toDate: "$_reviewedAt" },
    },
  },
  {
    $match: {
      createdAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
      createdAt: { $gt: new Date(new Date() - 60 * 60 * 60 * 24 * 1000) },
    },
  },
  {
    $group: {
      _id: 1,
      totalCount: { $sum: 1 },
    },
  },
]);

// Number of bounties created in past 30-days
// Count
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _createdAt2: "$createdAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      createdAt2: { $toDate: "$_createdAt2" },
    },
  },
  {
    $match: {
      //createdAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
      createdAt2: { $gt: new Date(new Date() - 60 * 60 * 60 * 24 * 1000) },
    },
  },
]);

// createdAt: count
// month-over-month
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
    },
  },
  {
    $match: {
      createdAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
  { $group: { _id: 1, totalCount: { $sum: 1 } } },
]);

db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
    },
  },
  {
    $match: {
      createdAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
  { $group: { _id: 1, totalCount: { $sum: 1 } } },
]);

// split sum of documents by month: jan 12, feb 4 (so far)
// e.g.: Go back 60-days,
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
    },
  },
  {
    $match: {
      createdAt: { $gt: new Date(new Date() - 60 * 60 * 60 * 24 * 1000) },
    },
  },
  { $group: { _id: { $month: "$createdAt" }, numdocbymonth: { $sum: 1 } } },
]);

// customerId yields different results from customer_id
db.bounties.aggregate([
  { $match: { customerId: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customerId: "$customerId",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
    },
  },
  {
    $project: {
      _id: 1,
      customerId: "$_customerId",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
    },
  },
  {
    $match: {
      createdAt: { $gt: new Date(new Date() - 60 * 60 * 60 * 24 * 1000) },
    },
  },
  { $group: { _id: { $month: "$createdAt" }, numdocbymonth: { $sum: 1 } } },
]);

// confirm January bounties (n = 24)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { createdAt: { $gte: "2022-01-01" } },
        { createdAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  { $group: { _id: { $month: "$createdAt" }, num_doc_by_month: { $sum: 1 } } },
]);

// Alternative version (customerId instead of customer_id) for January bounties (n = 24)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customerId: "834499078434979890" },
        { createdAt: { $gte: "2022-01-01" } },
        { createdAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  { $group: { _id: { $month: "$createdAt" }, num_doc_by_month: { $sum: 1 } } },
]);

// 60-day 2-months (December - January) count of Bounties (customer_id) (Dec, n = 27; Jan, n=24)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { createdAt: { $gte: "2021-12-01" } },
        { createdAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  { $group: { _id: { $month: "$createdAt" }, num_doc_by_month: { $sum: 1 } } },
]);

// Alternative version (customerId instead of customer_id)
// 60-day 2-months (December - January) count of Bounties (customerId) (Dec, n = 21; Jan, n=24)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customerId: "834499078434979890" },
        { createdAt: { $gte: "2021-12-01" } },
        { createdAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  { $group: { _id: { $month: "$createdAt" }, num_doc_by_month: { $sum: 1 } } },
]);

// Week-over-week (Dec 2021 - Jan 2022)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { createdAt: { $gte: "2021-12-01" } },
        { createdAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  { $group: { _id: { $week: "$createdAt" }, num_doc_by_week: { $sum: 1 } } },
]);

// Alternate: Week-over-week (Dec 2021 - Jan 2022)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customerId: "834499078434979890" },
        { createdAt: { $gte: "2021-12-01" } },
        { createdAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  { $group: { _id: { $week: "$createdAt" }, num_doc_by_week: { $sum: 1 } } },
]);

// Alternate: Month-over-Month (Dec 2021 - Jan 2022)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customerId: "834499078434979890" },
        { createdAt: { $gte: "2021-12-01" } },
        { createdAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  { $group: { _id: { $month: "$createdAt" }, num_doc_by_week: { $sum: 1 } } },
]);

// Alternate: Day-over-Day (Jan 2022)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customerId: "834499078434979890" },
        { createdAt: { $gte: "2022-01-01" } },
        { createdAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  {
    $group: { _id: { $dayOfYear: "$createdAt" }, num_doc_by_week: { $sum: 1 } },
  },
]);
