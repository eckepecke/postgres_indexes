FROM postgres:latest
RUN echo "shared_preload_libraries = 'pg_stat_statements'" >> /usr/share/postgresql/postgresql.conf