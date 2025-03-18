-- Allow connections from any IP
ALTER SYSTEM SET listen_addresses = '*';

-- Force changes to take effect
SELECT pg_reload_conf();