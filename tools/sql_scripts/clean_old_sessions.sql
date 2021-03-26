-- Delete all rows where expiration date is older than 2 weeks from now
DELETE FROM django_session WHERE  expire_date < now() - interval '14 days'