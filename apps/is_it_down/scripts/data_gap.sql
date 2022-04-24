SELECT
  hostname
  , MAX(gap) AS biggest_gap
FROM (
  SELECT
    hostname
    , ping_timestamp - LAG(ping_timestamp, 1) OVER(
      PARTITION BY hostname
      ORDER BY ping_timestamp
    ) AS gap
  FROM
    public.is_it_down
) AS gaps
WHERE
  gap IS NOT NULL
GROUP BY
  hostname
;
