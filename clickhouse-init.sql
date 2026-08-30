CREATE DATABASE IF NOT EXISTS audit_logs;

CREATE TABLE IF NOT EXISTS audit_logs.activity_stream (
    timestamp DateTime64(3, 'Europe/Moscow') DEFAULT now(),
    employee_name String,
    event_type String,
    payload_size_mb Float32,
    risk_score_ai UInt8 DEFAULT 0,
    ai_verdict String DEFAULT ''
) ENGINE = MergeTree()
ORDER BY (event_type, employee_name, timestamp);
