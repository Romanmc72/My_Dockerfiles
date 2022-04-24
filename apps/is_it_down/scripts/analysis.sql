WITH sessions AS (
  SELECT
    hostname
    , host_was_reachable
    , session_end - session_start AS session_length
    , session_start
    , session_end
  FROM (
    SELECT
      hostname
      , host_was_reachable
      , ping_timestamp AS session_start
      , LEAD(
          ping_timestamp, 1, (SELECT MAX(ping_timestamp) FROM public.is_it_down)
        ) OVER(
            PARTITION BY hostname
            ORDER BY ping_timestamp
        ) AS session_end
    FROM (
      SELECT
        hostname
        , host_was_reachable
        , LAG(
            host_was_reachable, 1, FALSE
          ) OVER(
              PARTITION BY hostname
              ORDER BY ping_timestamp
          ) AS previous_ping_host_was_reachable
        , ping_timestamp
      FROM
        public.is_it_down
    ) AS compare
    WHERE
      host_was_reachable <> previous_ping_host_was_reachable
  ) AS sessions
)
, session_stats AS (
  SELECT
    hostname
    , host_was_reachable
    , AVG(session_length) AS average_time
    , MIN(session_length) AS minimum_time
    , MAX(session_length) AS maximum_time
    , COUNT(*) AS sessions
    , STDDEV(session_length) AS standard_deviation_time
  FROM
    sessions
  GROUP BY
    hostname
    , host_was_reachable
)
, stats AS (
    SELECT
    hostname
    , SUM(CASE WHEN host_was_reachable THEN 1 ELSE 0 END) AS reaches
    , COUNT(*) AS attempts
    , MIN(ping_timestamp) AS period_begin
    , MAX(ping_timestamp) AS period_end
  FROM 
    public.is_it_down
  GROUP BY
    hostname
)

SELECT
  stats.hostname
  , stats.reaches
  , stats.attempts
  , ROUND(CASE
      WHEN stats.attempts = 0 THEN stats.attempts
      ELSE CAST(stats.reaches AS DECIMAL) / CAST(stats.attempts AS DECIMAL)
    END * 100, 2) AS percent_reachable
  , stats.period_end - stats.period_begin AS timespan
  , (SELECT host_was_reachable FROM public.is_it_down ORDER BY ping_timestamp DESC LIMIT 1) AS currently_reachable
  , reachable.sessions + unreachable.sessions AS total_session_flips
  , (stats.period_end - stats.period_begin)
      /
    (reachable.sessions + unreachable.sessions) AS time_between_session_flips
  , unreachable.average_time AS average_time_unreachable
  , unreachable.minimum_time AS minimum_time_unreachable
  , unreachable.maximum_time AS maximum_time_unreachable
  , unreachable.standard_deviation_time AS standard_deviation_time_unreachable
  , reachable.average_time AS average_time_reachable
  , reachable.minimum_time AS minimum_time_reachable
  , reachable.maximum_time AS maximum_time_reachable
  , reachable.standard_deviation_time AS standard_deviation_time_reachable
FROM 
  stats AS stats
LEFT JOIN
  session_stats AS unreachable ON (
    stats.hostname = unreachable.hostname 
    AND NOT unreachable.host_was_reachable
  )
LEFT JOIN
  session_stats AS reachable ON (
    stats.hostname = reachable.hostname 
    AND reachable.host_was_reachable
  )

